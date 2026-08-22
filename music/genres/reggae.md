Reggae's equivalent moment is **the version** — the dub pass where the vocals and the melody drop out, the mix opens up, and what's left (bass, drums, and the echoing ghosts of everything else) becomes the music. Jazz has the cadenza, pop has the bridge; reggae has the strip-down. The genre's radical idea is that removing material is an event: the one-drop holds the time, the bass carries the melody, and the engineer's delay throws become the lead instrument.

## What the version actually is

A "version" is the instrumental B-side of a reggae single — the same rhythm track with the vocal removed, which dub pioneers (King Tubby, Lee Perry) then mixed live: dropping the skank in and out of echoes, sweeping filters, letting a single chord stab repeat into infinity. Structurally it's the opposite of a build: instead of adding layers toward a climax, you subtract toward a skeleton, and the space itself gets interesting. The bass becomes the singer, the drums become the harmony (that one kick-and-rim drop is a chord change's worth of information), and every element you removed is still audible as a delay trail.

## The layers

- **Drums (one-drop)** — kick and rim together on beat 3 and nothing else: `~ ~ ~ ~ [bd,rim] ~ ~ ~`. No snare backbeat, no 2 and 4. This single decision creates most of the space in the genre. Hats on straight 8ths with a light accent pattern, `sh` for motion.
- **Skank** — the guitar/keys chop on beats 2 and 4: `gm_electric_guitar_muted` playing high `chord()` stabs through `.struct("~ ~ x ~ ~ ~ x ~")`, choked short with `.release(.1).cut(1)`. It's percussion that happens to have a pitch.
- **Bubble** — the organ's offbeat 8th dyads: `note("[e5,a5]*8")` on `gm_drawbar_organ` with gains that accent the ands — the glue between skank and bass, and the first thing an engineer mutes in the dub.
- **Bass** — the actual lead: `sine` with `.adsr(".008:.05:.9:.25")`, playing melodic minor-pentatonic lines around the root (A minor pent: A–C–D–E–G). Sparse, round, syncopated against the drop, and louder in the mix than anything except the kick.
- **Melodica / vocal lead** — `gm_flute` (the Augustus Pablo voice) with `.room(.5)` and a dotted-8th delay; phrases end early and let the echo finish them.
- **Dub effects** — the arrangement layer: `.delay(".34:.45:.4")` throws on the skank and percussion, `.jux(rev)` for width, `.lpf(saw.range(400,2200).slow(4))` sweeps that open and close the tune like a curtain.

## Sample kit

- **Drums** — default kit: `bd` + `rim` one-drop, `hh`/`sh` space. No machine bank — the kit should sound like a room. Roots flavor: VCSL `conga`/`bongo`/`clave`/`agogo` sparse hits, one per bar at most.
- **Skank** — `gm_electric_guitar_muted` (the chop); a `piano`/`steinway` skank is the equally idiomatic keys version. Alternate them by section.
- **Bubble** — `gm_drawbar_organ`; `gm_percussive_organ` for a tighter, barkier bubble.
- **Bass** — `sine` with the round ADSR (dub-correct); `gm_electric_bass_finger` when the line wants flatwound growl.
- **Melodica** — `gm_flute` works, but `gm_harmonica` (or VCSL `harmonica`) is the actual reed-against-keys voice of Augustus Pablo.
- **Dub texture** — Dirt `space`/`wind` behind the version sections; everything else is delay and filters.
- No pack needed — the preloaded tiers cover reggae and dub. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Simple, minor-leaning, and mostly two chords — the bass does the traveling. Key of A minor:

- **i–bVII** — Am | G: the default roots vamp; the skank alternates the two chords while the bass walks the pentatonic.
- **i–bVII–bVI–bVII** — Am | G | F | G: the four-bar move that adds gravity without really modulating.
- **i–iv** — Am | Dm: the deepest roots change (think "rootsy" steppers tunes); spelled Dm = D–F–A.
- **Chorus move: i–bVII–iv–i** — Am | G | Dm | Am: enough motion to mark a section, resolved enough to loop forever.
- **Major-key mode** — C | F | G | F with the same one-drop and skank: rocksteady/ska inheritance for brighter tunes.

