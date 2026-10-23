Minimal's equivalent moment is **the drift** — two copies of one short cell, perfectly in unison, until one slips ahead by a single note and the fabric turns into canon. As the copies drift apart the ear starts hearing melodies nobody is playing — ghost lines woven from the collisions, Reich's *resulting patterns* — and when the parts relock, the same twelve notes sound like a different piece. Not minimal techno: this is the classical process school — Steve Reich, Philip Glass, Terry Riley, La Monte Young — where one audible rule, followed without mercy, replaces composition.

## What the drift actually is

Process music: the rule is the piece. Reich phases (two tape loops, then two pianos, drifting out of and back into unison — "It's Gonna Rain", "Piano Phase", "Clapping Music"); Glass adds (a cell grows one note at a time until a plain figure sounds elaborate — "Music in Similar Motion", "1+1", the "Einstein" arpeggios); Riley sequences ("In C": 53 cells over a C pedal, each player deciding when to move on); Young sustains (drones measured in minutes). The listener must be able to infer the rule after two steps — determinism is the point. Nothing new is composed after the first cycle; everything after it is the same material *heard differently*, which is why the music can run twenty minutes without a new idea. This is the exact opposite of ambient's hiding strategy: ambient conceals its repetition (coprime periods, perlin drift), minimalism displays it.

## The layers

