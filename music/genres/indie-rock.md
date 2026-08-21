Indie rock's equivalent moment is **the jangle** — the intro guitar figure you can hum before the singer opens their mouth, which then refuses to leave for the remaining three minutes. Where pop spends its tension in a bridge and punk in a shout-along, indie rock spends it in **a hook played on a clean guitar**: melancholy chords at a bright tempo, a bass that walks instead of pumps, and a chorus that adds layers to the song rather than changing it. The genre's signature emotional move is sad words over happy strings — melancholy harmony under a jangly surface.

## What the jangle actually is

It's an arpeggiated clean-guitar figure — usually 16ths, usually built from the song's verse chords — that starts the track alone and functions as its identity card. There's no verified clean-electric GM patch in the toolkit, so the jangle lives on `pluck` (bright, picked, takes delay beautifully) or `triangle` arps (glassier, synth-adjacent); strums go to `gm_acoustic_guitar_muted`. The chorus doesn't replace the jangle, it buries it kindly: strums arrive on top, the arps get tucked underneath, a counter-line and a sparkle layer join — the song gets thicker, not different. And the outro brings the figure back alone, proving it was the song all along. The verse harmony carries the melancholy: **I–vi–iii–IV** is the axis, minor chords against a major tonic with no resolution to brightness.

## The layers

- **Jangle guitar** — `pluck`, 16th arps (`[g3 c4 e4 c4]*4` per bar), `room(.25)`, and a dotted-8th-ish `delay(".2:.19:.3")` so the figure circles behind itself. Pan slightly off-center.
- **Strum guitar** — `gm_acoustic_guitar_muted`, entering only in choruses, chords driven by `.struct("[x ~ x x ~ x x ~]")`: the syncopated strum sits on top of the straight arps.
- **Counter-line guitar** — `triangle` in choruses, sparse quarter-note phrases (`[c5@2 ~] [d5 c5]`), answering the vocal; its own delay makes it shimmer.
- **Bass** — `gm_acoustic_bass`, and critically **linear**: it walks between chord roots (`c2 b2 a2`, passing `cs3`/`fs3` tones) instead of pumping roots; the walk is where the song's craft hides.
- **Drums** — backbeat kit with a pushy kick (`bd ~ ~ bd`), rim ghosts in verses, crashes reserved for choruses, and **tom-heavy fills** (`[ht mt lt ht]`) — snare rolls are banned by taste.
- **Sparkle** — `gm_music_box` doubling the arp's top notes an octave up, quiet (`.gain(.12)`), choruses and outro only.

## Harmony

Key of C. Vocabulary: triads with add9/sus colors on the jangle (the `d4` over C, `e4` over D shapes), a borrowed bVII for the chorus lift, and iii used as a real emotional chord, not a passing one.

- **The melancholy verse: I–vi–iii–IV** — C, Am, Em, F (`[c3,g3] [a2,e3] [e3,b3] [f2,c3]`, arpeggiated as `[g3 c4 e4 c4]`, `[a3 c4 e4 c4]`, `[b3 e4 g4 e4]`, `[a3 c4 f4 c4]`) — two bars each. The iii is the sadness pivot; don't skip past it.
- **The chorus lift: IV–bVII–I** — F, Bb, C (`[f3,a3,c4] [bb3,d4,f4] [c4,e4,g4]`) — the borrowed Bb is the "suddenly wide" move; end the loop on a G (`[g3,b3,d4]`) turn to restart.
- **Middle-8: vi–IV–I–V** — Am, F, C, G (`[a2,e3] [f2,c3] [c3,g3] [g2,d3]`) — the reset; play it with the quietest kit so the last chorus lands.
- **The turnaround: iii–IV** — Em to F (`[e3,b3] [f2,c3]`) — half-step root slide into the downbeat; the cheapest poignancy in the genre and it works every time.

## Rhythm & feel

100–140 bpm; the example sits at 118, where 16th arps percolate without rushing. A whisper of `swing(.04)` on the hats gives a human lilt; the arps stay dead straight so the push comes from the kick. The kick pattern is the indie tell: `bd ~ ~ bd` — beat 1, then the "and" of 3 — a limping, hopeful gait. Melodic phrases anticipate the barline (start on the "and" of 4); fills land slightly late.

