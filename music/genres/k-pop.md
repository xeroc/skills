K-pop's equivalent moment is the killing part — the one or two bars at the top of the chorus engineered to be the most clipped, quoted, and choreographed second of the whole song — followed hard by the dance break, where the track stops singing and starts performing. If jazz builds one long arc toward a cadenza and electro drops, K-pop does neither: it's contrast architecture. A title track is less a song than a chain of hard arrangement switches — rap verse, sung pre-chorus, supersaw hook, electro dance break, strings bridge, modulated final chorus — and its identity lives in the cuts between sections, not inside any one of them. The whole track is arranged backward from the killing part: everything before it exists to make those two bars feel inevitable.

## What the killing part actually is

The killing part is a specific, named thing in K-pop production: the hook-within-the-hook, usually the first bar of the chorus, marked by a vocal riff, a chant, or an instrumental stab that gets its own choreography point and its own fancam zoom. It's short (one to two bars), extremely rhythmic rather than melodic, and engineered for repetition — you should be able to sing it after one hearing. Around it sits the rest of the contrast machine: a rap verse over a sparse dark bed, a sung pre-chorus that starts the engine (four-on-the-floor arrives here), the full-brightness chorus, an instrumental dance break built for the choreography showcase, a bridge that re-darkens (often strings or half-time), and a final chorus lifted up a whole step so the last hook is literally brighter than the first. Every switch lands on a barline, usually every 8 bars, with at most one bar of fill before it. Nothing crossfades; arrangement edits are cuts.

## The layers

- **Kick** — `bd`. Verses: half-time or trap-flavored and sparse (`"[bd ~ ~ ~] [~ ~ bd ~]"` plus a syncopated push), because the rap needs air. Pre-chorus: `bd*4` starts. Hooks: four-on-the-floor with a sidechain pump. Dance break: big-room stabs (`"[bd bd] ~ bd ~"`). `bank("RolandTR909")` for the brighter claps and snaps if you want that polish.
- **Backbeat** — `cp` claps stacked with `sd` in the hook (the classic K-pop double backbeat), dry `sd` alone in verses, `rim` when the bridge thins out. `ht mt lt` tom runs and `cp*8` rolls live in the last bar of every 8 — the transition is a drum fill plus a hard cut, never a fade.
- **Hats** — `hh*16` with a velocity pattern (`gain("[.14 .3]*8")`) for the trap sizzle under rap; `[~ oh]*4` offbeat open hats the moment the hook lifts.
- **Rap bed** — a dry, sparse riff: `gm_electric_guitar_muted` or `pluck`, low register, one or two notes per bar, heavily panned. It answers the rap flow; it never carries harmony on its own.
- **Hook synths** — `supersaw` chords with the filter wide open (`lpf` 2600–3400), short attack, and the killing part itself as a bright `supersaw` lead, often `jux(rev)` for width. `gm_synth_strings_1` carries the bridge and any ballad moment.
- **Bass** — `sawtooth`, filtered to around 900 Hz. Verses: lazy quarter-note roots. Hooks: the 8th-note pump — `ply` on whole-bar roots is the cheapest way to build it. It ducks to the kick.
- **Choir/vocal pads** — `gm_voice_oohs` for the bridge's sung-warmth section and any aah bed under the final chorus.

## Harmony

K-pop harmony is functional pop harmony with two signature moves: the relative-minor/major flip between verse and chorus, and borrowed or modal color landing exactly on an 8-bar boundary. In the worked key (C minor verses / Eb major hook / F major final):

- **Verse (C Aeolian): i – bVI – bIII – bVII** — Cm – Ab – Eb – Bb. Dark loop energy for the rap; every chord diatonic to the relative minor.
- **Pre-chorus: bVI – bVII into the relative major** — Ab – Bb – Cm, then Ab – Bb – Eb. The bVI–bVII–I "Aeolian cadence" is the single most reliable lift into a bright chorus.
- **Hook (Eb major): I – V – vi – IV** — Eb – Bb – Cm – Ab. Deliberately plain; the brightness is the arrangement's job, not the chord's.
- **Bridge (Fm): iv – bVI – bIII – bVII** — Fm – Ab – Eb – Bb. Re-darkening with the subdominant minor before the final lift; borrow the iv from C minor even though the hook never left Eb major.
- **Final hook: same I – V – vi – IV a whole step up** — F – C – Dm – Bb. The modulation is an arrangement event: same shape, same choreography, higher ceiling. Re-voice everything so the top note of the hook sits higher than the first chorus, not just transposed.

