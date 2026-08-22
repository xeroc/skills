Flamenco's equivalent moment is **the remate** — the closing of the compás: the last few beats of the twelve-count cycle where a falseta or a verse resolves, the rasgueado bursts open, the palmas hit their accents together, and everything converges on count 12 like water finding a drain. It is flamenco's drop, cadenza, and downbeat all at once, and it repeats every twelve beats — which is why the music can sustain such ferocity: the climax is structural, not sectional.

## What the remate actually is

Flamenco is organized by the compás, a repeating cycle of twelve counts (soleá, bulerías, alegrías all share it) with accents on 12, 3, 6, 8, and 10 — counted from 12, so the cycle starts on its own strongest accent. Guitar falsetas (melodic variations), sung verses, and dance steps are all phrases threaded through this cycle, and each one ends by landing on the accent pattern — a descending run closing on 10, a chord burst swallowing 8-through-12, a held breath on 11 resolving into 12. That convergence is the remate, and everyone in the room knows where it's going: palmas (hand-claps) reinforce the accents, the cajón pushes, and on a great remate the audience shouts into count 12 with it.

The twelve-beat cycle changes how you compose: a phrase isn't "four bars," it's "one compás" or "half a compás," and harmonic rhythm maps onto the counts — in a soleá, Am owns 12-through-2, G takes 3-through-5, F takes 6-through-7, and E takes 8-through-11, so the Andalusian cadence and the accent pattern are the same object. In strudel, make one cycle equal one full compás (`setcpm(counts_per_minute / 12)`) and write every layer as twelve-beat patterns — the accent skeleton `"cp ~ ~ cp ~ ~ cp ~ cp ~ cp ~"` is the genre's clave.

## The layers

- **Palmas** — `cp` on the accent skeleton `"cp ~ ~ cp ~ ~ cp ~ cp ~ cp ~"` (12, 3, 6, 8, 10). Real palmas come in corps: layer a second `cp` with `.off(1/48, x => x.gain(.3).pan(.75))` for the second pair of hands arriving a hair late — the slight spread is what makes claps read as people instead of a metronome.
- **Cajón** — `bd` for the deep tones (counts 12 and 6) and `sd` for the slaps clustered around the 8–10 tail, escalating during escobilla (dance/footwork) sections to near-continuous slaps.
- **Guitar — rasgueado** — `gm_acoustic_guitar_nylon`. Chord bursts written as nested brackets: `[[a3,c4,e4] [a3,c4,e4] [a3,c4,e4]]` is the chord strummed three times inside one count (a triplet flutter) — the outer bracket keeps the burst inside its count instead of stretching the grid. Short decay keeps them percussive; this is the engine of the comp.
- **Guitar — thumb** — the same instrument walking the chord roots on the accents: `note("a2 ~ ~ g2 ~ ~ f2 ~ e2 ~ e2 ~")`. The thumb states the harmony so the rasgueado can be pure rhythm.
- **Guitar — falsetas** — picado (picked single-note) runs in E phrygian: `note("[e4,a4] ~ b4 ~ c5 b4 a4 ~ g4 ~ f4 ~")`. Double-stops of a fourth, descending lines that close on an accent — these are the "verses" of the guitar.
- **Cante** — `gm_voice_oohs` for the sung line: spare, wailing phrases in the phrygian scale that dwell on one or two notes and resolve into the remate. Real cante is the lead; treat this lane as the melody and give it the top of the mix.
- **Jaleo accents** — occasional `oh` or `rim` hits as the shouts and encouragement that pepper a performance — sparse, unexpected, panned off-center.

## Sample kit

- **Cajón — the real thing** — VCSL `cajon`: two strokes (`hit1`/`hit2`) recorded at dynamics pp→fff with round-robins; probe `:k` indices — soft ones for comping, the hard ones land remates. The `bd`/`sd` simulation is the verified fallback.
- **Palmas** — `cp` states the skeleton; VCSL `clap` (4 human round-robins) is the corps layer — use it for the `.off(1/48, …)` second pair of hands, where a machine clap would read as flange.
- **Guitar** — `gm_acoustic_guitar_nylon` for rasgueado percussiveness; `gm_acoustic_guitar_nylon` for falsetas and thumb lines when the piece wants warmth over attack.
- **Cante** — `gm_voice_oohs`; keep it spare and top-of-mix.
- **Jaleo** — `oh`/`rim` shouts; a quietly doubled `clave` (VCSL) can mark counts without adding drum-machine flavor. No castanets exist in any preloaded set — don't reach for them.
- No pack covers real flamenco (palmas secas, true rasgueado) — the preloaded tiers are the honest palette. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

The mode is E phrygian (e, f, g, a, b, c, d) — the b2 (f natural against e) is the entire flavor. But the chords are not modal jazz voicings; they're bare triads, and the tonic is a MAJOR chord on the phrygian degree. Two positions cover most of the repertoire:

