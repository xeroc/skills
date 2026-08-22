# Sample Catalog — what to load, what's already there

Ground truth for sound names, compiled from the strudel source (`packages/repl/prebake.mjs`, `packages/soundfonts/gm.mjs`, the `felixroos/dough-samples` JSONs, `tidalcycles/uzu-drumkit`) and a full enumeration of the community packs listed in awesome-strudel. Names below are verified against those inventories. Audition anything: REPL `sounds` tab, or <https://strudel-samples.alternet.site>.

## Selection policy

1. **T0 — default names.** Always available, zero setup. Start here.
2. **T1 — preloaded upgrades.** Drum-machine `.bank()`s, VCSL acoustics, `gm_*` soundfonts, the Dirt texture subset, mridangam. Already loaded in every REPL session — same paste-and-play guarantee as T0, massively wider timbre. **Use these before reaching for packs.**
3. **T2 — community packs.** Require a `samples('github:…')` preamble; lazy-loading means the first play may be silent (press ctrl+enter again). Only when T0/T1 genuinely lacks the timbre (real funk breaks, berimbau, dusty lo-fi one-shots). Pin to repos below — packs rot.

Licensing: packs marked ⚠ contain copyrighted commercial recordings. Fine for strudel.cc playground/foreground use (ecosystem norm); **never for background-music deliverables** (MUSIC.md `purpose: background`) — those stay T0/T1.

## T0 — default kit (uzu-drumkit + synths)

Drums: `bd` `sd` `hh` `oh` `cp` `rim` `cr` `rd` `ht` `mt` `lt` `cb` `tb` `sh` `brk` `misc`.
Melodic synths: `sine` `triangle` `square` `sawtooth` `supersaw`. Piano: `piano` (plus the `.piano()` helper — auto-pan-by-pitch, clip, release).

Corrections vs older docs: there is no default `hc`, `perc`, `fx`, or `crackle` — `perc`/`fx` exist only as suffixes inside drum-machine banks; `misc` is the default grab bag. Don't ship bare names outside this list.

## T1 — preloaded upgrades

### Drum-machine banks (71, via `.bank()`)

Standardized suffixes (`_bd _sd _hh _oh _cp _cr _rd _rim _ht _mt _lt _cb _tb _sh _perc _misc`) — no bank has all; the sounds tab shows counts. Genre anchors:

| Bank | Kit | Genre fit |
|---|---|---|
| `RolandTR909` | bd cp cr hh ht lt mt oh rd rim sd | house, techno, trance |
| `RolandTR808` | bd cb cp cr hh ht lt mt oh perc rim sd sh | hip-hop, trap, electro |
| `RolandTR707` | full kit | vintage 80s: new wave, early house, italo |
| `RolandTR727` | **perc sh only** (no bd/sd) | latin percussion layer, stack over another kit |
| `RolandTR606` | bd cr hh ht lt oh sd | acid, electro |
| `LinnLM1` | bd cb cp hh ht lt oh perc rim sd sh tb | 80s pop/funk |
| `LinnDrum` | full kit | 80s pop/rock ballads |
| `OberheimDMX` | full kit | electro, golden-age hip-hop |
| `EmuSP12` | full kit | boom bap, 80s hip-hop |
| `AkaiMPC60` | bd cp cr hh ht lt misc mt oh perc rd rim sd | boom bap |
| `AkaiLinn` | bd cb cp cr hh ht lt mt oh rd sd sh tb | early hip-hop, new wave |
| `KorgMinipops` | bd hh misc oh sd | 60s vintage, easy listening, bossa-adjacent |
| `SimmonsSDS5` | bd hh ht lt mt oh rim sd | 80s synthpop toms, arena |
| `CasioVL1` | bd hh sd | toy punk, cheap lo-fi |
| `CasioRZ1` | bd cb cp cr hh ht lt mt rd rim sd | cheap 80s character, lo-fi |
| `ViscoSpaceDrum` | bd cb hh ht lt misc mt oh perc rim sd | space disco |
| `RhythmAce` | bd hh ht lt oh perc sd | 60s vintage |

Full list (AJKPercusyn … YamahaRY30): browse the sounds tab. Pattern the bank to shift feel mid-piece: `.bank("<RolandTR808 RolandTR909>")`. Variant selection `.n("0 1 2")` or `hh:3`.

### VCSL acoustics (~128 names, real recorded instruments)

Two kinds:

