# MUSIC.md — Format Specification

Version: alpha

MUSIC.md is a format for describing a piece of music to coding agents. It is to music what DESIGN.md is to visual identity: a persistent, structured understanding of the sound, so that compositions stay consistent across sessions and iterations.

A MUSIC.md file combines machine-readable tokens (YAML front matter) with human-readable musical rationale (markdown prose). **The tokens are context, not instructions. The prose is where the music lives.** A generated piece's quality is determined less by the precision of the BPM value than by how clearly the intent is described.

The file describes _one piece_ (or one tightly-related family of variations, e.g. a bed and its shorter cut-down). A project with two unrelated pieces uses two files (`MUSIC-loop.md`, `MUSIC-sting.md`).

## File structure

```md
---
name: Foyer Loop
purpose: background
key: Eb major
bpm: 74
structure: loop
---

## Overview

One specific, evocative reference sentence here — not adjectives.

## Sound Palette

…prose…

## Do's and Don'ts

…prose…
```

Two layers:

1. **YAML front matter** — delimited by `---` fences at the top. Normative values an agent can rely on mechanically (key, tempo, structure) plus starting points.
2. **Markdown body** — `##` sections in a fixed order (below). The rationale: why these values exist and how to apply them.

## Front-matter schema

All keys are optional except `name`. Unknown keys are accepted — the format grows through its users.

```yaml
version: alpha # optional
name: <string> # required — human name of the piece
purpose:
  background | foreground | soundtrack
  # background = must not demand attention (default assumption
  # if omitted); foreground = listened-to music;
  # soundtrack = synced to picture/events
key:
  <string> # e.g. "Eb major", "C Dorian", "A minor". The enharmonic
  # spelling is normative: use flats for flat keys, sharps for
  # sharp keys.
bpm: <number>
timeSignature: "4/4" # default 4/4; "3/4", "6/8", "7/8" also valid
structure: loop | fixed # loop = endless seamless bed; fixed = arranged duration
duration: <number> # seconds; required in practice when structure: fixed
palette: # roles -> Strudel sound names (starting points, not prisons)
  pad: juno
  bass: sine
  pulse: bd
  texture: crackle
references: # specific points, never bare adjectives
  - "Brian Eno — Ambient 1: Music for Airports (1/1)"
  - "hotel lobby at 7am, first coffee"
```

## Section order

Sections use `##` headings. All are optional; those present must appear in this order:

| #   | Section         | Aliases      | Contains                                                                                                                            |
| --- | --------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Overview        | Mood & Style | The specific reference. What world this music evokes; where it plays; who hears it. One concrete sentence beats a dozen adjectives. |
| 2   | Sound Palette   | Sound        | Instruments/timbres per role (pad, bass, pulse, melody, texture), registers, brightness/darkness, what carries what.                |
| 3   | Harmony         |              | Key, progression in Roman numerals, chord types and extensions, voicing style, harmonic rhythm.                                     |
| 4   | Rhythm & Feel   | Groove       | Pulse (or pulseless), subdivision, swing, density, ghost notes — and what rhythm must NOT feature.                                  |
| 5   | Form            | Structure    | For loops: variation strategy and seam behavior. For fixed: section map with durations (intro/body/outro) and energy curve.         |
| 6   | Context & Mix   | Interplay    | What the music accompanies (voice-over, visuals, room), loudness targets, frequency-lane discipline, headroom.                      |
| 7   | Do's and Don'ts |              | Negative constraints. Intentional, short, decisive.                                                                                 |

## Consumer behavior for unknown content

| Scenario                  | Behavior                                                                   |
| ------------------------- | -------------------------------------------------------------------------- |
| Unknown section heading   | Preserve; do not error                                                     |
| Unknown front-matter key  | Accept if the value is valid YAML                                          |
| Duplicate section heading | Error; reject the file                                                     |
| Token/prose conflict      | Prose wins; flag the conflict to the user and offer to sync the token      |
| Missing section           | Fill from sensible genre defaults, say so, offer to write it into the file |

## Philosophy

Carried over from DESIGN.md, transposed to sound:

- **Prose, not tokens, is the focus.** "A 1970s hotel lobby tape loop, warm and slightly out of tune" evokes a complete world — instrumentation, tempo, register, harmonic restraint. "Calm, pleasant, professional" evokes nothing specific.
- **A specific reference carries more than a list of adjectives.** Adjectives describe a region; a reference describes a point.
- **Negative constraints define character.** A specific enough reference brings its don'ts for free (a lobby bed does not drop, does not sing, does not solo). A short intentional don't-list on top is the sweet spot; a long rambling one means the Overview was too vague.
- **The format grows through its users, not its spec.** The standardized sections are the structural minimum. Anything a piece needs — synthesis constraints, sample budgets, stem requirements — belongs in a new section or key, and consumers must accept it.

## Writing guidance per section

**Overview.** Name a place, a moment, and at least one concrete musical reference (artist, album, or track). State the purpose in plain words ("plays under a 90-second product video", "loops all day in a hotel lobby").

**Sound Palette.** Assign every layer a role and a register. Say what the _top_ voice is and what the _bottom_ voice is — the ends define the perceived width. Prefer describing timbre ("soft mallet", "chorused pad", "round sub") over brand names; brand names go in `palette` tokens.

**Harmony.** Roman numerals, not letter names — they survive a key change. State the chord vocabulary (triads? maj7? m9?), the harmonic rhythm (bars per chord), and whether dominant function is allowed at all. Background music usually suspends it.

**Rhythm & Feel.** Say the pulse or say "pulseless". Density is the decision that most changes the result: state events-per-bar ceilings. If the piece must not draw attention, the don'ts here matter most ("no backbeat", "no fill ever resolves loudly").

**Form.** For `structure: loop`: how long before a listener notices repetition (or "they never should"), and the seam rule (bar 1 must not announce itself). For `structure: fixed`: section list with seconds, and the energy curve across them.

**Context & Mix.** What else is audible: voice-over (→ stay out of 1–4 kHz, keep gain low, duck-friendly), visuals with sync points (→ note the timestamps), room playback (small speakers → no sub-only information). Loudness in relative terms ("clearly quieter than speech", "felt before heard").

**Do's and Don'ts.** Each item one line, decisive, no hedging. Don'ts name the tempting mistake ("Don't add a melodic hook — this bed must lose attention contests to a voice-over").

## Validation

No linter exists. Agents validate by checklist:

1. Front matter parses as YAML; `name` present.
2. Present sections appear in the canonical order; no duplicate headings.
3. `key`/`bpm` tokens agree with Harmony/Rhythm prose; conflicts flagged, prose wins.
4. `structure: fixed` implies `duration` and a section map in Form; `structure: loop` implies a seam rule in Form.
5. Every role named in Sound Palette appears in `palette` or in prose with a timbre description.
