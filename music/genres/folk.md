Folk's equivalent moment is **the last verse** — the point three minutes into a plain, repeated tune where the story lands and the arrangement finally shows everything it was holding back. Pop earns its bridge by leaving the song; folk earns its last verse by never leaving it. The chords barely change from verse one; what changes is what the listener knows, and how many voices are carrying it.

## What the last verse actually is

Verses carry narrative; the refrain or chorus is the fixed stone you keep returning to. The last verse exploits that habit two ways, often both in sequence. First it **strips down** — two bars of voice alone (or voice with one bare instrument) so the room leans in; this only works because the arrangement spent two verses getting fuller. Then it **fills up beyond anything earlier** — every player returns at once, the fiddle doubles the melody, maybe an octave sparkle on top — and the same old refrain now reads as a conclusion instead of a refrain. The tune hasn't changed; the meaning has. That recontextualization is the entire emotional technology of the genre, and it's an arrangement move, not a compositional one: plan it from bar one, or it sounds like a fade-in by accident.

## The layers

- **Acoustic guitar, the default instrument** — `pluck` carries fingerpicked arpeggios beautifully (`room(.3)`, no synth flavor), and `triangle` is the honest bare-bones sketch voice for melodies. When you want a real strummed steel-string, `gm_acoustic_guitar_steel` with `.struct("x x x")`-style hits reads instantly as a second guitar.
- **Fiddle** — `gm_fiddle` (not `gm_violin` — the fiddle patch is brighter and folkier) for counter-lines, answer phrases between vocal lines, and unison doubling in the last verse.
- **Upright bass** — `gm_acoustic_bass`, but only when "the band shows up": root on beat one, fifth later in the bar, nothing clever. Solo and duo folk has no bass at all, and the music doesn't miss it.
- **Optional color** — `gm_flute` a low octave under the melody, `gm_music_box` for a music-box arrangement variant, `gm_banjo` when it tips toward old-time. These are garnish; the guitar-fiddle-voice triangle is the meal.
- **No drums** — the default folk ensemble has no percussion at all; meter comes from the guitar pattern. If you need the session feel, one foot stomp is the ceiling: `sound("bd ~ ~").gain(.22)` in 3/4, nothing more.

## Harmony

Two families, and knowing which one a song belongs to is most of the harmonizing. **Major-key diatonic**: the workhorses are I–V–vi–IV (in D: D–A–Bm–G) and I–vi–IV–V (D–Bm–G–A); verses are often just I with occasional V (D … A … D), saving the full four-chord loop for the refrain. **Modal**: dorian songs sit on a minor tonic with the major IV below it (Am–G, drone on a), mixolydian songs sit on major I with the bVII above it (D–C–G) — in both cases one or two chords for the whole song, and the melody does the moving. Melodies are mostly **pentatonic** (`n("0 1 2 4 5").scale("D:major:pentatonic")` gives you d e fs a b — note the strudel spelling, never `#`), which is why they survive generations of unaccompanied singing. Canonical progressions, roman and spelled in D:

- **I–V–vi–IV** → D A Bm G — the modern folk refrain
- **I–vi–IV–V** → D Bm G A — older ballad cadence, strong pull home
- **Dorian two-chord** → Am G (in A dorian) — drone the a under it and let the melody carry mode
- **Mixolydian two-chord** → D C (then home via G) — the dropped-third cadence that reads instantly as "old tune"

## Rhythm & feel

Two meters cover the tradition. **4/4 strummers and fingerpickers** run 100–140 bpm; the groove is a picked bass alternating with chord shapes — `note("d2 a2 d3 a2")` against strummed `[d3,a3,d4]` hits — with no swing at all, or at most a whispered `swing(.04)` on sung phrasing. **3/4 waltz songs** run 80–110 bpm and are where the genre's most famous melodies live; in strudel set the cycle to the 3/4 bar with `setcpm(bpm/3)` (divide by 3, not 4) and the skeleton is oom-pah-pah: bass root on beat one, guitar chord or arpeggio cells on two and three. The 3/4 arpeggio is six 8ths to the bar: `[d3 a3 d4 fs4 a4 fs4]`. Feel devices: the low open string rings under everything (let it — the sustain is the reverb), phrases start on beat one and end early (the space before beat one of the next bar is where the fiddle answers), and tempo is steady enough to walk to.

## Structure

