---
name: solana-security
description: Audit Solana programs (Anchor or native Rust) for security vulnerabilities. Use when reviewing smart contract security, finding exploits, analyzing attack vectors, performing security assessments, or when explicitly asked to audit, review security, check for bugs, or find vulnerabilities in Solana programs.
---

# Solana Security Auditing

Systematic security review framework for Solana programs, supporting both Anchor and native Rust implementations.

## Review Process

Follow this systematic 5-step process for comprehensive security audits:

### Step 1: Initial Assessment

Understand the program's context and structure:

- **Framework**: Anchor vs Native Rust (check for `use anchor_lang::prelude::*`)
- **Anchor version**: Check `Cargo.toml` for compatibility and known issues
- **Dependencies**: Oracles (Pyth, Switchboard), external programs, token programs
- **Program structure**: Count instructions, identify account types, analyze state management
- **Complexity**: Lines of code, instruction count, PDA patterns
- **Purpose**: DeFi, NFT, governance, gaming, etc.

### Step 2: Systematic Security Review

For each instruction, perform security checks in this order:

1. **Account Validation** - Verify signer, owner, writable, and initialization checks
2. **Arithmetic Safety** - Check all math operations use `checked_*` methods
3. **PDA Security** - Validate canonical bumps and seed uniqueness
4. **CPI Security** - Ensure cross-program invocations validate target programs
5. **Oracle/External Data** - Verify price staleness and oracle status checks

**→ See [references/security-checklists.md](references/security-checklists.md) for detailed checklists**

### Step 3: Vulnerability Pattern Detection

Scan for common vulnerability patterns:

- Type cosplay attacks
- Account reloading issues
- Improper account closing
- Missing lamports checks
- PDA substitution attacks
- Arbitrary CPI vulnerabilities
- Missing ownership validation
- Integer overflow/underflow

**→ See [references/vulnerability-patterns.md](references/vulnerability-patterns.md) for code examples and exploit scenarios**

### Step 4: Architecture and Testing Review

Evaluate overall design quality:

- PDA design patterns and collision prevention
- Account space allocation and rent exemption
- Error handling approach and coverage
- Event emission for critical state changes
- Compute budget optimization
- Test coverage (unit, integration, fuzz)
- Upgrade strategy and authority management

### Step 5: Generate Security Report

Provide findings using this structure:

**Severity Levels:**

- 🔴 **Critical**: Funds can be stolen/lost, protocol completely broken
- 🟠 **High**: Protocol can be disrupted, partial fund loss possible
- 🟡 **Medium**: Suboptimal behavior, edge cases, griefing attacks
- 🔵 **Low**: Code quality, gas optimization, best practices
- 💡 **Informational**: Recommendations, improvements, documentation

**Finding Format:**

````markdown
## 🔴 [CRITICAL] Title

**Location:** `programs/vault/src/lib.rs:45-52`

**Issue:**
Brief description of the vulnerability

**Vulnerable Code:**

```rust
// Show the problematic code
```
````

**Exploit Scenario:**
Step-by-step explanation of how this can be exploited

**Recommendation:**

```rust
// Show the secure alternative
```

**References:**

- [Link to relevant documentation or similar exploits]

````

**Report Summary:**
- Total findings by severity
- Critical issues first (prioritize by risk)
- Quick wins (easy fixes with high impact)
- Recommendations for testing improvements

## Quick Reference

### Essential Checks (Every Instruction)

**Anchor:**
```rust
// ✅ Account validation with constraints
#[derive(Accounts)]
pub struct SecureInstruction<'info> {
    #[account(
        mut,
        has_one = authority,  // Relationship check
        seeds = [b"vault", user.key().as_ref()],
        bump,  // Canonical bump
    )]
    pub vault: Account<'info, Vault>,

    pub authority: Signer<'info>,  // Signer required

    pub token_program: Program<'info, Token>,  // Program validation
}

// ✅ Checked arithmetic
let total = balance.checked_add(amount)
    .ok_or(ErrorCode::Overflow)?;
````

**Native Rust:**

```rust
// ✅ Manual account validation
if !authority.is_signer {
    return Err(ProgramError::MissingRequiredSignature);
}

if vault.owner != program_id {
    return Err(ProgramError::IllegalOwner);
}

// ✅ Checked arithmetic
let total = balance.checked_add(amount)
    .ok_or(ProgramError::ArithmeticOverflow)?;
```

### Critical Anti-Patterns

❌ **Never Do:**

- Use `saturating_*` arithmetic methods (hide errors)
- Use `unwrap()` or `expect()` in production code
- Use `init_if_needed` without additional checks
- Skip signer validation ("they wouldn't call this...")
- Use unchecked arithmetic operations
- Allow arbitrary CPI targets
- Forget to reload accounts after mutations

✅ **Always Do:**

- Use `checked_*` arithmetic (`checked_add`, `checked_sub`, etc.)
- Use `ok_or(error)?` for Option unwrapping
- Use explicit `init` with proper validation
- Require `Signer<'info>` or `is_signer` checks
- Use `Program<'info, T>` for CPI program validation
- Reload accounts after external calls that mutate state
- Validate account ownership, discriminators, and relationships

