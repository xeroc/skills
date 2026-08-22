House's equivalent moment is **the return** — the bar where the kick comes back. House is groove music: the track doesn't build to a dramatic reveal, it builds to the reinstatement of itself. The kick pulls out, a pad or a vocal swells in the vacuum, the filter drags shut — then the plain 909 four-on-the-floor lands again with bass, stabs and the offbeat open hat all pumping against it. If that landing doesn't feel like relief, nothing later in the track can fix it.

## What the return actually is

Eight to sixteen bars where the kick is pulled and replaced by the track's most musical material — pads, a vocal hook, a piano riff — often with the low end rolled off so the breakdown feels weightless. Then a 4–8 bar build: snare roll or noise riser, a filter opening, information density climbing bar by bar. Then the return: kick, bass, stabs and hats land together — usually after a one-beat gap of near-silence — and the sidechain pump converts the flat groove you started with into the biggest moment of the song. The tell that you did it right: the returning groove is usually the *simplest* material in the track. Tension came from what was removed; the payoff is the same loop restored, now with context.

## The layers

- **Kick** — `bd` from `.bank("RolandTR909")`, four on the floor, gain around .9, a little `shape(.2)` for grit. The 909 kick *is* the house kick — 808 is too soft for this job, and a sampled techno kick is too aggressive.
- **Offbeat open hat** — `oh` from the same 909 bank, `"[~ oh]*4"`, gain .25–.35. The single loudest genre signal available: it says "house" before any chord does.
- **Closed hats** — `hh` on 16ths with a real velocity pattern — `.gain("[.2 .45 .2 .3 .2 .45 .2 .3]*2")` — with `swing(.08)`–`swing(.12)` for the classic jack, near zero for mainroom.
- **Clap** — `cp` from the 909 bank on `"~ cp ~ cp"`, `room(.2)`. Bring it in late; a backbeat is something the track has to earn.
- **Shaker and percussion** — `sh` 16ths low in the mix, `rim` or `cb` for the Chicago jack. Percussion carries the humanity, the kick carries the machine.
- **Bass** — `sawtooth` through `lpf(700)`–`lpf(900)` (or `sine` for deep house) playing offbeat 8ths or root–octave 16ths, always in the gaps the kick leaves, always ducked by the kick with `duckorbit` — the pump is as much a part of the bassline as the notes are.
- **Chord stabs** — 7th/9th chords as short `sawtooth` hits — short `decay`, `sustain(0)`, a touch of `room` reads as organ — or `piano` for the New York variant. Syncopated placement on the "and"s matters more than the voicing.
- **Pad** — `gm_synth_strings_1` or `supersaw`, `attack` 1+, `release` 2+, `room(.8)`. The breakdown's floor.
- **Vocal texture** — `misc` chops or `gm_voice_oohs` low in the mix — atmosphere first, lyric second.

## Sample kit

