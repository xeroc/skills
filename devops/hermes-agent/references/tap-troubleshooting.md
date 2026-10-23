# Tap Troubleshooting Log

## witt3rd/oh-my-hermes (2025-05-21)

- Tap added successfully: `hermes skills tap add witt3rd/oh-my-hermes`
- Tap config stored at `~/.hermes/skills/.hub/taps.json` with path `skills/`
- The following skill names were NOT found in any source after adding the tap:
  - omh-deep-research
  - omh-ralplan
  - omh-ralplan-driver
  - omh-deep-interview
  - omh-ralph
  - omh-ralph-driver
  - omh-ralph-task
  - omh-autopilot
- `hermes skills search` across all sources returned zero matches for these names
- Possible causes: repo may not have an index.json, skills may not be published yet,
  or skill names may differ from what the user expected
- Resolution: user needs to verify repo contents at https://github.com/witt3rd/oh-my-hermes
