Grunge's equivalent moment is **the flip** — eight bars of tired, clean quiet that detonates into a fuzz chorus with no transition to speak of. Where trance spends its tension in a filter and jazz in a cadenza, grunge spends it in **dynamic dishonesty**: the verse pretends the song is small, and the chorus reveals it never was. Loud-quiet-loud isn't a structural preference in this genre; it's the whole emotional argument, and the size of the chorus is exactly the size of the lie the verse told.

## What the flip actually is

The verse is quiet — an arpeggiated or single-note clean guitar, a bass that's suddenly the lead instrument, drums on rims — and the chorus detonates the same or related chords at full fuzz, often with no pre-chorus fill at all: one beat of silence or a lone crash, then the wall. Crucially, the quiet material and the loud material are usually the same four chords; the dynamic does all the transforming. The second verse drops back down (the relapse), the bridge goes quiet again before building, and the final chorus is the first chorus plus one more layer — loudest by addition, not by turning anything up. The other axis is **sloppy vs precise**: verses drift (`degradeBy(.06)`, uneven note lengths), choruses lock; the precision is what makes the sloppiness sound like exhaustion rather than error.

## The layers

- **Clean guitar** — `pluck` arpeggios with `lpf(2200)` and `room(.3)`: tired, small, hungover. Add 9ths (`e4` over a D dyad) for the dirty-shimmer color.
- **Fuzz guitar** — `gm_overdriven_guitar` with `shape(.6)`: the distortion is a door slamming. Power dyads strummed through a syncopated `.struct("[x x ~ x ~ x x ~]")`, plus drop-D riffing on the low `d2`.
- **Bass** — `sawtooth` with `lpf(600)`, woolly and forward. In the quiet sections it's the lead instrument; in the loud ones it's the floor.
- **Drums** — verses: kick on 1, `rim` backbeat, 8th hats, all at gain .4 or less. Choruses: heavy 2-and-4 snare, kick with a 16th push (`bd ~ bd ~ bd ~ [bd bd]`), open hats, crash on the downbeat. Fills are tom crescendos, not snare rolls.
- **Vocals** — `gm_voice_oohs`, low and bored in verses (`d4` and below), anguished at the top of choruses (`d5` region), the final chorus doubled an octave down.

## Sample kit

- **Drums** — default kit at both extremes: `rim` + soft 8th hats when quiet, `sd` + `oh` + `cr` when loud. No machine bank — grunge drums are a room, not a clock.
- **Clean guitar** — `pluck` through `lpf(2200)` for the tired arpeggios; `gm_acoustic_guitar_steel` when the verse needs a warmer, more physical body.
- **Fuzz** — `gm_overdriven_guitar` + `shape(.6)`, the door slamming; `gm_distortion_guitar` reserved for the final chorus.
- **Bass** — `gm_electric_bass_finger`: woolly and forward, the lead instrument of the quiet sections. Synth fallback: `sawtooth` + `lpf(600)`.
- **Vocals** — `gm_voice_oohs`, bored and low in verses, anguished at the top of choruses.
- No pack needed — the preloaded tiers cover grunge. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Key of D throughout (drop-D feel: everything visits the low `d2`). Vocabulary: power dyads, and borrowed chords doing the sour lifting — bVI (Bb), bVII (C), bIV (Gb), bV (Ab), and the minor iv. The flat-fourth and flat-fifth slides are the genre's fingerprints; they resolve nowhere politely.

- **I–bVI–bVII–I** — D, Bb, C, D (`[d3,a3] [bb2,f3] [c3,g3] [d3,a3]`) — the grunge axis, used quiet in the verse and loud in the chorus with zero reharmonization. The flip's fuel.
- **IV–bIV–I** — G, Gb, D (`[g2,d3] [gb2,db3] [d3,a3]`) — the sour slide into the chorus; the half-step fall then drop to the tonic feels like the floor tilting.
- **I–bIII–IV** — D, F, C (`[d3,a3] [f2,c3] [c3,g3]`) — the major-key-but-miserable loop for verses that want motion without hope.
- **V–bV–I** — A, Ab, D (`[a2,e3] [ab2,eb3] [d3,a3]`) — bridge poison: the dominant sags a half step before the tonic arrives, the flattened-fifth sigh.

## Rhythm & feel

100–130 bpm — slow enough to wallow, fast enough to slam. One cycle = one bar of 4/4. Straight eighths, no swing, but deliberately imperfect: verse patterns get `degradeBy(.06)` and unquantized-feeling gains, chorus patterns are dead tight. The drag is behind-the-beat bass and a snare that lands heavy rather than early.

- **Drop-D riff skeleton** — `d2 d2 ~ d2 ~ d2 bb2 c2 d2` — the low-string stroll that walks down to Bb and climbs home
- **Quiet verse drums** — `bd ~ ~ ~` + `~ rim ~ rim` + `hh*8`, all soft
- **Chorus drums** — `bd ~ bd ~ bd ~ [bd bd]` + `~ sd ~ sd` + `[~ oh]*4` + crash
- **The detonation** — no fill: the last verse bar just stops, then `cr` on the chorus downbeat
- **The bridge crescendo** — `ht*8` and `sd*8` with gains climbing bar by bar (`"<.2 .3 .4 .5>"`)

