Classical's equivalent moment is **the recapitulation** — the return of the opening theme in the home key after the development has spent bars fragmenting it, modulating it and generally taking it apart. It's electro's drop wearing a wig: long departure, systematic destabilization, and then a return that lands as relief precisely because of how far from home the music traveled. Composers fought over how obvious to make it; audiences never once complained.

## What the recapitulation actually is

Sonata form is the genre's big engine. The **exposition** states theme 1 in the tonic, transitions, and states theme 2 in the dominant (or the relative major) — the second theme is the departure, and it's usually softer and more lyrical where theme 1 is square and rhythmic. The **development** takes fragments of the themes, sequences them through unrelated keys, thickens and destabilizes, and typically drives onto a dominant pedal point — bass holding the 5th degree while everything above churns — which is the held breath before the return. The **recapitulation** brings theme 1 back in the tonic and then, crucially, brings theme 2 back **also in the tonic** (not the dominant): the two themes reconcile, the music that left comes home. A coda hammers the point. Against this stand the form alternatives: **through-composed** (no reprise at all, music follows the text or program continuously — the recapitulation's emotional work must then be done by returning motives instead of sections), **ternary ABA** (one contrast, one return — sonata form with the middle third cut), **theme and variations** (the return happens transformed every time), and **rondo** (the refrain keeps interrupting the episodes — pop's chorus, in periwigs).

## The layers

The orchestra maps to GM names cleanly, by function: **strings are the body** — `gm_string_ensemble_1` for massed sustain (pads at low gain, `attack` and `release` long), solo lines on `gm_violin`, inner counterpoint on `gm_viola`, and the bass line on `gm_cello` (add `gm_contrabass` doubling an octave down, or `superimpose(x => x.transpose(-12))`, for weight in tuttis). **Winds answer and double** — `gm_flute` (lyrical seconds themes), `gm_oboe` and `gm_clarinet` (mid-color doublings), `gm_bassoon` (bass support and staccato wit). **Brass is structural punctuation** — `gm_french_horn` for sustained harmony that isn't pointing at itself, `gm_trumpet` and `gm_trombone` reserved for climaxes and codas (use sparingly; a trumpet that plays in the exposition has nowhere to go). **Timpani** — `gm_timpani` exists and is good; the lo-fi fallback is `rd` with long release as a roll and a low `bd` as a single tuned hit, but prefer the real patch with `note()` spelling the tuning (c2, g2). **Keyboards by era** — `gm_harpsichord` for baroque continuo and classical-period Alberti accompaniments, `gm_piano` for romantic chamber textures. **Color** — `gm_orchestral_harp` for arpeggiated transitions, `gm_pizzicato_strings` for scherzo lightness, `gm_choir_aahs` for the sacred pad. The scoring rule that matters: **orchestration is structure** — the same theme restated by a different section counts as a formal event; plan who plays what per section before writing a single note of counterpoint.

## Harmony

Functional harmony with goal-directed voice leading: chords are labeled by what they do, not what they are. The cadence vocabulary: **ii–V–I** (in C: Dm–G–C) is the engine; **ii6–V7–I** (Dm first inversion, G7, C) is its polished form — bass d–g–c, clean and final. Canonical progressions, roman and spelled in C major:

- **Authentic cadence** — ii6–V7–I → [d,f,a]–[g,b,d,f]–[c,e,g]: the sentence's full stop
- **Circle-of-fifths sequence** — I–vi–ii–V–I → C Am Dm G C, or extended Am–Dm–G–C–F–Bdim–Em–Am: development-section travel, each chord the V of the next
- **Deceptive cadence** — V–vi → G7 to Am: the promised resolution ducked, ideal at the end of a middle section or before a recapitulation delay
- **Secondary dominant** — V/V–V–I → D7–G–C: temporarily tonicizing the dominant; the standard way to wrench into a development key

Two voice-leading habits carry more style than any chord choice: **suspensions** (a voice holds its note into the new chord as a 4th against the bass, then resolves down by step, 4–3 — the single most "classical-sounding" two events available) and **contrary motion between outer voices** (when the melody goes up, the bass goes down, and vice versa; parallel motion in the outer voices is the thing the style systematically avoids).

