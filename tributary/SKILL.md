---
name: tributary
description: "Tributary — Solana recurring payment protocol. Covers program architecture (Rust/Anchor), SDK (TypeScript), composable pull payments, Lighthouse integration, and React frontend integration. Use when working on the Tributary codebase, designing features, writing specs, or integrating Tributary into apps."
version: 2.0.0
triggers:
  - tributary
  - tributary.so
  - recurring payments solana
  - pull payments
  - composable pull
  - payment policy
  - payment gateway
  - token delegation
  - SPL delegation
---

# Tributary — Solana Recurring Payment Protocol

Non-custodial payment protocol on Solana. Users delegate spending authority once; payments execute automatically within approved limits. Program ID: `TRibg8W8zmPHQqWtyAD1rEBRXEdy13Mu6qX1Sg42tJ`.

## Architecture Overview

```
User -> Create UserPayment (owner/mint)
    -> Create PaymentGateway (authority/signer)
    -> Create PaymentPolicy (user_payment/recipient/gateway)
    -> Approve Delegate (token account delegation)
    -> Execute Payment (permissionless, by gateway signer)
       -> Transfer to recipient + fees
```

### Account Hierarchy

| Account          | PDA Seeds                                     | Size       | Purpose                                                     |
| ---------------- | --------------------------------------------- | ---------- | ----------------------------------------------------------- |
| ProgramConfig    | `["config"]`                                  | 336B       | Global protocol config, fees, admin, emergency pause        |
| PaymentGateway   | `["gateway", authority]`                      | 296B       | Business-specific gateway, fees, signer, feature flags      |
| UserPayment      | `["user_payment", owner, mint]`               | 382B       | Per-user/mint tracker, policy counter                       |
| PaymentPolicy    | `["payment_policy", user_payment, policy_id]` | 586B       | Individual payment rule (Subscription/Milestone/PayAsYouGo) |
| ReferralAccount  | `["referral", gateway, code]`                 | 200B       | 3-level referral chain (zero_copy)                          |
| PaymentsDelegate | `["payments"]`                                | PDA signer | CPI authority for token transfers                           |

### PolicyType Enum (129 bytes: 1 discriminator + 128 payload)

All variants padded to exactly 128 bytes. Nested inside PaymentPolicy.

- **Subscription**: amount, auto_renew, max_renewals, payment_frequency, next_payment_due
- **Milestone**: 4x (amount, timestamp), current_milestone, release_condition bitmap, escrow_amount
- **PayAsYouGo**: max_amount_per_period, max_chunk_amount, period_length_seconds, current_period tracking

### PaymentFrequency Variants

Daily, Weekly, Monthly, Quarterly, SemiAnnually, Annually, Custom(u64)

### Fee Structure

- Protocol fee: 100 bps (1%) from ProgramConfig (or gateway custom override)
- Gateway fee: configurable bps (up to 10,000)
- Gross mode (default): fees deducted from amount
- Net mode (feature flag): fees added on top
- Referral rewards: subset of gateway fee, 3-tier distribution

### Feature Flags (PaymentGateway.feature_flags u8)

- bit 0 (0x01): Referral enabled
- bit 1 (0x02): Net amount mode
- bit 2 (0x04): Custom protocol fee override (protected, admin-only toggle)

### Milestone Release Conditions (bitmap u8)

- 0b0001: Check due date
- 0b0010: Gateway must sign
- 0b0100: Owner must sign
- 0b1000: Recipient must sign

### Instructions (17 total)

1. Initialize — create ProgramConfig
2. CreatePaymentGateway — business onboarding
3. DeletePaymentGateway
4. ChangeGatewayFeeRecipient
5. ChangeGatewaySigner
6. ChangeGatewayFeeBps
7. UpdateGatewayFeatureFlags
8. UpdateGatewayProtocolFee (admin + authority)
9. UpdateGatewayReferralSettings
10. CreateUserPayment — per user/mint
11. DeleteUserPayment — owner signs, requires 0 active policies
12. CreatePaymentPolicy — fee_payer signs, user doesn't
13. DeletePaymentPolicy — owner signs, rent to stored rent_payer
14. ChangePaymentPolicyStatus — Active <-> Paused
15. CreateReferralAccount — fee_payer signs, validates alphanumeric code
16. ExecutePayment — gateway signer OR owner OR recipient (PAYG only)
17. TransferTokens — standalone transfer with fee deduction

### Key Design Decisions

