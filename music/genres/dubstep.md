Dubstep's equivalent moment is **the wobble** — the first bar of the drop where the snare cracks on beat 3 and the mid-bass starts moving. The genre runs at 140 but the body hears 70, because the backbeat only fires on beat 3: half-time. The whole track is engineered around that single landing. A delicate, melodic intro makes a promise the drop then breaks with brute weight — sub sine, syncopated kick, and a sawtooth whose resonant filter opens and closes in rhythm. If the first wobble bar doesn't feel like the floor dropped out, restart the intro; the contrast is the composition.

## What the wobble actually is

A half-time drop: kick on 1, layered snare on 3, hats still running at 140 on top — the disagreement between the two speeds is the genre's engine. The wobble itself is a sustained mid-register sawtooth through a *resonant* lowpass whose envelope retriggers on every note: the note rate sets the wobble rate (8th notes lurch, triplet 8ths roll, 16ths machine-gun), and the filter envelope's decay (`lpd`) sets the vowel — fast decay is a quack, slow decay is a yawn. Underneath all of it sits a sine sub playing plain root notes, because the wobble's filter sweep eats the fundamental; sub and wobble are two instruments, never one. Before the drop: a 4–8 bar build (snare roll, riser, filter opening) and then the gap — a beat or two of near-silence so the landing has air to hit.

## The layers

- **Kick** — `bd` from `.bank("RolandTR909")` (or `.bank("RolandTR808")` for a subbier flavor), short and deep, on beat 1 only — plus one syncopated push, classically on the "and of 3", arriving in the drop.
- **Snare** — `sd` from the 909 bank layered with `cp`, `room(.5)`, on beat 3. Big and reverberant; this single hit is the half-time marker, so it earns layering.
- **Hats** — `hh` 16ths with `oh` accents (`"[hh hh oh hh]*4"`); the only thing that keeps running at 140 during the half-time drop. Triplet fills (`hh*12`) as transitional candy.
- **Sub bass** — `sine`, root notes an octave-plus below the wobble (`d1`), sustained per chord, gain near .9. The actual weight of the genre; on laptop speakers it vanishes, so double it an octave up quietly.
- **Wobble bass** — `sawtooth` at `d2`, `lpf(140)` with `lpq(9)` resonance, and the movement from the filter envelope: `.lpenv(7).lpa(.01).lpd(.18)`. Retrig per note; vary `lpenv` depth per bar for growl shape.
- **Melody** — `gm_music_box`, `pluck`, or `piano`: delicate, minor, carries the intro and the breakdown — the thing the drop will demolish.
- **Pad** — `gm_synth_strings_1`, dark voicings, `attack` 1+, under intro and breakdown.
- **Perc fills** — `rim` triplet runs and `perc` one-shots at section borders only.

## Harmony

Dark minor keys, D and E minor favorites (sub frequencies sit well on those roots). The wobble plays roots only; chords belong to the intro and breakdown.

- **The forever loop** — i – bVI – bIII – bVII in D minor: **Dm – Bb – F – C**. The genre's default four-chord cycle; two bars each.
- **The two-chord** — i – bVI: **Dm – Bb**, two bars each. Enough; most weight is carried by the sound design anyway.
- **The phrygian slide** — i – bII: **Dm – Eb**. The darkest move available; even the melody should flinch.
- **Same shape, E minor** — i – bVI – bIII – bVII: **Em – C – G – D**. The half-step-down-second-chord variant (Em – F) turns it phrygian.

## Rhythm & feel

- **Tempo**: 140 (the body feels 70). Producers who write "70bpm" are describing the same grid.
- **Skeleton** (8th grid, one bar): `"bd ~ ~ ~ [sd cp] ~ ~ ~"` — kick 1, layered snare 3. This one string is the genre.
- **The push**: `"bd ~ ~ ~ [sd cp] bd ~"` — syncopated kick on the "and of 3"; drop-only.
- **Hats**: `"[hh hh oh hh]*4"` on the 16th grid — double-time above the half-time backbeat.
- **Sub**: whole/half-bar roots, `attack(.02).sustain(.9)`; movement is a chord change, not a riff.
- **Wobble rates**: 8ths `n("0!8")`, triplet 8ths `n("0!12")`, 16ths `n("0!16")` — changing the rate is an arrangement event, so do it on 8-bar boundaries.
- **Feel**: zero swing; the lurch comes from the half-time backbeat and the wobble's own retrigger grid. Melodic layers phrase in 2-bar gestures (70bpm thinking), percussion in 1-bar (140 thinking).