## Structure

intro (clean hook) 4 | verse Q 8 | pre 4 | chorus L 8 | verse 8 | chorus 8 | bridge (quiet→build) 8 | final chorus 8 | outro 4 — 60 bars, about two minutes at 112 bpm. The pre-chorus is optional; the first flip often happens with no warning at all.

```
// energy: 3 - 4 - 6 - 10 - 4 - 10 - 2 then 8 - 11 - 5
// the gap between 4 and 10 IS the song
```

## Techniques that actually create "grunge"

- **Loud-quiet-loud via arrangement, not gain rides** — strip layers in verses (clean guitar, bass, rim kit), stack them in choruses (fuzz dyads, drop-D riff, full kit); the same chords read as two different songs.
- **The fuzz** — `gm_overdriven_guitar` with `shape(.6)` and gain pushed: sludgy, gated-feeling, wrong on purpose. Clean it up and it's just rock.
- **Drop-D feel** — center riffs on the low `d2` (`note("d2 d2 ~ d2 ~ d2 bb2 c2 d2")`), moving shapes in fret-distance units (d–bb–c) rather than functional roots.
- **Borrowed bV and bIV** — the `gb2,db3` and `ab2,eb3` slides; one per song is enough to make the whole thing taste off in the right way.
- **Sloppy verses, precise choruses** — `degradeBy(.06)` and uneven arpeggios when quiet; machine-straight struct patterns when loud. Precision reads as rage only after sloppiness has established the exhaustion.
- **Bass-led quiet sections** — in verses, give the bass the melody (`[d1 d1 d1 d1]` quarter pulses with movement) and let guitars arpeggiate around it.
- **The one-beat detonation** — into the first chorus, no fill: a bar of air or a lone crash, then everything at once.
- **Final chorus by addition** — first chorus plus `chorusStrum.transpose(12).gain(.3)`: one octave layer makes it the biggest without touching the mix.

## Practice approach

- Write one four-chord loop and arrange it quiet then loud with zero new chords — if the flip doesn't work with arrangement alone, the loop isn't good enough yet.
- Mute the drums and feel the flip with gain and layers only; drums should be the last thing that gets loud.
- Drill the bIV slide (G–Gb–D) and the bV slide (A–Ab–D) until the sourness sounds intentional.
- Build a riff vocabulary on the low `d2` string alone, moving in half and whole steps.
- Set verse gain around .25 and chorus around .7 by default; if you're tempted to go higher, add a layer instead.

## Example