- **Pulse river** — `piano` (or `pluck` for mallet weight) in dead-even 8ths, chord tones only, low gain: the floor that never stops and never accents. If it swells, groove, or breathes, it's downtempo, not minimal.
- **The cell pair** — the genre's core: two identical `piano` lines, one static, one processing — rotating a step per cycle, slipping by a pulse, or growing a note per phrase.
- **The interloper** — a `{...}%n` cell of coprime length on `gm_clarinet` (Reich's counterpoint voice), crossing the floor and realigning only every few cycles.
- **The grower** — the Glass voice: one line whose cell adds a note per phrase (`"<a5 [a5 e6] [a5 e6 g6]>"`) — density composes itself.
- **Drone** — `sine` on the root (or root + fifth), sustained: gravity, not a bassline. Felt, not heard.
- **The swell (optional)** — `gm_clarinet` or `gm_synth_strings_1` taking a resulting melody at the process peak, one long crescendo, then gone.

## Sample kit

- **The mallet upgrade** — minimalism's signature voices are preloaded VCSL multisamples: `marimba` (Music for 18 Instruments), `vibraphone` (+`_soft`), `glockenspiel` — swap the `piano` pulse river for one of these and the genre snaps into focus. `note()` is sample-accurate on all of them.
- **Counterpoint voice** — `gm_clarinet` ✓ (the Reich choice); `sax`/`saxello` (VCSL) for the jazzier Downtown variant, `recorder_alto_sus` for the early-music dialect.
- **Pulse floor** — `piano`/`pluck` in dead-even 8ths as written; `fmpiano` (felted) when the piece should whisper.
- **Drone & swell** — `sine` drone; `gm_synth_strings_1` swell, or VCSL `pipeorgan_quiet` for the sacred-minimal drift.
- No pack needed — the preloaded tiers cover minimalism better than any other genre. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Almost no harmony — a chosen pitch set held for the whole piece; "harmony" is where the cell happens to be standing. The example's set is the A-minor pentatonic subset A C D E G over an A aeolian gravity:

- **The drone** — A, or A–E (`[a2,e3]` on sine): the La Monte Young / "In C" discipline; one note is the whole harmony and every cell roams above it.
- **The neighbor shift: i ↔ ♭VII** — A ↔ G. Minimalism's chord change: same rhythm, same shape, new root. Re-voice, never progress.
- **The arrival: ♭VI** — the F dyad `[f3,c4]`, once per piece, held long: the Glassian wide-open moment (the gear-shift of "Glassworks" moves).
- **Modal, never functional** — no V, no leading tone, no cadence. If a dominant resolution appears, you've drifted into film score.

## Rhythm & feel

- No kit, no backbeat, no swing, no humanization — machine evenness is the expressive choice (the precise opposite of lo-fi's drag).
- Pulse quarter-note feel 120–160. Make the cell the cycle: a 12-pulse cell at ♩=126 → 252 eighth-pulses/min ÷ 12 = `setcpm(21)`.
- Interlock: cells of coprime lengths (`%5`, `%7`) crossing the floor; alignment returns at the lcm, and the return is a section change for free.
- One change at a time, and only on phrase boundaries (every 4 or 8 cycles). Two simultaneous changes is the genre's only crime.

## Structure

```
unison 8 | drift 12 (one step per cycle) | interlock 8 (+%7 clarinet, grower) | swell 8 (resulting melody, crescendo) | reunison 8 | coda 4
```

energy `2 · 3 · 5 · 8 · 4 · 1` — the paradox in numbers: the notes repeat identically while perceived energy climbs, because the listener's inference is the arrangement. At `setcpm(21)` this map is 48 cycles ≈ 2¼ minutes; stretch the sections, never add material.

## Techniques that actually create "minimal"

- **The process is the composition** — pick one rule (rotate, grow, drop, cross, retrograde) and follow it audibly to the end. Determinism: no `perlin`, no `rand`, no `degradeBy` — hidden randomness is ambient's tool; here predictability *is* the tension.
- **Discrete phasing (Clapping Music)** — `cell.iter(12)` rotates the pattern's start one event per cycle; or slip a copy in even steps with `.late("<0 1 2 … 11>/12")`. Continuous phasing ("Piano Phase") is a tempo offset — approximate it by staging `late` values section by section.
- **Resulting patterns** — during the drift, listen for lines neither lane is playing; when one is strong, hand it to the clarinet and let the process keep running underneath. Reich arranges his own hallucinations; so should you.
- **Interlock, don't accompany** — every layer is a pulse-instrument playing one simple cell; the ensemble is the sum. A new layer must fill rests the others leave and must never double an existing attack.
- **Additive growth** — `"<a5 [a5 e6] [a5 e6 g6] [a5 e6 g6 a6]>"`: each element fills its own cycle, so density grows without a single new compositional decision.
- **Re-voice, don't reharmonize** — new octave, new instrument, same pitches: the genre's version of a new chord.
- **The swell** — dynamics stay flat until the process peaks, then one long crescendo: `gain(saw.range(.15,.6).slow(8))`. Climax means louder, not more.
- **Palindrome process** — `palindrome()` runs a pattern forward then backward; or mirror the arrange sections so the piece climbs its own ladder back down.

## Practice approach

- Listen to "Clapping Music" and count the phase steps out loud; losing count and not minding is the listening skill this genre trains.
- Loop a four-note cell 32 times against `.iter(4)`; write down three ghost melodies you hear in the middle; keep one and discard the process that produced it.
- Compose a whole sketch on one pitch set; when bored, change register or instrument — never the notes (Glass's working rule).
- Schedule every change with `.every(8, …)` and allow nothing else; if the sketch bores at bar 8, the cell is weak, not the process.

## Example

```
// ═══ rivers in unison — minimal, pulse ♩=126, A aeolian ═══
// form: unison 8 | drift 12 | interlock 8 | swell 8 | reunison 8 | coda 4  (48 cycles ≈ 2¼ min)
// one audible process: the second piano rotates one step per cycle (clapping-music phasing),
// then a %7 clarinet and a growing cell cross it — no new material is ever composed
setcpm(21) // one cycle = the 12-pulse cell; ♩=126 → 252 eighths/min ÷ 12 = 21

// ── the cell: 12 pulses of A minor pentatonic — the entire piece's material ──
const cell = note("a4 c5 d5 e5 g5 e5 d5 c5 a4 c5 d5 e5").s("piano").gain(.3)

// ── pulse river — chord-tone quarters, no accents, never stops ──
$: note("a3 ~ e3 ~ a3 ~ e3 ~ a3 ~ e3 ~").s("piano").gain(.14).lpf(1400)

// ── drone — root and fifth, felt not heard ──
$: note("[a2,e3]").s("sine").sustain(.9).release(.3).gain(.1)

// ── static copy ──
$: cell.gain(.22)

// ── the process copy — rotates its start one event per cycle: the drift ──
$: arrange(
  [8, cell.gain(.22)],                                      // unison: two copies, one rhythm
  [12, cell.iter(12).gain(.24)],                            // drift: clapping-music steps, one per cycle
  [8, cell.iter(12).gain(.2)],                              // interlock: tucks under the newcomers
  [8, cell.iter(12).superimpose(x => x.transpose(12)).gain(.14)], // swell: octave double, behind the clarinet
  [8, cell.gain(.22)],                                      // relock: the same notes, somehow new
  [4, silence],
)

// ── the interloper — a 3-note cell every 7 pulses: crosses the 12, realigns every 7 cycles ──
$: arrange(
  [20, silence],
  [8, note("{e6 g6 d6}%7").s("gm_clarinet").gain(.13).room(.25)],
  [8, note("{e6 g6 d6}%7").s("gm_clarinet").gain(.1).room(.25)],
  [12, silence],
)

// ── the grower — the Glass voice: one added note per cycle, then the same growth an octave up ──
$: arrange(
  [20, silence],
  [8, note("<a5 [a5 e6] [a5 e6 g6] [a5 e6 g6 a6]>").s("piano").gain(.18)],
  [8, note("<a5 [a5 e6] [a5 e6 g6] [a5 e6 g6 a6]>").transpose(12).s("piano").gain(.12)],
  [12, silence],
)

// ── the swell — a resulting melody neither lane plays, one crescendo, then gone ──
$: arrange(
  [28, silence],
  [8, note("e6 ~ ~ g6 ~ ~ a6 ~ ~ ~ g6 e6 ~").s("gm_clarinet")
    .gain(saw.range(.08, .4).slow(8)).room(.35)],
  [12, silence],
)

// ── coda — the river and drone remain; the cell's first note, held ──
$: arrange(
  [44, silence],
  [4, note("a4 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~").s("piano").gain(.2).release(.5)],
)
```
