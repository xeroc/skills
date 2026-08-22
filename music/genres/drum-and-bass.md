Drum & bass's equivalent moment is **the drop** — but the specific one this genre owns: the bar where the double-time break snaps back at 174 after a half-time build. DnB's real protagonist is the breakbeat itself; the "lead instrument" is a drum pattern, chopped and ghosted until it rolls. Sub bass is its dance partner: long sine roots that hold the floor down while the kit flies above. Liquid and dark are the two poles — piano-and-strings lushness versus the reese growl — but both run on the same engine: a syncopated two-step kick/snare skeleton, ghost notes from euclids, and a sub that locks to the harmony, not the kick.

## What the drop actually is

The build usually lives in half-time or in filtered atmosphere — pads, a vocal or piano, the break hinted at through a lowpass — and then the full two-step lands: kick on 1, snare on 2, kick on the "and of 3", snare on 4, ghosts filling every gap, sub dropping to its root at the same instant. The tempo *feels* like it doubles even though the BPM never changed. The genre's arrangement lever is exactly this: half-time sections (kick 1, snare 3) and double-time drops are the same drum kit at the same BPM, and toggling between them is how DnB writes dynamics. A snare roll and one beat of silence right before the landing, and the first bar of the drop does the rest.

## The layers

- **Kick** — `bd` from `.bank("RolandTR909")` (or `.bank("RolandTR808")` for softer liquid), syncopated — never four-on-the-floor, that's the house line. Two placements carry 90% of the genre: beat 1 and the "and of 3".
- **Snare** — `sd` from `.bank("RolandTR909")` or `.bank("RolandTR707")` (the 707 snare is a DnB classic), on 2 and 4; layer `cp` quietly on top for the cut-through tick.
- **Ghost layer** — quiet euclids: `rim(3,16)`, `sd(5,16)` at gain .1–.12. This is what makes a programmed break sound chopped; without ghosts it's a rock beat at the wrong tempo.
- **Hats** — `"[hh hh oh hh]*4"` on 16ths, `sh` for texture. The sizzle that keeps 174 airborne during sparse bars.
- **Sub bass** — `sine` on long root notes, `attack(.01).sustain(.85)`, following the chord loop. In drop2 it often starts moving — root–octave 8ths — as the track's single escalation.
- **Reese** — `supersaw` lowpassed to 200–800Hz with the filter crawling (`lpf(saw.range(200, 800).slow(4))`): the dark/techstep signature, movement without notes.
- **Liquid keys** — `piano` chords and `gm_synth_strings_1` pads, 9ths and 7ths, pushed on offbeats, drenched in `room` and a dotted delay. The lush pole.
- **Atmos** — Dirt `space`/`wind` textures way back in `room(1)`, or a `gm_flute`/`gm_voice_oohs` figure — DnB intros live on atmosphere.

## Sample kit

- **Kit** — `.bank("RolandTR909")` two-step with 909/808 kick choice per pole; the 707 snare (`.bank("RolandTR707")`) is a DnB classic. Ghost euclids + hats stay default.
- **Real breaks — the genre's own tool** — `github:Bubobubobubobubo/Dough-Amen`: 80 chopped-ready breaks, BPM-tagged (`amen1` runs 135–178; grab the ones near 174):
  ```js
  samples('github:Bubobubobubobubo/Dough-Amen'); // first play may be silent while it loads — run again
  $: s("amen1:13").loopAt(1).chop(8)                  // the break as the lead instrument
  $: s("amen3:0").splice(8, "<0 1 2 3 4 5 6 7>")      // re-sequenced slices
  ```
  Layer a synthetic `bd` under for weight; license unknown — foreground/playground use. `github:yaxu/clean-breaks` adds the `amen` original plus 28 funk breaks.
- **Sub & reese** — synths, correctly: `sine` sub, `supersaw` reese with a crawling `lpf`.
- **Liquid keys** — `piano`/`steinway`, `gm_synth_strings_1`; atmosphere from Dirt `space`/`wind`.

## Harmony

Two vocabularies, one per pole. Liquid loves descending lush loops; dark loves two notes.