```
// ═══ plaid thunder — grunge in D, 112bpm, drop-D feel, loud-quiet-loud ═══
// form: intro 4 | verse Q 8 | pre 4 | chorus L 8 | verse 8 | chorus 8 | bridge 8 | final chorus 8 | outro 4
// energy: 3 - 4 - 6 - 10 - 4 - 10 - 2 then 8 - 11 - 5. the gap between 4 and 10 IS the song
setcpm(112 / 4) // one cycle = one bar of 4/4

// ── clean guitar — tired arpeggios of the SAME chords the fuzz will detonate: D Bb C D ──
const vArp = note("<[d3 a3 d4 a3 d4 a3 e4 a3] [d3 a3 d4 a3 d4 a3 e4 a3] [bb2 f3 bb3 f3 c4 f3 bb3 f3] [bb2 f3 bb3 f3 c4 f3 bb3 f3] [c3 g3 c4 g3 d4 g3 c4 g3] [c3 g3 c4 g3 d4 g3 c4 g3] [d3 a3 d4 a3 d4 a3 e4 a3] [d3 a3 d4 a3 e4 a3 d4 a3 a3]>") // the e4/d4 9ths are the tired shimmer

const clean = arrange(
  [4, note("<[d3 a3 d4 a3 d4 a3 e4 a3]!4>").gain(.3)], // the hook, small and hungover
  [8, vArp.gain(.26).degradeBy(.06)], // verse: sloppy on purpose
  [4, note("<[g3 d4 g4 d4]!2 [gb3 db4 gb4 db4]!2>").gain(.3).degradeBy(.06)], // pre: IV, then the bIV sour slide
  [8, silence], // chorus: the fuzz takes it
  [8, vArp.gain(.26).degradeBy(.06)],
  [4, note("<[g3 d4 g4 d4]!2 [gb3 db4 gb4 db4]!2>").gain(.3).degradeBy(.06)],
  [8, silence],
  [4, note("<[bb2 f3 bb3 f3]!4>").gain(.22)], // bridge: quiet again, the bass leads
  [4, silence],
  [8, silence],
  [4, note("<[d3 a3 d4 a3 d4 a3 e4 a3]!4>").gain(.3)], // outro: the hook returns, tape left running
).sound("pluck").lpf(2200).room(.3).release(.2)

// ── fuzz guitar — gm_overdriven_guitar + shape(.6): the distortion is a door slamming ──
const chorusStrum = note("<[d3,a3] [bb2,f3] [c3,g3] [d3,a3] [d3,a3] [bb2,f3] [c3,g3] [d3,a3]>").struct("[x x ~ x ~ x x ~]").gain(.7)
const dropRiff = note("d2 d2 ~ d2 ~ d2 bb2 c2 d2").gain(.6) // drop-D feel: everything visits the low d
const preStrum = note("<[g2,d3]!2 [gb2,db3]!2>").struct("[x x x x x x x x]").gain(.6)

const fuzz = arrange(
  [4, silence],
  [8, silence], // verses stay quiet: do not peak early
  [4, preStrum],
  [8, stack(chorusStrum, dropRiff)],
  [8, silence],
  [4, preStrum],
  [8, stack(chorusStrum, dropRiff)],
  [4, silence], // bridge: quiet half
  [4, stack( // bridge build: IV bIV V, gain climbing bar by bar
    note("<[g2,d3]!2 [gb2,db3] [a2,e3] [a2,e3]>").struct("[x x ~ x x ~ x x]").gain("<.4 .5 .6 .7>"),
    note("d2 d2 d2 d2 d2 d2 d2 d2").gain(.6),
  )],
  [8, stack(chorusStrum.gain(.75), dropRiff, chorusStrum.transpose(12).gain(.3))], // final: +octave, loudest by addition
  [4, note("[d2,d3]@4").gain(.8)], // the stamp, feedback implied
).sound("gm_overdriven_guitar").shape(.6).room(.2)

// ── bass — woolly sawtooth; in the quiet parts it is the lead instrument ──
const bassV = note("<[d1 d1 d1 d1]!2 [bb1 bb1 bb1 bb1]!2 [c2 c2 c2 c2]!2 [d1 d1 d1 d1]!2>").gain(.6)
const bassC = note("<d1*8 d1*8 bb1*8 bb1*8 c2*8 c2*8 d1*8 d1*8>").gain(.7)

const bass = arrange(
  [4, note("d1 d1 d1 d1").gain(.55)],
  [8, bassV],
  [4, note("<g1*8 g1*8 gb1*8 gb1*8>").gain(.6)],
  [8, bassC],
  [8, bassV],
  [4, note("<g1*8 g1*8 gb1*8 gb1*8>").gain(.6)],
  [8, bassC],
  [4, note("<[bb1 bb1 bb1 bb1]!2 [f1 f1 f1 f1]!2>").gain(.6)], // bVI IV under the quiet
  [4, note("<g1*8 g1*8 gb1*8 a1*8>").gain(.7)], // the climb
  [8, bassC.gain(.75)],
  [4, note("d1@4").gain(.7)],
).sound("gm_electric_bass_finger").lpf(600)
$: bass

// ── drums — rims when quiet, crashes when loud; the flip needs no warning fill ──
const kitQ = stack(sound("bd ~ ~ ~").gain(.4), sound("~ rim ~ rim").gain(.3), sound("hh*8").gain(.16))
const kitPre = stack(sound("bd ~ ~ bd").gain(.45), sound("~ sd ~ sd").gain(.45), sound("hh*8").gain(.18), sound("~ ~ ~ [ht mt lt]").gain(.3))
const kitC = stack(sound("bd ~ bd ~ bd ~ [bd bd]").gain(.65), sound("~ sd ~ sd").gain(.55), sound("[~ oh]*4").gain(.28), sound("<cr ~ ~ ~>").gain(.4))

const drums = arrange(
  [4, kitQ],
  [8, kitQ],
  [4, kitPre],
  [8, kitC], // detonation: no pre-chorus fill, just a crash
  [8, kitQ],
  [4, kitPre],
  [8, kitC],
  [4, kitQ],
  [4, stack(sound("ht*8").gain("<.2 .3 .4 .5>"), sound("sd*8").gain("<.1 .15 .25 .4>"))], // tom+snare crescendo
  [8, stack(kitC, sound("<~ ~ ~ [ht mt lt ht]>").gain(.35))],
  [4, stack(sound("cr ~ ~ ~").gain(.4), sound("[sd,bd] ~ ~ ~").gain(.5))],
)
$: drums

// ── vocals — low and bored in verses; anguished at the top of the choruses ──
const vVox = note("<d4@4 ~ a3@4 ~ bb3@4 ~ [a3 d4] ~>").gain(.4)
const cVox = note("<[d5@2 c5] [bb4@2 a4] [c5@2 bb4] [a4@4] [d5@2 c5] [bb4@2 a4] [c5@2 d5] [d5@4]>").gain(.55)

const vox = arrange(
  [4, silence],
  [8, vVox],
  [4, silence],
  [8, cVox],
  [8, vVox],
  [4, silence],
  [8, cVox],
  [8, note("<bb3@4 f4@4 ~ [c4 d4]>").gain(.35)], // the bridge mutter
  [4, silence],
  [8, stack(cVox, cVox.transpose(-12).gain(.3))], // final: the shout plus its shadow
  [4, silence],
).sound("gm_voice_oohs").room(.35)
$: vox

$: clean
$: fuzz
```