- **Kick** — `bd ~ ~ bd` (verse), `bd ~ bd ~ bd ~ bd bd` (chorus, with the 16th push at the end)
- **Backbeat** — `~ sd ~ sd` with a rim ghost layer in verses
- **Hats** — `hh*8` verses, `[~ oh]*4` pre-chorus, back to `hh*8` with more gain in choruses
- **The jangle grid** — `[g3 c4 e4 c4]*4`: four notes, continuous 16ths, never accents the same note twice in a row
- **The fill** — `~ ~ ~ [ht mt lt ht]`: toms descending, no snare roll, into every chorus

## Structure

intro (jangle alone) 4 | verse 8 | pre 8 | chorus 8 | verse 8 | chorus 8 | middle-8 8 | chorus 8 | outro (jangle alone) 4 — 64 bars, just over two minutes at 118. The figure is present in every section except it ducks (`.gain(.24)`) under choruses; the song is one continuous thread that gets dressed and undressed.

```
// energy: 4 - 5 - 6 - 8 - 5 - 8 - 6 - 9 - 6
// it rises by layers; the last chorus wins by one added sparkle, not by volume
```

## Techniques that actually create "indie rock"

- **The hook-first intro** — the arpeggio figure alone for four bars; if those four bars don't identify the song, the chorus won't save it.
- **Melancholy axis** — I–vi–iii–IV with real time on the iii; the major tonic keeps it from wallowing, the vi/iii keeps it from smiling.
- **Linear bass** — the bass walks between roots with passing tones (`cs3`, `fs3`); one good walk per section is the difference between a band and a loop.
- **Tom-heavy fills** — `[ht mt lt ht]` and tom 8ths; a snare roll instantly sounds like a different, more corporate genre.
- **Layer-addition dynamics** — choruses add strums, counter-line, and sparkle while the jangle stays; nothing gets louder so much as more crowded.
- **Delay circles** — `.delay(".2:.19:.3")` on the arp makes one guitarist sound like two; the echo is the second band member.
- **Capo brightness** — `.transpose(12)` on a doubled figure or the music box for the shimmer register without rewriting anything.
- **The "one more chorus" outro** — final chorus repeats, then drops to the solo figure with hats fading: the song ends by remembering its own intro.

## Practice approach

- Write the 4-bar arp figure before choosing any chords; if it doesn't stand alone, no arrangement will fix it.
- Compose one bass walk per section that connects every chord by step; then mute everything else and check it's actually melodic.
- Transcribe one R.E.M.-or-later progression and note where the iii chord gets its extra bar.
- For a week, fill only with toms; notice how the dynamics survive without rolls.
- Arrange a chorus purely by adding one layer per two bars — no gain changes — and listen to whether it still swells.

## Example