Folk forms are verse-driven: **strophic** (A A A, each verse 8 or 16 bars, refrain inside or between verses) is the default; **verse-refrain** (verse, two-line refrain sung by everyone) and modern **verse-chorus** are the 20th-century versions. A full arrangement: intro 4 (guitar alone states the material) | verse 1, 8 bars (voice + guitar only) | verse 2, 8 (+ bass, strum, fiddle answers) | last verse, 8 (bars 1–2 stripped to voice, then everything) | refrain, 8 (fullest) | outro 4 (guitar alone again). Energy graph: low → add a layer per verse → drop to nothing for two bars → all layers → release. The story arc maps to the arrangement arc: details accumulate, the drop is the confession, the final refrain is everyone singing.

## Techniques that actually create "folk"

- **The stripped opening of the last verse** — two bars of melody with no accompaniment (`silence` in every lane but the voice) before the band returns. This is the genre's drop; do not skip the preceding build or the drop reads as a mistake.
- **Refrain recontextualization** — keep the refrain melody and chords literally identical each time; change only orchestration and register. Meaning is made by what surrounds the unchanged thing.
- **Drone** — a sustained root or fifth under modal tunes (`note("a2@8")` pedal or just the low open string ringing in the pattern). The stillness underneath makes the modal melody feel timeless rather than merely minor.
- **Open-string voicings** — build guitar patterns around actual open strings (d3, a3, d4 in D; g3 d4 g4 in G) so shapes ring into each other. In mini-notation, favor arpeggios that revisit the open string: `[d3 a3 d4 fs4 a4 fs4]`.
- **Fiddle answers** — the fiddle plays only in the gaps the voice leaves: end of each two-bar phrase, one answer per four bars. Call and response, but polite — the fiddle never plays over the singer.
- **Octave sparkle in the final refrain** — the fiddle doubles the melody and adds `superimpose(x => x.transpose(12))` at low gain for one lift. One lift only; this is not trance.
- **Hammer-on feel** — quick pairs where a higher note snaps onto its target (`[e5@1 d5@3]` inside a beat) imitate guitar hammers and pulls better than any synth parameter.

## Practice approach

- Learn the words of one traditional ballad and notice where the story turns; the arrangement turn belongs at the same bar.
- Write the melody first, in pentatonic, singable, ending early — then harmonize it with the fewest chords that survive.
- Build the arrangement by addition rules only (what enters when, what never enters) before touching any note of a part.
- Write one strophic song where verses 1, 2 and 3 have identical notes and identical chords — if it still builds, the arrangement is doing its job.
- Play the 3/4 pattern at 80 and at 110 bpm and notice how the same six notes change character; choose the tempo last.

## Example