## Rhythm & feel

There is no kit; rhythm is made of **meter, bass motion and phrase**. The meter is clean and constant — the genre's beats are auditions for the downbeat. Accompaniment figures carry the pulse: the **Alberti bass** (`[c3 g3 e3 g3]`, broken chord bottom-top-middle-top) is the classical-era engine, ostinato repeats and walking quarter basses do the same work elsewhere. Phrases come in **antecedent–consequent pairs**: four bars that end on a half cadence (weak, question), four more that end authentic (strong, answer) — 8-bar periods are the default unit, and phrase endings should be audible in the arrangement even when nothing else changes. Tempo terms are bpm ranges: largo ≈ 45–50, adagio ≈ 55–70, andante ≈ 75–105 ("walking"), moderato ≈ 105–115, allegro ≈ 120–140, vivace ≈ 145–160, presto ≈ 165+. Map with `setcpm(bpm/4)` for 4/4 (one cycle = one bar), `setcpm(bpm/3)` for 3/4, and `setcpm(bpm/2)` for 6/8 where the cycle is two dotted-quarter beats. Rubato exists but in code it's better implied (staggered entries, `release` bleeding over bar lines) than executed.

## Structure

Sonata movement with bar counts: exposition T1 8 | T2 8 (both repeated in performance — just play them twice or accept the single pass) | development 8–16 (fragment, sequence, modulate, dominant pedal) | recapitulation T1 8 + T2-in-tonic 8 | coda 4–8. Energy graph: exposition steady-bright | development climbs with rising sequences and thickening orchestration | pedal point = the held breath | recapitulation is the loudest arrival | coda hammers and stops. Through-composed alternative: no reprise — keep one motive returning at structural points to do the recapitulation's emotional work. Ternary: A 8 | B 8 | A' 8, where A' re-orchestrates rather than repeats. The planning move that pays: write the energy graph **first**, assign sections to it, and only then fill notes.

## Techniques that actually create "classical"

- **Two-voice counterpoint** — two independent `note()` lanes (violin and viola, flute and oboe) that each make melodic sense alone. The cheap version that still works: contrary motion between the lanes, plus imitation — one lane states a figure, the other restates it a bar or two later at a different pitch.
- **Sequence** — a motive repeated at successively higher or lower pitch levels (`transpose(2)` per cycle or literal rewriting). The development section's main propulsion; three steps up is a rise, four starts to feel like panic, which is sometimes the point.
- **Fragmentation** — as tension rises, the motive gets shorter: theme `.fast(2)` cuts the unit in half. Drive the last bars of a development with fragments, not new material.
- **Suspensions 4–3** — hold the previous chord's note into the new chord, resolve down by step. Do it in an inner voice; it reads as instantly stylistic.
- **Dominant pedal before the return** — bass holds the 5th degree (`note("g2")` sustained) for two to four bars while upper voices move over it. The oldest tension device in the book and the correct setup for a recapitulation.
- **Dynamics as structure** — gain is a compositional dimension: terraced steps between sections (`gain(.3)` verse vs `.7` recap), bar-by-bar crescendo inside a development (`gain("<.4 .45 .5 .6>")` — one value per bar/cycle), the recapitulation simply **louder than the exposition ever was**. A classical arrangement that is dynamically flat is wrong no matter how good the notes are.
- **Orchestration as variation** — restate the recapitulation's theme 1 with winds doubling strings, harp arpeggios added, timpani reinforcing downbeats: same notes, bigger frame. This is what "return" sounds like when it means it.
- **Clean cadences** — end phrases with ii6–V7–I in the bass, root in both outer voices, and a beat of silence after. The silence is part of the cadence.

## Practice approach

- Take one Mozart or early Beethoven first movement and mark, with a pencil: T1 start, transition, T2 start, development start, pedal point, recapitulation. Do this before writing anything.
- Write 8 bars of two-voice counterpoint with strict contrary motion and one imitation; if either lane stops making sense alone, fix the other one.
- Sketch a full movement as an energy graph plus orchestration assignments (who plays, how loud, per section) with zero notes, then compose into the grid.
- Compose the exposition, then compose the recapitulation by re-orchestrating it — the notes should be nearly identical and the effect noticeably bigger.
- End every 8-bar period with an actual cadence in the bass for one full exercise; resist eliding.

