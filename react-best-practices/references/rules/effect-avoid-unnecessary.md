---
title: Avoid Unnecessary useEffect
impact: MEDIUM
impactDescription: reduces bugs, improves performance, simplifies code
tags: effect, useEffect, performance, react-patterns
---

## Avoid Unnecessary useEffect

Effects are for synchronizing with external systems (DOM, network, third-party widgets). Everything else should happen during rendering or in event handlers.

**Core Rule:** _"Does this code run because component was displayed, or because user did something?"_

- Displayed → Effect is appropriate
- User action → event handler

### Common Anti-Patterns

**1. Deriving state from props/state**

Calculate directly during render instead.

```tsx
// ❌ Unnecessary effect
function Profile({ firstName, lastName }: Props) {
  const [fullName, setFullName] = useState("");

  useEffect(() => {
    setFullName(`${firstName} ${lastName}`);
  }, [firstName, lastName]);

  return <div>{fullName}</div>;
}

// ✅ Calculate during render
function Profile({ firstName, lastName }: Props) {
  const fullName = `${firstName} ${lastName}`;
  return <div>{fullName}</div>;
}
```

**2. Caching expensive calculations**

Use `useMemo`, not `useEffect` + state.

```tsx
// ❌ Inefficient caching with effect
function FilteredList({ items, filter }: Props) {
  const [filtered, setFiltered] = useState<Item[]>([])

  useEffect(() => {
    setFiltered(items.filter(item => item.name.includes(filter)))
  }, [items, filter])

  return <div>{filtered.map(...)}</div>
}

// ✅ Proper memoization
function FilteredList({ items, filter }: Props) {
  const filtered = useMemo(
    () => items.filter(item => item.name.includes(filter)),
    [items, filter]
  )

  return <div>{filtered.map(...)}</div>
}
```

**3. Resetting all state on prop change**

Pass a `key` prop to force remount instead.

```tsx
// ❌ Manual state reset in effect
function UserProfile({ userId }: Props) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setData(null);
    setLoading(true);
    setError(null);
    fetchUserData(userId)
      .then(setData)
      .finally(() => setLoading(false));
  }, [userId]);

  // ...
}

// ✅ Use key to force remount
function UserProfile({ userId }: Props) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchUserData(userId)
      .then(setData)
      .finally(() => setLoading(false));
  }, [userId]);

  // ...
}

// Usage: key forces complete remount on userId change
<UserProfile key={userId} userId={userId} />;
```

**4. Adjusting partial state on prop change**

Set state during rendering, or store ID and derive during render.

```tsx
// ❌ Sync state in effect
function ItemList({ items, selectedId }: Props) {
  const [selectedItem, setSelectedItem] = useState<Item | null>(null);

  useEffect(() => {
    setSelectedItem(items.find((item) => item.id === selectedId) ?? null);
  }, [items, selectedId]);

  return <div>{selectedItem?.name}</div>;
}

// ✅ Derive during render
function ItemList({ items, selectedId }: Props) {
  const selectedItem = items.find((item) => item.id === selectedId) ?? null;
  return <div>{selectedItem?.name}</div>;
}
```

**5. Sending POST requests triggered by user action**

Put it in event handler, not an effect watching state.

```tsx
// ❌ Effect triggers on form submission
function ContactForm() {
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    if (submitted) {
      fetch("/api/contact", { method: "POST", body: JSON.stringify(formData) });
      setSubmitted(false);
    }
  }, [submitted]);

  return <button onClick={() => setSubmitted(true)}>Submit</button>;
}

// ✅ Direct in event handler
function ContactForm() {
  const handleSubmit = () => {
    fetch("/api/contact", { method: "POST", body: JSON.stringify(formData) });
  };

  return <button onClick={handleSubmit}>Submit</button>;
}
```

**6. Chains of effects updating state**

Compute everything in event handler in one pass.

```tsx
// ❌ Chain of effects
function Form() {
  const [value, setValue] = useState("");
  const [isValid, setIsValid] = useState(false);
  const [showError, setShowError] = useState(false);

  useEffect(() => {
    setIsValid(value.length >= 8);
  }, [value]);

  useEffect(() => {
    setShowError(!isValid);
  }, [isValid]);

  return <div>{showError && "Password too short"}</div>;
}

// ✅ Single computation in render/event handler
function Form() {
  const [value, setValue] = useState("");
  const isValid = value.length >= 8;
  const showError = !isValid;

  return <div>{showError && "Password too short"}</div>;
}
```

**7. Notifying parent of state changes**

Update both parent and child state in same event handler, or lift state up.

```tsx
// ❌ Effect notifies parent
function Expandable({ onToggle }: Props) {
  const [expanded, setExpanded] = useState(false);

  useEffect(() => {
    onToggle(expanded);
  }, [expanded, onToggle]);

  return <button onClick={() => setExpanded(!expanded)}>Toggle</button>;
}

// ✅ Event handler notifies parent
function Expandable({ onToggle }: Props) {
  const [expanded, setExpanded] = useState(false);

  const handleToggle = () => {
    const next = !expanded;
    setExpanded(next);
    onToggle(next);
  };

  return <button onClick={handleToggle}>Toggle</button>;
}

// ✅ Even better: lift state up
function Expandable({ expanded, onToggle }: Props) {
  return <button onClick={() => onToggle(!expanded)}>Toggle</button>;
}
```

**8. Subscribing to external stores**

Use `useSyncExternalStore` instead of manual Effect subscriptions.

```tsx
// ❌ Manual store subscription
function StoreCounter() {
  const [count, setCount] = useState(store.getState().count);

  useEffect(() => {
    const unsubscribe = store.subscribe(() => {
      setCount(store.getState().count);
    });
    return unsubscribe;
  }, []);

  return <div>{count}</div>;
}

// ✅ useSyncExternalStore (React 18+)
import { useSyncExternalStore } from "react";

function StoreCounter() {
  const count = useSyncExternalStore(
    store.subscribe,
    () => store.getState().count,
  );

  return <div>{count}</div>;
}
```

**9. Data fetching**

Fine to use Effects, but add cleanup/ignore flag to prevent race conditions. Prefer framework data fetching or custom `useData` hook.

```tsx
// ❌ Race condition possible
function UserList() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    fetch('/api/users').then(r => r.json()).then(setUsers)
  }, [])

  return <div>{users.map(...)}</div>
}

// ✅ Race condition protection
function UserList() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    let ignore = false

    fetch('/api/users')
      .then(r => r.json())
      .then(data => {
        if (!ignore) setUsers(data)
      })

    return () => { ignore = true }
  }, [])

  return <div>{users.map(...)}</div>
}

// ✅ Even better: use framework data fetching
function UserList() {
  const { data: users } = useSWR('/api/users', fetcher)
  return <div>{users?.map(...)}</div>
}
```

### Decision Heuristics

- If you can compute it during render, don't store it in state
- Fewer raw `useEffect` calls = easier to maintain
- Chained Effects that trigger each other are a red flag
- When two state variables need to stay in sync, lift state up instead
- If an Effect updates state without user interaction, consider if it can be computed instead

Reference: [https://react.dev/learn/synchronizing-with-effects#you-might-not-need-an-effect](https://react.dev/learn/synchronizing-with-effects#you-might-not-need-an-effect)
