Soul's equivalent moment is **the lift** — the gospel move where the tambourine doubles, the choir enters, the drummer opens up, and the singer goes to church. Jazz has the cadenza, pop has the bridge; soul has the modulation: the verse is restraint, delivered almost conversationally, and the lift is the release, when the same song is suddenly sung from the ceiling. If a soul record doesn't make you want to stand up somewhere in the last third, it hasn't done its job.

## What the lift actually is

The lift is arrangement, not composition: the chords may only move up a step, but the texture climbs — tambourine doubles from 8ths to a shimmer, full choir pads replace a single held ooh, horn stabs land on the strong beats, the drums go from a side-stick murmur to open backbeats and tom fills, and the melody moves up and starts running. It's gospel's inheritance: the verse is the sermon's setup, the lift is when the congregation joins. Crucially, it's earned by contrast — the quieter and more controlled the verses, the more the lift devastates.

## The layers

- **Piano** — the gospel instrument here: `piano` playing rolling 8th arpeggios of the changes (`.room(.35)`), switching to chord stabs on the two strong beats for bridges. Sustain pedaled via `.release(.4)`.
- **Bass** — `gm_acoustic_bass`, round and upright-flavored: roots held across the bar with an 8th-note pickup walk into the next chord. It never rushes; it's the floor the lift stands on.
- **Drums** — in 6/8: kick on beat 1, snare on the second dotted-quarter (`bd ~ ~ ~ ~ ~` + `~ ~ ~ sd ~ ~`), ghost snare on the last 8th at gain `.15`. In the lift, add tom fills (`ht mt lt` runs) and the ride.
- **Tambourine** — `tb` on all the 8ths with accents on the two pulse beats, doubling to 12ths (`tb*12`) in the lift. This is the single most identifiable soul sound after the voice.
- **Choir** — `gm_voice_oohs` on long chords (`.attack(.4).release(1.1).room(.6).jux(rev)`), answering the lead and blooming in the lift.
- **Lead** — `gm_tenor_sax` as the singer's shadow: restrained, melodic, phrased across the bar line, saving the runs (4-note 16th flourishes) for the lift and vamp.
- **Horns** — `gm_trumpet` stabs on the two pulse beats (`struct("x ~ ~ x ~ ~")`) with an octave-down double, entering only in the lift.

## Harmony

Diatonic warmth with one borrowed tear-jerker. Key of C:

- **Imaj7–vi–IV–V** — Cmaj7 | Am7 | Fmaj7 | G7: the spine; every soul ballad is a decoration of this loop.
- **Gospel ii–V–I** — Dm7 | G7 | Cmaj7: the cadential move that ends phrases; extend the G7 to a beat of G7sus before resolving for the sigh.
- **Borrowed iv** — Fm6 (F–A♭–C–D) into Cmaj7: the single most tear-producing chord in the genre; use it once, at the end of a bridge.
- **Bridge: vi–IV–ii–V** — Am7 | Fmaj7 | Dm7 | G7: the quiet interlude that sets up the lift.
- **The lift: everything up a whole step** — `.transpose(2)` on the C-major changes (Dmaj7 | Bm7 | Gmaj7 | A7), then a vamp of Dmaj7 | Gm6 (borrowed iv in the new key) | Dmaj7 | A7.

## Rhythm & feel

- Two worlds: 6/8 ballads at dotted-quarter ≈ 60–72, and mid-tempo 4/4 at 76–96.
- **The 6/8 trick in Strudel**: `setcpm(66 / 2)` makes one cycle exactly one bar of 6/8, so every pattern is six 8th-note slots; kick on slot 1, snare on slot 4, tambourine on all six.
- The lilt: melodies place a long note (3 slots, `@3`) then two short ones — `[e5@3 ~ g5 ~ ~ ~]` — that's the entire 6/8 soul phrasing vocabulary.
- Mid-tempo 4/4 skeleton: `bd ~ ~ ~ sd ~ ~ ~ bd ~ bd ~ sd ~ sd sd` with `tb*8` on top — backbeat soul, tambourine straight.
- No swing; the 6/8 meter is already the sway. Straight 8ths, weight on the two pulse beats.

## Structure

```
intro 2 | verse 8 | verse 8 (+choir) | bridge 4 | lift 8 (+2 transpose) | vamp 6 | out 2
   1         3          4                2          7                     8        3   (energy 0-10)
```

Intro: piano arpeggio alone. Verse: bass and murmuring drums under a restrained lead. Second verse adds choir and tambourine. The bridge strips back down — quietest point of the record. Then the lift: key up a whole step, horns, doubled tambourine, tom fills every four bars. The vamp rides the Dmaj7–Gm6 turn while the lead finally runs; the outro is one held chord.

