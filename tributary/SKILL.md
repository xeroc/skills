# React Tributary Subscriptions Integration

Integrate Tributary recurring payments into any React app. Simple SDK-based approach - connect wallet, create policies, protocol handles execution automatically.

## Use When

You need to add subscription/recurring payment buttons to an existing React application. User wants to set up automated payments with one-time approval and trustless execution.

## Prerequisites

```bash
# Install Tributary SDK
pnpm add @tributary-so/sdk

# Install Solana wallet adapter
pnpm add @solana/wallet-adapter-react @solana/wallet-adapter-wallets
```

## Quick Start

```typescript
import { Tributary } from "@tributary-so/sdk";
import { useWallet } from "@solana/wallet-adapter-react";
import BN from "bn.js";

function SubscriptionButton({ recipient, amount }) {
  const { publicKey } = useWallet();
  const connection = useConnection();

  if (!publicKey) return <button>Connect Wallet</button>;

  const sdk = new Tributary(connection, wallet);

  const handleClick = async () => {
    const instructions = await sdk.createSubscription(
      tokenMint: USDC_MINT,
      recipient,
      gateway: GATEWAY_PUBKEY,
      amount: new BN(amount * 1_000_000), // USDC has 6 decimals
      autoRenew: true,
      maxRenewals: null,
      paymentFrequency: PaymentFrequency.Weekly,
      memo: encodeMemo("Weekly subscription", 64),
      executeImmediately: true
    );

    // Build and send transaction
    const tx = new Transaction().add(...instructions);
    const signature = await wallet.signTransaction(tx);
    await connection.sendTransaction(tx);
  };

  return <button onClick={handleClick}>Subscribe ${amount}/week</button>;
}
```

## Core Concepts

### One-Time Setup, Forever Automation

Tributary uses token delegation for automated payments:

1. **User approves once** - Delegate authority to Tributary PDAs for total amount
2. **Protocol executes** - Payments run automatically on schedule
3. **User stays in control** - Pause/resume/cancel anytime via on-chain state

### No Backend Required

Everything happens client-side:

- SDK creates on-chain policies
- Protocol executes payments via gateway
- Your app reads state to show status
- Zero infrastructure needed

## Component Patterns

### Basic Subscribe Button

```tsx
import { Tributary } from "@tributary-so/sdk";
import BN from "bn.js";

export function SubscribeButton({ amount, recipient }: Props) {
  const sdk = useTributary();

  const subscribe = async () => {
    const instructions = await sdk.createSubscription(
      tokenMint: USDC_MINT,
      recipient: new PublicKey(recipient),
      gateway: GATEWAY_PUBKEY,
      amount: new BN(amount * 1_000_000),
      autoRenew: true,
      maxRenewals: 12,
      paymentFrequency: PaymentFrequency.Monthly,
      memo: encodeMemo("Monthly subscription", 64),
      executeImmediately: true
    );

    await sendTransaction(instructions);
  };

  return (
    <button
      onClick={subscribe}
      className="bg-blue-500 text-white px-4 py-2 rounded"
    >
      Subscribe ${amount}/month
    </button>
  );
}
```

### Subscription with Referral Code

```tsx
const subscribeWithReferral = async () => {
  const instructions = await sdk.createSubscription({
    tokenMint: USDC_MINT,
    recipient: RECIPIENT_PUBKEY,
    gateway: GATEWAY_PUBKEY,
    amount: new BN(50_000_000),
    autoRenew: true,
    maxRenewals: null,
    paymentFrequency: PaymentFrequency.Weekly,
    memo: encodeMemo("Referral subscription", 64),
    referralCode: "ABC123", // 6-char code
  });

  await sendTransaction(instructions);
};
```

### Pay-As-You-Go Button

```tsx
export function PayAsYouGoButton({ maxAmount }: Props) {
  const subscribe = async () => {
    const instructions = await sdk.createPayAsYouGo({
      tokenMint: USDC_MINT,
      recipient: RECIPIENT_PUBKEY,
      gateway: GATEWAY_PUBKEY,
      maxAmountPerPeriod: new BN(maxAmount * 1_000_000),
      maxChunkAmount: new BN(10_000_000),
      periodLengthSeconds: new BN(60 * 60 * 24 * 30), // 30 days
      memo: encodeMemo("Pay-as-you-go", 64),
    });

    await sendTransaction(instructions);
  };

  return <button onClick={subscribe}>Top up {maxAmount}</button>;
}
```

## SDK Initialization

```typescript
// lib/tributary.ts
import { Tributary } from "@tributary-so/sdk";
import { useConnection } from "@solana/wallet-adapter-react";

const USDC_MINT = new PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v");
const GATEWAY_PUBKEY = new PublicKey("your-gateway-pubkey-here");

export function useTributary() {
  const connection = useConnection();
  const wallet = useWallet();

  if (!connection || !wallet) return null;

  return useMemo(() => new Tributary(connection, wallet), [connection, wallet]);
}

export { USDC_MINT, GATEWAY_PUBKEY };
```

## Configuration

Create a config file for your environment:

```typescript
// config/tributary.ts
export const CONFIG = {
  programId: "TRibg8W8zmPHQqWtyAD1rEBRXEdyU13Mu6qX1Sg42tJ",
  usdcMint: new PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"),
  gateway: new PublicKey("GATEWAY_PUBKEY_HERE"),
  network: process.env.NEXT_PUBLIC_NETWORK || "mainnet",
};
```

## Reading Policies

