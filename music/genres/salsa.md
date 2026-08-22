Salsa's equivalent moment is **the mambo** — not the 1950s big-band dance of the same name (that's where the word drifted in from), but the shout chorus inside the arrangement: the bars where the singer steps back, the horn section stands up, and a short, nasty riff gets hammered over the full montuno while the cowbell takes over from the cáscara and the dancers drop partner-work for shines. It is electro's drop and jazz's cadenza compressed into eight bars — harmonic simplicity at maximum rhythmic density — and it only lands because everything before it was patient.

## What the mambo actually is

A full salsa arrangement moves from the diablo (the horn intro) through the cuerpo (verse) into the coro — call-and-response between a fixed chorus figure and an improvised pregón (lead line, sung or played). The mambo lands after the coro has settled in, or between solos: the horns play a moña, a two- or four-bar riff, in unison first, then restated with inner voices layered on top, repeating as long as the arranger wants the peak to hold. Nothing harmonic happens — one or two chords at most — and the piano montuno and bass tumbao keep doing exactly what they were doing. The lift is orchestration, not chord changes.

The riff itself is built from chord tones, syncopated against the clave (figures cluster around the "and of 2" and beat 4), and repeated with discipline — the repetition is the point, because the rhythm section has been implying this density for minutes and the horns finally state it. A piano mambo (the montuno doubling itself in octaves, louder and busier) does the same job when there's no horn section. If your mambo doesn't make people move more than the coro did, the riff — not the mix — is the problem.

## The layers

- **Clave** — `rim` as the woodblock, playing the two-bar 3-2 son clave `<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>`. This is the timeline every other part answers to; when a layer's rhythm agrees with the clave it feels right, and when it fights the clave it feels wrong even to listeners who can't name why.
- **Campana** — `cb` on the quarters (`cb*4`), the cowbell that rides on top of coros and doubles down in mambos. It is the cheapest energy dial in the idiom: add the bell and the band gets bigger without getting louder.
- **Congas** — the marcha, two bars of interlocked slaps and open tones: `<[lt ~ ht mt ~ ht lt ht] [lt ~ ht mt ~ ht ht ht]>`, with `lt` as the low tumba, `mt` the conga, `ht` the slap. `conga(3,8)` on top gives the rolling three-against-eight accents a good conguero sprinkles over the basic groove.
- **Timbales** — `rd` as the cáscara, the shell/ride pattern `rd ~ ~ rd ~ ~ rd ~ rd ~ ~ rd ~ ~ rd ~` (sixteenths on 1, 1a, 2&, 3, 3a, 4& — the African "standard pattern" the whole Caribbean inherited). `sd` and `oh` are the fills, bell accents, and crash markers at section boundaries.
- **Maracas** — `sh*8`, constant eighths with a velocity shape like `[.45 .22 .3 .22 .4 .22 .3 .26]` so the clave strokes pop out of the stream instead of a flat hiss.
- **Piano montuno** — the `piano` sample. Repeated octave dyads and guide-tone figures locked to the clave — one rhythmic cell, re-pitched per chord, not composed lines. For block stabs, `chord("<Cm7 Fm7 G7>").anchor("g4").voicing()` in the right register is the fast path.
- **Bass tumbao** — `gm_acoustic_bass`. One or two notes a bar: root on beat 2, the ponche near the barline, and beat 1 left empty — the silence on the downbeat is what makes the anticipation on the far side of it swing.
- **Horns** — `gm_trumpet` stating the moña, `gm_tenor_sax` doubling an octave down for weight. Unison on the first pass; if the mambo repeats, let the tenor drop to a harmony line.
- **Coro** — `gm_voice_oohs` as the chorus singing its two-bar response, with a `gm_trumpet` pregón improvising into the gaps — the call-and-response that carries everything between the verse and the mambo.

## Sample kit

