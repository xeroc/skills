Metal's equivalent moment is **the riff** — not the chorus, not a drop, not the solo: the riff is the main character and the singer knows it, which is why half the lyrics are just the riff's name. Where trance spends its tension in a low-pass filter and jazz in a cadenza, metal spends it in **palm-mute discipline**: bars of throttled low-E 16ths that make every open accented note land like a door being kicked in. Everything else — the double kick, the half-time drop, the raised 7th — is staging for the riff.

## What the riff actually is

A metal riff is rhythm first and pitch second. The engine is the contrast between the palm-muted chug (`gm_electric_guitar_muted` hammering 16ths on `e2`, with `decay(.09).sustain(0)` so every chok dies instantly) and the open accented note that escapes it (`gm_overdriven_guitar`, ringing, `.sustain(.9)`). Riffs live at one or two bars, phrased as question and answer — a gallop bar that asks, a pickup bar (`g2 a2 b2`) that answers and leans into the repeat. The structural payoff is **the breakdown**: the half-time drop where the snare moves to beat 3, the chug slows to 8ths, and the room's heads move as one. Headbang physics is accent placement: land the open notes on 1 and on the "and" of 3, and the riff does the work.

## The layers

- **Chug guitar** — `gm_electric_guitar_muted`, 16ths or the gallop on `e2`, envelope short. This layer is the genre's rhythmic identity; it welds to the kick drum.
- **Open guitar** — `gm_overdriven_guitar`, power dyads `[e2,b2]`, tritone stabs `[bb2,f3]`, and the sus2 dread chord `[e2,fs2,b2]` ringing over slow sections.
- **Lead guitar** — `gm_overdriven_guitar` up high, harmonic-minor runs, long held notes to close phrases; more melodic than fast.
- **Bass** — `sawtooth` doubling the riff's root an octave down, `lpf(500)`: felt more than heard.
- **Drums** — kick welded to the riff rhythm (`bd bd ~ bd …` matching the gallop), double kick `bd*16` for the payoff, half-time backbeat `bd ~ ~ ~ sd ~ ~ ~`, ride 8ths `rd*8`, crash `cr` on section entrances, tom gallops `[ht mt lt]` into changes.
- **Atmosphere** — `gm_synth_strings_1` with `attack(1)` or slower, blooming under intros and breakdowns; one dread chord per appearance, no more.

## Sample kit

- **Drums** — default kit, machine-tight and dry; the gallop welds kick to chug. Epic/doom layer: `east:6`–`east:8` (taiko) as war drums under intros; `anvil` for industrial accents.
- **Chug** — `gm_electric_guitar_muted` with `decay(.09).sustain(0)`: the palm mute is the envelope.
- **Open / lead** — `gm_overdriven_guitar`; escalate to `gm_distortion_guitar` when the riff demands violence.
- **Bass** — `gm_electric_bass_pick` doubling the riff an octave down, still under `lpf(500)`. Synth fallback: `sawtooth` + `lpf(500)`.
- **Atmosphere** — `gm_synth_strings_1` slow-attack dread; `timpani`/`timpani_roll` for symphonic weight.
- No pack needed — the preloaded tiers cover metal. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Vocabulary: power dyads, sus2 voicings `[e2,fs2,b2]`, tritone dyads, and harmonic minor's raised 7th (in E minor that's `ds` — spelled, never `#`). Key of E minor for everything below, because the low open E string is the genre's home address.

- **i–bII, the phrygian slide** — E5 to F5 (`[e2,b2]` to `[f2,c3]`) — the sabbath move: one fret up, back down, entire mood installed. Use it when the riff needs menace with two shapes.
- **i–bVI–bVII** — Em, C, D (`[e2,b2] [c3,g3] [d3,a3]`) — the classic verse cycle; the bVI is where the lead guitar goes melodic.
- **Harmonic minor i–iv–V** — Em, Am, B (`[e2,b2] [a2,e3] [b2,fs3]`, add `ds` color over the B) — the raised 7th is the "ancient" flavor; one splash per section maximum or it turns into a cartoon.
- **The tritone anchor** — E5 to Bb5 (`[e2,b2]` to `[bb2,f3]`) — one interval, whole genre. Use as the accent in a heavier riff or the stab on beat 4 of a chorus.

## Rhythm & feel