## Structure

Spiky contrast form — pretty versus brutal is the arrangement:

```
intro 8 | build 4 | gap | drop 16 | breakdown 8 | build2 4 | gap | drop2 16 | outro 4
energy ▃▄▂▃▅▆ █▇▇▇▇▇▇▇▇ ▃▄▂▃▅▆ █▇▇▇▇▇▇▇▇▇ ▃▂
```

Intro is melodic, nearly drumless or with a muffled skeleton. The build strips the melody and hands off to a roll + riser; the gap is one bar or one beat where the kick disappears but the snare stays; the drop lands at half-time with sub + wobble. Drop2 must differ in *rate* (triplets into 16ths) — same wobble, new engine. Breakdown returns the intro's beauty intact so the second demolition works.

## Techniques that actually create "dubstep"

- **The half-time illusion** — snare on 3 while hats run 140. Never move the snare; the disagreement is the identity.
- **Wobble via filter envelope** — `sawtooth` + `lpf(140)` + `lpq(9)` + `lpenv`/`lpa`/`lpd`, retriggered by note rate. Slow `lpd` = yawn, fast = quack; pattern the depth (`"<7 5 6 7>"`) for growl shapes.
- **Sub/mid split** — sine sub on roots an octave below the wobble. One bass that tries to do both turns to mud the moment the filter closes.
- **The syncopated second kick** — one extra `bd` on the "and of 3". More than one syncopated kick and it drifts toward garage.
- **The gap** — a beat of near-silence (snare only) at the end of the build. The drop needs air to hit.
- **Wobble rate as arrangement** — 8ths for 8 bars, then 16ths: a brand-new drop with zero new material.
- **Pretty/brutal contrast** — music box intro, brutal drop, music box returns. Write the drop first, then compose the intro *against* it.
- **Snare as an event** — layer `sd` + `cp` + `room(.5)`; in half-time one snare per bar carries the whole backbeat, so it must be huge.

## Practice approach

- Program one bar — kick 1, snare 3, 16th hats — and confirm it *feels* like 70 before adding anything.
- Hold one wobble pitch for 16 bars and vary only the rate and `lpd`; that's a complete drop.
- Always check the sub on small speakers; add a quiet octave double if it disappears, never a louder sub.
- Write the drop first, the intro second — contrast designed backwards is the genre's workflow.
- Reference the canon: Skream's "Midnight Request Line", Benga's "Night", Mala/DMZ, then Caspa/Rusko for the wobble-maximalist branch — notice how few drums actually play.

## Example

