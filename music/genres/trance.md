Trance's equivalent moment is **the breakdown**: the beat drops out, the filter closes all the way down to a whisper, a melody you haven't heard yet floats over bare pads — and then the kick returns, the filter rips open, and the same five notes that were ambient background become an anthem. Everything in trance production is engineered toward that one reveal. Where jazz spends its tension in a cadenza and pop in a bridge, trance spends it in a **low-pass filter**.

## What the template actually is

The classic strudel trance sketch — the one that gets pasted around — is six lines, and every line is load-bearing:

- **`setcpm(136/4)`** — 132–140bpm, the genre's window. One cycle = one bar of 4/4, so `*16` means 16th notes.
- **`register('acidenv', (x, pat) => pat.lpf(100).lpenv(x*9).lps(.2).lpd(.12))`** — a reusable chained function that bolts a TB-303-style filter envelope onto anything: the cutoff starts at 100Hz, the envelope slams it open by `x*9` semitones-equivalent, then it _exhales_ back down over `.lpd(.12)` seconds to a `.lps(.2)` sustain. This one envelope IS the trance sound — every sawtooth in the genre is a saw plus this breath.
- **`n("<0 4 0 9 7>*16")`** — the riff: scale degrees root–fifth–root–octave-plus-minor-third–root, hammered in 16ths. Root, fifth, octave, ♭3: that's the "Sandstorm"/"Children" DNA, the single most recognizable contour in the genre. Static, hypnotic, five notes.
- **`n("<0>*16").trans(-24).s("supersaw")`** — the bass: the same 16th grid, but only the root, two octaves down, on a detuned saw stack. The riff and bass are one instrument split in two.
- **`note("<g3bb3d4 bb3d4f4 eb3g3bb3 f3a3c4>*4")`** — offbeat 8th chord stabs on the i–ii–bVI–bVII loop (or its cousin i–bVI–bIII–bVII): minor-key four-chord cycling, hit on the "and" of every beat so the kick owns the downbeat.
- **`s("bd!4").duck("3:4:5:6").duckdepth(.8).duckattack(.16)`** — four-on-the-floor kick that **ducks** orbits 3, 4, 5 and 6: everything musical breathes around the kick. This is sidechain compression expressed as pattern language — the pump is the groove.
- **`slider(0.655)`** — the filter-envelope amount isn't a constant, it's a live slider. Trance is DJ music: the performer's main instrument is the filter cutoff, ridden for eight bars at a time.

## The layers, top to bottom

- **Kick** — plain, loud, four-on-the-floor. Never decorated; its job is to trigger the duck.
- **Rolling bass** — root 16ths, supersaw, low. Locked to the kick grid but filling the spaces the duck carves out.
- **The riff** — root–5th–octave 16ths, mid register, acid-env'd. The riff is percussion with pitch.
- **Offbeat stabs** — the chord loop, sawtooth, on every "&". Harmony as rhythm.
- **Top / offbeat open hat** — the "tss" on the offbeat 8ths. Without it, it's techno; with it, it's trance.
- **Pad** — sustained chords under the breakdown, the only layer allowed to be slow.

## Sample kit