Classic heavy sits 90–140 bpm, thrash 160–220; the example runs at 168. Machine-tight, zero swing — the discipline is the point. One cycle = one bar of 4/4, so a flat 16-event pattern is a bar of 16ths.

- **The gallop** — `[x x ~ x]` per beat: `e2 e2 ~ e2` — the genre's default pulse; pairs of sixteenths then a breath, hoofbeat physics
- **The chug** — `e2*16` flat, for the passages that just drive
- **Double kick** — `bd*16` under the chug: the payoff, earned after the half-time
- **The half-time drop** — `bd ~ ~ ~ sd ~ ~ ~`: the breakdown; guitar drops to 8ths, everything breathes at half speed
- **The fill** — `[ht mt lt]*2` or `{ht mt lt ~}%3` (toms in 3 drifting against the 4/4 kit) on the way into a new section

## Structure

intro 4 | verse A 8 | chorus B 8 | verse 8 | chorus 8 | solo 8 | breakdown 8 | final chorus 8 | outro 4 — 60 bars. The riff is stated alone first, alternated with its answer, then surrendered only to the solo (which plays over it anyway), halved for the breakdown, and restated biggest at the end.

```
// energy: 7 - 6 - 9 - 6 - 9 - 8 - 5 - 7 - 10 - 8
// the breakdown dips so the final chorus can weigh the most
```

## Techniques that actually create "metal"

- **Palm mute as envelope** — the mute is not a sound, it's `decay(.09).sustain(0)` versus the open note's `sustain(.9)`: the contrast between choked and ringing IS the articulation.
- **The gallop** — `[e2 e2 ~ e2]` per beat with the kick playing the identical rhythm; when guitar and kick weld into one instrument, it's metal.
- **The half-time drop** — moving the snare from 2/4 to 3 (`bd ~ ~ ~ sd ~ ~ ~`) without changing tempo reads as the floor giving way; use once, late.
- **Double kick as escalation** — `bd*16` reserved for the bars after the breakdown; it's the "now we run" switch.
- **Harmonic minor color** — one raised 7th (`ds` in E) in the lead per phrase; it's spice, not the meal.
- **Tritone and sus2** — `[bb2,f3]` for menace, `[e2,fs2,b2]` for dread: two voicings cover most of the genre's non-dyad needs.
- **Riff economy** — question bar, answer bar, repeat; a four-bar riff is progressive rock wearing a jacket.
- **The pickup** — end the gallop bar with `g2 a2 b2 ~` climbing into the downbeat; the lean-in is what makes the loop feel inevitable.

## Practice approach

- Write ten one-bar riffs using only `e2` and rhythm — no pitch variety allowed; when they sound different from each other, you've found the genre's engine.
- Practice the gallop at three tempos (120, 150, 180) with the kick welded to it before adding anything melodic.
- One breakdown per song, and it goes after the solo; two breakdowns is a different genre with worse hair.
- Steal the contour of one Black Sabbath tritone riff and re-rhythm it in 16ths.
- Mute everything except chug guitar and kick: if that pair alone doesn't groove, no lead will save it.

## Example