```
// ═══ cold harbour — dubstep, 140bpm, half-time ═══
// form: intro 8 | build 4 (gap on its last bar) | drop 16 | breakdown 8 | build2 4 | drop2 16 | outro 4
// half-time: the bar runs at 140, the snare hits on 3 — the body hears 70
setcpm(140 / 4) // one cycle = one bar of 4/4

// ── harmony: Dm – Bb, two bars each (i – bVI in D minor); the wobble plays roots only ──
const roots = "<0!2 5!2>" // scale degrees of d and bb in d minor

// ── drums — kick on 1, layered snare on 3; the "& of 3" kick push arrives with the drop ──
const skel = sound("bd ~ ~ ~ [sd cp] ~ ~ ~").bank("RolandTR909").room(.3)
const push = sound("bd ~ ~ ~ [sd cp] bd ~").bank("RolandTR909").room(.3)
const noKick = sound("~ ~ ~ ~ [sd cp] ~ ~ ~").bank("RolandTR909") // snare alone: gaps and breakdowns
const drums = arrange(
  [8, skel.gain(.45).lpf(1200)],  // intro: the skeleton, muffled
  [3, skel.gain(.6).lpf(saw.range(1200, 8000).slow(3))], // build: opening
  [1, noKick.gain(.5)],           // the gap: beat 1 goes missing
  [16, stack(push.gain(.9), sound("[hh hh oh hh]*4").bank("RolandTR909").gain(.24))], // drop 1
  [8, noKick.lpf(900).gain(.4)],  // breakdown: the ghost of the backbeat, no kick
  [3, skel.gain(.7)],
  [1, sound("~ ~ sd ~").bank("RolandTR909").gain(.6)], // gap 2: the snare, alone
  [16, stack(push.gain(.95), sound("[hh hh oh hh]*4").bank("RolandTR909").gain(.26),
             sound("hh*16").bank("RolandTR909").gain(.1))], // drop 2: hats double up
  [4, sound("~ ~ sd ~").bank("RolandTR909").room(.6).gain(.4)], // outro: it walks off alone
)

// ── sub — sine roots at d1, one note per two bars, sustained: the actual weight ──
const sub = arrange(
  [12, silence], // intro + builds: no weight yet
  [16, n("<0!2 5!2>").scale("d1:minor").gain(.85)],
  [12, silence], // breakdown floats
  [20, n("<0!2 5!2>").scale("d1:minor").gain(.9)], // drop 2 + outro: the root rings out
).sound("sine").attack(.02).sustain(.9).release(.4)

// ── the wobble — sawtooth through a resonant lowpass whose envelope retriggers per note: rate = wobble rate, lpd = the vowel ──
const wobFx = p => p.sound("sawtooth").lpf(140).lpq(9).lpenv("<7 5 6 7>").lpa(.01).lpd("<.18 .1 .3 .14>").gain(.5)
const wob8 = wobFx(n("0!8".add(roots)).scale("d2:minor"))    // 8ths: the lurch
const wobTri = wobFx(n("0!12".add(roots)).scale("d2:minor")) // triplet 8ths: the roll
const wob16 = wobFx(n("0!16".add(roots)).scale("d2:minor"))  // 16ths: the machine gun
const wobble = arrange(
  [12, silence],
  [8, wob8],
  [8, wob16],  // drop 1, second half: the rate doubles — that is the arrangement
  [12, silence],
  [8, wobTri], // drop 2 opens in triplets...
  [8, wob16],  // ...then locks to the grid
)

// ── the melody — music box, delicate on purpose: something for the drop to demolish ──
const mel = n("<[7 ~ ~ 5] [4 ~ ~ ~] [5 ~ ~ 4] [2 ~ ~ ~]>").scale("d5:minor")
const melody = arrange(
  [8, mel.gain(.4)],
  [4, mel.gain(.3).lpf(2000)], // build: it retreats as the riser climbs
  [16, silence],
  [8, mel.gain(.35)],          // breakdown: the beauty returns
  [4, mel.gain(.25).lpf(1500)],
)

// ── pad — dark strings under intro and breakdown ──
const pad = arrange(
  [12, chord("<Dm!2 Bb!2>").anchor("d3").voicing().gain(.3)],
  [16, silence],
  [8, chord("<Dm!2 Bb!2>").anchor("d3").voicing().gain(.32)],
)

// ── the builds — snare roll + pitch climb; the second one is bigger ──
const riser = arrange(
  [8, silence],
  [4, stack(sound("<sd*4 sd*8 sd*16>").bank("RolandTR909").gain("<.2 .35 .5>"),
             note("<d4 eb4 f4 g4>").sound("sawtooth").lpf(2000).gain("<.1 .2 .3 .4>"))],
  [24, silence],
  [4, stack(sound("<sd*4 sd*8 sd*8 sd*16>").bank("RolandTR909").gain("<.25 .4 .5 .7>"),
             note("<d4 eb4 f4 a4>").sound("sawtooth").lpf(2500).gain("<.15 .25 .35 .5>"))],
)

$: drums
$: sub
$: wobble
$: melody
$: pad
$: riser
```