## Framework-Specific Patterns

### Anchor Security Patterns

**→ See [references/anchor-security.md](references/anchor-security.md) for:**

- Account constraint best practices
- Common Anchor-specific vulnerabilities
- Secure CPI patterns with `CpiContext`
- Event emission and monitoring
- Custom error handling

### Native Rust Security Patterns

**→ See [references/native-security.md](references/native-security.md) for:**

- Manual account validation patterns
- Secure PDA derivation and signing
- Low-level CPI security
- Account discriminator patterns
- Rent exemption validation

## Modern Practices (2025)

- **Use Anchor 0.30+** for latest security features
- **Implement Token-2022** with proper extension handling
- **Use `InitSpace` derive** for automatic space calculation
- **Emit events** for all critical state changes
- **Write fuzz tests** with Trident framework
- **Document invariants** in code comments
  - **Follow progressive roadmap**: Dev → Audit → Testnet → Audit → Mainnet

## Advent of Bugs Day Series - Common Security Issues

The @accretion_xyz Twitter account runs an "Advent of Bugs" series where they tweet about one Solana security bug each day for 24 days leading to Christmas. Based on Advent of Code patterns, these bugs commonly fall into these categories:

### Type Cosplay Attacks

**🔴 CRITICAL**

**Bug: PDA Type Confusion**

````markdown
## 🐛 PDA Type Cosplay - Invalid Account Type Passed to CPI

**Vulnerable Code:**

```rust
// ❌ WRONG: Trusts CPI target account type without validation
invoke_instruction(
    &vault_account,  // Could be ANY account type
    &mut,
    &[SystemProgramId::from(vault_program_id)],
)?;

// Attacker passes malicious PDA that mimics expected type
// but has different internal structure - exploits CPI logic
```
````

**Exploit Scenario:**
Attacker creates a malicious PDA that matches the expected discriminator (first 8 bytes) but has completely different internal structure. When the target program validates `account_type` discriminator or uses it for indexing, the mismatch causes unexpected behavior or allows bypassing of checks.

**Secure Alternative:**

```rust
// ✅ CORRECT: Validate PDA account type with discriminator check
#[derive(Accounts)]
pub struct Transfer<'info> {
    #[account(mut)]
    from: Signer<'info>,

    #[account(
        address = vault_program_id,
        // CRITICAL: Enforce this is a Vault account
        // The CPI checks is_signer before invoking
    )]
    vault: Account<'info, Vault>,

    // Additional type-safe wrapper
}

pub fn validate_and_transfer(
    ctx: Context<'_, '_, '_, Transfer<'info>>,
    from: &Account<'info, Signer<'info>>,
    to: &AccountInfo,
    amount: u64,
) -> Result<()> {
    // CPI will fail if `to` is not a valid Vault account
    accounts::transfer(ctx, from, to, amount)?;

    Ok(())
}
```

**Detection:**

- ❌ Missing discriminator validation before CPI invocation
- ❌ Using generic `&AccountInfo` instead of specific account types
- ✅ Pattern: Derive separate account types for each expected PDA variant

---

**Bug: Anchor Account Constraint Bypass**

````markdown
## 🐛 Anchor Constraint Bypass - Skipping has_one Constraint

**Vulnerable Code:**

```rust
// ❌ WRONG: Manually passes accounts without Anchor's automatic validation
pub fn vulnerable_withdraw(
    ctx: Context<'_, '_, '_, '_, '_, Withdraw>,
    authority: &Signer<'info>,
    vault: &Account<'info, Vault>,  // Should have has_one constraint
    amount: u64,
) -> Result<()> {
    // ❌ No constraint check - Anchor doesn't validate has_one automatically
    // when accounts.withdraw is called
    // if vault and authority point to different vaults - both can be passed!

    vault.authority = *authority.key;
    **vault.withdraw(ctx, vault, authority, amount)?**
}

// Anchor.toml
#[derive(Accounts)]
pub struct Withdraw<'info> {
    #[account(mut)]
    authority: Signer<'info>,

    // ❌ Missing: has_one constraint
    // ❌ Missing: init_if_needed if should enforce single use
}
```
````

**Exploit Scenario:**
Attacker creates two different "vault" accounts (with same discriminator but different seeds) and rapidly switches between them. Because Anchor doesn't enforce `has_one` at the instruction level, both can be used simultaneously, allowing parallel exploitation or draining funds.

**Secure Alternative:**