- **Andalusian cadence, por medio** — Am – G – F – E (in A minor: iv – bIII – bII – I) — the spine of soleá, bulerías, and alegrías. Am and G trade the front of the compás, F–E is the cadential crux that lands across counts 8–12.
- **Andalusian cadence, por arriba** — Em – D – C – B — the same shape up a fourth; B major functions exactly like E does por medio.
- **Phrygian tonic vamp** — E – F – E (i – bII – i) — the two-chord rub at maximum concentration; the F never becomes a dominant, it just leans on the E until it falls back.
- **Soleá copla move** — F – G – Am – G – F – E — the cadence stretched through one and a half compases for sung verses; the extra G rotation is where the singer finds the next phrase.

No sevenths on the cadence chords, no extensions, no substitutions — the tension is rhythmic (the accents) and modal (the b2), and adding chord tones just dilutes it.

## Rhythm & feel

Tempo is counted per beat, not per bar: soleá at roughly 90–110 counts/min (heavy, ceremonial), bulerías at 200–260 (the same cycle at double-plus speed, party tempo). Write `setcpm(104/12)` and one cycle is one full compás. The skeletons:

- **Compás accents** (12 counts) — `cp ~ ~ cp ~ ~ cp ~ cp ~ cp ~` — claps on 12, 3, 6, 8, 10.
- **Cajón, light** (12 counts) — `bd ~ ~ ~ ~ ~ bd ~ ~ ~ sd ~` — deep tones on 12 and 6, a slap on 10.
- **Cajón, escobilla** (12 counts) — `bd sd sd sd bd sd sd sd bd sd sd sd` — relentless slaps between the tones.
- **Chord placement, por medio** — Am at 12, G at 3, F at 6, E at 8.
- **Rasgueado burst** (inside one count) — `[[e3,gs3,b3,e4] [e3,gs3,b3,e4] [e3,gs3,b3,e4] [e3,gs3,b3,e4]]` — four strums inside the count; the outer bracket holds the grid at twelve.
- **Remate figure** (last four counts) — `~ ~ ~ ~ ~ ~ ~ ~ ~ ~ sd sd` — the roll on 10–11 into 12.

Feel devices: the cycle counts from 12, so the downbeat of your intuition is the middle of the pattern's tension; accents land 12-3-6-8-10 with 12 strongest and the 8-9-10 tail the busiest; dynamics are cliffs, not slopes — a solo falseta at whisper to a full-corps remate at full shout in the space of one count; and within cante sections the singer stretches and compresses time while the palmas keep the count — hold the skeleton metronomic and let the melody argue with it.

## Structure

A traditional soleá performance, in compases (one compás = 12 counts): the form runs `falseta 2 → cante 3 → falseta 2 → escobilla 4 → remate 2` with energy `3 · 5 · 4 · 5→8 · 10→12`.

The opening falseta states the falseta-to-cante ratio: guitar alone, quiet. Cante brings palmas and light cajón under the voice. The second falseta is a breather. The escobilla is the long build — the same comp, the cajón doubling and doubling again, energy rising by repetition rather than addition. The remate is the payoff: everything plays, the roll closes the last compás, and the final chord rings out with one accent left in it. Bulerías takes this same form at 2.5× speed with more shouting; rumba flamenca (4/4, "Entre Dos Aguas") is the pop cousin that abandoned the cycle entirely.

## Techniques that actually create "flamenco"

- **Compás discipline** — nothing may blur where 12 is. Write every layer as an explicit twelve-count pattern and the accents stay honest; if a layer loses the count, the whole fabric visibly unravels — there is no backbeat to hide behind.
- **The rasgueado burst** — nested-bracket chords (`[[e3,gs3,b3,e4] [e3,gs3,b3,e4] [e3,gs3,b3,e4] [e3,gs3,b3,e4]]`) with short decay are the strumming engine. Reserve `!4` replication for patterns where a redivided grid doesn't matter — inside a twelve-count cycle it stretches everything. Bursts on counts 8 or 10 and left off elsewhere mark the remate; played every count they turn into a pump — use that escalation deliberately.
- **Picado runs that close on accents** — falseta lines are descending or arpeggiated runs whose last note lands on 10 or 12. Compose the target accent first, then walk backward to the start of the phrase.
- **The F–E crux** — the bII–I move, struck or walked, is the cadence of the style. Land it across 8-through-12 with the thumb stating f2 then e2 on consecutive accents and the remate practically builds itself.
- **Palmas as the chorus** — claps are not a metronome, they're the crowd. Layer them with tiny timing offsets (`.off(1/48, ...)`), drop them to a single soft pair during falsetas, and let them hit full-width at remates.
- **Dynamics as cliffs** — move from solo guitar to full ensemble inside one count, not across a section. The drama of flamenco is the snap, and a gradual fade-in anywhere reads as rock balladry.
- **The held breath** — one count of near-silence (everything but a ringing open string) right before the final 12 is the loudest thing in the piece. Spend it once.

## Practice approach