- **Pitched multisamples** — `note()` is sample-accurate across the range: `steinway` `kawai` `piano1` `fmpiano` `clavisynth` · `harp` `folkharp` · `harmonica` `harmonica_soft` `harmonica_vib` · `recorder_{soprano,alto,tenor,bass}_{stacc,sus,vib}` · `ocarina` `ocarina_small` `ocarina_vib` · `sax` `saxello` (`+_stacc/_vib`) · `dantranh` `dantranh_tremolo` `dantranh_vibrato` · `super64` `super64_acc` `super64_vib` · `strumstick` · `psaltery_pluck` `psaltery_spiccato` `psaltery_bow` · mallets: `marimba` `vibraphone` (+`_soft` `_bowed`) `xylophone_{hard,medium,soft}_{ff,pp}` (no plain form) `glockenspiel` `balafon` (+`_hard/_soft`) `kalimba` … `kalimba5` `tubularbells` `tubularbells2` · `belltree` `handchimes` · `organ_4inch` `organ_8inch` `organ_full` `pipeorgan_loud` `pipeorgan_quiet` (±`_pedal`) · `wineglass` `wineglass_slow`.
- **Percussion with articulation variants** — flat arrays; `n`/`:k` picks the hit (round-robins and articulations), `note()` only pitch-shifts: `conga` `bongo` `cabasa` `cajon` `clave` `agogo` `cowbell` `guiro` `darbuka` `tambourine` `tambourine2` `timpani` `timpani2` (+`timpani_roll`) `snare_hi` `snare_low` `snare_modern` `snare_rim` `woodblock` `gong` `gong2` `clash` `clash2` `sus_cymbal` `sus_cymbal2` `triangles` `anvil` `brakedrum` `framedrum` `oceandrum` `slitdrum` `handbells` `didgeridoo` `vibraslap` `flexatone` `ratchet` `trainwhistle` `ballwhistle` `bassdrum1` `bassdrum2` `hihat` `clap`.

Genre notes: latin core = `conga bongo clave cowbell guiro cabasa agogo tambourine`; brushes alternative = Dirt `jazz` (below); mallet ballads = `vibraphone_soft`/`marimba`; flamenco-adjacent = `cajon` + `clap` + nylon guitar (gm).

### GM soundfonts (125, `gm_*` prefix)

Full General MIDI, multisampled, `note()`-accurate. The single biggest underused lever — real instrument timbres for free:

- **Guitars**: `gm_acoustic_guitar_nylon` `gm_acoustic_guitar_steel` `gm_electric_guitar_jazz` `gm_electric_guitar_clean` `gm_electric_guitar_muted` (reggae skank, funk chank) `gm_overdriven_guitar` (grunge, rock) `gm_distortion_guitar` (punk, metal power chords) `gm_guitar_harmonics`.
- **Bass**: `gm_acoustic_bass` (jazz walking!) `gm_electric_bass_finger` `gm_electric_bass_pick` `gm_fretless_bass` `gm_slap_bass_1` `gm_slap_bass_2` (funk) `gm_synth_bass_1` `gm_synth_bass_2`.
- **Keys/organ**: `gm_piano` `gm_epiano1` `gm_epiano2` `gm_harpsichord` `gm_clavinet` (funk) `gm_drawbar_organ` `gm_percussive_organ` (afrobeat bubble) `gm_rock_organ` `gm_church_organ` `gm_accordion` `gm_bandoneon` `gm_harmonica`.
- **Strings/brass/reeds**: `gm_violin` `gm_viola` `gm_cello` `gm_contrabass` `gm_pizzicato_strings` `gm_string_ensemble_1` `gm_string_ensemble_2` `gm_tremolo_strings` `gm_orchestral_harp` `gm_timpani` · `gm_trumpet` `gm_muted_trumpet` `gm_trombone` `gm_tuba` `gm_french_horn` `gm_brass_section` (mambo/ska horns) `gm_orchestra_hit` · `gm_soprano_sax` `gm_alto_sax` `gm_tenor_sax` `gm_baritone_sax` · `gm_oboe` `gm_english_horn` `gm_bassoon` `gm_clarinet` `gm_flute` `gm_piccolo` `gm_pan_flute` `gm_shakuhachi` `gm_whistle`.
- **Synth**: leads `gm_lead_1_square` … `gm_lead_8_bass_lead`; pads `gm_pad_new_age` `gm_pad_warm` `gm_pad_poly` `gm_pad_choir` `gm_pad_bowed` `gm_pad_metallic` `gm_pad_halo` `gm_pad_sweep`; fx `gm_fx_rain` `gm_fx_soundtrack` `gm_fx_crystal` `gm_fx_atmosphere` `gm_fx_brightness` `gm_fx_goblins` `gm_fx_echoes` `gm_fx_sci_fi`.
- **Ethnic/perc**: `gm_sitar` `gm_banjo` `gm_shamisen` `gm_koto` `gm_kalimba` `gm_bagpipe` `gm_fiddle` `gm_shanai` · `gm_agogo` `gm_steel_drums` `gm_woodblock` `gm_taiko_drum` `gm_melodic_tom` `gm_synth_drum` `gm_reverse_cymbal` `gm_tinkle_bell`.