## Techniques that actually create "soul"

- **The lift** — add layers and energy in the last third rather than changing the song; the verse's restraint is the setup, and the contrast is the payoff.
- **The whole-step modulation** — `.transpose(2)` on every melodic and harmonic layer at the lift; cheap in code, priceless in the chest.
- **Borrowed iv (Fm6)** — one appearance at a bridge's end buys you the room's eyes; spelled `[f3,ab3,c4,d4]`.
- **Tambourine doubling** — `tb*6` to `tb*12` is the audible gear-change of the lift.
- **Choir answers** — `gm_voice_oohs` pads under the lead's phrase-ends, wide with `.jux(rev)`, never doubling the melody rhythm.
- **The 6/8 lilt** — long-short-short phrasing (`@3` holds, two 8ths) keeps melodies swaying instead of marching.
- **Melisma runs** — 4-note 16th flourishes (`[[b4 a4] [fs4 e4]]` within a slot) reserved for the vamp; scarcity is what makes them testify.
- **Tom fills at the seams** — `ht mt lt` descending runs every fourth bar of the lift; gospel punctuation, not rock bombast.

## Practice approach

- Write the verse melody first and deliberately under-write it — save the top of the range and every run for after the lift.
- Loop the Imaj7–vi–IV–V changes and practice the Fm6 insert in all its positions (before I, before vi) until you feel which one cries.
- Sing the tambourine part while listening to any Atlantic-era record; the accents tell you where the band's weight is.
- Write one 4-bar drum fill plan for the lift — nothing before bar 4, ghost at 8, toms at every 4th bar — and resist deviating.
- Transcribe one 6/8 soul ballad's bass line; count how many notes per bar (it's fewer than you think).

## Example

