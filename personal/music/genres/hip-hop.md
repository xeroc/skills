Hip-hop's equivalent moment is **the break** — the two-bar stretch where the sampled loop and the drums lock into a head-nod and then just stay there. Jazz builds to a cadenza, pop builds to a bridge; boom-bap builds to the pocket itself, the moment you stop waiting for the song to go somewhere and realize the loop is the destination. Space is the instrument: what you leave out of those two bars is what actually makes the neck move.

## What the break actually is

A break is a short, usually one- or two-bar drum groove lifted from a funk or soul record, looped, and treated as the composition. The producer's job is not to write more material — it's to frame the same material so well that it never gets old: filter it, drop layers in and out, chop it, flip it backwards, and leave holes for the MC. Verse/chorus dynamics come from arrangement (what's muted, what's opened up), not from harmonic development. The pocket sits slightly behind the grid, the sample hisses, the sub fills the kick's holes, and the whole thing repeats until it's hypnotic. If every 16th note in the bar is occupied, you haven't written boom-bap — you've written a drum exercise.

## The layers

- **Sample / melody** — the chopped record, the emotional core. `pluck` for the soul-loop feel, `piano` for Rhodes-and-strings chops, `gm_music_box` for music-box melancholy, `gm_flute` for the flute-loop era. Treat everything like vinyl: `.hpf(220).lpf(2600)` to band-limit it, `.degradeBy(.08)` for dust, occasional `.speed(-1)` to flip a stab backwards, `.swing(.15)` so it drags with the drums.
- **Sub bass (the "808")** — pure `sine` synth an octave below everything, long `adsr` sustain, roots only. It plays the sample's root notes and lives exclusively where the kick isn't. Busy sub = dead loop.
- **Kick & snare** — `.bank("RolandTR808")`: `bd` deep with the boom, `sd` dry and cracking. The skeleton is everything; get it right before touching anything else.
- **Hats** — `hh` on swung 16ths (`.swing(.15)`) with a velocity pattern that accents the 8th offbeats, never flat. One `oh` per bar as a breath. `.degradeBy(.06)` loosens them off the grid.
- **Ghost snares & percussion** — whispered `sd` hits at gain .1–.15 between the backbeats, `sh` at gain .03 as vinyl air. You should barely hear them and immediately miss them when muted.
- **Ear candy** — a reversed stab (`speed(-1)`) that swells into a hook, a delay throw on the last hit of a phrase, a clap layer that shadows the snare in the chorus only.

## Sample kit

- **Kit** — `.bank("RolandTR808")` is the default skeleton sound. Character alternates: `.bank("EmuSP12")` / `.bank("AkaiMPC60")` for grittier boom-bap, `.bank("LinnLM1")` / `.bank("OberheimDMX")` for the 80s.
- **Real breaks** — the genre's foundation as samples: `github:yaxu/clean-breaks` carries the canonical loops by name —
  ```js
  samples('github:yaxu/clean-breaks'); // funkydrummer apache think impeach amen useme …
  $: s("funkydrummer").loopAt(2).gain(.5) // layer under the skeleton, or chop(8)/splice(8, "…") it
  ```
  First play may be silent while the pack loads — run again. **Copyrighted recordings: foreground/playground use only**, never background-music deliverables. `github:eddyflux/crate` supplies dusty one-shot alternatives (see lo-fi).
- **Sub** — `sine` synth, roots only. For 808-decay variants without a pack: full Dirt-Samples adds the `808bd` tuning series (`BD0000`→`BD7575`).
- **Sample/melody sources** — `pluck` soul loops, `piano`/`steinway` Rhodes-and-strings chops, `gm_music_box`, `gm_flute`.

## Harmony

Chord vocabulary is whatever the chopped record implies: minor 7ths, minor 9ths, and major 7ths on bVI and bVII dominate. Melodies are almost always minor pentatonic — in F minor that's F–A♭–B♭–C–E♭ — with the occasional dorian D♮ as color. Canonical loops, in F minor:

- **i–bVII** — Fm7 | E♭maj7: the two-bar sample loop. Ninety percent of the genre is a decorated version of this.
- **i–bVI–bVII (–iv)** — Fm7 | D♭maj7 | E♭ | B♭m7: the descending-Aeolian sigh, the "nostalgic walk home."
- **i7–iv7** — Fm9 | B♭m7: a minimal two-chord sway; the sub walks F→B♭ while the sample chops around it.
- **One-chord vamp** — Fm9 for eight bars straight: the drums and the filtering do the arranging; harmony just holds the couch down.