## Example

```
// ═══ sonatina in c, i. allegro — 120 bpm ═══
// sonata form: exposition T1 8 | T2 8 | development 8 | recap T1 8 + T2-in-C 8 | coda 4
// energy: T1 steady | T2 softer | dev: fragments rising, crescendo, dominant pedal | recap: the drop | coda: hammer and stop
setcpm(120 / 4) // one cycle = one bar of 4/4

// theme 1: square, rhythmic; antecedent ends half-cadence (bar 4), consequent closes home (bar 8)
const t1 = "<[c5 e5 g5 e5] [f5 e5 d5 e5] [f5 e5 d5 c5] [b4 c5 d5 ~] [c5 e5 g5 e5] [f5 e5 d5 e5] [e5 f5 e5 d5] [c5 ~ ~ ~]>"
// theme 2 in G (the departure), then the same theme recapitulated in C (the reconciliation)
const t2 = "<[[b4 d5] g5 ~ ~] [[c5 e5] g5 ~ ~] [[b4 d5] g5 b5 ~] [a5 fs5 d5 ~] [[b4 d5] g5 ~ ~] [[c5 e5] a5 ~ ~] [[d5 fs5] a5 ~ ~] [g5 ~ ~ ~]>"
const t2c = "<[[g4 c5] e5 ~ ~] [[f4 a4] c5 ~ ~] [[g4 c5] e5 g5 ~] [e5 c5 g4 ~] [[g4 c5] e5 ~ ~] [[f4 a4] d5 ~ ~] [[d5 g5] b5 ~ ~] [c5 ~ ~ ~]>"
// development: t1 fragments, sequenced and rising onto the dominant pedal
const dev = "<[[c5 e5] a5 g5] [[f5 a5] g5 f5] [[d5 g5] a5 b5] [fs5 g5 a5 b5] [d5 d5 e5 e5] [f5 f5 e5 e5] [d5 c5 d5 e5] [d5 ~ ~ ~]>"
// violin: states t1, rests for t2, climbs the dev crescendo, leads the recap tutti
const violin = arrange(
  [8, note(t1).gain(.5)], [8, silence], // t2 is the flute's; contrast by absence
  [8, note(dev).gain("<.4 .45 .5 .55 .6 .65 .7 .75>")], // bar-by-bar crescendo — dynamics as structure
  [8, note(t1).gain(.68)], // the return, bigger than bar 1 ever was
  [8, note(t2c).transpose(12).gain(.24)], // doubling the flute 8va: tutti
  [4, note("<[~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [c5 ~ ~ ~]>").gain(.6)],
).sound("gm_violin").room(.4)
// viola: the counterpoint lane — independent line, mostly contrary motion to the violin
const violaT1 = "<[e4 c4 b3 c4] [a3 b3 c4 b3] [c4 b3 a3 g3] [d4 b3 g3 b3] [e4 c4 b3 c4] [a3 b3 c4 d4] [b3 a3 g3 fs3] [e4 ~ c4 ~]>"
const violaDev = "<[a3 ~ ~ ~] [c4 ~ ~ ~] [b3 ~ a3 ~] [b3 ~ d4 ~] [a3 a3 gs3 gs3] [a3 a3 g3 g3] [b3 c4 b3 a3] [b3 ~ ~ ~]>"
const viola = arrange(
  [8, note(violaT1).gain(.3)], [8, silence],
  [8, note(violaDev).gain("<.25 .28 .3 .32 .36 .4 .44 .48>")],
  [8, note(violaT1).gain(.4)], [8, silence],
  [4, note("<[~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [e4 ~ c4 ~]>").gain(.4)],
).sound("gm_viola").room(.4)
// flute: owns theme 2, restates it in C in the recap, takes the final high note
const flute = arrange(
  [8, silence], [8, note(t2).gain(.45)], [8, silence], [8, silence],
  [8, note(t2c).gain(.5)], [4, note("<[~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [c6 ~ ~ ~]>").gain(.5)],
).sound("gm_flute").room(.45)
// harpsichord: Alberti bass under theme 1 — the classical-era engine (the recap reuses it)
const alberti = "<[c4 g4 e4 g4] [f3 c4 a3 c4] [c4 g4 e4 g4] [g3 d4 b3 d4] [c4 g4 e4 g4] [f3 c4 a3 c4] [g3 d4 b3 d4] [c4 g4 e4 g4]>"
const harpsichord = arrange(
  [8, note(alberti).gain(.22)], [8, silence], [8, silence], // t2 gets strings only: lighter frame
  [8, note(alberti).gain(.3)], [8, silence], [4, silence],
).sound("gm_harpsichord")

// cello: the functional bass — quarter walks, cadences at phrase ends, dominant pedal in the dev
const bassT1 = "<[c3 g2 e2 g2] [f2 c3 a2 c3] [e2 g2 c3 e3] [d3 b2 g2 b2] [c3 g2 e2 g2] [f2 c3 a2 c3] [g2 d3 b2 d3] [c3 g2 c3 ~]>"
const bassT2 = "<[g2 d3 b2 d3] [c3 g2 e2 g2] [g2 d3 b2 d3] [d3 a2 fs2 a2] [g2 d3 b2 d3] [c3 g2 e2 g2] [d3 a2 fs2 a2] [g2 d3 g2 ~]>"
const bassDev = "<[a2 e3 c3 e3] [f2 c3 a2 c3] [g2 d3 b2 d3] [d3 b2 g2 b2] [g2 g2 g2 g2] [g2 g2 g2 g2] [g2 g2 g2 g2] [g2 b2 d3 g2]>" // bars 5-8: the pedal
const bassT2C = "<[c3 g2 e2 g2] [f2 c3 a2 c3] [c3 g2 e2 g2] [d3 b2 g2 b2] [c3 g2 e2 g2] [f2 c3 a2 c3] [g2 d3 b2 d3] [c3 g2 c3 c2]>"
const cello = arrange(
  [8, note(bassT1).gain(.5)], [8, note(bassT2).gain(.4)],
  [8, note(bassDev).gain("<.45 .48 .5 .52 .55 .58 .6 .62>")],
  [8, note(bassT1).gain(.62)], [8, note(bassT2C).gain(.62)],
  [4, note("<[c3 g2 c3 g2] [c3 b2 c3 g2] [g2 g2 g2 g2] [c2 ~ ~ ~]>").gain(.7)],
).sound("gm_cello").room(.35)
// string ensemble pads — the frame that thickens toward the return
const pad = changes => chord(changes).anchor("c4").voicing().attack(.3).release(1.5).gain(.14).sound("gm_string_ensemble_1").room(.5)
const strings = arrange(
  [8, silence], [8, pad("<G C G D G C D G>")], [8, pad("<Am F G G G G G G>")],
  [8, pad("<C F C G C F G C>").gain(.2)], [8, pad("<C F C G C F G C>").gain(.2)],
  [4, pad("<C C C C>").gain(.24)],
)
// horn enters only at the dev pedal; timpani marks the recap downbeat and takes the coda roll
const horn = arrange(
  [8, silence], [8, silence],
  [8, note("<[~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [g2] [g2] [g2] [g2]>")],
  [8, silence], [8, silence], [4, silence],
).sound("gm_french_horn").attack(.4).release(1.5).gain(.24).room(.5)
const timpani = arrange(
  [8, silence], [8, silence],
  [8, note("<[~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [g2 g2 g2 g2] [g2 g2 g2 g2] [g2 g2 g2 g2] [g2 ~ g2 ~]>").gain("<.15 .18 .22 .26>")],
  [8, note("<[c2 ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~]>").gain(.5)], [8, silence],
  [4, note("<[c2*4] [c2*4] [c2*8] [c2 ~ ~ ~]>").gain(.4)], // roll into the final chord
).sound("gm_timpani").room(.5)
$: violin
$: viola
$: flute
$: harpsichord
$: cello
$: strings
$: horn
$: timpani
```