- Count the compás out loud — "12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11" — while clapping only 12, 3, 6, 8, 10 until you can drop back in after losing your place. That is the entire prerequisite skill.
- Learn one Paco de Lucía soleá falseta and mark which count each note lands on; the discovery is always that the run was aimed at 10 from its first note.
- Program the accent skeleton with palmas alone at 104 counts/min and improvise phrygian single notes over it — anything that doesn't resolve to an accent will teach you more than any scale exercise.
- Take the Andalusian cadence (Am–G–F–E) and place it on the compás three ways: all chords on 12, one chord per accent, F and E split across 8–12. Hear the same harmony become three different pieces of music.
- Record a two-compás loop of rasgueado plus thumb, then delete the rasgueado from random counts — flamenco comp swings hardest when the strumming implies more than it states.

## Example

```
// ═══ soleá por bulerías — flamenco, 104 counts/min ═══
// one cycle = one full 12-count compás — accents land on 12 · 3 · 6 · 8 · 10
// form: falseta 2 | cante 3 | falseta 2 | escobilla 4 | remate 2
// energy: 3        5        4        5→8         10→12
setcpm(104 / 12) // the cycle is the whole compás, not one bar — counts run at 104/min

// ── the compás: palmas on 12 3 6 8 10 — the skeleton everything measures itself against ──
const palmas = s("cp ~ ~ cp ~ ~ cp ~ cp ~ cp ~").gain(.5)
const palmasCorps = palmas.off(1/48, x => x.gain(.3).pan(.75)) // the second pair of hands, a hair late

// ── cajón: deep tone on 12 and 6, slaps around the 8–10 tail ──
const cajonLight = s("<[bd ~ ~ ~ ~ ~ bd ~ ~ ~ sd ~] [bd ~ ~ ~ ~ ~ bd ~ sd sd sd sd]>").gain(.45)
const cajonHeavy = s("bd sd sd sd bd sd sd sd bd sd sd sd").gain(.55) // escobilla: relentless

// ── guitar comp: the Andalusian cadence rides the accents — Am 12 · G 3 · F 6 · E 8 ──
// rasgueado = nested brackets: the chord strummed three/four times inside ONE count (grid stays 12)
const rasg = note("[[a3,c4,e4] [a3,c4,e4] [a3,c4,e4]] ~ ~ [[g3,b3,d4] [g3,b3,d4] [g3,b3,d4]] ~ ~ [[f3,a3,c4] [f3,a3,c4] [f3,a3,c4]] ~ [[e3,gs3,b3,e4] [e3,gs3,b3,e4] [e3,gs3,b3,e4] [e3,gs3,b3,e4]] ~ [gs3,b3,e4] ~").sound("gm_acoustic_guitar_nylon").gain(.5)
const thumb = note("a2 ~ ~ g2 ~ ~ f2 ~ e2 ~ e2 ~").sound("gm_acoustic_guitar_nylon").gain(.68)

// ── falsetas: picado single-note runs in E phrygian (e f g a b c d), closing on accents ──
const falseta1 = note("[e4,a4] ~ b4 ~ c5 b4 a4 ~ g4 ~ f4 ~")
const falseta2 = note("b4 ~ a4 g4 ~ f4 e4 ~ f4 ~ e4 ~")
const falseta3 = note("e5 d5 c5 b4 a4 g4 f4 e4 f4 ~ g4 ~")

const guitar = arrange(
  [2, cat(falseta1, falseta2)],       // naked guitar — the opening statement
  [3, stack(rasg, thumb)],           // cante: comp only, supporting the voice
  [2, cat(falseta3, falseta2)],       // a breather between verses
  [4, stack(rasg, thumb)],           // escobilla: same comp, the cajón brings the energy
  [2, note("<[e4 f4 g4 a4 b4 c5 d5 e5 d5 ~ ~ ~] [[e2,e3,gs3,b3,e4] ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~]>")], // remate: run up, then the E rings
).sound("gm_acoustic_guitar_nylon").gain(.55).room(.2)

// ── cante: the voice — spare, wailing, resolving into the remate ──
const cante = arrange(
  [2, silence],
  [3, note("<[c5 ~ b4 ~ a4 ~ ~ g4 ~ ~ ~ ~] [a4 ~ ~ g4 f4 ~ e4 ~ f4 ~ e4 ~] [~ ~ c5 ~ b4 ~ a4 ~ g4 ~ ~ ~]>")],
  [2, silence],
  [4, silence],                      // escobilla: the dance owns the floor
  [2, note("<[b4 ~ ~ a4 ~ ~ g4 ~ f4 ~ e4 ~] [~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~]>")], // one last wail, then out
).sound("gm_voice_oohs").gain(.35).room(.45)

// ── percussion book: cliffs, not slopes — membership snaps between sections ──
const perc = arrange(
  [2, silence],                                                              // falseta: naked
  [3, stack(palmas.gain(.35), cajonLight.gain(.35))],
  [2, s("cp ~ ~ cp ~ ~ cp ~ cp ~ cp ~").gain(.2)],                           // palmas only, hushed
  [4, stack(palmas, palmasCorps, cat(cajonLight, cajonLight, cajonHeavy, cajonHeavy))], // the build
  [2, stack(palmas, palmasCorps, cajonHeavy, s("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ sd sd").gain(.6))],  // roll on 10–11 into 12
)

$: perc
$: guitar
$: cante
```