```rust
// ✅ CORRECT: Use Anchor's has_one constraint properly
#[derive(Accounts)]
pub struct Withdraw<'info> {
    #[account(mut)]
    authority: Signer<'info>,

    // ✅ CRITICAL: Enforce single vault at a time
    #[account(
        address = vault_program_id,
        has_one = vault,  // Single active vault instance
    )]
    vault: Account<'info, Vault>,

    // Optional: only allow reinitialization with new authority
    #[account(
        init_if_needed,
        seeds = [authority.key().as_ref()],
    )]
    vault_state: Option<Account<'info, VaultState>>,
}

pub fn secure_withdraw(
    ctx: Context<'_, '_, '_, '_, Withdraw>,
    authority: &Signer<'info>,
    vault: &Account<'info, Vault>,
    vault_state: Option<&Account<'info, VaultState>>,
    amount: u64,
) -> Result<()> {
    // Anchor automatically validates has_one constraint
    accounts::withdraw(ctx, authority, vault, vault_state, amount)?;

    Ok(())
}
```

**Detection:**

- ❌ Missing `has_one` constraint for singleton accounts
- ❌ No `init_if_needed` to enforce reinitialization rules
- ✅ Pattern: Use Anchor's built-in constraints, don't bypass them manually

---

### Account Validation Issues

**🟠 HIGH**

**Bug: Missing Signer Authority Check**

````markdown
## 🐛 Missing Authority Check - Privilege Escalation

**Vulnerable Code:**

```rust
// ❌ WRONG: Function doesn't verify account.signer relationship
pub fn vulnerable_function(
    ctx: Context<'_, '_, '_, '_, MyAccount>,
    my_account: &Account<'info, MyAccount>,  // Attacker controlled account
) -> Result<()> {
    // ❌ No is_signer check
    // Anyone who owns the account can invoke instruction
    // Even if they didn't sign the transaction

    dangerous_action(ctx, my_account)?;
}

// ❌ WRONG: Missing Signer<'info> constraint
#[derive(Accounts)]
pub struct MyAccount {
    #[account(mut)]  // ❌ No signer constraint
    data: u64,
}
```
````

**Exploit Scenario:**
If an account can be created without requiring a signer, or if the `is_signer` check is missing, attackers can create controlled accounts that bypass authorization requirements. This is particularly dangerous if combined with missing owner validation.

**Secure Alternative:**

```rust
// ✅ CORRECT: Always enforce signer requirements
#[derive(Accounts)]
pub struct MyAccount {
    #[account(
        mut,
        // ✅ CRITICAL: Must be signer
        // Optional: seeds to validate signer relationship
    )]
    authority: Signer<'info>,
    data: u64,
}

// ✅ Alternative: Verify owner manually if needed
pub fn secure_function(
    ctx: Context<'_, '_, '_, '_, MyAccount>,
    my_account: &Account<'info, MyAccount>,
) -> Result<()> {
    // Verify this account was authorized
    require!(
        my_account.authority == *ctx.accounts.authority.key,
        SecurityError::UnauthorizedAccess
    );

    dangerous_action(ctx, my_account)?;
}
```

**Detection:**

- ❌ Functions accept any account without verifying signer status
- ❌ Missing `Signer<'info>` or `is_signer` constraints
- ✅ Pattern: Always validate signer authority before privileged operations

---

**Bug: Missing Owner Validation**

````markdown
## 🐛 Owner Validation Bypass - Unauthorized State Modification

**Vulnerable Code:**

```rust
// ❌ WRONG: Anyone can modify account if they're the "owner"
pub struct Vault {
    pub owner: Pubkey,  // ❌ No constraint - anyone can pass any pubkey
    pub balance: u64,
}

pub fn vulnerable_withdraw(
    ctx: Context<'_, '_, '_, Vault>,
    authority: Pubkey,  // ❌ Passed directly, no validation
    vault: &mut Vault,
    amount: u64,
) -> Result<()> {
    // ❌ No owner check - any authority can drain vault
    require!(
        vault.owner == authority,  // This check is useless if owner wasn't validated at init
        VaultError::InvalidOwner
    );

    vault.balance -= amount;
    Ok(())
}
```
````

**Exploit Scenario:**
Attackers call `withdraw` passing their own pubkey as `authority`. Since there's no constraint ensuring `authority` was actually set to the true owner during initialization, the check passes and funds are drained.

**Secure Alternative:**

```rust
// ✅ CORRECT: Use Signer constraint and validate at initialization
#[derive(Accounts)]
pub struct Vault {
    #[account(
        init,
        // ✅ Owner must be signer to set initially
    )]
    owner: Signer<'info>,

    pub balance: u64,
}

pub fn new_vault(
    ctx: Context<'_, '_, '_, Vault>,
    owner: Signer<'info>,
) -> Result<()> {
    // ✅ Set owner during initialization
    let vault = Vault {
        owner: *owner.key,
        balance: 0,
    };

    accounts::vault_init(ctx, owner, vault)?;
    Ok(())
}

pub fn secure_withdraw(
    ctx: Context<'_, '_, Vault>,
    owner: &Signer<'info>,  // ✅ Only owner can withdraw
    vault: &mut Vault,
    amount: u64,
) -> Result<()> {
    // ✅ Owner is enforced by Signer constraint
    require!(
        vault.owner == *owner.key,
        VaultError::InvalidOwner
    );

    vault.balance -= amount;
    Ok(())
}
```

