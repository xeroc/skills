Reggaeton's equivalent moment is **the lock-in** — the bar, usually eight or sixteen in, where the dembow finally starts. Before it you had a sub, a ghost of a snare pattern, maybe a hook teased; then the kick-and-snare engine drops and the track simply becomes perreo for as long as it runs. Like electro, the beat itself is the main character; the genre's entire dramatic machinery exists to make one unchanged one-bar loop feel like the payoff.

## What the lock-in actually is

The dembow is a one-bar drum figure descended from the 1991 "Dem Bow" dancehall riddim: kick on 1 and the "a of 1" (the dotted pair), plus a third kick on the "and of 2"; snares as "chk-chk" doubles on 2&-2a and 3&-3a with a single snare on 4& that pulls straight into the next downbeat. That's the whole engine. Everything else in a reggaeton track — sub, maracas-level percussion, a sparse flute-ish hook, the voice — is furniture arranged around a loop that never varies.

The lock-in works because the intro underplays it: the snare skeleton alone (2&, 3&, 4) or just sub and vocal, so that when the full kick pattern arrives with its 808 weight and everything ducks under it, the loop feels inevitable rather than repetitive. From there, sections are built by changing what sits on top — never by touching the dembow. Producers treat the loop like a law of physics; the creativity is in what you build in its shadow.

The third character is the voice. Perreo vocals don't float over the beat — their syllables lock into the snare doubles, so a sung phrase and the dembow read as one rhythm. When you replace the voice with an instrumental hook, it has to behave the same way: phrase endings on the 4& snare, entrances on the kick's 1, and long silences that the loop fills by itself.

## The layers

- **Kick** — `bd`, ideally `.bank("RolandTR808")` for the sub-forward thump: `"bd ~ ~ bd ~ ~ bd ~ ~ ~ ~ ~ ~ ~ ~ ~"` (1, 1a, 2&) with a little `shape` for grit. This is the layer that gets the sidechain — chain `.duckorbit("2:3").duckdepth(.8).duckattack(.16)` on it so the sub and percussion duck under every hit.
- **Snare** — `sd`: `"~ ~ ~ ~ ~ ~ sd sd ~ ~ sd sd ~ ~ sd ~"`. The doubles are the genre's fingerprint — two 16ths back to back, twice, then the lone 4& pickup. Played alone as its 8th-note skeleton (`~ ~ ~ sd ~ sd sd ~`) it works as the "ghost" version for intros and breakdowns.
- **Sub bass** — `sine`, notes in the 50–80 Hz zone (c2, ab1, bb1, eb2 in C minor). Roots only, long release, follows the kick loosely. The relationship between sub and kick — ducked, never competing — is the mix.
- **Percussion candy** — `sh*16` at whisper gain for motion, a `cb` hit every other bar, `misc` fills degraded with `degradeBy` at section ends. Everything sits low; the dembow owns the mid.
- **Hook lead** — `gm_flute` for the whistle-flute lineage (or a `triangle`/`sawtooth` synth for the modern Tainy sound). Sparse minor-pentatonic phrases with bars of nothing between them — space reads as luxury here, busyness reads as cheap.
- **Voices** — `gm_voice_oohs` chopped as a response layer behind the hook. Reggaeton is vocal music first; even instrumental, leave holes where a voice would answer.

## Sample kit

- **Kit** — `.bank("RolandTR808")` kick + default `sd` for the dembow doubles; layer a `.bank("RolandTR909")` clap on the backbeat for the reggaetón-pop polish.
- **Latin accents — the VCSL upgrade** — sparse `conga`/`clave`/`agogo` hits (one per 2–4 bars) sit under the dembow without crowding the mid; `guiro` for the old-school salsa-nodding intros.
- **Sub** — `sine` at 50–80 Hz ✓, ducked under the kick; no sample does this better.
- **Hook lead** — `gm_flute` (whistle lineage) or `triangle`/`sawtooth` (modern); `gm_ocarina` is a surprisingly good whistle-flute cousin.
- **Voices** — `gm_voice_oohs` chopped as the response layer.
- No pack needed — the preloaded tiers cover reggaeton. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Minor keys, almost always, with progressions that loop every 4–8 bars and avoid jazz cadence — pull comes from bVII→i and bVI→iv slides, not from V7 resolution. In C minor:

- **i – bVI – bIII – bVII** — Cm – Ab – Eb – Bb — the four-chord hook engine ("Gasolina" family), two bars per chord so the sub can really sit on each root.
- **i – iv** — Cm – Fm — the smoky verse loop; the sub holds each root and the dembow carries all the interest.
- **i – bVII** — Cm – Bb — the minimal perreo two-chord; use it when the hook is strong enough that harmony would only distract.
- **i – bVI – bVII – i** — Cm – Ab – Bb – Cm — a turnaround that closes on i instead of a dominant, so the loop can run forever without feeling like it owes you a cadence.

## Rhythm & feel

90–100 BPM (`setcpm(96/4)`); straight 16ths, no swing, half-time never. The skeletons:

- **Dembow kick** (one bar of 16ths) — `bd ~ ~ bd ~ ~ bd ~ ~ ~ ~ ~ ~ ~ ~ ~` — hits on 1, 1a, 2&; trim it to `bd ~ ~ bd ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~` for the old-school dotted pair only.
- **Dembow snare** (one bar of 16ths) — `~ ~ ~ ~ ~ ~ sd sd ~ ~ sd sd ~ ~ sd ~` — chk-chk on 2&-2a, chk-chk on 3&-3a, single chk on 4&.
- **Snare skeleton** (one bar of 8ths) — `~ ~ ~ sd ~ sd sd ~` — 2&, 3&, 4; the ghost used in intros, breakdowns, and outros.
- **Sub** (follows the kick loosely) — `c2 ~ ~ ~ ~ ~ c2 ~ ~ ~ ~ ~ ~ ~ ~ ~` — roots with huge space around them.

Feel devices: the kick and the first snare collide on 2& — that layered thud is the perreo signature, don't separate them; the lone 4& snare is the pickup that makes the loop pull into the downbeat instead of stopping at it; club edits add a four-on-the-floor kick but the canonical groove is the three-kick shape above; and everything except the dembow ducks under the kick, which is what makes the collisions hit instead of mush.

## Structure

The form runs `intro 4 → verse 8 → hook 8 → verse2 8 → hook2 8 → outro 4` with energy `2 · 5 · 8 · 6 · 8 · 4→7`.

The intro is the setup (no dembow), the first hook is the payoff, and every repeat earns itself by stripping back down in between. The outro often fakes an ending — dembow dissolves to the snare ghost, sub lands one last root, and a final two bars of full loop close the door. Long intros are a modern Bad Bunny-era flex; classic perreo gets to the loop in four.

## Techniques that actually create "reggaeton"

- **Dembow constancy** — the loop never changes, never fills, never varies. If a section needs more energy, add a layer on top; if it needs less, remove one. The moment you "develop" the dembow you've written a different genre.
- **The dropout bars** — two or four bars before a hook, drop the kick and leave only the snare skeleton (or silence plus sub). It's the held breath that makes the lock-in land; skip it and the hook arrives at the same energy as the verse.
- **Sub-kick monogamy** — one low voice at a time. The sub plays roots the kick isn't currently occupying, ducks under every kick hit, and releases long. Two things fighting for 60 Hz is the most common way this genre demo turns to mud.
- **Sparse pentatonic hooks** — C minor pentatonic (c, eb, f, g, ab), one phrase per four bars, repeated with tiny variation. The hook is a chant, not a melody; if it needs more notes to be interesting it isn't finished.
- **Call and response** — hook phrase, then empty bars (or a voice chop answering). The gaps are where the listener's body supplies the missing rhythm.
- **Velocity-flattened percussion** — candy layers (sh, cb, perc) sit so low in gain they're felt as texture. If you can hum along to a percussion layer in a reggaeton track, it's too loud.
- **The late flip** — for the final hook only: switch the kick to four-on-the-floor or double the snare skeleton. One sanctioned variation, at the end, bought by six minutes of discipline.
- **Vocal rhythm as second dembow** — every melodic layer's phrase endings should land on the snare positions (2&, 3&, 4&) so melody and drums fuse into one figure. A hook that ends mid-beat, off the snare grid, instantly sounds like a foreign object dropped on the loop.

## Practice approach