### Dirt-Samples subset (preloaded textures)

- `jazz` — 8-piece brushed kit, index map: `0` BD · `1` CB · `2` FX · `3` HH · `4` OH · `5` P1 · `6` P2 · `7` SN. Use as `s("jazz:7")` etc. The jazz-ballad drums.
- `east` — Japanese percussion: wood block, ohkawa (mute/open), shime (hi/mute), taiko ×3. Taiko epic layer: `s("east:6")`.
- `space` `wind` `crow` `insect` `metal` `casio` (high/low/noise) `numbers` (0–9 spoken) — ambience/texture lanes for intros, breakdowns, sound design.

### Mridangam (preloaded)

Solkattu syllables as named samples — exact set: `ardha chaapu dhi dhin dhum gumki ka ki na nam ta tha thom`. Carnatic/Indian fusion percussion; also excellent glitchy one-shots.

## T2 — community packs

Preamble form (top of the block, before any `$:` lane):

```js
samples('github:Bubobubobubobubo/Dough-Amen');
```

| Pack | Contents | Genre fit | Confidence | License |
|---|---|---|---|---|
| `github:tidalcycles/dirt-samples` | full Dirt library, ~300 names | everywhere | high (official) | mixed per folder ⚠ |
| `github:Bubobubobubobubo/Dough-Amen` | `amen1`(20, BPM-tagged 135–178) `amen2`(40) `amen3`(20 named) | jungle, dnb, breakbeat | high | unknown ⚠ |
| `github:yaxu/clean-breaks` | 32 canonical funk breaks: `funkydrummer apache think impeach amen useme hitormiss …` | hip-hop, breaks, dnb | high (yaxu) | **copyrighted recordings** ⚠ |
| `github:eddyflux/crate` | lo-fi one-shots, `crate_`-prefixed: bd sd(54) hh cp(37) + `clave conga bongo djembe` | lo-fi, hip-hop | medium | unknown ⚠ |
| `github:salsicha/capoeira_strudel` | `hits`(50 berimbau/caxixi/atabaque) `loops`(25) | world/latin fusion | medium | unknown |
| `github:sonidosingapura/rochormatic` | trip-hop named breaks: `kompira ritachao karmacoma portis gndym …` | trip-hop, downtempo | medium | likely sampled ⚠ |
| `github:terrorhank/samples` | `gothenburg03_*` kit + wobble bass/loops | dubstep-adjacent | low | unknown |
| `github:RikyBac15/samples` | 303 bass/lead/brass one-shots at fixed pitches | acid stabs | low | unknown |
| `github:kaiye10/strudelSamples` | 4 loops: `jungle apache idm finger` | jungle | low | ⚠ |

Notes:

- **Break idiom** (Dough-Amen / clean-breaks): pick a break near your BPM, then re-chop — `s("amen1:3").chop(8)`, or `.splice(8, "<0 1 2 3 4 5 6 7>")` to re-sequence slices; layer a synthetic `bd` under for weight. The BPM in the filename is the loop's native tempo — `loopAt(1)` fits it to a cycle.
- **Full Dirt-Samples** adds melodic one-shots (`gtr` `moog` `pluck` `pad` `sitar` `tabla` `sax` `stab` …) plus the `808bd`/`808cy` tuning series (BD0000→BD7575 = decay variants) and rave kicks. They are **unpitched file arrays** — build a pitched map for tonal use, as the official docs show:
  ```js
  samples({ 'moog': { 'g3': 'moog/005_Mighty%20Moog%20G3.wav' } }, 'github:tidalcycles/dirt-samples');
  ```
- Hyphenated sample names (e.g. RikyBac15's `303-bass`) are risky in mini-notation — prefer array/object map forms or `.s()` with `cat()`.
- Packs rot (TodePond/samples: 404). Run `scripts/check-packs.sh` from this skill occasionally; deliverables must always name a T0/T1 fallback for any T2 sound.

## Loading mechanics & gotchas

- `samples('github:<user>/<repo>')` assumes `strudel.json` at repo root; add `/branch` if not `main`.
- Lazy loading: first trigger per sample may be silent (fetch in flight). Loops self-heal next cycle; for fixed-duration pieces, note "press ctrl+enter twice" or keep T0/T1.
- Browsers cache `strudel.json` aggressively; pack authors bust with `?v=2`.
- Custom pitched maps: `samples({ 'gtr': { 'c3': 'gtr/x.wav' } }, 'github:…')` — sampler picks nearest zone per note.
- Local disks: REPL → sounds → import-sounds folder, or `npx @strudel/sampler` + `samples('http://localhost:5432/')`.