```
// ═══ iron discipline — riff-metal in E minor, 168bpm ═══
// form: intro 4 | verse A 8 | chorus B 8 | verse 8 | chorus 8 | solo 8 | breakdown 8 | final chorus 8 | outro 4
// the riff is the singer: everything else is staging
setcpm(168 / 4) // one cycle = one bar of 4/4

// ── riff A (verse) — the gallop [x x ~ x] per beat, palm-muted, pickup notes open ──
const riffA = note("e2 e2 ~ e2 e2 e2 ~ e2 e2 e2 ~ e2 g2 a2 b2 ~").decay(.09).sustain(0).gain(.7)
// ── riff B (chorus) — open power dyads in 8ths, tritone stab on beat 4 ──
const riffB = note("[e2,b2] [e2,b2] [e2,b2] [bb2,f3] [e2,b2] [e2,b2] [g2,d3] [a2,e3]").sustain(.9).release(.12).gain(.75)
// ── riff C (breakdown) — 8th chugs, tritone accent ending every bar ──
const riffC = note("e2 e2 e2 e2 e2 e2 e2 [e2,bb2]").decay(.1).sustain(0).gain(.8)

// ── chug guitar — the palm-muted low string; the envelope IS the technique ──
const chug = arrange(
  [4, riffA],
  [8, riffA], [8, silence], [8, riffA], [8, silence],
  [8, riffA], // under the solo the riff never yields the floor
  [8, riffC], [8, riffC.gain(.7)], [4, riffA], // muted chugs under the final chorus: the heaviest it gets
).sound("gm_electric_guitar_muted").room(.08)

// ── open guitar — dyads, the sus2 dread chord, the i bVI bVII slides under the solo ──
const open = arrange(
  [4, note("[e2,fs2,b2]@4").sustain(1).release(.8).gain(.4)], // Esus2 ringing: the ominous open
  [8, silence],
  [8, riffB],
  [8, silence],
  [8, riffB],
  [8, note("<[e2,b2]!3 [c3,g3]!2 [d3,a3]!3>").sustain(.8).release(.15).gain(.65)],
  [8, silence],
  [8, riffB],
  [4, note("[e2,b2]@4").sustain(1).release(1).gain(.7)],
).sound("gm_overdriven_guitar").room(.12)

// ── lead — E harmonic minor: the ds is the raised 7th, one splash of color per phrase ──
const run = note("e6 ds6 cs6 b5 a5 g5 fs5 e5 e5 fs5 g5 a5 b5 cs6 ds6 e6").gain(.6)
const lead = arrange(
  [36, silence],
  [2, run],
  [2, note("[b5@4] [cs6 b5 a5 g5]")],
  [2, run.add(-2)], // the same run dropped a tone, chasing the C chord
  [2, note("[a5 b5 cs6 ds6] [e6@4]")], // climb, then hold the peak
  [12, silence],
).sound("gm_overdriven_guitar").room(.25).pan(.6)

// ── bass — the riff's shadow, an octave down, felt more than heard ──
const bassRiffA = note("e1 e1 ~ e1 e1 e1 ~ e1 e1 e1 ~ e1 g1 a1 b1 ~")
const bass = arrange(
  [4, note("e1*8")],
  [8, bassRiffA], [8, note("e1*8")], [8, bassRiffA], [8, note("e1*8")],
  [8, bassRiffA],
  [8, note("e1 e1 e1 e1 e1 e1 e1 e1")],
  [8, note("e1*8")],
  [4, note("e1*8")],
).sound("gm_electric_bass_pick").lpf(500).gain(.55)
$: bass

// ── strings — slow-attack dread in the intro, bloom under the breakdown ──
const pad = arrange(
  [4, note("[e3,b3,e4]@4").attack(1).release(2).gain(.18)],
  [32, silence],
  [8, note("<[c4,g4]!4 [d4,a4]!4>").attack(1.5).release(2).gain(.16)],
  [12, silence],
).sound("gm_synth_strings_1").room(.8)
$: pad

// ── drums — kick welded to the riff; the half-time and the double kick are the two big moves ──
const kickA = sound("bd bd ~ bd bd bd ~ bd bd bd ~ bd ~ ~ ~ ~") // welded to riff A
const verseKit = stack(kickA.gain(.8), sound("~ sd ~ sd").gain(.5), sound("rd*8").gain(.3))
const chorusKit = stack(sound("bd*4").gain(.85), sound("~ sd ~ sd").gain(.5), sound("<cr ~ ~ ~>").gain(.38))
const halfKit = stack(sound("bd ~ ~ ~ sd ~ ~ ~").gain(.8), sound("hh*16").gain(.12)) // the half-time drop
const doubleKit = stack(sound("bd*16").gain(.75), sound("~ ~ ~ ~ sd ~ ~ ~").gain(.5)) // the payoff

const drums = arrange(
  [4, stack(sound("cr ~ ~ ~").gain(.4), sound("bd ~ bd ~ sd ~ [ht mt lt]").gain(.6))], // toms announce the riff
  [8, verseKit], [8, chorusKit], [8, verseKit], [8, chorusKit], [8, verseKit],
  [4, halfKit],
  [4, stack(doubleKit, sound("{ht mt lt ~}%3").gain(.25))], // double kick + toms in 3, drifting against 4
  [8, chorusKit.every(2, x => stack(x, sound("~ ~ ~ ~ ht mt lt ht").gain(.3)))],
  [4, stack(sound("cr ~ ~ ~").gain(.45), sound("bd*4").gain(.7), sound("[ht mt lt]*2").gain(.5))],
)
$: drums

$: chug
$: open
$: lead
```