## Rhythm & feel

- Tempo 70–80. Not 90 — the space only breathes below 80.
- One-drop skeleton: `~ ~ ~ ~ [bd,rim] ~ ~ ~` — the kick and rim hit beat 3 together; beats 1, 2, and 4 are empty on purpose.
- Skank: `~ ~ x ~ ~ ~ x ~` (beats 2 and 4, short). Bubble: offbeat-accented 8ths underneath it.
- Bass placement: root around beat 1, then pentatonic moves on the "and"s — `a1@3 ~ ~ a1 ~ c2 d2 ~` — ending phrases early so the drop lands alone.
- Steppers variant (choruses): `bd ~ bd ~ bd ~ bd ~`, kick on every beat, rim still on 3 — the gear-change that says "chorus" without changing a chord.
- No swing anywhere: reggae 8ths are dead straight; the feel comes from what's missing.

## Structure

```
intro 4 | verse 16 | chorus 8 | dub 8 | verse 8 | chorus 8 | dub-out 4
   2         4          5       3        4          5         2    (energy 0-10)
```

Intro: bass and drums alone — the skeleton stated plainly. Verse: skank, bubble, and melodica join. Chorus switches to steppers with the iv chord move. Then the dub: melody and bubble vanish, the skank dissolves into delay, the filter sweeps, and the bass sings solo for eight bars. The rebuild sounds like relief. The dub-out strips even further — one delay throw hanging in air at the end.

## Techniques that actually create "reggae"

- **The one-drop** — kick and rim together on 3 and nothing on 1: the single most identifying pattern; if the downbeat is occupied you've written rock with a skank.
- **The skank** — short high chord stabs on 2 and 4, choked with `cut(1)`; keeps harmony and time while leaving the low mid completely empty for the bass.
- **Bubble organ** — offbeat 8th dyads that fill the skank's gaps; muting it is the classic dub move, so bring it in and out by section.
- **Bass as melody** — the top line of the arrangement is at `a1`; write it like a singer's part (pentatonic, phrases that end early) and everything else becomes accompaniment.
- **Subtractive arrangement** — the dub section removes the exact layers a pop song would feature; what remains defines the tune.
- **Delay as lead instrument** — a dotted-8th `.delay(".34:.45:.4")` on one skank stab or percussion hit carries whole bars; the echo is the melody's memory.
- **Filter curtain** — `.lpf(saw.range(lo,hi).slow(n))` sweeps over the skank open and close the tune slowly, the mixer's hand made audible.
- **Steppers switch** — moving the kick from one drop to all four beats marks a chorus more powerfully than any chord change.

## Practice approach

- Program the one-drop alone and listen to it for a minute; if it doesn't already feel like a song, fix the space (hats, shaker) before adding anything.
- Sing the bass line aloud, then transpose what you sang to `a1`–`g2`; if you can't sing it, it's too busy.
- Write one two-chord vamp (Am–G) and produce three sections from it using only layer muting, delay, and filter sweeps.
- Play the skank on 2 and 4 while counting the bass's offbeats out loud; internalizing that split is the whole groove.
- Study one King Tubby dub and note each element's exit — the order of removals is the composition.

## Example