- User does NOT sign CreatePaymentPolicy or CreateUserPayment (fee_payer does)
- Manual close with CLOSE_DISCRIMINATOR (not Anchor's default close)
- policy_id is monotonic per UserPayment (never reused)
- Emergency pause blocks all execute_payment calls
- Transfer hook mints are rejected at UserPayment creation

## Composable Pull Payments (Next Phase)

Extends Tributary beyond simple SPL transfer to arbitrary CPI routing. Pulled tokens route into whitelisted programs (swap, LP, invest, etc.). See `references/composable-pull-architecture.md` for the full design and architecture comparison.

### Key Insight: Separate Account Type for Composable Policies

The composable pull layer should use its own account type (`ComposablePolicy`) with a common header, separate from the existing `PaymentPolicy`. Reasons:

1. **Padding tax** — Adding a composable variant to PolicyType would need >128 bytes for forward config + Lighthouse assertion params. Bumping VARIANT_SIZE increases rent for ALL existing policies.
2. **Conditions are a separate dimension** — Lighthouse assertions (oracle prices, balance thresholds, Merkle proofs) can apply to ANY policy type. Nesting them in the enum is combinatorial.
3. **Audit surface** — CPI + intermediate PDAs + ATA creation is fundamentally different from a clean SPL transfer.
4. **Solana Foundation pattern** — Their subscriptions program uses separate account types (FixedDelegation, RecurringDelegation, SubscriptionDelegation) all sharing a common 107-byte Header. Each type gets its own exact size with no wasted padding.

### Lighthouse Integration

Lighthouse is a runtime assertion Solana program that fails transactions when on-chain state diverges from expected conditions. Assertion types: AssertAccountInfo, AssertAccountData, AssertAccountDelta, AssertMintAccount, AssertTokenAccount, AssertStakeAccount, AssertSysvarClock. Multi-assertion instructions batch assertions to save tx space and compute.

For Tributary, Lighthouse enables programmable execution gates: oracle price conditions, balance thresholds, governance outcomes — anything on-chain can gate a pull. This belongs in a separate ConditionConfig section on ComposablePolicy, not embedded in the policy type enum.

## Solana Foundation Subscriptions (Reference Implementation)

Located at `subscriptions/` in the repo. Uses Pinocchio (no_std) + Codama for IDL generation. Key pattern: all delegation types share a 107-byte Header (discriminator + version + bump + delegator + delegatee + payer + init_id). AccountDiscriminator enum identifies concrete type at offset 0. Program ID: `De1egAFMkMWZSN5RvYXRj9CAdheBamobVNubTsi9avR44`.

## x402 Integration

Tributary powers HTTP 402 (Payment Required) for web micropayments. Three schemes: deferred (subscription), x402://payg (pay-as-you-go), x402://prepaid. Express middleware (`createX402Middleware`) handles JWT verification, payment processing, and access control. Metering utilities: TokenMeter, ComputeMeter for LLM/API usage tracking.

## React Frontend Integration

### Prerequisites

```bash
pnpm add @tributary-so/sdk @solana/wallet-adapter-react @solana/wallet-adapter-wallets
```

### Quick Start

```typescript
import { Tributary } from "@tributary-so/sdk";
import { useWallet } from "@solana/wallet-adapter-react";
import BN from "bn.js";

const sdk = new Tributary(connection, wallet);
const instructions = await sdk.createSubscription({
  tokenMint: USDC_MINT,
  recipient,
  gateway: GATEWAY_PUBKEY,
  amount: new BN(10_000_000),
  autoRenew: true,
  maxRenewals: 12,
  paymentFrequency: PaymentFrequency.Monthly,
  memo: encodeMemo("Monthly subscription", 64),
  executeImmediately: true,
});
```

### Policy Management

```typescript
sdk.pausePolicy(policyPda);
sdk.resumePolicy(policyPda);
sdk.cancelPolicy(policyPda);
sdk.getPaymentPoliciesByUserPayment(userPaymentPda);
```

### Configuration

```typescript
export const CONFIG = {
  programId: "TRibg8W8zmPHQqWtyAD1rEBRXEdyU13Mu6qX1Sg42tJ",
  usdcMint: new PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"),
  gateway: new PublicKey("GATEWAY_PUBKEY_HERE"),
  network: process.env.NEXT_PUBLIC_NETWORK || "mainnet",
};
```

## Build Commands

```bash
pnpm run lint          # Lint all workspaces
pnpm run lint:fix      # Auto-fix linting
anchor test            # Run Solana program tests
cd sdk && pnpm run build  # Build SDK
cd app && pnpm run dev    # Start dev server
make prep              # Setup Solana toolchain (v1.18.20, Anchor 0.31.0)
```

## Code Style

- TypeScript strict types, avoid `any` except Anchor wallet compat
- Solana imports first, then Anchor, then local
- camelCase variables/functions, PascalCase types/classes
- snake_case for Rust files, camelCase for TypeScript
- Prefer `accountsStrict()` over `accounts()` for type safety
- Use PDAs consistently with helpers from pda.ts

## References

- `references/composable-pull-architecture.md` — Composable pull payment design, Solana Foundation comparison, Lighthouse integration analysis
- AGENTS.md — Build/test commands, code style, architecture overview
- METEORA.md — DLMM integration spec (execute_delegate_to_program)
- "Composable Pull Payments on Solana.md" — Article draft with use cases and funding rationale
- PROJECT.md — Full project summary

## Hosted Documentation (tributary.so)

Full reference guides served from the landing page. Use `webfetch` to load on demand.

| Document             | URL                               | Scope                                                |
| -------------------- | --------------------------------- | ---------------------------------------------------- |
| SKILL.md (hub)       | tributary.so/SKILL.md             | Overview, quickstart, package index                  |
| SKILL-cli.md         | tributary.so/SKILL-cli.md         | CLI commands, parameters, workflows                  |
| SKILL-sdk.md         | tributary.so/SKILL-sdk.md         | Architecture, SDK/React/x402/Payments integration    |
| SKILL-composables.md | tributary.so/SKILL-composables.md | Composable anatomy, Lighthouse facade, ForwardConfig |