## Rhythm & feel

- Tempo 80–95 BPM. Below 80 it's a sway, above 100 you're in trap or club territory.
- The skeleton (one cycle = one 4/4 bar, 16th grid): `bd ~ ~ ~ sd ~ ~ ~ bd bd ~ ~ sd ~ ~ ~` — kick on 1, snare on 2 and 4, the doubled kick around beat 3. Its spoken essence is `bd … sd … bd bd … sd`, the anchor string `bd ~ ~ sd ~ bd bd ~ sd ~` every drummer in the lineage knows.
- Swing the 16ths: `.swing(.15)` on hats, ghosts, sub 16ths, and the sample. Straight 16ths sound like techno wearing a jacket.
- Variants: pull the second kick earlier (`~ ~ bd` on 3), push one onto the a-of-4 (`~ bd`) to mark the last bar before a hook, and add `sd sd sd` 16th fills only at 8-bar seams.
- The space rule: at least a third of the 16 slots in any bar are rests. The rests are the instrument.

## Structure

```
intro 4 | verse 16 | dropout 1 | hook 8 | verse 8 | dropout 1 | hook 8 | outro 4
   2         4         0          7        5         0          8        3      (energy 0-10)
```

Intro is the sample alone with vinyl air. Verse: drums and sub in, keys low. Hook: the chop climbs, claps shadow the snare, the reversed stab flips into place. The dropout — one bar of near-silence (ghost snares and hiss only) before each hook — is the single cheapest, most effective move in the genre. Outro sinks the sample back under a closing filter.

## Techniques that actually create "hip-hop"

- **The two-bar loop** — everything derives from one or two bars of material; variation comes from what's muted and filtered, not from new parts. If your B section is a new chord progression, you've left the genre.
- **Space as instrument** — program the rests as deliberately as the hits; the holes are where the listener's imagination (and the MC) lives.
- **Sample treatment** — `.hpf()`/`.lpf()` band-limiting, `.degradeBy()` dust, `.speed(-1)` flips, and `.rev` on the odd phrase make synth parts read as sampled records.
- **Filter arrangement** — the same loop at `.lpf(800)` is an intro, at full range is a hook. You arranged the song without touching the notes.
- **Ghost notes at gain .1** — whispered snares between backbeats create the head-nod's inner life; they're felt, not heard.
- **The dropout** — one bar of near-silence before the hook resets the ear so the hook lands like a punch.
- **Sub in the kick's holes** — the sine only sounds where the kick doesn't; when they collide the low end turns to mud and the neck stops moving.
- **Swung 16ths everywhere** — `.swing(.15)` on every rhythmic layer so the whole machine drags identically.

## Practice approach

- Loop two bars of a Premier, Pete Rock, or RZA beat and write out its 16-slot skeleton on paper; you'll find the rests outnumber the hits.
- Program drums first, sample second — if the skeleton doesn't nod alone, no melody will save it.
- Run the mute test: mute any one layer; if nothing changes, the layer was decoration — delete it.
- Count in 16ths out loud while writing kick patterns; the push before beat 1 only works if you know exactly which slot it's in.
- Write one chord loop (i–bVII is plenty) and make three distinct sections using only gain, filters, and dropouts.

## Example