- Program the dembow from the 16th-grid strings above until you can write it from memory — kick 1, 1a, 2&; snares 2&, 2a, 3&, 3a, 4& — then check it against "Gasolina" and "Safaera" and fix whatever your ear catches.
- Write a hook using only four notes of C minor pentatonic, then remove notes until it stops working; add back exactly one. That last note is the hook.
- Build the full stack (dembow, sub, candy, hook) and then mix it with the sub and kick only — if that pair alone doesn't make you move, no layer will save it.
- Study Shabba Ranks' "Dem Bow" next to a modern track to hear what 30 years of subtraction did: same loop, less everything else.
- Practice the dropout: take a finished 8-bar loop, delete the kick from bars 7–8 of every 8, and notice how the return now does the work the hook used to have to do.
- Chant a nonsense syllable line over your loop, transcribe where the syllables actually land, and rebuild your hook on those positions — the body already knows where perreo phrasing goes.

## Example

```
// ═══ perreo nocturno — reggaeton, 96 bpm ═══
// form: intro 4 | verse 8 | hook 8 | verse2 8 | hook2 8 | outro 4
// energy:  2        5       8        6        8        4→7
// the dembow loop never changes — everything else changes around it
setcpm(96 / 4) // one cycle = one 4/4 bar

// ── the dembow: kick 1 · 1a · 2& — snares chk-chk on 2&-2a, 3&-3a, single on 4& ──
const kick = s("bd ~ ~ bd ~ ~ bd ~ ~ ~ ~ ~ ~ ~ ~ ~").bank("RolandTR808").shape(.2)
  .duckorbit("2:3").duckdepth(.8).duckattack(.16) // sub and candy duck under every kick
const snare = s("~ ~ ~ ~ ~ ~ sd sd ~ ~ sd sd ~ ~ sd ~").gain(.6).room(.18)
const dembow = stack(kick, snare)
const snareGhost = s("~ ~ ~ sd ~ sd sd ~").gain(.45) // the skeleton, for where the full loop is too much

// ── percussion book: when the full dembow plays, when it dissolves ──
const beat = arrange(
  [4, stack(snareGhost, s("sh*16").gain(.08))],                                  // intro: the ghost of the loop to come
  [8, dembow],                                                                   // verse: it locks in
  [8, stack(dembow, s("sh*16").gain(.1), s("<~ ~ cb ~ ~ ~ ~ ~>").gain(.18))],    // hook: candy on top
  [8, dembow],
  [8, stack(dembow, s("sh*16").gain(.1), s("<~ ~ cb ~ ~ ~ ~ ~>").gain(.18))],
  [4, stack(snareGhost, s("misc*8").degradeBy(.6).gain(.2))],                    // outro: dissolve back to ghost
)

// ── sub: sine, roots only, follows the kick loosely — the space IS the arrangement ──
// verse: Cm vamp | hook: Cm Cm Ab Ab Eb Eb Bb Bb (two bars each)
const subVerse = note("<[c2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~] [c2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ eb2 ~]>")
const subHook = note("<[c2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~] [c2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ab1 ~] [ab1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~] [ab1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ eb2 ~] [eb2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~] [eb2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ bb1 ~] [bb1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~] [bb1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ c2 ~]>")
const sub = arrange(
  [4, note("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ c2 ~")],   // one pickup note, that's the whole intro
  [8, subVerse],
  [8, subHook],
  [8, subVerse],
  [8, subHook],
  [4, note("<[bb1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~] [c2@10 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~]>")], // final root, held
).sound("sine").attack(.005).sustain(.7).release(.3).gain(.75).lpf(120)

// ── the hook: gm_flute, C minor pentatonic, four bars of mostly nothing ──
const hook = note("<[g4 ~ ~ ~ ~ ~ ab4 ~] [~ ~ ~ g4 ~ ~ ~ ~] [eb5 ~ ~ c5 ~ ~ ~ ~] [~ ~ ~ ~ ~ ~ ~ ~]>")
const hookAnswer = note("<[~ ~ ~ ~ ~ ~ ~ ~] [~ ~ g4 ~ ~ ~ eb4 ~] [~ ~ ~ ~ f4 ~ ~ ~] [~ ~ ~ ~ ~ ~ ~ ~]>")

const lead = arrange(
  [4, silence],
  [8, silence],                                    // verse 1: voice territory, no lead
  [8, hook],
  [8, hookAnswer],                                 // verse 2: the answer becomes the question
  [8, hook.superimpose(x => x.transpose(12).gain(.16))], // final hook: one octave ghost on top
  [4, note("<[~ ~ ~ ~ ~ ~ ~ ~] [~ ~ [c5,g5] ~ ~ ~ ~ ~]>")],
).sound("gm_flute").gain(.42).room(.4).delay(".16:.25:.2")

$: beat
$: sub
$: lead
```
