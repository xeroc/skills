# Composable Pull Architecture — Design Analysis

Date: 2026-06-10

## Problem

Tributary's existing PaymentPolicy uses a monolithic enum (PolicyType) with all variants padded to 128 bytes. Adding composable pull payments (CPI to arbitrary programs + Lighthouse assertion conditions) doesn't fit this structure:

1. Composable pulls need forward_program, instruction_data, condition config — too much for 128 bytes
2. Bumping VARIANT_SIZE increases rent for ALL existing policies (including simple subscriptions)
3. Lighthouse conditions are a separate dimension from payment type (oracle gates on subscriptions, balance thresholds on PAYG)
4. CPI execution path is fundamentally different from SPL transfer — different audit surface

## Solana Foundation Subscriptions Pattern (Reference)

The `subscriptions/` program uses separate account types sharing a common header.

### Common Header (107 bytes)

```rust
// state/header.rs
pub struct Header {
    pub discriminator: u8,    // offset 0 — identifies concrete type
    pub version: u8,          // offset 1 — schema version
    pub bump: u8,             // offset 2
    pub delegator: Address,   // offset 3  (32 bytes)
    pub delegatee: Address,   // offset 35 (32 bytes)
    pub payer: Address,       // offset 67 (32 bytes)
    pub init_id: i64,         // offset 99
}
```

### Three Delegation Types (all share same PDA seed pattern)

| Type | Discriminator | Size | PDA Seeds |
|------|--------------|------|-----------|
| FixedDelegation | 2 | 187B | `["delegation", sub_auth, delegator, delegatee, nonce]` |
| RecurringDelegation | 3 | 211B | `["delegation", sub_auth, delegator, delegatee, nonce]` |
| SubscriptionDelegation | 4 | 155B | `["subscription", plan_pda, subscriber]` |

Each type has its own exact size — no padding waste. The discriminator at byte 0 differentiates at runtime. Adding a new type doesn't affect existing account sizes.

### Key Differences from Tributary

- **Pinocchio** (no_std) not Anchor — manual `#[repr(C, packed)]` + unsafe transmute for zero-copy
- **Codama** for IDL generation from `#[codama(...)]` attributes
- **Version field** in header enables account migration (see `state/versioning/`)
- **Plan** is a separate account type with whitelisted pullers and destinations
- **init_id** links delegations to a SubscriptionAuthority for staleness detection

## Recommendation: Separate ComposablePolicy Account

### Proposed Layout

```
ComposablePolicy (new account type)
├── Header (discriminator, version, bump, user_payment_ref, gateway_ref)
├── BasePolicy (amount, schedule — reuse strategy pattern)
├── ForwardConfig (target_program, instruction_data_hash or reference)
├── ConditionConfig (Lighthouse assertion params, oracle feeds, thresholds)
└── State (execution tracking: total_paid, payment_count, timestamps)
```

### PDA Seeds

`["composable_policy", user_payment, policy_id]` — distinct from `["payment_policy", ...]`

### Why Separate, Not Extended

1. **No padding tax** — ComposablePolicy gets its own size budget; existing PaymentPolicy unchanged
2. **Lighthouse as a layer** — Conditions are not a payment type, they're an execution gate that can combine with any schedule
3. **Independent audit** — CPI path (intermediate PDAs, ATA creation, sweep) is separate from clean SPL transfer
4. **METEORA spec already separates** — `execute_delegate_to_program` has its own account struct, not a modified `execute_payment`
5. **Upgrade path** — New composable types added without touching existing accounts (following Solana Foundation pattern)

### What Stays Shared

- Fee calculation utilities (protocol fee + gateway fee)
- Strategy pattern for schedule validation (Subscription timing, PAYG periods)
- UserPayment reference and policy_id counter
- PaymentGateway reference and signer validation
- Referral reward processing

### Gateway Model for Composable Pulls

- **Permissioned** (default for composable): Gateway signer must sign execution. Business controls timing. Easier to implement, more flexibility.
- **Permissionless**: Anyone triggers when conditions met. Requires policy PDA to contain all parameters. Needs per-program custom validation in the contract.

Roadmap: start permissioned, expand to permissionless for specific programs (e.g., Jupiter swaps) when demand justifies.

## Lighthouse Integration Notes

Lighthouse provides runtime assertion instructions that fail a transaction when on-chain state diverges. For Tributary:

- **AssertAccountData**: Check oracle price feeds, token balances, account state fields
- **AssertAccountInfo**: Verify account ownership, lamports, data length
- **AssertAccountDelta**: Compare two accounts (e.g., before/after state)
- **AssertSysvarClock**: Time-based conditions (alternative to Tributary's built-in timing)
- **Multi-assertion**: Batch assertions to save tx space; error code 0x1900 + failed assertion index

Lighthouse assertions would be evaluated BEFORE the composable pull executes. Fail assertion = revert transaction. This enables: oracle-gated swaps, balance-threshold triggers, governance-dependent payments, Merkle proof gates.

## Existing METEORA Spec Key Points

- `execute_delegate_to_program` instruction: separate from `execute_payment`
- Program mode detected by `recipient.executable == true`
- Hard-coded whitelist of allowed program IDs (requires program upgrade to add)
- Fees deducted in source token BEFORE CPI
- No slippage check in Tributary — target program handles it
- PDA intermediate tokens created lazily, swept and closed after execution
- Raw instruction data passed through without parsing