```
// ═══ brownstone — boom-bap, 88bpm ═══
// form: intro 4 | verse 16 | dropout 1 | hook 8 | verse 8 | dropout 1 | hook 8 | outro 4
// energy: 2 4 4 0 7 5 0 8 3 — the two silence bars are the whole arrangement
setcpm(88 / 4) // one cycle = one bar of 4/4

// ── the sample — chopped soul loop in F minor pentatonic, treated like vinyl ──
const chopVerse = note("<[[~ c5 ~ ab4] [~ f4 ~ ~] [bb4 ~ ~ ab4] [~ ~ g4 ~]] [[~ c5 ~ ab4] [~ f4 ~ ~] [~ eb5 ~ c5] [~ bb4 ~ ~]]>")
const chopHook = note("<[[~ c5 ~ ab4] [~ f4 ~ ~] [bb4 ~ ~ ab4] [~ ~ g4 ~]] [[~ c5 ~ ab4] [~ f4 ~ ~] [[eb5 f5] ~ c5 ~] [~ ~ ab4 ~]]>")
const sample = arrange(
  [4, chopVerse.gain(.26)],
  [16, chopVerse.gain(.4)],
  [1, silence], // the dropout: held breath before the hook
  [8, chopHook.gain(.5).off(1/16, x => x.transpose(-12).gain(.15))], // hook: octave shadow a 16th behind
  [8, chopVerse.gain(.4)],
  [1, silence],
  [8, chopHook.gain(.5).off(1/16, x => x.transpose(-12).gain(.15))],
  [4, chopVerse.gain(.2)], // outro: the sample sinks back into the record
).sound("pluck").hpf(220).lpf(2600).degradeBy(.08).room(.25).swing(.15)

// ── keys — the loop's harmony, voiced where a sampled Rhodes would sit ──
const keys = arrange(
  [4, chord("<Fm9 Fm7>").anchor("ab4").voicing().gain(.16)],
  [16, chord("<Fm9 Fm9 Db^7 Eb>").anchor("ab4").voicing().gain(.28)],
  [1, silence],
  [8, chord("<Fm9 Ab^7 Bbm7 Db^7>").anchor("ab4").voicing().gain(.32)],
  [8, silence], // second verse: keys drop out, the sample carries it alone
  [1, silence],
  [8, chord("<Fm9 Ab^7 Bbm7 Db^7>").anchor("ab4").voicing().gain(.32)],
  [4, chord("<Db^7 Fm9>").anchor("ab4").voicing().gain(.14)],
).sound("piano").room(.3).swing(.15)

// ── the 808 — sine sub on roots only, living in the kick's holes ──
const subVerse = note("<[f1@5 ~ ab1 ~] [f1@5 ~ bb1 ab1]>")
const subHook = note("<[f1@5 ~ ab1 ~] [ab1@5 ~ bb1 ~] [bb1@5 ~ db2 ~] [db1@5 ~ c2 ab1]>")
const sub = arrange(
  [4, note("f1")], [16, subVerse], [1, silence], [8, subHook],
  [8, subVerse], [1, silence], [8, subHook], [4, note("<[f1@6 ~ ~ ~]>")],
).sound("sine").adsr(".004:.12:.85:.4").gain(.85)

// ── drums — the skeleton: bd 1, sd 2 & 4, doubled kick around 3, ghosts at .11 ──
const boom = sound("bd ~ ~ ~ sd ~ ~ ~ bd bd ~ ~ sd ~ ~ ~").bank("RolandTR808").gain(.9)
const ghosts = sound("~ ~ ~ sd ~ ~ sd ~ ~ ~ ~ sd ~ ~ sd sd").bank("RolandTR808").gain(.11) // the whisper engine
const hats = sound("hh*16").gain("[.42 .12 .26 .12 .44 .12 .26 .12]*2").swing(.15).degradeBy(.06)
const kit = stack(boom, ghosts, hats, sound("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ oh ~ ~").swing(.15).gain(.16))
const fill = stack(sound("bd ~ ~ ~ sd ~ sd ~ bd ~ sd sd sd sd sd sd").bank("RolandTR808").gain(.9), hats.gain(.3))
const ghostline = sound("~ ~ ~ sd ~ ~ ~ ~ ~ ~ ~ sd ~ ~ sd sd").bank("RolandTR808").gain(.2)
const dropout = stack(ghostline.gain(.15), sound("sh*16").gain(.03).hpf(6000)) // held breath + vinyl air
const drums = arrange(
  [4, ghostline], // intro: ghosts only — the loop before the loop
  [16, cat(kit, kit, kit, fill, kit, kit, kit, fill)],
  [1, dropout],
  [8, kit],
  [8, cat(kit, kit, kit, fill, kit, kit, kit, fill)],
  [1, dropout],
  [8, stack(kit, sound("cp ~ ~ ~ cp ~ ~ ~").gain(.28))], // hook: claps shadow the snare
  [4, ghostline],
)

// ── ear candy — a reversed music-box stab swells into each hook ──
const flip = arrange(
  [21, silence],
  [8, note("[~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [eb5 ~ ~ ~]").sound("gm_music_box").speed(-1).gain(.3)],
  [9, silence],
  [8, note("[~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [ab4 ~ ~ ~]").sound("gm_music_box").speed(-1).gain(.3)],
)

$: sample
$: keys
$: sub
$: drums
$: flip
```