- **The liquid descent** — i9 – bIII^9 – bVII^9 – bVI^7 in F minor: **Fm9 – Ab^9 – Eb^9 – Db^7**, two bars each. Falls through the key like water; the sub outlines the same roots.
- **The minor roller** — i9 – bVI^7 – bVII9: **Fm9 – Db^7 – Ebm9**. Chunkier, half-step-lower, made for the reese.
- **The dark two-note** — **F – Eb** (i – bVII in F minor): the techstep riff. The sub just walks F–Eb; all menace comes from the sound.
- **The liquid major** — I^9 – vi9 – ii9 – V7 in C: **C^9 – Am9 – Dm9 – G7**. Sunday-afternoon liquid; keep the drums heavy anyway.

## Rhythm & feel

- **Tempo**: 170–175 — 174 is the default; 170 for loungey liquid, 175+ for the jumpier end.
- **Two-step skeleton** (16th grid, one bar): `"bd ~ ~ ~ sd ~ ~ ~ ~ ~ bd ~ sd ~ ~ ~"` — kick 1, snare 2, kick "and of 3", snare 4. This string is the genre's genome.
- **Half-time skeleton** (8th grid): `"bd ~ ~ ~ sd ~ ~ ~"` — kick 1, snare 3; feels like 87 at the same BPM. Use for mids and builds.
- **Ghosts**: `rim(3,16)` + `sd(5,16)` at gain .1, running continuously under the skeleton.
- **Hats**: `"[hh hh oh hh]*4"`, or bare `hh*16` in darker variants.
- **Sub**: whole-bar roots; when it moves, root–octave 8ths — `n("[0 7]*8")` in scale degrees.
- **Fills**: every 4th or 8th bar, a 16th-snare run on beat 4 (`"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ sd sd sd sd"`) — the "chop" that simulates an edited break.
- **Feel**: no swing. The roll comes from ghost placement and the "and of 3" kick; the grid stays dead straight.

## Structure

```
intro 8 | build 4 | drop 16 | half-time mid 8 | build2 4 | drop2 16 | outro 8
energy ▃▄▂▃▅▆▇▇▇▇▇▇▇▇▇▇ ▄▄▄▅ ▅▆ █▇▇▇▇▇▇▇▇▇▇▇▇ ▅▄▃
```

Intro: atmosphere (pads/strings/keys) with the break filtered to a whisper. Build: roll + riser + one-beat gap. Drop: full break + sub. The half-time mid is the genre's signature move — the same kit at half pressure so drop2 has somewhere to land. Drop2 escalates *one* thing: the sub starts rolling, or the reese replaces the sine. Outro mirrors the intro for the DJ.

## Techniques that actually create "drum & bass"

- **Layered break from three sounds** — two-step skeleton + euclid ghosts + 16th hats = a "chopped break" with zero samples. The ghosts are non-negotiable; straight two-step alone reads as pop-rock at 174.
- **Sub locks to harmony, not the kick** — the bass holds long roots while the kick syncopates around them. Bass that doubles the kick pattern turns DnB into big room.
- **Half-time/double-time as the dynamic** — `"bd ~ ~ ~ sd ~ ~ ~"` sections are how you write a quiet verse without changing tempo or kit.
- **Liquid vs dark as a one-switch choice** — swap `piano`/strings for `supersaw` reese over the same chord loop and the track changes species. Write the loop, then decide the pole.
- **The roll and the gap** — `<sd*4 sd*8 sd*16 sd*16>` into one beat of silence. The silence is load-bearing.
- **Escalate one thing in drop2** — sub starts moving, hats double, ghosts get a fill. Never all three; pick the one your drop1 lacked.
- **Long subs, ducked lightly** — `.duckdepth(.5)` or less: DnB kicks are short, so the pump is subtle; you're clearing 100ms, not breathing.

## Practice approach

- Loop the two-step + ghosts at 174 until it rolls with zero swing — if it feels stiff, add or move ghosts, never quantize harder.
- Write the sub line first, drums second; the kit's job is to decorate the bass's gaps.
- Take one chord loop and produce it twice — once liquid (piano + strings + sine), once dark (reese + stabs) — to internalize the pole switch.
- Write the half-time mid *before* drop2 so the escalation is budgeted, not improvised.
- Reference: Calibre and LTJ Bukem for liquid, Goldie's "Terminator" and Ed Rush for the dark engine, and any Roni Size for the dialogue between the two.

## Example