The rule underneath all of it: harmonic changes and arrangement switches share boundaries. A borrowed chord that arrives mid-section wastes its surprise; one that arrives with a drum cut feels like the song changed costumes.

## Rhythm & feel

- **Tempo** — 100–130, sweet spot 118–128 for a dance title track, 100–110 for a hip-hop-leaning B-side.
- **Verse skeleton** — `"[bd ~ ~ ~] [~ ~ bd ~]"` with one syncopated push per 4 bars (`"[~ bd ~ bd]"` tail), `hh*16` velocity-shaped on top. The pocket is straight but the kick is lazy; syncopation comes from hats and the rap, not the kick.
- **Hook skeleton** — `bd*4`, `[~ oh]*4` open hats, claps+snare stacked on 2 and 4. The pump: `duckorbit`/`duckdepth`/`duckattack` chained on the kick pattern, with pads and bass dipping on every beat.
- **Fills** — the last bar of every 8 belongs to the transition: `[ht mt lt ht]`, `cp*8`, or a 16th hat riser (`hh*16` with `hpf`). One bar, no more — then the cut.
- **Feel** — no swing. The humanity is in velocity patterns, section contrast, and the occasional deliberately early push into a new section, not in grid feel.

## Structure

```
intro 4 | v1 rap 8 | pre 8 | hook 8 | post-hook chant 4 | v2 rap 8 | pre 8 | hook 8 |
dance break 8 | bridge 8 | final hook (up a whole step) 8 | outro 4
```

The post-hook chant is optional but common — a 4-bar vocal or instrumental repeat of the killing part at reduced energy, a exhale before verse 2. The dance break sits after the second hook or after the bridge; either way it's the one section with no lead vocal, built on percussion and synth stabs. Energy graph (each character ~4 bars):

```
intro __  v1 ___  pre _____  HOOK █████  post ██  v2 ____  hook2 █████  BREAK ██████  bridge __↓  final ██████  outro _
```

Note the shape: two big peaks, a deliberate valley, then a final peak higher than the first. That final-louder contour is why the modulation exists.

## Techniques that actually create "k-pop"

- **The killing part** — design the first bar of the chorus before anything else: short, rhythmic, repeatable, with a gap in it (space inside the hook is what makes it chantable). Everything upstream is built to frame it.
- **Hard arrangement switches every 8 bars** — treat each section boundary as a hard cut in a video editor: drums change pattern, bass changes register, timbre family changes (muted guitar → supersaw). Never crossfade between sections.
- **Rap/sung contrast** — the verse is a different genre from the chorus on purpose: sparse dark bed + flow versus bright wall + melody. If your verse and chorus use the same sound palette, it isn't K-pop yet.
- **Relative-major flip** — write the verse in the relative minor and the chorus in the major; arrive via bVI–bVII. Cheapest possible "the lights came on" effect that isn't a key change.
- **Borrowed chords and modal shifts as section markers** — iv, bVI, bVII from the parallel/minor side, and the Fm-style dark bridge, each landing on a section boundary.
- **The final-chorus modulation up a step** — same hook, +2 semitones, often with the top voicing pushed even higher and the drums at maximum. The song's last trick and its biggest.
- **Sidechain pump in hooks** — pads and bass audibly dipping on each kick turns a static four-on-the-floor into a breathing, current-pop feel.
- **Dance break** — instrumental, percussion-forward, synth stabs (`sawtooth` short decays), tom figures; write it as a place for choreography, i.e. with strong, regular rhythmic markers.
- **Transition fill discipline** — exactly one bar of fill (toms, clap roll, riser, or a reversed cymbal `rd` with negative `speed`) before every switch. More than that and the cut stops feeling hard.

## Practice approach