- **Congas — the real thing** — VCSL `conga` replaces the tom simulation, variants grouped by drum: `:0–:9` conga (mid), `:10–:19` quinto (high), `:20+` tumba (low); probe adjacent indices for slap vs open strokes and write the marcha as `<[conga:20 ~ conga:10 conga:4 …]>`. `bongo` sits on top if the arrangement wants it. Tom-based `lt/mt/ht` marcha is the verified fallback.
- **Clave & bells** — `clave:0` is a real wood clave (upgrade over `rim`); `cowbell` for campana (or default `cb`); `agogo` and `guiro` for extra Latin percussion voices.
- **Timbales** — no dedicated sample: `rd` cáscara with `sd`/`oh` fills remains the idiom.
- **Montuno** — `piano`, or `steinway` for a real grand; octave dyads + guide tones as in the layers.
- **Bass** — `gm_acoustic_bass` tumbao.
- **Horns** — `gm_trumpet` + `gm_tenor_sax` (the moña stack); `gm_brass_section` when the section speaks as one body.
- No pack needed — the preloaded tiers cover salsa. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Salsa harmony is functional but unhurried — chord changes every one or two bars, with the tumbao anticipating each new root on the "and of 4". Work a minor key (C minor below); flip to the parallel major only when a coro goes bright.

- **ii–V–i in minor** — Dm7b5 – G7b9 – Cm7 (C minor: ii°7 – V7b9 – i) — the spine of salsa dura verses, descargas, and anything that wants to feel like it's working toward something. The b9 on the V is not optional flavor; it is the minor-mode sound.
- **i–iv–V7 montuno vamp** — Cm7 – Fm7 – G7, two bars each — the basic coro/montuno treadmill. Hold the V open at the end of the cycle so it pulls back around to i instead of resolving.
- **i – bVI – V7 · iv – V7 (the mambo lift)** — Cm – Ab – G7 – Fm – G7 — the bVI (Ab major) is the color chord; arriving on the flat side before the V7 gives mambos their sudden width.
- **Parallel-major son vamp** — C – F – G – F (I–IV–V–IV) — when a coro turns bright, this is the loop, straight out of son montuno; the same tumbao and montuno cell work over it unchanged.

## Rhythm & feel

180–200 BPM — salsa dura lives at the top; write `setcpm(190/4)` and feel it in cut time (the music breathes in two, subdivides in four). Everything is straight: no swing anywhere, the groove is the grid plus the clave. The skeletons:

- **Clave son 3-2** (two bars of 8ths) — `[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]` — the 3-side then the 2-side; the whole band's reference frame.
- **Tumbao** (one bar of 8ths) — `~ ~ c2 ~ ~ ~ c2 ~` — root on 2, ponche on 4; beat 1 stays empty so the downbeat is implied, not stated.
- **Tumbao with anticipation** — `~ ~ c2 ~ ~ ~ ~ c2` — the 4& sneaks the next chord's root in early; use it on chord-change bars.
- **Conga marcha** (two bars of 8ths) — `[lt ~ ht mt ~ ht lt ht] [lt ~ ht mt ~ ht ht ht]`.
- **Cáscara** (one bar of 16ths) — `rd ~ ~ rd ~ ~ rd ~ rd ~ ~ rd ~ ~ rd ~`.
- **Montuno cell** (one bar of 8ths) — `[dyad] ~ ~ [dyad] ~ ~ [dyad] [pickup]` — hits on 1, 2&, 4, and the 4& pickup.

Feel devices: accents shadow the clave no matter what pattern they're in; the "and of 2" is the strongest weak beat in the music; the bass never states beat 1 (the downbeat is implied by everything pointing at it); and the cáscara and the clave are in permanent, productive disagreement — that friction is the engine.

## Structure

A típico salsa dura arrangement runs `diablo 4 → cuerpo 8–16 → coro/pregón 8–16 → mambo 8 → solo 8–16 → mambo 8 → coda 4` with energy `7 · 5–6 · 7 · 9 · 6–8 · 9–10 · 8`.

