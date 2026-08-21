Blues' equivalent moment is **the turnaround** — bars 11 and 12 of the twelve-bar form, the two bars that decide whether the music throws you back to the top for another chorus or finally lets the song end. Everything else in the genre (the shuffle, the blue notes, the AAB lyric) exists to make that door at the end of the form feel inevitable: every chorus walks the same I–IV–V road, and the turnaround is where it either swings open again or closes for good.

## What the turnaround actually is

The last four bars of a 12-bar chorus are V7 – IV7 – I7 – (I7 or V7). Bar 11 lands the tonic; bar 12 is the decision point. If another chorus is coming, bar 12 becomes the V7 chord — often with a little descending lick on top — and its third (the leading tone) physically pulls the ear back to the top of the form. On the final chorus the band refuses the push: bar 12 stays on I, the drummer sets up one accent, and the song ends with the root. That refusal, after eleven and a half bars of harmonic habit, is the ending gesture of the genre. The other half of the mechanic is the **quick change** in bars 1–2 (I7 going to IV7 early, then back), which gives long performances internal variety without ever leaving the form. In practice the turnaround and the shuffle feel are one machine: the triplet grid keeps time horizontal, and the form gives it somewhere to go.

## The layers

- **Delta blues (rural, one player, 60–80 bpm)** — one guitar is the whole band: `gm_acoustic_guitar_nylon` with the thumb playing a monotonic bass on the low string (`note("a2 a2 a2 a2")`, barely moving, often damped and thuddy) while the fingers state riffs up high on the top strings. The voice and the guitar riff trade — the vocal line answers its own accompaniment.
- **Chicago blues (1950s band, 96–116 bpm)** — `gm_piano` comps 7th and 9th voicings with triplet-flavored stabs; `gm_harmonica` takes the lead (small `room`, a touch of `shape` so it sounds cupped and reedy rather than clean); `gm_electric_guitar_clean` (or `gm_overdriven_guitar` for the later south-side sound) plays shuffle figures an octave below the piano; `gm_acoustic_bass` walks four quarters to the bar; and a small kit shuffles — ride or hi-hat in triplets, snare on 2 and 4, kick on 1 (and sometimes 3), never four-on-the-floor.
- **Texas / west-coast jump (110–128 bpm)** — same engine, horns added: `gm_tenor_sax` sections playing riff figures in octaves, piano moved to boogie tenths, bass walking harder. This is where blues tips into early rock and roll.

## Harmony

The default chord quality is the **domant 7th on I, IV and V** — not because it needs to resolve, but because the flat 7 rubs against the major triad and that friction is the sound. The 12-bar form in A, spelled out: `A7 A7 A7 A7 | D7 D7 A7 A7 | E7 D7 A7 E7` — that last E7 is the turnaround. With the quick change: `A7 D7 | A7 A7 | D7 D7 | A7 A7 | E7 D7 | A7 E7`. In strudel that's one pattern: `chord("<A7 A7 A7 A7 D7 D7 A7 A7 E7 D7 A7 E7>")` with one chord per bar. Canonical progressions, roman and spelled:

- **12-bar major blues**: I7–IV7–V7 → A7 D7 A7 E7 (the form itself)
- **Quick change**: I7 IV7 | I7 I7 … → A7 D7 | A7 A7 … (bar 2 goes to IV early)
- **Jazz-blues turnaround**: I7–VI7–II7–V7 → A7 F#7 B7 E7 (dresses up bar 12; chromatic roots)
- **Minor blues**: i7–iv7–V7 → Am7 Dm7 Am7 Am7 | Dm7 Dm7 Am7 Am7 | F7 E7 Am7 Am7 (darker, and the F7–E7 cadence replaces the plain V)

On top of all of it sit the **blue notes**: the b3, b5 and b7 of the key (over A: c natural, eb, g). Melody and vocals live in the minor pentatonic (a c d e g) plus eb as a passing grind, played against clean dominant changes. The c natural grinding against the A7's c# is not a mistake — that collision is the entire expressive core of the genre.

## Rhythm & feel

The engine is the **shuffle triplet**: divide each beat into three, hit on 1 and the third triplet. As mini-notation that's `[x@2 x]` per beat, so a bar of ride is `"[rd@2 rd] [rd@2 rd] [rd@2 rd] [rd@2 rd]"`. Write it literally rather than faking it with `swing()` — the triplet is the feel, not an approximation of it. Tempo ranges by style: delta 60–80 and loose (edges rubato, bar lines approximate), chicago shuffle 96–116, texas jump 110–128, slow blues down at 60 where the whole groove moves into 12/8 and the bar becomes `"[bd ~ ~] [~ sd ~] [bd ~ ~] [~ sd ~]"`. The kick sits on 1 and 3 at most; four-on-the-floor kills a shuffle. Hi-hat chicks on the swing 'a' of each beat (`"[~ ~ hh]"` per beat) are the glue. Skeleton kit: kick `"bd ~ bd ~"`, snare `"~ sd ~ sd"`, ride as above.

