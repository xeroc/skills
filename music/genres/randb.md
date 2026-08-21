R&B's equivalent moment is **the vamp** — the late section where the harmony settles into a two- or four-chord loop, the drums go half-time, and the melody stops delivering the song and starts testifying. Jazz has the cadenza, pop has the bridge; R&B has the run: the moment the vocalist takes a scale you've heard a thousand times and bends it across the bar line until the room exhales. Everything before the vamp exists to earn it.

## What the vamp actually is

The vamp is a gospel device smuggled into pop: loop a warm progression (IV–V–I–vi is the classic), drop the arrangement down to keys, sub, and pocket drums, and let the melody improvise with increasing freedom — pentatonic lines first, then chromatic runs, then held notes that fight the chord changes. The drums never fill; they open up just slightly. The bass walks more. Each four-bar pass should be more decorated than the last. It's the structural opposite of hip-hop's loop: instead of repeating one bar perfectly forever, you repeat it imperfectly, climbing.

## The layers

- **Warm keys** — the fake Rhodes: `piano` softened with `.lpf(1800)`, a touch of `attack(.02)`, and `.room(.35)`. It carries the 9th chords, voiced mid-register around `eb4`, and comps on the offbeat 8ths.
- **Muted guitar comp** — `pluck` with `.release(.12).cut(1)` playing offbeat-8th chord fragments (`.struct("[~ x] [~ x] [~ x] [~ x]")`), the D'Angelo skank. Quiet, high in the mix's imagination, low in its reality.
- **Sub bass** — `sine` with a long `adsr` sustain, syncopated around the kick. It doesn't walk like soul or pop like funk; it sighs — roots and fifths with slow approach notes.
- **Drums** — half-time: `sd` on beat 3, not 2 and 4. The kick is syncopated (`bd ~ ~ ~ ~ ~ bd ~ …`), hats are quiet dragged 16ths (`.swing(.12)`), a rim ghost on the and-of-4 fills the gap before the snare. The whole kit sounds like it woke up ten minutes ago, in the best way.
- **Lead vocal** — wordless `gm_voice_oohs` carries the melody: restrained in verses, an octave up in choruses, chromatic 16th runs in the vamp. The `.swing(.1)` and a small `delay` are what stop it sounding clinical.
- **Choir pad** — `gm_voice_oohs` on long chords (`.attack(.4).release(1.1).room(.6)`) answering the lead, wide with `.jux(rev)`. Enters at choruses; blooms fully in the vamp.

## Harmony

Everything is 7ths, 9ths, and 11ths; plain triads read as a different genre. Key of E♭:

- **Imaj9–vi9** — E♭maj9 | Cm9: the verse loop, warm and motionless enough to improvise over.
- **I–vi–IV–V dressed up** — E♭maj9 | Cm9 | A♭maj9 | B♭9: the full chorus turn; the V9 stays unaltered — R&B resolves softly.
- **IV–iii–V–vi** — A♭maj9 | Gm7 | B♭9 | Cm9: the lift variant, landing on vi so nothing ever fully closes.
- **The vamp: IV–V–I–vi** — A♭maj9 | B♭9 | E♭maj9 | Cm9: gospel's endless loop, ideal for runs because every chord is a stable landing spot.
- **Bridge: ii–v into IV** — Cm9 | Fm9 → A♭: the one place functional harmony shows its face, right before the vamp dissolves it.

E♭maj9 = E♭–G–B♭–D–F; Cm9 = C–E♭–G–B♭–D; B♭9 = B♭–D–F–A♭–C.

## Rhythm & feel

- Tempo 60–90: slow jams live at 62–72, grooves at 85–90. Past 95 you're writing neo-disco.
- Half-time feel: one backbeat per bar, `sd` on beat 3 (`~ ~ ~ ~ sd ~ ~ ~` in 8ths). The perceived pulse halves and everything breathes.
- Syncopated kick, 16th grid: `bd ~ ~ ~ ~ ~ bd ~ ~ ~ ~ bd ~ ~ ~ ~` — beat 1, the and-of-2, and the a-of-3. Never four-on-the-floor.
- Hats: quiet 16ths at `.swing(.12)` with accents on the 8th offbeats, gain around .3 — felt more than heard.
- The drag: every melodic layer gets a small swing and sits slightly behind. Consistently late is the pocket; randomly late is a mistake.

## Structure

```
intro 4 | verse 16 | chorus 8 | verse 8 | chorus 8 | bridge 4 | vamp 16 | out 4
   2         3         5        4         6          3       7 -> 8      2    (energy 0-10)
```