```typescript
// Get all policies for current user
const policies = await sdk.getPaymentPoliciesByUserPayment(userPaymentPda);

// Get specific policy
const policy = await sdk.program.account.paymentPolicy.fetch(policyPda);

// Display in UI
{
  policies.map((policy) => (
    <PolicyCard key={policy.publicKey}>
      <h3>
        {formatAmount(policy.amount)} {getFrequencyLabel(policy.policyType)}
      </h3>
      <p>Status: Active</p>
      <button onClick={() => pausePolicy(policy.publicKey)}>Pause</button>
    </PolicyCard>
  ));
}
```

## Managing Policies

### Pause Subscription

```typescript
const pausePolicy = async (policyPda: PublicKey) => {
  const instruction = await sdk.pausePolicy(policyPda);
  await sendTransaction(instruction);
};
```

### Resume Subscription

```typescript
const resumePolicy = async (policyPda: PublicKey) => {
  const instruction = await sdk.resumePolicy(policyPda);
  await sendTransaction(instruction);
};
```

### Cancel Policy

```typescript
const cancelPolicy = async (policyPda: PublicKey) => {
  const instruction = await sdk.cancelPolicy(policyPda);
  await sendTransaction(instruction);
};
```

## Transaction Helper

```typescript
// lib/transaction.ts
import { Connection, Keypair } from "@solana/web3.js";
import { useWallet } from "@solana/wallet-adapter-react";

export async function sendTransaction(
  instructions: TransactionInstruction[]
): Promise<string> {
  const { connection } = useConnection();
  const wallet = useWallet();

  const tx = new Transaction().add(...instructions);

  try {
    const signature = await wallet.signTransaction(tx);
    const { blockhash, lastValidBlockHeight } =
      await connection.getLatestBlockhash();

    tx.recentBlockhash = blockhash;
    tx.lastValidBlockHeight = lastValidBlockHeight;

    const result = await connection.sendTransaction(tx);

    if (result.value?.err) {
      throw new Error(`Transaction failed: ${result.value.err}`);
    }

    return result.value.signature;
  } catch (error) {
    console.error("Transaction error:", error);
    throw error;
  }
}
```

## Error Handling

```typescript
try {
  const instructions = await sdk.createSubscription({...});
  await sendTransaction(instructions);
} catch (error) {
  if (error.message.includes("Insufficient funds")) {
    alert("Insufficient USDC balance");
  } else if (error.message.includes("Referral")) {
    alert("Invalid referral code");
  } else {
    alert("Transaction failed. Please try again.");
  }
}
```

## Common Patterns

### Loading States

```tsx
const [loading, setLoading] = useState(false);

const handleSubscribe = async () => {
  setLoading(true);
  try {
    await subscribe();
    toast.success("Subscription created!");
  } catch (error) {
    toast.error(error.message);
  } finally {
    setLoading(false);
  }
};

<button onClick={handleSubscribe} disabled={loading}>
  {loading ? "Creating..." : "Subscribe"}
</button>;
```

### Amount Input

```tsx
const [amount, setAmount] = useState(50);

return (
  <div>
    <label>Amount (USDC)</label>
    <input
      type="number"
      value={amount}
      onChange={(e) => setAmount(Number(e.target.value))}
      min="1"
      step="1"
    />
    <button onClick={() => subscribe(amount)}>Pay {amount}/month</button>
  </div>
);
```

### Frequency Selector

```tsx
const [frequency, setFrequency] = useState<PaymentFrequency>(
  PaymentFrequency.Weekly
);

return (
  <select value={frequency} onChange={(e) => setFrequency(e.target.value)}>
    <option value={PaymentFrequency.Daily}>Daily</option>
    <option value={PaymentFrequency.Weekly}>Weekly</option>
    <option value={PaymentFrequency.Monthly}>Monthly</option>
    <option value={PaymentFrequency.Quarterly}>Quarterly</option>
    <option value={PaymentFrequency.Yearly}>Yearly</option>
  </select>
);
```

## Styling

Tailwind CSS classes for payment components:

```tsx
// Primary button
<button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg transition-colors">
  Subscribe
</button>

// Success state
<div className="bg-green-50 border border-green-200 rounded-lg p-6">
  <div className="text-green-700 text-4xl font-bold">✓</div>
  <p className="text-green-600 mt-2">Subscription active</p>
</div>

// Loading spinner
<button disabled={loading} className="opacity-50 cursor-not-allowed">
  {loading && <Spinner className="animate-spin mr-2" />}
  Subscribe
</button>
```

## Testing

```typescript
import { render, screen } from "@testing-library/react";
import { SubscribeButton } from "./SubscribeButton";

describe("SubscribeButton", () => {
  it("calls createSubscription on click", async () => {
    const mockSdk = { createSubscription: vi.fn() };

    render(<SubscribeButton sdk={mockSdk} amount={10} />);

    fireEvent.click(screen.getByText("Subscribe $10/month"));

    await waitFor(() => {
      expect(mockSdk.createSubscription).toHaveBeenCalledWith(
        expect.objectContaining({
          amount: expect.any(BN),
          autoRenew: true,
        })
      );
    });
  });
});
```

## Deployment Checklist

- [ ] Replace `GATEWAY_PUBKEY` with your gateway
- [ ] Set correct `USDC_MINT` for target network (devnet/mainnet)
- [ ] Configure environment variables in `.env`
- [ ] Test on devnet before mainnet
- [ ] Add error handling for all user actions
- [ ] Verify transaction confirmations before showing success
- [ ] Handle wallet disconnection gracefully

## Resources

- [Tributary SDK](https://github.com/tributary-so/tributary)
- [Solana Wallet Adapter](https://github.com/solana-labs/wallet-adapter)
- [USDC on Solana](https://www.circle.com/usdc)
- [Tributary Docs](https://docs.tributary.so)