- **Kit** — default kit or `.bank("RolandTR909")` for the canonical supersaw-era drums; the offbeat `oh` is the genre's fingerprint either way.
- **Bass & riff** — `supersaw` rolling bass, acid-env'd `sawtooth` riff: synths, no samples — this is correct for the genre.
- **Offbeat stabs** — `sawtooth`; `gm_lead_2_sawtooth` is a preloaded alternative with a slightly softer grain.
- **Breakdown pad** — `gm_synth_strings_1` (or `gm_string_ensemble_1` for a more orchestral lift), `attack` 2+, `room(.9)`.
- No pack needed — the preloaded tiers cover trance. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Minor-key four-chord loops, two bars per chord, running the entire track — the chords are a circle, not a journey. In A minor (the example's key):

- **i – ♭VI – ♭III – ♭VII** — Am – F – C – G. The genre's default loop (the "Children" / "Sandstorm" family): fully diatonic aeolian, so a riff walked through it stays pure chord tones — and it never cadences, the ♭VII simply turns back into the i.
- **i – ii – ♭VI – ♭VII** — Am – Bm – F – G. The supertonic cousin (the "Adagio for Strings" family); the ii on the front of the loop darkens it without breaking the circle.
- **The two-chord teaser: i – ♭VI** — Am – F. For intros and second breakdowns: half the loop is the whole harmony. State it filtered, let the full four chords arrive with the drop.
- **The walk, not the change** — `.add("<0!2 5!2 2!2 6!2>")` transposes the five-note roll diatonically through the loop (roots a → f → c → g): same riff, four chords, zero new material. Movement comes from walking material over static harmony, never from new chords.

One key per track, no modulation, no dominant resolution. The loop's refusal to arrive is what makes eight minutes of the same four chords feel like flight instead of stagnation.

## Techniques that actually create "trance"

- **The roll as hypnosis** — a five-note 16th loop works because it repeats for 8+ bars without apology. Trance is the one genre where repetition is the feature, not a bug to be varied away. Structure changes every 8 bars; the pattern doesn't.
- **The duck is the groove** — with `duckdepth(.8)` and a slow-ish attack, every chord stab and bass note swells _behind_ the kick. The rhythm section breathes like one lung.
- **Filter = emotion axis** — the exact same loop at `acidenv(slider(.3))` is a breakdown and at `slider(.7)` is a climax. Nothing about the notes changed. If a trance track feels flat, the fix is almost always envelope amount automation, not new notes.
- **Supersaw width** — the built-in `supersaw` sound (a detuned saw stack) make single notes fill the stereo field. One note, many voices.
- **Minor-key loop discipline** — i–bVI–bIII–bVII or i–ii–bVI–bVII, two bars per chord, forever. The chords are a circle, not a journey.
- **Sliders as performance** — register the macro, expose the amount, play it. The code equivalent of a DJ riding the filter for the crowd.

## The trance problem: movement without breaking the loop

A static five-note roll plateaus after two loops. The genre's solution is not to change the loop — it's to move things _over_ it:

- **Walk the riff through the chords** — `n("<0 4 0 9 7>*16".add("<0!2 5!2 2!2 6!2>"))` transposes the shape diatonically through i–bVI–bIII–bVII. Same five notes, four chords, zero new material — the loop appears to travel.
- **The melody is a traveller, not a loop** — over the static 16ths, write long notes that change _once per chord_: one held chord tone, one step, breathe. The roll is the floor; the melody is the person walking on it. Contour rule same as pop: peak late, on the bVII chord, ideally a suspended tone (the ♭7 or 4th) that aches to resolve.
- **Octave lift for the anthem** — the breakdown states the melody, the anthem restates it with the last phrase lifted an octave. Identical rhythm, doubled altitude: the cheapest huge move in electronic music.
- **Question/answer with yourself** — state a phrase, then answer it reversed (`.jux(rev)`, `.rev()`) or echoed an octave down (`.off(1/8, x => x.transpose(-12))`).
- **Breakdown physics** — pull kick and bass entirely, keep the pad, state the melody small and filtered. The size of the anthem is exactly the size of the silence before it.

## Structure (DJ logic, 8-bar multiples)

intro (roll, filtered, no kick) → groove (kick + bass + duck enter) → build (stabs arrive, snare roll, filter opens) → **roll** (full template, the track as a loop) → **breakdown** (beat gone, pad blooms, melody first statement) → build 2 (kick returns, melody re-asks its question) → **anthem** (melody restated with octave lift + harmony, everything at full filter) → variation (echoes, mirrors, riff octave sparkle) → outro (drums and bass alone — long enough to mix out of).

## Practice approach

- Copy the six-line template and change nothing but the key. Get the pump right before adding a single note.
- Play the sliders for a full minute before writing any new pattern — feel what envelope amount alone does to the loop.
- Walk the riff through the chords with `.add()` before writing a melody; that's the whole genre in one transformation.
- Write the melody with one note per chord change first. If it doesn't move you that sparse, denser notes won't save it.
- Steal the contour of one anthem you love (peak on the bVII, resolve on the loop restart) and re-voice it in your key.

## Example

```
// ═══ awoken — classic trance, 136bpm ═══
// form: intro 8 | groove 8 | build 4 | roll 8 | breakdown 8 | build2 4 | anthem 8 | variation 8 | outro 8
// the template expanded: the roll first states itself, then learns to walk (chord-following via .add),
// then a melody travels over it — breakdown states it small, the anthem lifts it an octave
setcpm(136 / 4) // one cycle = one bar of 4/4

// the genre in one macro: a saw + this filter envelope = trance (amount exposed as a live slider)
register('acidenv', (x, pat) => pat.lpf(100)
  .lpenv(x * 9).lps(.2).lpd(.12)
)

// ── harmony: Am–F–C–G, i–bVI–bIII–bVII in A minor — diatonic, so the walked roll stays pure chord tones ──
const walk = "<0!2 5!2 2!2 6!2>" // roots: a → f → c → g, two bars each

// the roll: root–5th–root–♭3(oct)–root, the archetype; walked = the same five notes through four chords
const riffRoll = n("<0 4 0 9 7>*16".add(walk)).scale("a2:minor")
const riffStatic = n("<0 4 0 9 7>*16").scale("a2:minor") // pure identity, for intro/breakdown/outro
const riffUp = n("<0 4 0 9 7>*16".add(walk)).scale("a4:minor") // two octaves up, the sparkle

// ── the melody — the traveller over the static floor. one movement per chord, peak (f6) on the bVII ──
const melA = n("<[0@3 ~] [2 1] [3@2 2] [1 ~] [2@2 3] [4 ~] [5@2 4] [2 1]>").scale("a5:minor")
// the anthem: same question, but the answer climbs to the octave (a6) instead of falling home
const melB = n("<[0@3 ~] [2 1] [3@2 2] [1 ~] [2@2 4] [5 ~] [7@2 5] [4 2]>").scale("a5:minor")
const melBh = n("<[0@3 ~] [2 1] [3@2 2] [1 ~] [2@2 4] [5 ~] [7@2 5] [4 2]>".add(-2)).scale("a5:minor") // a third below
const melAlow = n("<[0@3 ~] [2 1] [3@2 2] [1 ~] [2@2 3] [4 ~] [5@2 4] [2 1]>".add(-7)).scale("a5:minor") // an octave below

// ── kick — plain, four on the floor; its only job is to duck everything musical ──
const kick = arrange(
  [8, silence],
  [8, s("bd!4")],
  [4, s("bd!4")],
  [8, s("bd!4")],
  [8, silence],   // breakdown: the beat is pulled entirely
  [4, s("bd!4")], // build 2: the pump returns before the anthem
  [8, s("bd!4")],
  [8, s("bd!4")],
  [8, s("bd!4")], // outro: drums alone, long enough to mix out of
).duckorbit("2:3:4:5").duckdepth(.75).duckattack(.16)

// ── bass — the roll's shadow: root 16ths, supersaw, two octaves down ──
const bass = arrange(
  [8, silence],
  [8, n("<0>*16".add(walk)).scale("a1:minor").gain(.5)],
  [4, n("<0>*16".add(walk)).scale("a1:minor").gain(.5)],
  [8, n("<0>*16".add(walk)).scale("a1:minor").gain(.52)],
  [8, silence],
  [4, silence],
  [8, n("<0>*16".add(walk)).scale("a1:minor").gain(.54)],
  [8, n("<0>*16".add(walk)).scale("a1:minor").gain(.5)],
  [8, n("<0>*16".add(walk)).scale("a1:minor").gain(.4)],
).s("supersaw").acidenv(slider(.632)).orbit(2)

// ── the riff — same five notes all song; only the filter amount and the walk change ──
const riff = arrange(
  [8, riffStatic.gain(.18).acidenv(slider(.28))], // intro: dark whisper, the identity stated
  [8, riffRoll.gain(.34).acidenv(slider(.55))],   // groove: it learns to walk
  [4, riffRoll.gain(.4).acidenv(slider(.6))],
  [8, riffRoll.gain(.42).acidenv(slider(.655))],  // the roll: the template at full breath
  [8, riffStatic.gain(.1).acidenv(slider(.22))],  // breakdown: five notes, almost gone
  [4, riffRoll.gain(.3).acidenv(slider(.5))],     // build 2: re-entering, opening
  [8, riffRoll.gain(.22).acidenv(slider(.5))],    // anthem: tucked under the voice
  [8, stack( // variation: the octave sparkle — the same roll, twice as high, singing along
    riffRoll.gain(.36).acidenv(slider(.62)),
    riffUp.gain(.1).acidenv(slider(.62)),
  )],
  [8, riffStatic.gain(.25).acidenv(slider(.3))], // outro: static again, the door closing
).s("sawtooth").orbit(3)

// ── offbeat stabs — the chord loop as rhythm, hit on every & ──
const stabs = arrange(
  [16, silence],
  [4, note("<[a3,c4,e4] [f3,a3,c4] [c4,e4,g4] [g3,b3,d4]>*4").gain(.9).acidenv(slider(.4))],
  [8, note("<[a3,c4,e4] [f3,a3,c4] [c4,e4,g4] [g3,b3,d4]>*4").gain(1.1).acidenv(slider(.495))],
  [12, silence],
  [8, note("<[a3,c4,e4] [f3,a3,c4] [c4,e4,g4] [g3,b3,d4]>*4").gain(1.1).acidenv(slider(.495))],
  [8, note("<[a3,c4,e4] [f3,a3,c4] [c4,e4,g4] [g3,b3,d4]>*4").gain(1).acidenv(slider(.45))],
  [8, silence],
).s("sawtooth").room(.3).orbit(3)

// ── pad — the only layer allowed to be slow; blooms in the breakdown ──
const pad = arrange(
  [8, chord("<Am!2 F!2 C!2 G!2>").anchor("a3").voicing().gain(.08)],
  [8, chord("<Am!2 F!2 C!2 G!2>").anchor("a3").voicing().gain(.1)],
  [4, chord("<Am!2 F!2 C!2 G!2>").anchor("a3").voicing().gain(.1)],
  [8, chord("<Am!2 F!2 C!2 G!2>").anchor("a3").voicing().gain(.12)],
  [8, chord("<Am!2 F!2 C!2 G!2>").anchor("a3").voicing().gain(.18)], // the floor of the breakdown
  [4, chord("<Am!2 F!2 C!2 G!2>").anchor("a3").voicing().gain(.18)],
  [8, chord("<Am!2 F!2 C!2 G!2>").anchor("a3").voicing().gain(.18)],
  [8, chord("<Am!2 F!2 C!2 G!2>").anchor("a3").voicing().gain(.12)],
  [8, silence],
).s("supersaw").attack(1.2).release(2.5).room(.8).orbit(5)

// ── the melody — movement over the loop: stated small, lifted for the anthem, mirrored in the variation ──
const melody = arrange(
  [28, silence],
  [8, melA.gain(.32).acidenv(slider(.45))], // breakdown: first statement, small and filtered
  [4, melA.gain(.28).acidenv(slider(.4))],  // build 2: the question asked again, the anthem will answer
  [8, stack( // anthem: octave lift in the answer, plus a third below — the same voice, grown
    melB.gain(.42).acidenv(slider(.7)),
    melBh.gain(.26).acidenv(slider(.6)),
  )],
  [8, stack( // variation: answered by its own reflection — mirrored right, octave-divisi left
    melA.gain(.34).acidenv(slider(.55)).jux(rev),
    melAlow.gain(.18).acidenv(slider(.5)),
  )],
  [8, silence],
).s("supersaw").orbit(4).room(.5).delay(".22:.35:.25").release(.3)

// ── hats — the offbeat "tss" is the genre marker; 16ths only when it's full ──
const hats = arrange(
  [8, sound("[~ oh]*4").gain(.22)],
  [8, stack(sound("[~ oh]*4").gain(.28), sound("hh*16").gain(.1))],
  [4, stack(sound("[~ oh]*4").gain(.28), sound("hh*16").gain(.12))],
  [8, stack(sound("[~ oh]*4").gain(.3), sound("hh*16").gain(.12))],
  [8, silence], // breakdown: air
  [4, silence], // the riser owns this
  [8, stack(sound("[~ oh]*4").gain(.3), sound("hh*16").gain(.12))],
  [8, stack(sound("[~ oh]*4").gain(.3), sound("hh*16").gain(.14))],
  [8, sound("[~ oh]*4").gain(.2)],
)

// ── clap backbeat — only where the track is at its fullest ──
const clap = arrange(
  [20, silence],
  [8, sound("~ cp ~ cp").gain(.3).room(.2)],
  [12, silence],
  [8, sound("~ cp ~ cp").gain(.32).room(.2)],
  [8, sound("~ cp ~ cp").gain(.3).room(.2)],
  [8, silence], // outro: drums bare
)

// ── the builds — roll, noise riser, and a scale climb that doesn't resolve ──
const riser = arrange(
  [16, silence],
  [4, stack(
    sound("<sd*4 sd*8 sd*16 sd*16>").gain("<.2 .3 .45 .6>"),
    sound("hh*8").speed("<1 1.5 2 4>").gain("<.1 .18 .26 .36>"),
    n("<0 1 2 3>").scale("a5:minor").s("sawtooth").gain("<.06 .1 .16 .22>").acidenv(slider(.7)),
  )],
  [16, silence],
  [4, stack( // bigger the second time — the anthem is closer
    sound("<sd*8 sd*16 sd*16 sd*16>").gain("<.3 .45 .55 .7>"),
    sound("hh*8").speed("<1 2 3 4>").gain("<.15 .22 .3 .4>"),
    n("<0 2 4 6>").scale("a5:minor").s("sawtooth").gain("<.08 .14 .2 .28>").acidenv(slider(.7)),
  )],
  [24, silence],
)

$: kick
$: bass
$: riff._pianoroll()
$: stabs
$: pad
$: melody._pianoroll()
$: hats
$: clap
$: riser
```