Intro: keys and sub alone. Verse: voice enters, drums at half. Chorus: choir pad, shaker, the melody up an octave. Bridge strips to keys and a near-solo vocal — the quietest four bars of the song. The vamp then rebuilds from the pocket outward over sixteen bars, each pass more ornate, and the outro is one held note over the final chord.

## Techniques that actually create "R&B"

- **Half-time backbeat** — moving the snare to beat 3 is the genre's single most identifying rhythmic feature; do it first, everything else follows.
- **9ths on everything** — maj9 and m9 voicings (anchored around `eb4`) are the warmth; the 9th is the yearning.
- **Vocal runs as structure** — in the vamp, alternate a sung bar with a run bar (`[[f5 eb5 c5 bb4] ab4 ~ g4 ~]`), each run climbing further; the melody becomes an arc, not a loop.
- **The drag** — `.swing(.1)`–`.12` on keys, voice, and hats so the whole band leans back identically.
- **Call and response** — choir `ooh` chords answer the lead's phrases (`superimpose` an octave-down double at `.gain(.2)` for thickness).
- **Sidechain glue** — `.duckorbit("2:3").duckdepth(.8).duckattack(.16)` on the kick makes the mix exhale around it without audible pumping.
- **Space in the bass** — the sub only moves when the kick doesn't; syncopation between the two, never on top of each other.
- **The strip before the bloom** — the quiet bridge is what makes the vamp's first run land; don't skip the hush.

## Practice approach

- Play the vamp loop (A♭maj9–B♭9–E♭maj9–Cm9) for four minutes straight and improvise; notice when your ear wants decoration and resist it twice before giving in.
- Write one vocal melody, then write three increasingly decorated versions of it — that's your verse/chorus/vamp map.
- Program the kick pattern first and hand-play everything against it; if a layer fights the kick's syncopation, mute it.
- Sing every melodic line you write — oohs or not, if you can't hum the run, it's too fast for the genre.
- Transcribe one D'Angelo-level drum groove's hats alone; the ghost/rim placement is the whole feel.

## Example