```
// ═══ stand up — 6/8 soul ballad, dotted quarter = 66 ═══
// form: intro 2 | verse 8 | verse 8 +choir | bridge 4 | lift 8 +2 | vamp 6 | out 2
// energy: 1 3 4 2 7 8 3 — the bridge is the hush that makes the lift devastate
setcpm(66 / 2) // one cycle = one bar of 6/8 (six 8th slots, two dotted-quarter pulses)

// ── piano — rolling 8th arps of the changes; C: C | Am | Dm | G7 ──
const arp = note("<[c4 e4 g4 c5 g4 e4] [a3 c4 e4 a4 g4 e4] [d4 f4 a4 d5 c5 a4] [d4 g4 b4 d5 c5 b4]>")
const arpVamp = note("<[d4 fs4 a4 db5 a4 fs4] [g3 bb3 d4 e4 d4 bb3] [d4 fs4 a4 db5 a4 fs4] [a3 c4 e4 g4 e4 c4]>") // Dmaj7 Gm6 Dmaj7 A7
const bridgeKeys = chord("<Am7 F^7 Dm7 G7>").anchor("c4").voicing().struct("x ~ ~ x ~ ~")
const piano = arrange(
  [2, arp.gain(.3)],
  [8, arp.gain(.35)],
  [8, arp.gain(.35)],
  [4, bridgeKeys.gain(.3)], // bridge: arps become stabs — the texture holds its breath
  [8, arp.transpose(2).gain(.4)], // the lift: same arps, up a whole step
  [6, arpVamp.gain(.42)],
  [2, chord("<D^7>").anchor("d4").voicing().gain(.35)],
).sound("piano").room(.35).release(.4)

// ── bass — upright warmth: roots held, 8th-note walk into the next change ──
const bassLine = note("<[c2@2 ~ g1] [a1@2 ~ e2] [d2@2 ~ a1] [g1@2 ~ d2]>")
const bass = arrange(
  [2, silence], [8, bassLine], [8, bassLine],
  [4, note("<[a1@2 ~ e2] [f1@2 ~ c2] [d2@2 ~ a1] [g1@2 ~ d2]>")],
  [8, bassLine.transpose(2)],
  [6, note("<[d2@2 ~ a1] [g1@2 ~ d2] [d2@2 ~ a1] [a1@2 ~ e2] [d2@2 ~ a1] [a1@2 ~ e2]>")],
  [2, note("d1")],
).sound("gm_acoustic_bass").gain(.8).room(.2)

// ── drums — 6/8: bd 1, sd on the second pulse, ghost on the last 8th; tb doubles at the lift ──
const kitVerse = stack(sound("<[bd ~ ~ ~ ~ ~] [bd ~ ~ ~ ~ ~] [bd ~ ~ ~ ~ ~] [bd ~ ~ ~ ~ bd]>").gain(.7), sound("~ ~ ~ sd ~ ~").gain(.45), sound("~ ~ ~ ~ ~ sd").gain(.15), sound("sh*6").gain(.07))
const kitVerse2 = stack(kitVerse, sound("tb*6").gain("[.5 .2 .3 .42 .32 .3]"))
const kitLift = stack(sound("<[bd ~ ~ ~ ~ bd] [bd ~ ~ ~ ~ bd]>").gain(.75), sound("~ ~ ~ sd ~ sd").gain(.5), sound("tb*12").gain(.2), sound("rd*6").gain(.2))
const fill = stack(sound("[bd ~ ~ ~ ~ ~] [bd ~ ~ sd ~ [ht mt lt]]").gain(.75), sound("tb*12").gain(.2))
const drums = arrange(
  [2, sound("bd ~ ~ ~ ~ ~").gain(.5)],
  [8, kitVerse],
  [8, kitVerse2], // tambourine arrives: the first gear-change
  [4, stack(sound("<[bd ~ ~ ~ ~ ~] [~ ~ ~ ~ ~ ~]>").gain(.5), sound("~ ~ ~ rim ~ ~").gain(.3))], // the hush
  [8, cat(kitLift, kitLift, kitLift, fill, kitLift, kitLift, kitLift, fill)],
  [6, kitLift],
  [2, sound("~ ~ ~ sd ~ ~").gain(.3)],
)

// ── lead — tenor as the singer: restrained verses, running after the lift ──
const leadVerse = note("<[e5@3 ~ g5 ~ ~ ~] [g5@2 ~ e5 d5 ~ ~] [c5@3 ~ d5 ~ c5 ~] [d5 ~ ~ ~ ~ ~] [e5@3 ~ g5 a5 ~ ~] [g5@2 ~ e5 d5 ~ ~] [c5@3 ~ b4 ~ d5 ~] [c5 ~ ~ ~ ~ ~]>")
const leadLift = note("<[fs5@3 ~ a5 ~ ~ ~] [a5@2 ~ fs5 e5 ~ ~] [d5@3 ~ e5 ~ d5 ~] [e5 ~ ~ ~ ~ ~] [fs5@3 ~ a5 b5 ~ ~] [a5@2 ~ fs5 e5 ~ ~] [d5@3 ~ db5 ~ d5 ~] [d5 ~ ~ ~ ~ ~]>")
const leadVamp = note("<[[b4 a4] [fs4 e4] d5@3 ~ ~ ~] [[d5 e5] [fs5 a5] b5@2 ~ ~ ~] [b5@3 ~ a5 fs5 ~ ~] [[a5 fs5] [e5 d5] fs5 ~ ~ ~] [g5@3 ~ fs5 e5 ~ ~] [[fs5 e5] [d5 db5] d5 ~ ~ ~]>")
const lead = arrange(
  [2, silence], [8, leadVerse.gain(.4)], [8, leadVerse.gain(.44)],
  [4, note("<[c5@3 ~ a4 ~ g4 ~] [a4@3 ~ g4 ~ f4 ~] [f4@3 ~ g4 a4 ~ ~] [b4@3 ~ ~ ~ ~ ~]>").gain(.38)],
  [8, leadLift.gain(.5)], // a whole step up and suddenly it testifies
  [6, leadVamp.gain(.52)], // sing, run, climb, resolve
  [2, note("d5").release(1).gain(.4)],
).sound("gm_tenor_sax").room(.4)

// ── choir — oohs answering under verse two, blooming in the lift ──
const choir = arrange(
  [18, silence],
  [8, chord("<C^7 Am7 Dm7 G7>").anchor("g4").voicing().gain(.14)],
  [4, silence],
  [8, chord("<C^7 Am7 F^7 G7>").anchor("g4").voicing().transpose(2).gain(.2)],
  [6, chord("<D^7 Gm6 D^7 A7>").anchor("g4").voicing().gain(.22)],
).sound("gm_voice_oohs").attack(.4).release(1.1).room(.6).jux(rev)

// ── horns — trumpet stabs on the two pulses, tenor shadow an octave down ──
const horns = chord("<C F G C>").anchor("c5").voicing().struct("x ~ ~ x ~ ~").sound("gm_trumpet").room(.3).superimpose(x => x.transpose(-12).gain(.5))
const section = arrange([22, silence], [8, horns.transpose(2).gain(.35)], [6, horns.gain(.38)])

$: piano
$: bass
$: drums
$: lead
$: choir
$: section
```
