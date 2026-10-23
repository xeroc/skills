# Rate Limit Mitigation for Parallel Subagents

## Problem

When dispatching 3+ concurrent `delegate_task` subagents on rate-limited models (especially glm-5.1), HTTP 429 errors are frequent. One or more subagents fail per round, requiring retry.

## Observed Pattern (glm-5.1, June 2025)

| Concurrency | 429 Rate | Notes |
|-------------|----------|-------|
| 3           | ~33%     | 1 of 3 typically fails |
| 2           | ~10%     | Occasional failure |
| 1           | ~0%      | Sequential is safe |

## Mitigation Protocol

### Tier 1: Start at 3 Concurrent

```
delegate_task(batch_1), delegate_task(batch_2), delegate_task(batch_3)
```

If all succeed, continue at 3. If any 429:

### Tier 2: Drop to 2 Concurrent + 30s Cooldown

```python
terminal("sleep 30")
delegate_task(batch_retry), delegate_task(batch_next)
```

If still failing:

### Tier 3: Sequential (1 at a time) + 45s Cooldown

```python
terminal("sleep 45")
delegate_task(batch_retry)  # solo
```

### Recovery

After 2 consecutive clean rounds at lower concurrency, attempt to scale back up.

## Key Rules

1. **Never loop-sleep.** One sleep, then one retry. If it fails again, increase the sleep duration.
2. **Retry failed batches solo**, not concurrently with new batches.
3. **Track which batches completed** to avoid re-processing. Use the batch JSON file as the source of truth.
4. **30-45s is the sweet spot** for glm-5.1. Shorter (10-15s) is insufficient; longer (60s+) wastes time.
5. **Context compaction risk:** If the session runs long (20+ batches), the controller's context may compact. Save batch progress to a JSON file so it survives compaction.

## Batch JSON as Checkpoint

Save all batches to `/tmp/batches.json` at the start. After each successful round, note which batch numbers completed. If context compacts, re-read the JSON and resume from the last completed batch.

```python
# Save checkpoint
import json
with open("/tmp/batch_progress.json", "w") as f:
    json.dump({"completed": [1,2,3,4,5], "failed": [6], "pending": [7,8,9,10]}, f)
```