```
// ═══ after hours — slow-jam R&B, 72bpm, half-time ═══
// form: intro 4 | verse 16 | chorus 8 | verse 8 | chorus 8 | bridge 4 | vamp 16 | out 4
// energy: 2 3 5 4 6 3 7->8 2 — the vamp is where the runs live
setcpm(72 / 4) // one cycle = one bar of 4/4

// ── keys — the fake Rhodes: piano, filtered warm, 9ths anchored mid-register ──
const keysLoop = chord("<Eb^9 Eb^9 Cm9 Bb9>").anchor("eb4").voicing()
const keysChorus = chord("<Ab^9 Gm7 Bb9 Cm9>").anchor("eb4").voicing()
const keys = arrange(
  [4, keysLoop.gain(.3)],
  [16, keysLoop.gain(.34)],
  [8, keysChorus.gain(.38)],
  [8, keysLoop.gain(.32)],
  [8, keysChorus.gain(.38)],
  [4, chord("<Cm9 Fm9>").anchor("eb4").voicing().gain(.3)], // bridge: ii-v into the hush
  [16, chord("<Ab^9 Bb9 Eb^9 Cm9>").anchor("eb4").voicing().gain(.4)], // the vamp loop
  [4, chord("<Eb^9 ~>").anchor("eb4").voicing().gain(.25)],
).sound("piano").lpf(1800).attack(.02).room(.35).swing(.1)

// ── muted guitar comp — offbeat 8ths, the skank under everything ──
const comp = chord("<Eb^7 Cm9>").anchor("bb4").voicing().struct("[~ x] [~ x] [~ x] [~ x]")
const compC = chord("<Ab^7 Bb9>").anchor("bb4").voicing().struct("[~ x] [~ x] [~ x] [~ x]")
const guitar = arrange(
  [4, silence], [16, comp.gain(.2)], [8, compC.gain(.22)], [8, silence], [8, compC.gain(.22)],
  [4, silence], [16, compC.gain(.24).jux(rev)], [4, silence],
).sound("pluck").release(.12).cut(1).pan(.65)

// ── sub bass — sine, sighs: roots and fifths with slow approaches ──
const bassVerse = note("<[eb1@5 ~ bb1 ~] [eb1@5 ~ ab1 ~]>")
const bassChorus = note("<[ab1@5 ~ eb1 ~] [bb1@5 ~ f1 ~] [eb1@5 ~ bb1 ~] [c2@5 ~ g1 ~]>")
const sub = arrange(
  [4, note("eb1")], [16, bassVerse], [8, bassChorus], [8, bassVerse], [8, bassChorus],
  [4, note("<[c2@5 ~ g1 ~] [f1@5 ~ c2 ~]>")], [16, bassChorus], [4, note("eb1")],
).sound("sine").adsr(".006:.1:.9:.35").gain(.85)

// ── the vocal — oohs: verse restrained, chorus up, vamp = runs that climb ──
const leadVerse = note("<[bb4@3 ~ g4 ab4 bb4 ~ ~ ~] [c5@3 ~ bb4 ab4 g4 ~ f4 ~] [g4@3 ~ f4 eb4 ~ f4 g4 ~] [ab4@5 ~ ~ ~ g4 ~ f4 ~]>")
const leadChorus = note("<[eb5@3 ~ ~ c5 ~ bb4 ~ ~] [ab4@3 ~ bb4 c5 ~ d5 ~ ~] [eb5@3 ~ d5 c5 bb4 ~ ab4 ~] [g4@5 ~ f4 ~ g4 ~ bb4 ~]>")
const leadVamp = note("<[[f5 eb5 c5 bb4] ab4 ~ g4 ~] [g4@3 ~ bb4 ~ ab4 g4 ~ ~] [[bb4 c5 d5 eb5] f5 ~ ~ ~] [eb5 ~ ~ ~ ~ ~ ~ ~] [[g5 f5 eb5 c5] bb4 ~ ab4 ~] [ab4@3 ~ c5 ~ bb4 ab4 ~ ~] [[c5 bb4 ab4 g4] f4 ~ g4 ~] [g4 ~ ~ ~ ~ ~ ~ ~]>")
const lead = arrange(
  [4, silence],
  [16, leadVerse.gain(.4)],
  [8, leadChorus.gain(.46)],
  [8, leadVerse.gain(.4)],
  [8, leadChorus.gain(.46).superimpose(x => x.transpose(-12).gain(.2))], // octave double = the stack
  [4, note("<[ab4@3 ~ g4 ~ f4 ~ eb4 ~] [bb4 ~ ~ ~ ~ ~ ~ ~]>").gain(.35)], // bridge: nearly alone
  [16, leadVamp.gain(.5)], // sing a bar, run a bar, climb for eight bars
  [4, note("<eb5@4 ~ ~ ~ ~ ~ ~ ~>").gain(.35).release(.8)],
).sound("gm_voice_oohs").room(.45).swing(.1).delay(".21:.15:.2")

// ── drums — half-time: sd on 3, syncopated kick, dragged hats, rim ghost on &4 ──
const kick = sound("bd ~ ~ ~ ~ ~ bd ~ ~ ~ ~ bd ~ ~ ~ ~").duckorbit("2:3").duckdepth(.8).duckattack(.16) // the mix breathes around the kick
const snare = sound("~ ~ ~ ~ ~ ~ ~ ~ sd ~ ~ ~ ~ ~ rim ~").gain(.5)
const ghosts = sound("~ ~ rim ~ ~ ~ ~ ~ ~ ~ ~ ~ rim ~ ~ ~").gain(.15)
const hats = sound("hh*16").swing(.12).gain("[.3 .1 .18 .1 .32 .1 .18 .1]*2")
const kitSlow = stack(kick.gain(.8), snare, ghosts, hats)
const kitChorus = stack(kick.gain(.85), snare.gain(.55), ghosts.gain(.18), sound("hh*16").swing(.12).gain(.28), sound("~ ~ ~ ~ ~ ~ ~ ~ cp ~ ~ ~ ~ ~ ~ ~").gain(.22), sound("sh*16").swing(.12).gain(.08))
const fill = stack(kick, sound("~ ~ ~ ~ ~ ~ ~ ~ sd ~ ~ sd sd sd sd sd").gain(.5), hats)
const drums = arrange(
  [4, silence],
  [16, kitSlow],
  [8, kitChorus],
  [8, kitSlow],
  [8, kitChorus],
  [4, stack(sound("bd ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ bd ~ ~ ~ ~").gain(.6), sound("~ ~ ~ ~ ~ ~ ~ ~ rim ~ ~ ~ ~ ~ ~ ~").gain(.3))], // the hush
  [16, cat(kitChorus, kitChorus, kitChorus, fill, kitChorus, kitChorus, kitChorus, fill, kitChorus, kitChorus, kitChorus, fill, kitChorus, kitChorus, kitChorus, fill)],
  [4, sound("~ ~ ~ ~ ~ ~ ~ ~ sd ~ ~ ~ ~ ~ ~ ~").gain(.3)],
)

$: keys
$: guitar
$: sub
$: lead
$: drums
```