**Detection:**

- ❌ Owner field without Signer constraint
- ❌ Missing validation at initialization that owner was signer
- ✅ Pattern: Owner must be Signer and set during init

---

### Arithmetic Safety Issues

**🟠 HIGH**

**Bug: Integer Overflow/Underflow**

````markdown
## 🐛 Arithmetic Overflow - Value Manipulation

**Vulnerable Code:**

```rust
// ❌ WRONG: Unchecked arithmetic operations
pub fn vulnerable_transfer(
    from: &mut Account,
    to: &mut Account,
    amount: u64,
) -> Result<()> {
    // ❌ Can overflow silently
    from.balance -= amount;    // Underflow to zero
    to.balance += amount;     // Overflow to max value

    Ok(())
}

// ❌ WRONG: Casting without overflow checks
pub fn vulnerable_multiply(
    value: u64,
    multiplier: u64,
) -> Result<u64> {
    // ❌ No overflow check
    Ok(value * multiplier)  // Can wrap around
}
```
````

**Exploit Scenario:**
Attackers manipulate amounts to cause arithmetic underflow (balance goes negative, but since it's unsigned, it wraps to a very large number) or overflow (balance becomes max value). This allows:

- Draining accounts by underflowing balances
- Creating infinite tokens through overflow
- Bypassing balance checks that should fail

**Secure Alternative:**

```rust
// ✅ CORRECT: Use Solana's checked arithmetic
use solana_program::account_info::AccountInfo;
use anchor_lang::prelude::*;

pub fn secure_transfer(
    from: &mut Account,
    to: &mut Account,
    amount: u64,
) -> Result<()> {
    // ✅ Check for underflow
    from.balance = from.balance.checked_sub(amount)
        .ok_or(SecurityError::Underflow)?;

    // ✅ Check for overflow
    to.balance = to.balance.checked_add(amount)
        .ok_or(SecurityError::Overflow)?;

    Ok(())
}

// ✅ Alternative: Use safe arithmetic wrapper
#[error_code]
pub enum SecurityError {
    #[error("Arithmetic underflow")]
    Underflow,
    #[error("Arithmetic overflow")]
    Overflow,
}
```

**Detection:**

- ❌ Using `-`, `+=`, `-=` operators on unsigned types
- ❌ No checked arithmetic for financial operations
- ✅ Pattern: Always use `checked_*` methods or `ok_or()` wrappers

---

### Oracle/External Data Issues

**🟡 MEDIUM**

**Bug: Stale Oracle Data Exploitation**

````markdown
## 🐛 Stale Oracle - Price Manipulation

**Vulnerable Code:**

```rust
// ❌ WRONG: Using oracle price without staleness check
pub fn vulnerable_swap(
    ctx: Context<'_, '_, PriceOracle>,
    amount: u64,
) -> Result<()> {
    let price = accounts::get_price(ctx, oracle)?;

    // ❌ No staleness check - attacker can manipulate price
    // and profit from stale data

    let calculated_amount = amount * price;
    accounts::execute_swap(ctx, calculated_amount)?;

    Ok(())
}

// ❌ WRONG: Ignoring oracle status flags
#[derive(Accounts)]
pub struct PriceOracle {
    #[account()]
    pub price: u64,
    pub last_update: i64,  // ❌ Timestamp not checked
    pub is_frozen: bool,
}
```
````

**Exploit Scenario:**
Oracle providers have outages or delayed updates. Attackers front-run the delay or submit transactions with stale prices, then benefit from price differences. This is particularly dangerous for:

- DeFi protocols using price feeds
- Staking protocols with variable rewards
- Liquidation protocols

**Secure Alternative:**

```rust
// ✅ CORRECT: Implement staleness checks and status validation
const MAX_PRICE_AGE_SECONDS: u64 = 300; // 5 minutes

#[derive(Accounts)]
pub struct PriceOracle {
    #[account()]
    pub price: u64,
    pub last_update: i64,  // ✅ Track update time
    pub is_frozen: bool,     // ✅ Respect frozen status
}

pub fn secure_swap(
    ctx: Context<'_, '_, PriceOracle>,
    amount: u64,
) -> Result<()> {
    let oracle = accounts::get_price(ctx, oracle)?;

    // ✅ Check if price is stale
    let clock = Clock::get()?;
    let price_age = clock.unix_timestamp - oracle.last_update;

    require!(
        price_age <= MAX_PRICE_AGE_SECONDS,
        SecurityError::StalePrice
    );

    require!(
        !oracle.is_frozen,
        SecurityError::OracleFrozen
    );

    let calculated_amount = amount * oracle.price;
    accounts::execute_swap(ctx, calculated_amount)?;

    Ok(())
}
```

**Detection:**

- ❌ No timestamp validation for oracle data
- ❌ Ignoring `is_frozen` or similar status flags
- ✅ Pattern: Always validate price staleness and respect oracle status

---

### PDA Derivation Issues

**🟠 HIGH**

**Bug: PDA Seed Manipulation**

````markdown
## 🐛 PDA Seed Manipulation - Account Hijacking

**Vulnerable Code:**

```rust
// ❌ WRONG: User-provided seeds without validation
pub fn vulnerable_create_vault(
    ctx: Context<'_, '_, '_, '_, Vault>,
    seed: Vec<u8>,  // ❌ User controls - could guess
    bump: u8,
) -> Result<()> {
    // ❌ Derive PDA from user seed - attacker can collide
    let (pda, _bump) = Pubkey::find_program_address(
        ctx.program_id,
        &ctx.accounts.signer.key(),
        &[seed.as_slice(), b"vault_seed"],
        bump,
    );

    // Attack provides malicious seeds to get PDA of YOUR vault
    // Then drains it

    let vault_data = Vault {
        authority: *ctx.accounts.signer.key(),
        balance: MAX_U64,
    };

    ctx.accounts.vault.create(vault_data)?;
    Ok(())
}
```
````

**Exploit Scenario:**
Attackers craft seeds that produce the same PDA address as a legitimate vault. When they call instructions targeting that PDA, the program operates on the attacker's account instead of the legitimate one. This allows:

- Account hijacking and draining
- Overwriting legitimate PDAs
- Accessing sensitive data

**Secure Alternative:**

```rust
// ✅ CORRECT: Use canonical bumps and validate seed sources
use anchor_lang::prelude::*;
use solana_program::system_program;

// ✅ Use program ID + constant for canonical bump
#[derive(Accounts)]
pub struct CreateVault<'info> {
    #[account(mut)]
    authority: Signer<'info>,

    #[account(
        init,
        seeds = [authority.key().as_ref()],
        bump,
        // ✅ Canonical bump seeds prevent PDA collision attacks
    )]
    vault: Account<'info, Vault>,
}

pub fn secure_create_vault(
    ctx: Context<'_, '_, '_, CreateVault>,
    authority: &Signer<'info>,
    bump: u8,
) -> Result<()> {
    let (pda, _bump) = Pubkey::find_program_address(
        ctx.program_id,
        &[
            authority.key().as_ref(),  // ✅ Use signer as seed
            b"vault_v1"                       // ✅ Use versioned constant seed
        ],
        bump,
    );

    // ✅ Validate no existing vault exists first
    let vault = Vault {
        authority: *authority.key(),
        balance: 0,
    };

    // This fails if vault already exists (PDA collision check)
    accounts::vault_init(ctx, authority, bump, vault)?;

    Ok(())
}

// ✅ Alternative: Use init if needed with authority check
// When creating PDAs, validate that:
// 1. PDA derivation uses correct seeds
// 2. Authority/signer validated before creation
// 3. Check for duplicate PDAs if security-critical
```

**Detection:**

- ❌ Using user-controlled or predictable seeds
- ❌ Missing canonical bump seeds (`b"constant_name"`)
- ❌ No validation for existing PDA before creation
- ✅ Pattern: Always use signer seeds + constant bump seeds, validate existence

---

## Key Takeaways for Auditing

When reviewing code that implements Advent of Bugs patterns, watch for:

1. **Anchor Constraint Bypass**: Programs manually managing accounts instead of using Anchor's built-in constraints (`has_one`, `seeds`)
2. **Missing Authority Checks**: Functions that don't verify signer/owner relationships
3. **Unchecked Arithmetic**: Using `-`, `+=` operators instead of `checked_*` methods
4. **Stale Oracle Data**: Using external data without timestamp or status validation
5. **PDA Manipulation**: User-provided seeds or missing canonical bumps
6. **Account Confusion**: Missing discriminator validation or type checking

**Reference**: @accretion_xyz's "Advent of Bugs" series provides real-world examples of these vulnerabilities. Use the solana-development skill alongside this security skill when reviewing bugs: https://github.com/accretion-xyz/simple-program-monitoring

**Severity Classification**: 🔴 CRITICAL vulnerabilities can drain funds; 🟠 HIGH vulnerabilities can disrupt protocol; 🔵 MEDIUM vulnerabilities cause suboptimal behavior

## Security Fundamentals

**→ See [references/security-fundamentals.md](references/security-fundamentals.md) for:**

- Security mindset and threat modeling
- Core validation patterns (signers, owners, mutability)
- Input validation best practices
- State management security
- Arithmetic safety
- Re-entrancy considerations

## Common Vulnerabilities

**→ See [references/vulnerability-patterns.md](references/vulnerability-patterns.md) for:**

- Missing signer validation
- Integer overflow/underflow
- PDA substitution attacks
- Account confusion
- Arbitrary CPI
- Type cosplay
- Improper account closing
- Precision loss in calculations

Each vulnerability includes:

- ❌ Vulnerable code example
- 💥 Exploit scenario
- ✅ Secure alternative
- 📚 References

## Security Checklists

**→ See [references/security-checklists.md](references/security-checklists.md) for:**

- Account validation checklist
- Arithmetic safety checklist
- PDA and account security checklist
- CPI security checklist
- Oracle and external data checklist
- Token integration checklist

## Known Issues and Caveats

**→ See [references/caveats.md](references/caveats.md) for:**

- Solana-specific quirks and gotchas
- Anchor framework limitations
- Testing blind spots
- Common misconceptions
- Version-specific issues

## Security Resources

**→ See [references/resources.md](references/resources.md) for:**

- Official security documentation
- Security courses and tutorials
- Vulnerability databases
- Audit report examples
- Security tools (Trident, fuzzers)
- Security firms and auditors

## Key Questions for Every Audit

Always verify these critical security properties:

1. **Can an attacker substitute accounts?**
   - PDA validation, program ID checks, has_one constraints

2. **Can arithmetic overflow or underflow?**
   - All math uses checked operations, division by zero protected

3. **Are all accounts properly validated?**
   - Owner, signer, writable, initialized checks present

4. **Can the program be drained?**
   - Authorization checks, reentrancy protection, account confusion prevention

5. **What happens in edge cases?**
   - Zero amounts, max values, closed accounts, expired data

6. **Are external dependencies safe?**
   - Oracle validation (staleness, status), CPI targets verified, token program checks

## Audit Workflow

### Before Starting

1. Understand the protocol purpose and mechanics
2. Review documentation and specifications
3. Set up local development environment
4. Run existing tests and check coverage

### During Audit

1. Follow the 5-step review process systematically
2. Document findings with severity and remediation
3. Create proof-of-concept exploits for critical issues
4. Test fixes and verify they work

### After Audit

1. Present findings clearly prioritized by severity
2. Provide actionable remediation steps
3. Re-audit after fixes are implemented
4. Document lessons learned for the protocol

## Testing for Security

Beyond code review, validate security through testing:

- **Unit tests**: Test each instruction's edge cases
- **Integration tests**: Test cross-instruction interactions
- **Fuzz testing**: Use Trident to discover unexpected behaviors
- **Exploit scenarios**: Write POCs for found vulnerabilities
- **Upgrade testing**: Verify migration paths are secure

## Core Principle

**In Solana's account model, attackers can pass arbitrary accounts to any instruction.**

Security requires explicitly validating:

- ✅ Every account's ownership
- ✅ Every account's type (discriminator)
- ✅ Every account's relationships
- ✅ Every account's state
- ✅ Every signer requirement
- ✅ Every arithmetic operation
- ✅ Every external call

There are no implicit guarantees. **Validate everything, trust nothing.**

---

## Solana-Specific Vulnerabilities from Security Auditor

**Reference**: @agent/security-auditor.md - Comprehensive vulnerability analysis for Solana protocols

### Critical Solana Vulnerability Patterns

The following vulnerabilities are extracted from professional security audits and align with Advent of Bugs findings:

#### S01: Missing Signer Checks 🔴 CRITICAL

**Description**: Failing to verify that required accounts are signers allows unauthorized actions.

**Vulnerable Code:**

```rust
pub fn vulnerable_update(ctx: Context<UpdateBalance>, new_balance: u64) -> Result<()> {
    let account = &mut ctx.accounts.user_account;
    account.balance = new_balance; // No signer check
    Ok(())
}
```

**Secure Alternative:**

```rust
#[derive(Accounts)]
pub struct UpdateBalance<'info> {
    #[account(mut, signer)] // Enforces signer requirement
    pub user_account: Account<'info, UserAccount>,
}

pub fn secure_update(ctx: Context<UpdateBalance>, new_balance: u64) -> Result<()> {
    let account = &mut ctx.accounts.user_account;
    account.balance = new_balance;
    Ok(())
}
```

**Detection Patterns:**

- ❌ Functions modify state without `Signer<'info>` or `is_signer` checks
- ❌ Missing `#[account(signer)]` constraint in account structs
- ✅ Pattern: Always enforce signer requirements for privileged operations

---

#### S02: Incorrect PDA Derivation 🟠 HIGH

**Description**: Using wrong seeds or bumps for PDA creation allows collisions or unauthorized access.

**Vulnerable Code:**

```rust
pub fn create_pda(ctx: Context<CreatePda>, user: Pubkey) -> Result<()> {
    let (pda, _bump) = Pubkey::find_program_address(
        ctx.program_id,
        &[user.as_ref(), b"user"], // Wrong seeds, can collide
        ctx.program_id,
    );
    // Attacker provides malicious seeds to get PDA of YOUR account
    Ok(())
}
```

**Secure Alternative:**

```rust
#[derive(Accounts)]
pub struct CreatePda<'info> {
    #[account(
        init,
        seeds = [authority.key().as_ref()], // Use signer as seed
        bump, // Canonical bump prevents collision
    )]
    pub pda_account: Account<'info, PdaAccount>,
}

pub fn create_pda(ctx: Context<CreatePda>, bump: u8) -> Result<()> {
    let (pda, _bump) = Pubkey::find_program_address(
        ctx.program_id,
        &[
            authority.key().as_ref(),  // Signer-controlled
            b"pda_v1", // Versioned constant prevents replay
        ],
        bump,
    );
    Ok(())
}
```

**Detection Patterns:**

- ❌ Using user-controlled or predictable seeds
- ❌ Missing canonical bump seeds (e.g., `b"constant_name"`)
- ❌ No validation for existing PDA before creation
- ✅ Pattern: Use signer seeds + constant bump seeds, validate existence

---

#### S04: Reinitialization Attacks 🟠 HIGH

**Description**: Allowing accounts to be reinitialized after creation enables state manipulation.

**Vulnerable Code:**

```rust
pub fn init_account(ctx: Context<InitAccount>) -> Result<()> {
    let account = &mut ctx.accounts.user_account;
    account.balance = 0; // Can be called multiple times
    Ok(())
}
```

**Secure Alternative:**

```rust
#[derive(Accounts)]
pub struct InitAccount<'info> {
    #[account(init, payer = user)] // One-time initialization
    pub user_account: Account<'info, UserAccount>,
}

pub fn init_account(ctx: Context<InitAccount>) -> Result<()> {
    let account = &mut ctx.accounts.user_account;
    account.balance = 0;
    Ok(())
}

// If account exists, Anchor automatically rejects reinitialization
```

**Detection Patterns:**

- ❌ Missing `init` constraint on account structs
- ❌ Functions don't check if account was already initialized
- ✅ Pattern: Use `#[account(init)]` for one-time creation, no `init_if_needed` without checks

---

#### S08: Front-Running and MEV 🟡 MEDIUM

**Description**: Exploiting transaction ordering in Solana's mempool to gain advantage.

**Vulnerable Code:**

```rust
pub fn swap(ctx: Context<Swap>, amount: u64) -> Result<()> {
    // Direct swap, vulnerable to front-running
    transfer_tokens(ctx, from, to, amount)?;
    Ok(())
}
```

**Secure Alternative:**

```rust
pub fn swap(
    ctx: Context<Swap>,
    amount: u64,
    slippage_bps: u16, // Accept slippage tolerance
    deadline: i64, // Time limit for valid execution
) -> Result<()> {
    // Slippage protection prevents front-running exploitation
    transfer_tokens(ctx, from, to, amount)?;
    Ok(())
}
```

**Detection Patterns:**

- ❌ No slippage protection in swap functions
- ❌ Transactions that can be observed in mempool before execution
- ✅ Pattern: Implement slippage parameters, use commit-reveal or private mempools

---

#### S17: Sysvar Address Checking 🟠 HIGH

**Description**: Not validating sysvar accounts allows for fake accounts to manipulate protocol state.

**Vulnerable Code:**

```rust
pub fn check_sysvar(ctx: Context<CheckSysvar>, sysvar_key: Pubkey) -> Result<()> {
    msg!("Rent Key -> {}", sysvar_key); // Logs arbitrary key
    Ok(())
}

// No validation that sysvar_key actually belongs to sysvar program
```

**Secure Alternative:**

```rust
use anchor_lang::prelude::*;
use solana_program::sysvar;

#[derive(Accounts)]
pub struct CheckSysvar<'info> {
    #[account()]
    pub clock: Sysvar<'info, Clock>, // Hardcoded to correct sysvar
}

pub fn check_sysvar(ctx: Context<CheckSysvar>) -> Result<()> {
    let clock = Clock::get()?;

    // Anchor validates sysvar account ownership automatically
    msg!("Current slot: {}", clock.slot);
    Ok(())
}
```

**Detection Patterns:**

- ❌ Accepting arbitrary sysvar addresses without validation
- ❌ Manually logging sysvar keys instead of using Sysvar<'info>
- ✅ Pattern: Use Anchor's Sysvar<'info> for automatic validation

---

#### S19: Exit Logic Pitfalls 🟡 MEDIUM

**Description**: Using incorrect comparison operators (`<=`, `>=`) when checking sequential operations can allow jumps.

**Vulnerable Code:**

```rust
pub fn process_epoch(ctx: Context<Epoch>, epoch: u64) -> Result<()> {
    let state = &ctx.accounts.user_state;

    // ❌ Using <= allows jumping to any epoch
    if state.last_processed_epoch <= epoch {
        // Process can skip validation
        process_yield(ctx, epoch)?;
    }

    state.last_processed_epoch = epoch;
    Ok(())
}
```

**Secure Alternative:**

```rust
pub fn process_epoch(ctx: Context<Epoch>, epoch: u64) -> Result<()> {
    let state = &mut ctx.accounts.user_state;

    // ✅ Validate first operation explicitly
    if state.last_processed_epoch == 0 && epoch != 1 {
        return Err(ErrorCode::InvalidFirstEpoch);
    }

    // ✅ Enforce strict sequential processing
    if state.last_processed_epoch > 0 && epoch != state.last_processed_epoch + 1 {
        return Err(ErrorCode::InvalidEpochSequence);
    }

    state.last_processed_epoch = epoch;
    Ok(())
}
```

**Detection Patterns:**

- ❌ Using `<=` or `>=` for state transitions instead of `==` or explicit checks
- ❌ Missing validation for initial state (e.g., `last_processed_epoch == 0`)
- ✅ Pattern: Validate state transitions explicitly, use `==` for exact matches

---

#### S21: Sequential Validation Gaps 🟡 MEDIUM

**Description**: Failing to validate initial operations while enforcing later sequential processing enables exploit paths.

**Vulnerable Code:**

```rust
pub fn process_claim(ctx: Context<Claim>, epoch: u64) -> Result<()> {
    let state = &ctx.accounts.user_state;

    // First claim is always allowed (no validation)
    // ❌ This allows exploits in later epochs
    claim_rewards(ctx, epoch)?;

    state.last_claimed_epoch = epoch;
    Ok(())
}
```

**Secure Alternative:**

```rust
pub fn process_claim(ctx: Context<Claim>, epoch: u64) -> Result<()> {
    let state = &mut ctx.accounts.user_state;

    // ✅ Validate first claim explicitly
    if state.last_claimed_epoch == 0 && epoch != 1 {
        return Err(ErrorCode::InvalidFirstClaim);
    }

    claim_rewards(ctx, epoch)?;

    state.last_claimed_epoch = epoch;
    Ok(())
}
```

**Detection Patterns:**

- ❌ Missing validation for initial state before processing
- ❌ Allowing state changes without checking starting conditions
- ✅ Pattern: Always validate initial state, use explicit checks for all operations

---

#### S24: Solana-Specific Additional Vulnerabilities

**S24.1: Account Reloading** 🟠 HIGH

**Description**: Anchor accounts don't automatically refresh after CPI calls, leading to stale state usage.

**Vulnerable Code:**

```rust
pub fn mint_to(ctx: Context<MintTo>, authority: Pubkey) -> Result<()> {
    let mint_to = &ctx.accounts.mint_to;

    // Check balance before CPI
    let balance_before = mint_to.balance;

    anchor_spl::token::mint_to(ctx, authority, amount)?;

    // ❌ Mint_to.balance is stale - balance changed in CPI
    let balance_after = mint_to.balance; // Stale value
    emit_event(balance_after); // Wrong emission
}
```

**Secure Alternative:**

```rust
pub fn mint_to(ctx: Context<MintTo>, authority: Pubkey) -> Result<()> {
    let mint_to = &ctx.accounts.mint_to;

    // Check balance before CPI
    let balance_before = mint_to.balance;

    anchor_spl::token::mint_to(ctx, authority, amount)?;

    // ✅ Reload account after CPI to get fresh state
    mint_to.reload(ctx)?;
    let balance_after = mint_to.balance; // Fresh value
    emit_event(balance_after); // Correct emission
}
```

**Detection Patterns:**

- ❌ Using stale account data after CPI without reloading
- ❌ Relying on pre-CPI account state for post-CPI operations
- ✅ Pattern: Always reload accounts after CPI that mutate state

---

### Integration with Existing Content

These Solana-specific vulnerabilities complement the vulnerability patterns documented elsewhere in this skill:

- **Missing Signer Checks**: See [Account Validation Issues](#account-validation-issues) section
- **PDA Security**: See [PDA Derivation Issues](#pda-derivation-issues) section
- **Arithmetic Safety**: See [Arithmetic Safety Issues](#arithmetic-safety-issues) section
- **Account Lifecycle**: See [Account Lifecycle Mismanagement](#account-lifecycle-mismanagement) section

**Key Takeaways:**

1. **Solana Account Model**: Attackers can pass arbitrary accounts to any instruction—validate everything
2. **Anchor vs Native**: Anchor provides automatic validation, but doesn't prevent all mistakes
3. **CPI Reloading**: Always reload accounts after external calls that mutate state
4. **Sysvar Validation**: Use Anchor's `Sysvar<'info>` for automatic ownership checks
5. **Sequential State**: Enforce explicit validation for state transitions to prevent jumps