## Structure

The unit of form is not the song, it's the **12-bar chorus** — a song is just N choruses in a row. A performance: 4-bar intro vamp (usually the last four bars of the form, or I–IV–I–V) → 4 to 12 lyric choruses → 2 to 4 solo choruses (harp, guitar, piano) → a final chorus with the big ending. The lyric inside each chorus is **AAB**: line sung over bars 1–2, the same line again over bars 3–4 (varied slightly), and the punch line over bars 5–6, with bars 7–8 open for band fills before the third line at bars 9–10 and the turnaround at 11–12. Energy graph: vamp low → verses steady → first solo up → solos trade higher → final chorus peaks → refusal of the turnaround → one accent, out.

## Techniques that actually create "blues"

- **Call and response** — every layer answers another: vocal phrase bars 1–2, guitar or harp fill in the gap before bars 3–4. In code this is literal alternation: phrase pattern, then rests where another lane answers.
- **Blue notes against clean changes** — keep the accompaniment strictly I7/IV7/V7 and let the melody use c natural and eb over A7. The friction between the lanes is the sound; if both sides bend, nothing grinds.
- **AAB lyric form** — repeat the first line. The repetition is structural, not lazy: it sets up the expectation the third line breaks.
- **Monotonic thumb bass** — the delta groove is a near-static low string (`note("a2 a2 a2 a2")` with short decay) under busy treble. The less the bass moves, the more the top moves.
- **9th-chord comping** — chicago piano voices A7 as A9 (rootless even better: c#-e-g-b). Voice it manually as a mini-notation chord `[cs4,e4,g4,b4]` when the chord symbols get too plain.
- **Stop-time** — during a solo chorus, the whole band hits beat 1 only (`struct("x ~ ~ ~")` on comp and bass) and the soloist plays across the holes. One chorus of this after two normal choruses resets the ear.
- **The big ending** — final chorus bar 12: no V7. The band sets up one accent (kick plus snare), lands the tonic on the next downbeat, and stops. Clean, loud, final.

## Practice approach

- Sing the 12-bar form until you never have to count it — the genre lives in people who feel bar 9 coming.
- Transcribe one delta piece (Robert Johnson or Skip James) note for note on guitar, and one Chicago performance (Little Walter with a band) by ear.
- Improvise 20 choruses using only minor pentatonic plus blue notes over the form; resist adding anything else until the blue notes land where you mean them.
- Clap the shuffle `[x@2 x]` at 60, 90 and 120 bpm until the triplet is automatic, then write grooves from the clap.
- Write one complete performance arrangement — vamp, two verses, one solo chorus, final chorus with the refusal ending — before adding variations.

## Example

```
// ═══ blues in a — chicago shuffle, 108 bpm ═══
// form: vamp 4 | head 12 | harp solo 12 | final 12 (refuses the turnaround) | tag 2
// the 12-bar chorus is the song: A7 x4 | D7 x2 | A7 x2 | E7 D7 | A7 E7(bar 12 = the turnaround)
setcpm(108 / 4) // one cycle = one bar of 4/4

// the changes — one chord per bar; bar 12's E7 throws you back to the top of the form
const form = "<A7 A7 A7 A7 D7 D7 A7 A7 E7 D7 A7 E7>"
const vamp = "<A7 D7 A7 E7>"

// walking bass — four quarters a bar: chord tones on strong beats, chromatic steps into the next root
const walkHead = "<[a2 cs3 e3 fs3] [fs3 e3 cs3 a2] [a2 cs3 e3 g3] [a2 cs3 e3 cs3] [d3 fs3 a3 c3] [c3 a2 fs2 d2] [a2 cs3 e3 g3] [a2 e2 gs2 b2] [e2 gs2 b2 d3] [d3 c3 a2 fs2] [a2 cs3 e3 g3] [e2 d3 b2 gs2]>"
// final chorus: same road, but bars 11-12 sit on the root — the refusal
const walkFinal = "<[a2 cs3 e3 fs3] [fs3 e3 cs3 a2] [a2 cs3 e3 g3] [a2 cs3 e3 cs3] [d3 fs3 a3 c3] [c3 a2 fs2 d2] [a2 cs3 e3 g3] [a2 e2 gs2 b2] [e2 gs2 b2 d3] [d3 c3 a2 fs2] [a2 e3 a2 cs3] [a2 ~ ~ ~]>"

// drums — the shuffle triplet: each beat split in 3, hit on 1 and the 3rd triplet: [x@2 x]
const ride = "[rd@2 rd] [rd@2 rd] [rd@2 rd] [rd@2 rd]"
const kit = stack(
  sound(ride).gain(.32).room(.3),                         // the engine
  sound("~ sd ~ sd").gain(.5).room(.3),                   // backbeat 2 & 4
  sound("bd ~ bd ~").gain(.65),                           // kick 1 & 3 — never four-on-the-floor
  sound("[~ ~ hh] [~ ~ hh] [~ ~ hh] [~ ~ hh]").gain(.2),  // hat chick on the 'a' of every beat
)
const ghosts = sound("[~ ~ sd] [~ ~ ~] [~ ~ sd] [~ ~ ~]").gain(.15) // loose answers under the solo

const drums = arrange(
  [4, stack(sound(ride).gain(.22), sound("bd ~ bd ~").gain(.5))], // vamp: time first, band second
  [12, kit],
  [12, stack(kit, ghosts)],
  [12, kit],
  [2, sound("bd sd ~ ~").gain(.7)],                       // the tag: one accent and out
)

const bass = arrange(
  [4, note("<[a2 cs3 e3 g3] [d3 fs3 a3 c3] [a2 e2 cs3 a2] [e2 gs2 b2 d3]>")],
  [12, note(walkHead)],
  [12, note(walkHead)],                                   // bass keeps walking under the solo
  [12, note(walkFinal)],
  [2, note("<[a2 ~ ~ ~] [a1 ~ ~ ~]>")],
).sound("gm_acoustic_bass").gain(.8).room(.15)

// piano — 7ths voiced around cs4: stabs on 2 & 4 in the head, full shuffle 8ths under the solo
const compSparse = "~ [x@2 x] ~ [x@2 x]"
const compFull = "[x@2 x] [x@2 x] [x@2 x] [x@2 x]"
const piano = arrange(
  [4, chord(vamp).anchor("cs4").voicing().struct(compSparse)],
  [12, chord(form).anchor("cs4").voicing().struct(compSparse)],
  [12, chord(form).anchor("cs4").voicing().struct(compFull)],
  [12, chord(form).anchor("cs4").voicing().struct(compSparse)],
  [2, chord("<A7 A7>").anchor("cs4").voicing().struct("<[x ~ ~ ~] [x ~ ~ ~]>")],
).sound("gm_piano").gain(.38).room(.3)

// rhythm guitar — same changes an octave down, quiet: the grease under the piano
const guitar = arrange(
  [4, silence],
  [12, chord(form).anchor("a3").voicing().struct(compFull)],
  [12, chord(form).anchor("a3").voicing().struct(compFull)],
  [12, chord(form).anchor("a3").voicing().struct(compSparse)],
  [2, chord("<A7 A7>").anchor("a3").voicing().struct("<[x ~ ~ ~] [~ ~ ~ ~]>")],
).sound("gm_electric_guitar_clean").gain(.2).room(.25)

// harmonica — aab head in a minor pentatonic (a c d e g): the c natural grinding on the a7's
// c# is the blue note doing its job. solo chorus gets busier; final chorus takes the big ending.
const head = "<[e5@2 g5] e5 ~ d5> <[c5@2 a4] ~ ~ ~> <[e5@2 g5] e5 ~ d5> <a4 ~ ~ ~> <[d5@2 c5] a4 fs4 ~> <a4 ~ ~ ~> <~ ~ ~ ~> <~ ~ ~ ~> <[b4@2 e5] g5 ~ e5> <d5 c5 a4 ~> <[a4@2 cs5] e5 ~ ~> <[b4@2 d5] gs4 ~ ~>"
const solo = "<[[a4 c5] [a4 c5]] e5 ~ d5> <[c5@2 a4] ~ [a4 c5] ~> <[e5@2 d5] c5 a4 ~> <[a4 c5] d5 [e5 d5] ~> <[d5@2 a4] c5 ~ ~> <[fs4 a4] [fs4 a4] d5 ~> <~ ~ [a4 c5] [e5 d5]> <~ ~ ~ ~> <[e5@2 g5] e5 b4 d5> <[b4 gs4] b4 e5 ~> <a4 cs5 e5 a5> <[gs5@2 e5] b4 gs4 ~>"
const finalChorus = "<[e5@2 g5] e5 ~ d5> <[c5@2 a4] ~ ~ ~> <[e5@2 g5] e5 ~ d5> <a4 ~ ~ ~> <[d5@2 c5] a4 fs4 ~> <a4 ~ ~ ~> <~ ~ ~ ~> <~ ~ ~ ~> <[b4@2 e5] g5 ~ e5> <d5 c5 a4 ~> <[cs5@2 e5] a5 ~ ~> <a5 ~ ~ ~>" // bar 12: no turnaround

const harp = arrange(
  [4, silence],                    // the harp waits; the band establishes the shuffle first
  [12, note(head)],
  [12, note(solo).gain(.62)],
  [12, note(finalChorus)],
  [2, note("<[a5 ~ ~ ~] [~ ~ ~ ~]>")],
).sound("gm_harmonica").gain(.55).room(.25).shape(.2)

$: drums
$: bass
$: piano
$: guitar
$: harp
```