```
// ═══ satellite hearts — indie rock in C, 118bpm, jangle-first ═══
// form: intro 4 | verse 8 | pre 8 | chorus 8 | verse 8 | chorus 8 | middle-8 8 | chorus 8 | outro 4
// energy: 4 - 5 - 8 - 5 - 8 - 6 - 9 - 6. the hook outlives the sections
setcpm(118 / 4) // one cycle = one bar of 4/4

// ── the jangle — 16th arpeggios over I vi iii IV (C Am Em F); the figure IS the song ──
const iJangle = note("<[g3 c4 e4 c4]*4 [b3 e4 g4 e4]*4 [a3 c4 f4 c4]*4 [g3 c4 e4 d4]*4>").gain(.42) // intro variant, walks down at the end
const vJangle = note("<[g3 c4 e4 c4]*4 [g3 c4 e4 c4]*4 [a3 c4 e4 c4]*4 [a3 c4 e4 c4]*4 [b3 e4 g4 e4]*4 [b3 e4 g4 e4]*4 [a3 c4 f4 c4]*4 [a3 c4 e4 d4]*4>").gain(.4)

const jangle = arrange(
  [4, iJangle],
  [8, vJangle],
  [8, vJangle.gain(.38)], // pre-chorus: same figure, hats open around it
  [8, vJangle.gain(.24)], // chorus: tucked under the strums — addition, not replacement
  [8, vJangle],
  [8, vJangle.gain(.24)],
  [8, vJangle.gain(.36)], // middle-8: exposed again
  [8, vJangle.gain(.24)],
  [4, iJangle.gain(.4)],  // outro: the song remembers its intro
).sound("pluck").room(.25).delay(".2:.19:.3")

// ── strums — acoustic-muted, choruses only, syncopated against the straight arps ──
const chorusStrum = note("<[f3,a3,c4]!2 [bb3,d4,f4]!2 [c4,e4,g4]!3 [g3,b3,d4]>").struct("[x ~ x x ~ x x ~]").gain(.5) // IV bVII I, V turn

const strums = arrange(
  [20, silence],
  [8, chorusStrum],
  [8, silence],
  [8, chorusStrum],
  [8, silence],
  [8, chorusStrum],
  [4, note("[c4,e4,g4]@4").gain(.4)], // let the last chord ring
).sound("gm_acoustic_guitar_muted").room(.25)

// ── counter-line — triangle, sparse answers, echoing in its own delay ──
const counterA = note("<[c5@2 ~] [d5 c5] [bb4@2 ~] [c5 bb4] [e5@2 d5] [c5 g4] [a4 b4] [d5@4]>").gain(.3)
const counterB = note("<[c5@2 ~] [d5 c5] [bb4@2 ~] [c5 bb4] [e5@2 d5] [e5 d5] [c5 d5] [g4@4]>").gain(.3)

const counter = arrange(
  [20, silence],
  [8, counterA],
  [8, silence],
  [8, counterB],
  [8, silence],
  [8, counterA],
  [4, silence],
).sound("triangle").room(.3).delay(".2:.19:.25")

// ── bass — gm_acoustic_bass, LINEAR: walks between roots, passing tones allowed ──
const bassI = note("<[c2 c2 e2 g2] [c2 c2 b2 a2]>") // intro: root, then already walking
const bassV = note("<[c2 c2 b2 a2]!2 [a2 a2 b2 cs3]!2 [e2 e2 fs3 g3]!2 [f2 f2 e2 d2]!2>").gain(.6) // the walk: never just roots
const bassC = note("<[f2 f2 f2 f2]!2 [bb1 bb1 bb1 bb1]!2 [c2 c2 c2 c2]!2 [c2 c2 c2 g2]!2>").gain(.65)
const bassM = note("<[a1 a1 a1 e2]!2 [f1 f1 f1 c2]!2 [c2 c2 c2 g2]!2 [g1 g1 g1 d2]!2>").gain(.55)

const bass = arrange(
  [4, bassI],
  [8, bassV],
  [8, bassV],
  [8, bassC],
  [8, bassV],
  [8, bassC],
  [8, bassM],
  [8, bassC],
  [4, note("[c2 c2 g2 c2]").gain(.5)], // outro: the bass hums the walk one last time
).sound("gm_acoustic_bass").gain(.55)
$: bass

// ── drums — pushy kick, rim ghosts, crashes reserved, tom-heavy fills only ──
const tomfill = sound("~ ~ ~ ~ [ht mt lt ht]")
const kitI = stack(sound("bd ~ ~ ~").gain(.35), sound("~ rim ~ rim").gain(.28), sound("hh*8").gain(.14))
const kitV = stack(sound("bd ~ ~ bd").gain(.5), sound("~ sd ~ sd").gain(.42), sound("hh*8").gain(.18).swing(.04))
const kitP = stack(sound("bd ~ bd bd").gain(.5), sound("~ sd ~ sd").gain(.45), sound("[~ oh]*4").gain(.22), sound("<~ ~ [ht mt lt ht] [ht mt lt ht]>").gain(.3))
const kitC = stack(sound("bd ~ bd ~ bd ~ bd bd").gain(.5), sound("~ sd ~ sd").gain(.5), sound("hh*8").gain(.22), sound("<cr ~ ~ ~>").gain(.32))
const kitM = stack(sound("bd ~ ~ bd").gain(.45), sound("~ sd ~ sd").gain(.4), sound("sh*16").gain(.1), sound("<~ [ht mt lt ht]>").gain(.28))

const drums = arrange(
  [4, kitI],
  [8, kitV.every(8, x => tomfill)],
  [8, kitP],
  [8, kitC],
  [8, kitV.every(8, x => tomfill)],
  [8, kitC],
  [8, kitM],
  [8, stack(kitC, sound("~ ~ ~ [ht mt lt ht]").gain(.3))],
  [4, sound("hh*8").gain(.12)], // outro: hats only, fading
)
$: drums

// ── sparkle — the music box doubles the arp tops, an octave up, choruses and outro ──
const sparkle = arrange(
  [20, silence],
  [8, note("<f5!2 bb5!2 c5!2 [c5 g5]>").gain(.12)],
  [8, silence],
  [8, note("<f5!2 bb5!2 c5!3 g5>").gain(.12)],
  [8, silence],
  [8, note("<f5!2 bb5!2 c5!3 g5>").gain(.13)],
  [4, note("<c5 g4 e4 c4>").gain(.12)], // the hook dissolving
).sound("gm_music_box").room(.4)

$: jangle
$: strums
$: counter
$: sparkle
```