The verse is the calm, the coro is the slow climb, the mambo is the summit — and you can re-summit after every solo because the montuno never stopped. Every section count is even so the two-bar clave never flips; a one-bar section in salsa is an arrangement bug.

## Techniques that actually create "salsa"

- **Clave alignment** — every rhythm in the band either states, implies, or decorates the clave. Before adding a layer, check it against the two-bar pattern; a figure whose accents land anti-clave makes the whole groove queasy.
- **The tumbao anticipation** — the bass plays the next chord's root before the barline and then rests on 1. This single displacement is most of the genre's forward lean; without it you have a pop bassline in a salsa costume.
- **The montuno cell** — piano figures are one syncopated cell re-pitched per chord, not through-composed lines. Octave dyads (root or 5th plus its octave) keep them ringing and loud through a full band.
- **The moña stack** — state the horn riff in unison, then on the repeat have the tenor drop to an octave or harmony below. Two passes of the same riff with added weight beats a new riff every two bars.
- **Coro–pregón call and response** — a fixed two-bar chorus figure, improvised fills in the holes. The fixed part is what the audience sings; the holes are where the music breathes.
- **Campana as an energy dial** — cáscara (quieter, busier) for cuerpos, cowbell quarters for coros and mambos. Swapping them is a section change you can hear from the street.
- **Orchestral dynamics, not gain dynamics** — sections get bigger by adding layers, not by turning up. Play your arrangement at flat gains and listen for whether the mambo still peaks.
- **The break/cue** — one or two bars where the whole rhythm section hits a written figure together (even just `[bd sd ~ sd]` quarters) before the groove resumes. Use at section seams, sparingly.

## Practice approach

- Loop the clave alone at 190 BPM and clap the cáscara, tumbao, and montuno cell against it until each one stops feeling like counting — they have to be reflexes before you write a note.
- Learn one real moña at the keyboard — "Oye Como Va" is a four-note economy study in montuno, Eddie Palmieri's "Azúcar Pa' Tí" shows how busy is too busy.
- Transcribe the coro/pregón exchange on Willie Colón & Rubén Blades' "Pedro Navaja" — seven minutes of arrangement patience before the payoff.
- Write an 8-bar ii–V–i in C minor and comp it three ways: block chords, montuno cell, montuno cell plus block stabs on the 2-side. Feel which one makes the progression actually move.
- Record your tumbao with and without the beat-1 bass note. Once you hear the version without, you can't unhear it.

## Example