```
// ═══ the last verse — folk waltz in d, 96 bpm, 3/4 ═══
// form: intro 4 | verse 1 (voice + guitar) 8 | verse 2 (+ bass, strum, fiddle answers) 8 |
//       last verse 8 — bars 1-2 voice alone, then everyone back | refrain 8 | outro 4
// energy: guitar only → +voice → +band → two bare bars (the drop) → everyone → release
setcpm(96 / 3) // one cycle = one bar of 3/4 — divide by 3, not 4

// changes — honest triads, one per bar: verse D A Bm G | D G A D; refrain G A D Bm | G A D D
const verseCh = "<D A Bm G D G A D>"
const refrainCh = "<G A D Bm G A D D>"

// guitar — travis-ish arpeggios, six 8ths to the bar; the low open d rings under everything
const introArps = "<[d3 a3 d4 fs4 a4 fs4] [g2 d3 g3 b3 d4 b3] [a2 e3 a3 cs4 e4 cs4] [d3 a3 d4 fs4 a4 fs4]>"
const verseArps = "<[d3 a3 d4 fs4 a4 fs4] [a2 e3 a3 cs4 e4 cs4] [b2 fs3 b3 d4 fs4 d4] [g2 d3 g3 b3 d4 b3] [d3 a3 d4 fs4 a4 fs4] [g2 d3 g3 b3 d4 b3] [a2 e3 a3 cs4 e4 cs4] [d3 a3 d4 fs4 a4 fs4]>"
const v3Arps = "<[b2 fs3 b3 d4 fs4 d4] [g2 d3 g3 b3 d4 b3] [d3 a3 d4 fs4 a4 fs4] [g2 d3 g3 b3 d4 b3] [a2 e3 a3 cs4 e4 cs4] [d3 a3 d4 fs4 a4 fs4]>" // bars 3-8 only
const refrainArps = "<[g2 d3 g3 b3 d4 b3] [a2 e3 a3 cs4 e4 cs4] [d3 a3 d4 fs4 a4 fs4] [b2 fs3 b3 d4 fs4 d4] [g2 d3 g3 b3 d4 b3] [a2 e3 a3 cs4 e4 cs4] [d3 a3 d4 fs4 a4 fs4] [d3 a3 d4 fs4 a4 fs4]>"
const guitarArp = arrange(
  [4, note(introArps)], [8, note(verseArps)], [8, note(verseArps)],
  [2, silence], // the drop: guitar stops, voice alone
  [6, note(v3Arps)], [8, note(refrainArps)], [4, note(introArps)], // outro empties the way it filled
).sound("pluck").gain(.5).room(.35)

// bass — root on 1, fifth on 3: the oom, the guitar covers the pah-pah
const verseBass = "<[d2 ~ a2] [a2 ~ e2] [b2 ~ fs2] [g2 ~ d2] [d2 ~ a2] [g2 ~ d2] [a2 ~ e2] [d2 ~ a2]>"
const v3Bass = "<[b2 ~ fs2] [g2 ~ d2] [d2 ~ a2] [g2 ~ d2] [a2 ~ e2] [d2 ~ a2]>"
const refrainBass = "<[g2 ~ d2] [a2 ~ e2] [d2 ~ a2] [b2 ~ fs2] [g2 ~ d2] [a2 ~ e2] [d2 ~ a2] [d2 ~ a2]>"
const bass = arrange(
  [4, silence], [8, silence], // verse 1 is a duo; the band hasn't arrived yet
  [8, note(verseBass)], [2, silence], [6, note(v3Bass)],
  [8, note(refrainBass)], [4, note("<[d2 ~ a2] [g2 ~ d2] [a2 ~ e2] [d2 ~ ~]>")],
).sound("gm_acoustic_bass").gain(.55).room(.2)

// second guitar — strums on every beat, only from verse 2 on
const strum = chords => chord(chords).anchor("d3").voicing().sound("gm_acoustic_guitar_steel").struct("x x x").gain(.17).room(.4)
const guitarStrum = arrange(
  [4, silence], [8, silence], [8, strum(verseCh)], [2, silence],
  [6, strum("<Bm G D G A D>")], [8, strum(refrainCh)], [4, strum("<D G A D>")],
)

// the voice — triangle, plain and forward; phrases end early, the gap is where the fiddle answers
const verseVoice = "<[fs4 a4 b4] [a4@3] [fs4 e4 d4] [e4@3] [fs4 a4 b4] [a4 fs4 d4] [e4 fs4 e4] [d4@3]>"
const v3Open = "<[d4 fs4 a4] [fs4@3]>" // the confession, quieter and lower
const v3Rest = "<[fs4 e4 d4] [e4@3] [fs4 a4 b4] [a4 fs4 d4] [e4 fs4 e4] [d4@3]>"
const refrainVoice = "<[a4 b4 d5] [d5@3] [b4 a4 gb4] [a4@3] [a4 b4 d5] [e5 d5 ~] [b4 db5 e5] [d5@3]>" // b-flats only: transpose(12) breaks on s/f spellings
const voice = arrange(
  [4, silence], [8, note(verseVoice).gain(.45)], [8, note(verseVoice).gain(.5)],
  [2, note(v3Open).gain(.4)], // alone: the moment the whole file is built around
  [6, note(v3Rest).gain(.5)], [8, note(refrainVoice).gain(.55)],
  [4, note("<[fs4 a4 b4] [a4@3] [e4 fs4 e4] [d4@3]>").gain(.35)],
).sound("triangle").gain(.5).room(.3)

// fiddle — answers only, in the gaps; doubles the refrain with one octave sparkle at the end
const answers = "<[~ ~ ~] [~ ~ ~] [[d5 fs5] a5 ~] [g5@3] [~ ~ ~] [~ ~ ~] [[e5 d5] cs5 ~] [a4@3]>"
const fiddle = arrange(
  [4, silence], [8, silence], [8, note(answers)], [2, silence], [6, silence],
  [8, note(refrainVoice).superimpose(x => x.transpose(12).gain(.2))], // everyone sings, plus the lift
  [4, note("<[~ ~ ~] [~ ~ ~] [~ ~ ~] [d5@3]>")],
).sound("gm_fiddle").gain(.4).room(.35)

// one foot stomp in the last verse and refrain — the percussion ceiling of the genre
const stomp = arrange(
  [4, silence], [8, silence], [8, silence], [2, silence],
  [6, sound("bd ~ ~")], [8, sound("bd ~ ~")], [4, silence],
).gain(.2)

$: guitarArp
$: guitarStrum
$: bass
$: voice
$: fiddle
$: stomp
```