```
// ═══ glass river — liquid drum & bass, 174bpm ═══
// form: intro 8 | build 4 | drop 16 | half-time mid 8 | build2 4 | drop2 16 | outro 8
// the break is the lead: two-step skeleton + euclid ghosts + 16th hats = a breakbeat from three sounds
setcpm(174 / 4) // one cycle = one bar of 4/4

// ── harmony: Fm9 – Ab^9 – Eb^9 – Db^7, two bars each — i9 bIII^9 bVII^9 bVI^7 in F minor ──
const walk = "<0!2 2!2 4!2 5!2>" // degrees of f, ab, eb, db in f minor

// ── the break — kick 1, snare 2, kick "and of 3", snare 4, on the 16th grid ──
const twoStep = sound("bd ~ ~ ~ sd ~ ~ ~ ~ ~ bd ~ sd ~ ~ ~").bank("RolandTR909")
const halfTime = sound("bd ~ ~ ~ sd ~ ~ ~").bank("RolandTR909").room(.4) // kick 1, snare 3 — feels like 87
const ghosts = stack(sound("rim(3,16)").bank("RolandTR909").gain(.12),
                     sound("sd(5,16)").bank("RolandTR909").gain(.1))
const hats = sound("[hh hh oh hh]*4").bank("RolandTR909").gain(.22)
const fill = sound("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ sd sd sd sd").bank("RolandTR909").gain(.4)

const drums = arrange(
  [8, twoStep.gain(.35).lpf(900)],            // intro: the break, filtered, half-heard
  [4, sound("<sd*4 sd*8 sd*16 sd*16>").bank("RolandTR909").gain("<.2 .3 .45 .6>")], // the roll
  [16, stack(twoStep.gain(.9), ghosts, hats)], // drop: full break
  [8, stack(halfTime.gain(.8),
            sound("hh*8").bank("RolandTR909").gain(.15))], // mid: half-time, the air changes
  [4, sound("<sd*4 sd*8 sd*16 sd*16>").bank("RolandTR909").gain("<.25 .35 .5 .65>")],
  [16, stack(twoStep.gain(.95).every(4, x => stack(x, fill)), ghosts, hats,
             sound("sh*16").bank("RolandTR909").gain(.1))], // drop2: ghosts answer the fill
  [8, twoStep.gain(.4).lpf(800)],
)

// ── sub — long sine roots in the drops; the rolling octave line arrives in drop2 ──
const subLong = n("<0!2 2!2 4!2 5!2>").scale("f1:minor").gain(.85)
const subRoll = n("[0 7]*8".add(walk)).scale("f1:minor").gain(.7) // root–octave 8ths

const sub = arrange(
  [12, silence],
  [16, subLong],
  [8, silence],  // half-time mid: weightless on purpose
  [4, silence],
  [16, subRoll], // drop2: the one escalation — the sub starts moving
  [8, n("<0>").scale("f1:minor").gain(.6)],
).sound("sine").attack(.01).sustain(.85).release(.3)

// ── keys — the liquid signature: 9th chords on piano, pushed on the "and of 3" ──
const keys = chord("<Fm9!2 Ab^9!2 Eb^9!2 Db^7!2>").anchor("f4").voicing()
  .struct("[x ~ ~ ~ ~ x ~ ~]")

const keysL = arrange(
  [8, keys.gain(.4)],
  [4, silence],
  [16, keys.gain(.5)],
  [8, keys.gain(.35)],
  [4, silence],
  [16, keys.gain(.5).jux(rev)], // drop2: the echo answers itself across the stereo field
  [8, keys.gain(.3)],
).sound("piano").room(.5).delay(".35:.25:.3")

// ── pad — strings under the intro and the half-time mid ──
const pad = arrange(
  [8, chord("<Fm9!2 Ab^9!2 Eb^9!2 Db^7!2>").anchor("f3").voicing().gain(.25)],
  [24, silence],
  [8, chord("<Fm9!2 Ab^9!2 Eb^9!2 Db^7!2>").anchor("f3").voicing().gain(.3)],
  [24, silence],
).sound("gm_synth_strings_1").attack(1.5).release(3).room(.9)

// ── the reese — the dark pole shown once: detuned supersaw, filter crawling, mid section only ──
const reese = arrange(
  [28, silence],
  [8, n(walk).scale("f1:minor").lpf(saw.range(200, 800).slow(4)).gain(.5)],
  [28, silence],
).sound("supersaw")

$: drums
$: sub
$: keysL
$: pad
$: reese
```