- **Kit** — `.bank("RolandTR909")` throughout: the 909 kick is the genre's kick. `.bank("RolandTR707")` for the vintage/Chicago character, `.bank("RolandTR808")` never for the kick.
- **Organ stabs — the idiom upgrade** — `gm_drawbar_organ` (deep/garage) or `gm_percussive_organ` (bright, jackin') replaces the filtered-sawtooth stab: short `decay(.1).sustain(0)`, syncopated on the "and"s. `piano` remains the New York variant.
- **Bass** — `sawtooth` under `lpf(700–900)` (synth-correct); `gm_synth_bass_1` for a rounder sampled feel in deep house.
- **Pad** — `gm_synth_strings_1` or `supersaw`, long attack/release, `room(.8)`.
- No pack needed — the preloaded tiers cover house completely. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Extended-chord harmony: m7, m9, ^7, ^9, 7ths. A bare triad reads as pop-EDM; the 7th is the minimum ticket. Minor keys, four chords, two bars each — let the filter do the developing.

- **The deep house loop** — i9 – bIII^9 – iv9 – v7 in F minor: **Fm9 – Ab^9 – Bbm9 – Cm9**. Warm, horizontal, endless. Works at 122 in a basement and at 126 on a terrace.
- **The gospel lift** — ii9 – V7 – I^9 in Eb: **Fm9 – Bb7 – Eb^9**. The organ-house cadence; landing the I^9 on the return's first bar is the oldest trick that still works every time.
- **The piano anthem** — bVI^9 – bVII9 – i9 in C minor: **Ab^9 – Bbm9 – Cm9**. Hands-in-the-air loop; the i arriving with the returning kick is the whole arrangement.
- **The eternal two-chord** — ii9 – V7 in C that never resolves: **Dm9 – G7**, forever. Loopy deep house trusts the groove over the cadence.

Voice with `chord("<Fm9!2 Ab^9!2 Bbm9!2 Cm9!2>").anchor("f4").voicing()`; move the anchor to `c5` when a section needs to lift.

## Rhythm & feel

- **Tempo**: 120–128 — deep house 118–122 with swing on, classic/NY 122–125, mainroom/tech 126–128 with swing off.
- **Kick**: `bd*4` — dead center, never syncopated. Everything else syncopates around the kick; the kick never returns the favor.
- **Open hat**: `"[~ oh]*4"` — every offbeat 8th, the "tss tss" that is half the genre.
- **Clap**: `"~ cp ~ cp"` — 2 and 4.
- **Shaker**: `"sh*16"` with a two-step velocity pattern, swung.
- **Bass**: `"~ f1 ~ f1 ~ f1 ~ f1"` — offbeat 8ths, the pump — or root–octave `"[f1 f2]*8"` for the jack.
- **Stabs**: 8th-grid struct `"[~ x ~ ~ ~ x ~ ~]"` — the "and of 1" and the "and of 3".
- **Feel**: swing only the hats and shaker (`.08`–`.12`), never the kick. The kick is the grid; swing is the sauce on top of it.

## Structure

DJ form — 8-bar phrases, a long drum intro and outro so it can be mixed:

```
intro 8 | groove 8 | bass 16 | stabs 16 | breakdown 8 | build 4 | return 16 | outro 8
energy ▂▂▂▃▃▃▄▄▄▅▅▂▂▁▂▃▆▆▆▆▆▅▄▃▂
```

One element enters or leaves every 8 bars; the breakdown is the only place the kick stops; the build is 4 bars and belongs to the riser; the return's first bar lands kick + bass + stab together after a one-beat gap.

## Techniques that actually create "house"

- **The offbeat open hat** — one sound, instantly legible genre. Program it first; if the kick + oh loop alone doesn't feel like house, no chord will save it.
- **The sidechain pump** — kick carries `.duckorbit("2:3").duckdepth(.8).duckattack(.16)`, bass and stabs ride `.orbit(2)`/`.orbit(3)`. Bass that isn't ducked against a four-on-the-floor reads as a demo.
- **Seventh-chord stabs on the upbeats** — the placement does the genre work; the 9ths just make it lush. Hit the "and"s, leave the downbeats to the kick.
- **Bass in the gaps** — offbeat 8ths or root–octave 16ths, never on the kick. The empty downbeat is what makes the pump audible.
- **The breakdown → return arc** — pull the kick, float the pad, run a 4-bar riser, one-beat gap, land. Relief is the product; the returning pattern being the simplest of the song is the proof.
- **The filter build** — sweep an `lpf` open across the last 8 bars (`saw.range(400, 6000).slow(8)`) so the return arrives already moving.
- **The organ tone** — sawtooth + fast decay + small room = organ-ish stab without a patch change; `piano` for the NY flavor.
- **The jack layer** — quiet `sh` 16ths and a `cb` hit give the Chicago push; it's the difference between a groove and a loop.

## Practice approach

- Loop eight bars of just kick + offbeat open hat and make *that* feel good before adding anything.
- Program a bassline that never once lands on a kick — then duck it anyway.
- Reference the canon by ear — Frankie Knuckles, MK's "Burning", Masters At Work, Kerri Chandler, Mr Fingers' "Can You Feel It" — and notice how few sounds are actually playing.
- Ride one filter for 16 bars without touching the notes; that's a house arrangement lesson in a single move.
- Write the same chord loop at 121 and at 127 and A/B them. Tempo is a genre decision in house, not a technicality.

## Example

```
// ═══ basement hours — deep house, 124bpm ═══
// form: intro 8 | groove 8 | bass 16 | stabs 16 | breakdown 8 | build 4 | return 16 | outro 8
// the genre in three moves: 909 four-on-the-floor, the offbeat open hat, everything ducking against the kick
setcpm(124 / 4) // one cycle = one bar of 4/4

// ── harmony: Fm9 – Ab^9 – Bbm9 – Cm9, two bars each — i9 bIII^9 iv9 v7 in F minor ──
const chords = "<Fm9!2 Ab^9!2 Bbm9!2 Cm9!2>"
const roots = "<0!2 2!2 3!2 4!2>" // degrees of f, ab, bb, c in f minor

// ── kick — the 909, dead straight; its second job is ducking orbits 2 (bass) and 3 (stabs, pad) ──
const kick = arrange(
  [8, s("bd*4").bank("RolandTR909").gain(.6).lpf(700)],       // filtered: the mix-in
  [40, s("bd*4").bank("RolandTR909").gain(.9)],                // groove→stabs: unbroken floor
  [8, silence],                                                // breakdown: the floor is pulled
  [4, s("bd*4").bank("RolandTR909").gain(.65)],                // build: the pump sneaks back early
  [16, s("bd*4").bank("RolandTR909").gain("[1 .92 .96 .92]")], // the return: biggest, and simplest
  [8, s("bd*4").bank("RolandTR909").gain(.75).lpf(900)],       // outro: the door closing
).duckorbit("2:3").duckdepth(.8).duckattack(.16)

// ── hats + clap — the offbeat open hat is the genre marker; the backbeat is earned late ──
const ohh = sound("[~ oh]*4").bank("RolandTR909").gain(.3)
const chh = sound("hh*16").bank("RolandTR909").gain("[.2 .45 .2 .3 .2 .45 .2 .3]*2").swing(.1)
const clp = sound("~ cp ~ cp").bank("RolandTR909").gain(.45).room(.2)
const shake = sound("sh*16").gain(.1).pan(sine.slow(4).range(.35, .65))

const drums = arrange(
  [8, ohh.gain(.22)],
  [8, stack(ohh, chh.gain(.18))],
  [32, stack(ohh, chh.gain(.2), clp, shake)], // bass + stabs sections: full breath
  [8, ohh.gain(.15)],                         // breakdown: one breath left
  [4, chh.gain(.1)],                          // the build belongs to the riser
  [16, stack(ohh.gain(.32), chh.gain(.22), clp.gain(.5))], // the return
  [8, ohh.gain(.24)],
)

// ── bass — offbeat 8ths in the kick's gaps, root follows the chords, ducked on orbit 2 ──
const bassline = n("[~ 0]*4".add(roots)).scale("f1:minor")
const bass = arrange(
  [16, silence],
  [32, bassline],
  [12, silence],
  [16, bassline.every(4, x => x.ply(2))], // the return: a 16th push every 4th bar
  [8, note("<f1 ~>").gain(.4)],           // outro: one note, exhaling
).sound("sawtooth").decay(.18).sustain(0).gain(.6).lpf(800).orbit(2)

// ── stabs — the 9th chords as rhythm: organ-ish saw on the "and of 1" and the "and of 3" ──
const stab = chord(chords).anchor("f4").voicing().struct("[~ x ~ ~ ~ x ~ ~]")
const stabs = arrange(
  [32, silence],
  [16, stab.gain(.5).decay(.16).sustain(0)],
  [12, silence],
  [16, stab.gain(.6).off(1/8, x => x.transpose(-12).gain(.2))], // the return, octave-down echo
).sound("sawtooth").room(.3).orbit(3)

// ── pad — strings under the chords; the breakdown's floor, ducked with everything else ──
const padChord = chord(chords).anchor("f3").voicing()
const pad = arrange(
  [8, silence],
  [40, padChord.gain(.12)],
  [8, padChord.gain(.2)],  // breakdown: the pad is the floor
  [20, padChord.gain(.14)],
).sound("gm_synth_strings_1").attack(1.5).release(3).room(.9).orbit(3)

// ── the build — a noise riser made of hats, plus one clap ping ──
const riser = arrange(
  [48, silence],
  [4, stack(sound("hh*8").bank("RolandTR909").speed("<1 1.5 2 4>").gain("<.12 .2 .3 .45>"),
             sound("<~ ~ ~ cp>").bank("RolandTR909").gain(.3).room(.4))],
)

$: kick
$: drums
$: bass
$: stabs
$: pad
$: riser
```