```
// ═══ descarga en do menor — salsa dura, 190 bpm ═══
// form: diablo 4 | cuerpo 8 | coro 8 | mambo 8 | coda 4
// energy:  7         6         7        9        8
// the clave is two bars long, so every section keeps an even bar count — never flip it
setcpm(190 / 4) // one cycle = one 4/4 bar

// ── clave son 3-2: the timeline everything else answers to ──
const clave = s("<[rim ~ ~ rim ~ ~ rim ~] [~ ~ rim ~ rim ~ ~ ~]>").gain(.45)

// ── cáscara (timbale shell on the ride), 1-bar 16th loop — hits 1, 1a, 2&, 3, 3a, 4& ──
const cascara = s("rd ~ ~ rd ~ ~ rd ~ rd ~ ~ rd ~ ~ rd ~").gain(.2).room(.2)

// ── campana: cowbell quarters — the cheapest energy dial in the band ──
const campana = s("cb*4").gain(.3)

// ── congas: two-bar marcha (lt = tumba, mt = conga, ht = slap) + rolling accents ──
const congas = s("<[lt ~ ht mt ~ ht lt ht] [lt ~ ht mt ~ ht ht ht]>").gain(.55)
const roll = s("conga(3,8)").gain(.28).pan(.7)

// ── maracas: constant 8ths, shaped so the clave strokes pop ──
const maracas = s("sh*8").gain("[.45 .22 .3 .22 .4 .22 .3 .26]")

const perc = arrange(
  [4, stack(clave, maracas, congas, roll, campana)],                    // diablo: guns out
  [8, stack(clave, maracas, congas, roll, cascara)],                     // cuerpo: shell instead of bell
  [8, stack(clave, maracas, congas, roll, cascara, campana.gain(.2))],   // coro: bell sneaks in
  [8, stack(clave, maracas, congas, roll, campana.gain(.38), s("oh ~ ~ ~ oh ~ ~ ~").gain(.3))], // mambo!
  [4, stack(clave, maracas, congas, s("<[bd sd ~ sd] [bd sd sd sd]>").bank("RolandTR707").gain(.6))], // coda breaks
)

// ── tumbao: root on 2, ponche before the barline, beat 1 never plays ──
// cuerpo: Dm7b5 G7 Cm Cm (x2) | coro: Cm x4 then Ab to G7 | mambo: Cm Cm Ab G7 | Fm Fm G7 G7
const tumbao = arrange(
  [4, note("<[~ ~ d2 ~ ~ ~ d2 ~] [~ ~ d2 ~ ~ ~ ~ g1] [~ ~ g1 ~ ~ ~ g1 ~] [~ ~ g1 ~ ~ ~ ~ c2]>")],
  [8, note("<[~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ ~ c2] [~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ ~ c2]>")],
  [8, note("<[~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ ~ c2] [~ ~ ab1 ~ ~ ~ ab1 ~] [~ ~ ab1 ~ ~ ~ ~ g1] [~ ~ g1 ~ ~ ~ g1 ~] [~ ~ g1 ~ ~ ~ ~ c2]>")],
  [8, note("<[~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ ~ ab1] [~ ~ ab1 ~ ~ ~ ab1 ~] [~ ~ ab1 ~ ~ ~ ~ g1] [~ ~ f2 ~ ~ ~ f2 ~] [~ ~ f2 ~ ~ ~ ~ g1] [~ ~ g1 ~ ~ ~ g1 ~] [~ ~ g1 ~ ~ ~ ~ c2]>")],
  [4, note("<[~ ~ c2 ~ ~ ~ c2 ~] [~ ~ c2 ~ ~ ~ ~ b1] [c2@6 ~ ~ ~ ~ ~ ~ ~] [~ ~ ~ ~ ~ ~ ~ ~]>")],
).sound("gm_acoustic_bass").gain(.9).room(.12)

// ── piano montuno: one cell per bar — dyad on 1, 2&, 4, pickup on 4& — re-pitched per chord ──
const cuerpoFigs = note("<[[d4,d5] ~ ~ [f4,f5] ~ ~ [c5,f5] [g4,b4]] [[g4,g5] ~ ~ [b4,d5] ~ ~ [f4,f5] [c4,e4]] [[c4,c5] ~ ~ [eb4,eb5] ~ ~ [g4,g5] [c4,c5]] [[c4,c5] ~ ~ [eb4,eb5] ~ ~ [bb4,g4] [d4,f4]] [[d4,d5] ~ ~ [f4,f5] ~ ~ [c5,f5] [g4,b4]] [[g4,g5] ~ ~ [b4,d5] ~ ~ [f4,f5] [c4,e4]] [[c4,c5] ~ ~ [eb4,eb5] ~ ~ [g4,g5] [c4,c5]] [[c4,c5] ~ ~ [eb4,eb5] ~ ~ [g4,g5] [g4,b4]]>")
const mamboFigs = note("<[[c4,c5] ~ ~ [eb4,eb5] ~ ~ [g4,g5] [c4,c5]] [[c4,c5] ~ ~ [eb4,eb5] ~ ~ [g4,g5] [ab4,c5]] [[ab3,ab4] ~ ~ [c4,c5] ~ ~ [eb4,eb5] [eb4,f4]] [[ab3,ab4] ~ ~ [c4,c5] ~ ~ [eb4,eb5] [g4,b4]] [[f3,f4] ~ ~ [ab3,ab4] ~ ~ [c4,f4] [c4,f4]] [[f3,f4] ~ ~ [ab3,ab4] ~ ~ [c4,f4] [g4,b4]] [[g3,g4] ~ ~ [b3,d4] ~ ~ [f4,g4] [f4,g4]] [[g3,g4] ~ ~ [b3,d4] ~ ~ [f4,g4] [c4,e4]]>")

const piano = arrange(
  [4, chord("<Cm Cm Fm G7>").anchor("g4").voicing().struct("x ~ ~ x ~ ~ x ~")],
  [8, cuerpoFigs],
  [8, chord("<Cm7 Cm7 Cm7 Cm7 Ab Ab G7 G7>").anchor("g4").voicing().struct("x ~ ~ x ~ ~ x x")],
  [8, mamboFigs],
  [4, note("<[~ ~ [c4,g4,eb5] ~ ~ ~ [bb4,c5] ~] [[c4,g4,c5]@6 ~ ~ ~ ~ ~ ~ ~] [~ ~ ~ ~ ~ ~ ~ ~] [~ ~ ~ ~ ~ ~ ~ ~]>")],
).sound("piano").gain(.5).room(.25)

// ── horns: trumpet states, tenor doubles an octave down — the mambo is their moment ──
const riffDiablo = note("<[[eb5 g5] ~ ~ [eb5 g5] ~ ~ [c5 eb5] ~] [f5 ~ eb5 ~ c5 ~ ~ ~] [g5 ~ ~ f5 ~ eb5 ~ ~] [c5 ~ ~ ~ ~ ~ ~ ~]>")
const cabeza = note("<[c5 ~ ~ eb5 ~ ~ g5 ~] [ab5 ~ g5 ~ ~ ~ f5 ~] [eb5 ~ ~ c5 ~ ~ eb5 ~] [d5 ~ ~ ~ ~ ~ ~ ~]>")
const pregon = note("<[~ ~ ~ ~ ~ ~ ~ ~] [~ ~ ab5 g5 ~ eb5 ~ ~] [~ ~ ~ ~ ~ ~ ~ ~] [~ ~ g5 ~ f5 ~ eb5 ~]>")
const riffMambo = note("<[c5 c5 ~ [c5,g5] ~ eb5 ~ ~] [f5 ~ eb5 ~ c5 ~ bb4 ~] [ab4 ~ ~ c5 ~ ~ eb5 ~] [g5 ~ f5 ~ eb5 ~ ~ ~]>")
const riffFinal = note("<[g5 f5 ~ eb5 ~ d5 ~ ~] [eb5 ~ ~ ~ ~ ~ ~ ~]>")

const trumpet = arrange(
  [4, riffDiablo],
  [8, cabeza],
  [8, pregon],      // pregón answers the coro
  [8, riffMambo],
  [4, riffFinal],
).sound("gm_trumpet").gain(.5).room(.3)

const tenor = arrange(
  [4, riffDiablo.transpose(-12)],
  [8, silence],               // cuerpo stays single-horn: save the weight
  [8, silence],
  [8, riffMambo.transpose(-12)],    // the moña stack: tenor drops the octave
  [4, riffFinal.transpose(-12)],
).sound("gm_tenor_sax").gain(.4).room(.3).pan(.6)

const coro = arrange(
  [4, silence],
  [8, silence],
  [8, note("<[g4 c5 ~ ~ eb5 ~ ~ ~] [c5 ~ ~ ~ g4 ~ ~ ~] [eb4 ab4 ~ ~ c5 ~ ~ ~] [d4 ~ ~ ~ ~ ~ ~ ~]>")],
  [8, silence],               // mambo: the voices yield to the horns
  [4, note("<[g4 c5 ~ ~ eb5 ~ ~ ~] [[c4,g4] ~ ~ ~ ~ ~ ~ ~]>")],
).sound("gm_voice_oohs").gain(.4).room(.5).pan(.35)

$: perc
$: tumbao
$: piano
$: trumpet
$: tenor
$: coro
```