```
// ═══ version — roots reggae with a dub pass, 76bpm ═══
// form: intro 4 | verse 16 | chorus 8 | dub 8 | verse 8 | chorus 8 | dub-out 4
// energy: 2 4 5 3 4 5 2 — the dub sections are the point, not a break
setcpm(76 / 4) // one cycle = one bar of 4/4

// ── drums — one-drop: kick and rim TOGETHER on beat 3, everything else is space ──
const onedrop = sound("~ ~ ~ ~ [bd,rim] ~ ~ ~").gain(.8)
const hats = sound("hh*8").gain("[.35 .18 .3 .18 .4 .18 .3 .18]")
const stepper = sound("bd ~ bd ~ bd ~ bd ~") // chorus: steppers — kick on every beat
const percDelay = sound("tb ~ ~ cb ~").delay(".34:.42:.4") // the engineer's throw
const kitVerse = stack(onedrop, hats, sound("sh*8").gain(.08))
const kitChorus = stack(stepper, sound("~ ~ ~ ~ rim ~ ~ ~"), hats, sound("sh*8").gain(.1))
const kitDub = stack(onedrop, hats.gain(.2), percDelay)
const drums = arrange(
  [4, stack(onedrop, hats.gain(.25))], // intro: the skeleton stated plainly
  [16, kitVerse],
  [8, kitChorus],
  [8, kitDub],
  [8, kitVerse], // the rebuild sounds like relief
  [8, kitChorus],
  [4, stack(onedrop.gain(.7), percDelay)], // dub-out: even sparser
)

// ── skank — muted guitar chops on 2 & 4, choked short; harmony as percussion ──
const skankV = chord("<Am G>").anchor("a4").voicing().struct("~ ~ x ~ ~ ~ x ~")
const skankC = chord("<Am G Dm Am>").anchor("a4").voicing().struct("~ ~ x ~ ~ ~ x ~")
const skankEcho = chord("<Am G>").anchor("a4").voicing().struct("~ ~ x ~ ~ ~ x ~").delay(".34:.45:.4").jux(rev).lpf(saw.range(400, 2200).slow(4))
const skank = arrange(
  [4, silence], [16, skankV.gain(.3)], [8, skankC.gain(.32)], [8, skankEcho.gain(.1)], // dub: the chop becomes its own echo
  [8, skankV.gain(.3)], [8, skankC.gain(.32)], [4, skankEcho.gain(.08)],
).sound("gm_electric_guitar_muted").release(.1).cut(1)

// ── bubble — drawbar organ, offbeat-accented 8ths; first thing the dub mutes ──
const bubV = note("<[e5,a5]*8 [d5,g5]*8>")
const bubC = note("<[e5,a5]*8 [d5,g5]*8 [a4,d5]*8 [e5,a5]*8>")
const bubble = arrange(
  [4, silence], [16, bubV.gain("[.16 .4 .16 .4 .16 .4 .2 .4]")], [8, bubC.gain("[.16 .4 .16 .4 .16 .4 .2 .4]")],
  [8, silence], // muted: the dub's opening statement
  [8, bubV.gain("[.16 .4 .16 .4 .16 .4 .2 .4]")], [8, bubC.gain("[.16 .4 .16 .4 .16 .4 .2 .4]")],
).sound("gm_drawbar_organ").release(.15)

// ── bass — the singer: A minor pentatonic, round sine, phrases that end early ──
const bassV = note("<[a1@3 ~ ~ a1 ~ c2 d2 ~] [a1@3 ~ ~ ~ g1 e2 g2]>")
const bassC = note("<[a1@3 ~ ~ g1 ~ a1 ~ ~] [a1@3 ~ ~ ~ g1 e2 g2] [d2@3 ~ ~ a1 ~ d2 ~ ~] [a1@3 ~ ~ ~ g1 e2 g2]>")
const bass = arrange(
  [4, bassV.gain(.7)], [16, bassV], [8, bassC], [8, bassV], [8, bassV], [8, bassC], [4, note("a1").release(1)],
).sound("sine").adsr(".008:.05:.9:.25").gain(.85)

// ── melodica — the lead: states the phrase, lets the delay finish it ──
const leadV = note("<[a4@3 ~ c5 ~ b4 a4 ~ ~] [e5@3 ~ d5 c5 b4 ~ a4 ~] [c5@2 ~ e5 ~ g5 e5 ~ ~] [a4 ~ ~ ~ ~ ~ ~ ~]>")
const leadDub = note("<[a5 ~ ~ ~ ~ ~ ~ ~] [~ ~ ~ ~ ~ ~ ~ ~]>") // one stab every two bars; the echo carries the rest
const lead = arrange(
  [4, silence], [16, leadV.gain(.35)], [8, silence], [8, leadDub.gain(.4).delay(".38:.5:.5")],
  [8, leadV.gain(.35)], [8, silence], [4, note("a5").delay(".38:.55:.5").gain(.4)], // the final throw hangs in air
).sound("gm_flute").room(.5).delay(".25:.25:.3")

$: drums
$: skank
$: bubble
$: bass
$: lead
```