- Take three title tracks from different groups and eras and mark every arrangement switch with a bar number — you'll find the 8-bar grid and the hard-cut discipline immediately.
- Write the killing part first, at 124 bpm, as a two-bar loop. If it doesn't survive ten repeats with nothing else playing, rewrite it before building anything else.
- Derive the verse riff from the hook's rhythm (same skeleton, muted, low, sparse) so the sections feel related by DNA even while contrasted in color.
- Program one full arrangement with `arrange()` where every section boundary changes at least three things at once (drum pattern, bass register, timbre) — train the cut, not the blend.
- A/B your hook against the final modulated hook: the last one must feel brighter, not just higher. If it doesn't, re-voice rather than re-transpose.

## Example

```
// ═══ neon district — k-pop title track, 124 bpm ═══
// identity = contrast: dark C-minor rap verses against a bright Eb-major supersaw hook, an electro dance break,
// an Fm strings bridge, and a final hook lifted a whole step to F. switches land on barlines — arrangements cut.
// form: intro 4 | v1 8 | pre 8 | hook 8 | v2 8 | hook2 8 | break 8 | bridge 8 | final 8 | outro 4
setcpm(124 / 4) // one cycle = one bar of 4/4
// ── kick: half-time under the rap, four-on-floor from the pre, big-room stabs in the break ──
const vBed = sound("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ bd ~ bd]") // verse bed: sparse, air for the flow
const pump = sound("bd*4").duckorbit("2:3").duckdepth(.8).duckattack(.16) // hook: sidechain pump engaged
const kick = arrange(
  [4, sound("[bd ~ ~ ~] [~ ~ bd ~]")],
  [8, vBed], [8, sound("bd*4")], // v1, then the pre starts the engine
  [8, pump], [8, vBed], // hook, v2
  [8, pump], [8, sound("[bd bd] ~ bd ~ [bd bd] ~ bd ~")], // hook2, then the break's festival stabs
  [8, sound("~ bd ~ bd ~ bd ~ bd")], // bridge: offbeat pulse — the kick becomes tension
  [8, pump], [4, sound("bd ~ ~ ~ ~ ~ ~ ~")], // final hook, outro
)

// ── drums: backbeat stack + the last-bar fills that punt each section into the next ──
const vKit = stack(
  sound("hh*16").gain("[.14 .3]*8").hpf(6000), // verse sizzle, loud on the ands
  sound("~ sd ~ sd").gain(.46).room(.2), // dry snap snare
  sound("<~!7 [ht mt lt ht]>").gain(.4),
)
const hKit = stack(
  sound("[~ oh]*4").gain(.32), sound("hh*16").gain(.2), // offbeat open hats = the lift
  sound("~ cp ~ cp").gain(.58), sound("~ sd ~ sd").gain(.38), // clap + snare stacked — the k-pop backbeat
  sound("<~!7 cp!4>").gain(.5),
)
const drums = arrange(
  [4, stack(sound("hh*8").gain(.18), sound("~ cp ~ cp").gain(.4))], [8, vKit],
  [8, stack(sound("[~ oh]*4").gain(.3), sound("~ cp ~ cp").gain(.52), sound("<~!7 [ht mt lt ht]>").gain(.44))], [8, hKit],
  [8, vKit], [8, hKit], // v2 + hook2
  [8, stack(sound("hh*8").gain(.26), sound("~ cp ~ cp").gain(.6), sound("[~ ~ sd ~] [sd ~ sd sd]").gain(.45), sound("<[ht mt lt ht] ~!6 [cp*8]>").gain(.5))], // break opens with a fill, closes with a roll
  [8, stack(sound("hh*8").gain(.2), sound("~ rim ~ rim").gain(.3), sound("<~!7 [hh*16]>").gain(.3).hpf(3000))], // bridge + riser out of it
  [8, hKit], [4, stack(sound("hh*8").gain(.14), sound("~ cp ~ cp").gain(.4))], // final + outro
)

// ── chords: the key plan IS the arrangement — Cm verses, Eb hook, Fm bridge, F final ──
const pl = c => c.anchor("eb4").voicing().sound("pluck").decay(.2)
const sw = (c, a = "eb4") => c.anchor(a).voicing().sound("supersaw").attack(.02).release(.25).lpf(3200)
const st = (c, a) => c.anchor(a).voicing().sound("gm_synth_strings_1").attack(.5).release(1.2).gain(.22).room(.7)
const pads = arrange(
  [4, st(chord("<Cm Cm Ab Bb>"), "eb4").attack(.4).gain(.2)],
  [8, pl(chord("<Cm Ab Eb Bb>")).gain(.3)], [8, pl(chord("<Ab Bb Cm Cm Ab Bb Eb Eb>")).gain(.34)], // v1, pre
  [8, sw(chord("<Eb Bb Cm Ab>")).gain(.24)], [8, pl(chord("<Cm Ab Eb Bb>")).gain(.3)], // hook, v2
  [8, sw(chord("<Eb Bb Cm Ab>")).gain(.24)], [8, chord("<Cm Cm Ab Bb>").anchor("eb4").voicing().sound("sawtooth").decay(.12).gain(.2)], // hook2, break stabs
  [8, st(chord("<Fm Ab Eb Bb Fm Ab Bb Bb>"), "f4").gain(.24)], // bridge
  [8, sw(chord("<F C Dm Bb>"), "f4").lpf(3400).gain(.26)], // the lift: same shape, +2
  [4, st(chord("<F Dm Bb F>"), "f4").attack(.6).release(1.5).gain(.2)],
)

// ── bass: lazy quarter roots under the rap, 8th-note pump under the hooks (ply = the pump) ──
const bass = arrange(
  [4, note("<c1 ~ ~ c1 ~ ~ bb0 ~>")],
  [8, note("<c1 ab0 eb1 bb0>").ply(8)], [8, note("<ab1 bb1 c2 c2 ab1 bb1 eb1 eb1>").ply(4)], // v1, pre
  [8, note("<eb1 bb1 c2 ab1>").ply(16)], [8, note("<c1 ab0 eb1 bb0>").ply(8)], // hook, v2
  [8, note("<eb1 bb1 c2 ab1>").ply(16)], [8, note("<c1 c1 ab1 bb1>").ply(16)], // hook2, break
  [8, note("<f1 ab1 eb1 bb1 f1 ab1 bb1 bb1>").ply(2)], // bridge: near-whole notes, tension
  [8, note("<f1 c2 d2 bb1>").ply(16)], [4, note("<f1 ~ ~ bb0 ~ ~ f1 ~>")], // final, outro
).sound("sawtooth").decay(.22).sustain(0).gain(.6).lpf(900)

// ── lead: muted-guitar riff answers the rap; the supersaw hook IS the killing part ──
const rapRiff = note("<[c4 ~ eb4 ~] [~ ~ g3 ~] [bb3 ~ ~ ~] [~ c4 eb4 g4]>")
const hookA = note("<[[eb5 eb5] ~ ~ eb5] [~ bb4 ~ eb5] [g4 ~ ab4 ~] [~ ~ bb4 ~]>")
const hookB = note("<[[eb5 eb5] ~ ~ eb5] [~ bb4 ~ eb5] [g4 ~ ab4 ~] [c5 ~ bb4 ~]>") // last phrase climbs
const lead = arrange(
  [4, silence], [8, rapRiff.sound("gm_electric_guitar_muted").gain(.36).pan(.3)],
  [8, note("<ab4@2 ~ bb4 c5 ~ ~ bb4 c5>").sound("gm_electric_guitar_muted").gain(.3)], [8, hookA.sound("supersaw").lpf(2600).gain(.42).jux(rev)], // pre, HOOK
  [8, rapRiff.sound("gm_electric_guitar_muted").gain(.36).pan(.3)], [8, hookB.sound("supersaw").lpf(2600).gain(.42).jux(rev)], // v2, hook2
  [8, note("<[c5 ~ c5 ~] [~ eb5 ~ c5] [~ ~ bb4 ~] [~ c5 ~ ~]>").sound("pluck").decay(.15).gain(.4)], // instrumental break hook
  [8, note("<f4@2 ab4 bb4@2 g4 f4@2 ab4 c5@2 bb4>").sound("gm_voice_oohs").attack(.3).release(.8).gain(.3).room(.7)], // the choir takes the bridge
  [8, hookA.add(2).sound("supersaw").lpf(2800).gain(.44).jux(rev)], // same hook, up a whole step — the lift
  [4, note("<f5 ~ ~ ~>").sound("supersaw").lpf(2600).release(.8).gain(.35)],
)

$: kick
$: drums
$: pads
$: bass
$: lead
```
