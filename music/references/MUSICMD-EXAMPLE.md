# MUSIC.md — Annotated Example

A fully worked example: a background bed for a 90-second product video that loops in a lobby afterward. Shown twice — first the complete file verbatim, then the section-by- section commentary and the Strudel code it produced. Blockquote annotations are teaching commentary; strip them in a real MUSIC.md.

## The file

```md
---
name: Foyer Loop
purpose: background
key: Eb major
bpm: 74
timeSignature: "4/4"
structure: loop
palette:
  pad: juno
  bass: sine
  pulse: bd
  sparkle: hh
  motif: pluck
  texture: crackle
references:
  - "Brian Eno — Ambient 1: Music for Airports (1/1), minus the anxiety"
  - "Nujabes — Feather, at half attention"
  - "hotel lobby at 7am, first coffee, marble and warm light"
---

## Overview

A warm, unhurried lobby loop for the Accord product video. It plays under a voice-over at low level and must lose every attention contest — felt before heard. The world is Eno's airport calm with a jazz-café warmth: nothing announces itself, nothing resolves dramatically, nothing ends.

## Sound Palette

Six roles, each in its own register lane:

- **Pad (juno, octaves 3–4)** — the harmonic floor; chorused, dark, filtered.
- **Bass (sine, octave 2)** — round sub, roots only, no attack character.
- **Pulse (bd)** — one soft heartbeat per bar, felt not heard.
- **Sparkle (hh)** — feather brush on quarters, half of them swallowed.
- **Motif (pluck, octave 4)** — a single note per bar, more silence than note.
- **Texture (crackle)** — vinyl air at the edge of perception.

The top voice is the plucked motif; the bottom is the sub bass. Everything between is pad.

## Harmony

Eb major. Progression, one chord per bar, no dominant anywhere:

Imaj7 – vi7 – IVmaj7 – Imaj7 (Ebmaj7 – Cm7 – Abmaj7 – Ebmaj7)

Vocabulary: four-note voicings with a major 7th or 9th color, voiced by common tones so chords melt into each other. Harmonic rhythm: glacial — the same four bars circle without cadencing.

## Rhythm & Feel

Pulse: 74 BPM, straight, no swing. Density ceiling: one kick per bar, one brushed hi-hat per beat at most, half randomly muted. No backbeat, no fills, no snare. If a listener can clap along without trying, it is too rhythmic.

## Form

Endless loop, and the seam must be invisible: bar 1 never announces itself. Variation comes from independent slow modulations — filter, pan, texture level — cycling at periods that never realign (9, 13, 7 bars), so the four-bar harmony circles inside a texture that never repeats twice.

## Context & Mix

Sits under a calm female voice-over for 90 seconds, then loops alone in a lobby. Total level clearly quieter than speech; nothing in the 1–4 kHz presence region above a whisper; leave 6 dB of headroom under the voice. Must also survive laptop speakers: no musical information carried by the sub alone — the pad always states the root.

## Do's and Don'ts

- **Don't** add a melodic hook. The motif is one note per bar, never a phrase.
- **Don't** introduce a snare, backbeat, or any fill louder than the kick.
- **Don't** use a dominant chord or a strong V–I resolution. This bed floats.
- **Don't** let the filter open past ~1.5 kHz on the pad; brightness reads as urgency.
- **Do** keep every layer's gain below 0.5; the voice-over is the melody.
- **Do** let rests do half the work. Silence is the arrangement.
```

## Why each section works

> **Front matter** — every token is mechanically load-bearing: key/bpm/tempo set the grid, `structure: loop` selects the generative-loop form, and `palette` names starting-point sounds so iterations don't drift instrument-to-instrument.

> **Overview** — one concrete world ("Eno's airport calm with jazz-café warmth, hotel lobby at 7am") plus the deployment fact (voice-over bed, then lobby loop). A model reading only this section already knows what not to do.

> **Sound Palette** — roles × registers × timbre, with the ends named (top = motif, bottom = sub). The "laptop speakers" concern is deferred to Context & Mix, where it belongs.

> **Harmony** — Roman numerals survive key changes; "no dominant" is the single highest-leverage constraint in the file; "voiced by common tones" tells the agent _how_ to voice, not just _what_ chords.

> **Rhythm & Feel** — a density ceiling ("one kick, one hat per beat, half muted") is checkable; "laid back groove" is not. The test sentence ("if a listener can clap along…") gives the agent an eval.

> **Form** — names the seam rule and the variation strategy with the actual periods (9/13/7). This maps one-to-one onto `.slow(n)` calls in Strudel.

> **Context & Mix** — the mix is part of the composition: presence-region discipline, headroom, and a small-speaker rule that changes the voicing (pad states the root).

> **Do's and Don'ts** — each don't names the _tempting_ mistake (hooks, snare, V–I, bright filter). Short, decisive, checkable against the final code.

## The Strudel code it produced

```js
// Foyer Loop — Eb major, 74 BPM, endless background bed
setcpm(18.5); // 74 BPM = 18.5 cycles per minute (bpm / 4)

// Pad: Imaj7 – vi7 – IVmaj7 – Imaj7, common-tone voicings, breathing filter
$: note("<[eb3,g3,bb3,d4] [eb3,g3,bb3,c4] [eb3,g3,ab3,c4] [eb3,g3,bb3,d4]>")
  .s("juno")
  .gain(0.24)
  .room(0.4)
  .lpf(perlin.range(500, 1400).slow(9)) // organic, period 9 bars
  .pan(cosine.range(0.35, 0.65).slow(13)); // slow stereo drift, period 13

// Bass: round sub, roots only, octave 2
$: note("<eb2 c2 ab2 eb2>").s("sine").gain(0.45).shape(0.15);

// Pulse: one soft heartbeat per bar
$: sound("bd ~ ~ ~").gain(0.35).room(0.1);

// Sparkle: brushed quarters, half swallowed
$: sound("hh*4?").gain(0.1).room(0.2);

// Motif: one note per bar, in key, occasionally an octave up and softer
$: note("<[~ eb4] [~ f4] [~ ab4] [~ bb4]>")
  .s("pluck")
  .gain(0.3)
  .room(0.5)
  .delay(0.25)
  .sometimes((x) => x.add(12).gain(0.12));

// Texture: vinyl air at the edge of perception
$: s("crackle*4").gain(sine.range(0.02, 0.06).slow(7));
```

## How the brief maps to the code

| Brief                                | Code                                                                  |
| ------------------------------------ | --------------------------------------------------------------------- |
| Imaj7–vi7–IVmaj7–Imaj7, common tones | The four pad chords share eb3+g3; only the upper two voices move      |
| No dominant, floats                  | No V chord anywhere; the circle returns to I without cadencing        |
| One note per bar motif, in key       | `<[~ eb4] [~ f4] [~ ab4] [~ bb4]>` — Eb-major notes, rest first       |
| Periods 9/13/7 never realign         | `.slow(9)` filter, `.slow(13)` pan, `.slow(7)` texture level          |
| Seam invisible                       | Only periodic-per-bar events (kick, hats); texture mods are aperiodic |
| Presence region whisper              | Motif at 0.3 gain with room+delay; pad filtered under 1.4 kHz         |
| Nothing above 0.5 gain               | Max layer gain is the bass at 0.45                                    |
| Half the hats swallowed              | `hh*4?` — the `?` randomly mutes ~50%                                 |
