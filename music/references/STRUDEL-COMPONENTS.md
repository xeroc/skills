# Strudel Component Catalog — primitives and composites

Everything the Strudel REPL (strudel.cc) can do, extracted by category from the official workshop (`strudel/website/src/pages/workshop/`), the technical manual, and the learn pages (sounds, tonal, effects). Primitives are single functions/notations; **composites** are recognizable multi-primitive idioms (multiple sounds/beats/controls combined) with copy-ready shapes. Every name below is verified against the docs — if a name is not in this file, verify it before shipping.

## 1. Sound sources

Drum map (default bank = uzu-drumkit): `bd` kick · `sd` snare · `rim` rimshot · `cp` clap · `hh` closed hat · `oh` open hat · `cr` crash · `rd` ride · `ht`/`mt`/`lt` toms · `cb` cowbell · `tb` tambourine · `sh` shaker · `brk` · `misc`. (No default `perc`/`fx` — those are bank suffixes only.)

- Sample variants: `s("hh:0 hh:1 hh:2")` or `n("0 1 [4 2] 3*2").sound("jazz")` — `:k`/`n` selects the sample file; numbers wrap around.
- Drum machines: `.bank("RolandTR909")` — 71 banks preloaded (RolandTR808/909/606/707/727, LinnLM1/LM2/LinnDrum, OberheimDMX, EmuSP12, AkaiMPC60, KorgMinipops, BossDR550, CasioRZ1/VL1, RhythmAce, SimmonsSDS5, ViscoSpaceDrum, YamahaRX5/RY30 …), all with standardized `_bd _sd _hh …` suffixes; no bank has every suffix. Bank can be patterned: `.bank("<RolandTR808 RolandTR909>")`. Bank↔genre table: `references/SAMPLE-CATALOG.md`.
- Melodic synths (built-in): `sawtooth` · `square` · `triangle` · `sine` · `supersaw` (detuned saw stack).
- Sampled instruments (all preloaded, `note()`-playable): VCSL acoustics (~128: `steinway kawai fmpiano harp folkharp harmonica vibraphone marimba xylophone glockenspiel kalimba conga bongo clave guiro cabasa cajon agogo tambourine darbuka timpani gong woodblock clap snare_hi snare_low …`) — pitched multisamples are note-accurate, percussion entries pick hits via `n`; GM soundfonts (125 `gm_*`: `gm_acoustic_guitar_nylon gm_electric_guitar_muted gm_overdriven_guitar gm_distortion_guitar gm_acoustic_bass gm_slap_bass_1 gm_clavinet gm_drawbar_organ gm_percussive_organ gm_brass_section gm_tenor_sax gm_flute gm_sitar gm_taiko_drum …`); Dirt subset textures (`jazz` brushed kit by index 0–7, `east` taiko/shime, `space wind crow insect metal casio numbers`); `mridangam` solkattu syllables; `piano` (+ `.piano()` helper).
- Sound switching vs stacking: `.sound("piano gm_acoustic_guitar_steel")` alternates per event; `.sound("piano, gm_acoustic_guitar_steel")` plays both.
- Custom samples: `samples({...}, 'https://...')`, `samples('github:user/repo')`, or a `strudel.json`; pitched maps `{'g3': 'file.wav'}`. Community packs: only the vetted T2 table in `references/SAMPLE-CATALOG.md` — first play may be silent (lazy load); background beds stay on preloaded sounds.

## 2. Pitch and tonal

- `note("c4 eb4 g4")` — letters (flats `bb4`, sharps `fs4` — never `#`), MIDI numbers, decimals ok.
- `n("0 2 4").scale("C:minor")` — scale degrees, guaranteed in key. Root may carry an octave (`"A2:minor"`), scales can be stacked (`":minor:pentatonic"`), patterned (`"<C:major D:mixolydian>/4"`).
- `.transpose(12)` semitones; `.scaleTranspose(2)` scale steps.
- Chord symbols → auto voicings: `chord("<Am7 F7>").anchor("c5").voicing()` — smooth voice-led piano/guitar-style voicings. Controls: `dict` (voicing dictionary, e.g. `'lefthand'`, custom via `addVoicings`), `anchor` (top-note target, default c5), `mode` (`below`/`above`/`duck`/`root`), `offset`, `n` (play voicing like a scale). Symbol vocabulary is iReal-style: `^` maj, `-` min, `7`, `9`, `^7`, `-7`, `7sus`, `sus`, `add9`, `7b9`, `7#11`, `7alt`, `-7b5`, `h7`, `o7`, …
- `"<Am C D F>".rootNotes(2)` — chord symbols → bass root notes (octave arg).
- Mini-notation chords are commas: `[c3,e3,g3,b4]`; stacked in sub-sequences too: `"[bd, [c3,e3,g3]]"`.

## 3. Mini-notation (the rhythm language)

| Syntax | Meaning | Example |
|---|---|---|
| space | sequence (squished into one cycle) | `"bd hh sd hh"` |
| `-` or `~` | rest | `"bd ~ sd ~"` |
| `[a b]` | sub-sequence (subdivide a slot) | `"bd [hh hh] sd"` |
| `[[a b] c]` | nest arbitrarily deep | `"bd [[rim rim] hh]"` |
| `,` | parallel (stack) | `"hh*8, bd casio"` |
| `<a b>` | one per cycle (alternation); `= [a b]/n` — adding elements doesn't change tempo | `"<bd bd hh bd>*8"` |
| `*n` / `/n` | speed up / slow down (fractions ok: `*1.5`) | `"hh*16"`, `"[c d e f]/2"` |
| `@n` | elongate (default @1) | `"c@3 e"` |
| `!n` | replicate/elongate event n cycles | `"bd!4"`, `"c!2"` |
| `?` / `?p` | 50% / p-probability mute | `"hh*8?"` |
| `(p,s)` | Euclidean rhythm | `"bd(3,8)"` |
| `(p,s,r)` | Euclidean + rotation | `"sd(5,8,2)"` |
| backticks, newlines | multi-line patterns (whitespace-flexible) | see below |
| `a b` across lines | still one sequence | free-form layout |

## 4. Time operations

`setcpm(n)` (cycles/min; `setcpm(bpm/4)` = one cycle per 4/4 bar) · `setcps` · `fast(n)` / `slow(n)` (patternable: `.fast("<1 [2 4]>")`) · `hurry(2)` (fast + pitch up) · `early(n)` / `late(n)` (shift in time) · `clip(n)` (event length) · `loopAt(n)` (fit sample to n cycles) · `.fit()` (fit sample to event) · `.struct("x x ~ x")` (impose rhythm from another pattern) · `cat(a, b, …)` / `seq` / `stack` · `stepcat([3,"e3"],[1,"g3"])` (proportional) · `arrange([4, patternA], [8, patternB], …)` (song form; shorter patterns loop) · `polymeter("c eb g", "c2 g2")` / `{a b c, d e}%6` (different cycle lengths superimposed) · `inside(n, fn)` / `outside(n, fn)` · `palindrome()` (forward then backward).

**Bar math**: with `setcpm(bpm/4)`, one cycle = one bar of 4/4; seconds per bar = 240/bpm; `bars = seconds × bpm / 240`.

## 5. Conditional & stochastic

`.every(n, fn)` / `.when("pattern", fn)` / `.firstOf(n, fn)` / `.lastOf(n, fn)` · `.sometimes(fn)` (50%) · `.sometimesBy(p, fn)` · `.often` (75%) / `.rarely` (25%) · `.someCycles(fn)` / `.someCyclesBy(p, fn)` · `.degradeBy(p)` / `.degrade()` / `.undegradeBy(p)` (random event removal) · `.choose()` · `irand(n)` · `rand` in `n()` for random notes · `.segment(n)` (sample a signal at n points).

## 6. Pattern effects (structure-level)

- `rev()` — reverse the pattern.
- `jux(fn)` — split left/right channel, apply fn to the right (e.g. `.jux(rev)`).
- `add(x)` — add numbers/notes to a pattern; before `.scale()` it shifts **scale degrees** (diatonic transpose).
- `ply(n)` — repeat each event n times (patternable: `.ply("<1 2 3>")`).
- `off(time, fn)` — copy, shift by time, modify (nestable: `.off(1/16, x => x.speed(2).gain(.2).off(3/16, y => y...))`).
- `superimpose(fn)` — stack a modified copy on itself (`.superimpose(x => x.transpose(12))` octave double).
- `layer(f1, f2)` — run multiple transforms of one source in parallel.
- `arp(pattern)` / `arpWith(fn)` — re-sequence stacked chord notes by index (`.arp("[0 1 2 1]*4")`).

## 7. Audio effects

**Filters**: `lpf` / `hpf` / `bpf` (+`lpq`/`hpq`/`bpq` resonance, `':'` notation `"1000:10"` = freq:q; `ftype` `12db`/`ladder`/`24db`) · `vowel` formant filter (`"<a e i o u>"`).

**Filter envelopes** (the acid/303 family): `lpenv` (amount) · `lpa`/`lpd`/`lps`/`lpr` (attack/decay/sustain/release) — also `hpenv`, `bpenv`, pitch env `penv`, FM env `fmenv`.

**Amplitude**: `gain` · `postgain` · `adsr("a:d:s:r")` or `.attack/.decay/.sustain/.release` · `shape(n)` waveshape warmth/distortion · `distort` · `coarse` (sample-rate reduction) · `crush` (bit depth) · `compressor` · `tremolo` (with `tremolosync`/`tremolodepth`/`tremoloskew`).

**Space & motion**: `pan` (0–1) · `delay("volume:time:feedback")` e.g. `".5:.25:.4"` · `room` / `roomsize` (reverb) · `dry` · `speed` (playback rate; negative = reverse, patternable `"<1 2 -1 -2>"`) · `phaser` · `vib` vibrato · `seg(n)` (chop a continuous signal into n triggers) · `.cut(n)` (cut groups) · `.hush()` (silence a lane).

**Signal chain order** (single-use per param): gain → lpf → hpf → bpf → vowel → coarse → crush → shape → distort → tremolo → compressor → pan → phaser → post → {dry, delay, reverb} per **orbit**.

## 8. Signals (continuous automation)

Waveforms as parameter values: `sine`, `cosine`, `saw`, `tri`, `square`, `rand`, `perlin` (all 0–1; `*2` variants are bipolar). Then `.range(lo, hi)` · `.slow(n)` / `.fast(n)` · `.segment(n)`.

- Filter sweep: `.lpf(saw.range(400, 4000).slow(8))` — monotonic open over 8 cycles.
- Organic motion: `.cutoff(perlin.range(500, 2000))` · `.speed(perlin.range(.9, 1.1))`.
- LFO pan: `.pan(sine.range(.3, .7).slow(4))`.
- Continuous params (move without new triggers): ADSR, penv/fmenv, filter envelopes, tremolo, phaser, vib, duckorbit. For step-sampled params add triggers: `s("supersaw").seg(16).lpf(tri.range(100,5000))`.

## 9. Mixer, orbits, ducking

- One delay + one reverb **per orbit**; patterns on the same orbit overwrite each other's `room`/`roomsize`. Give lush lanes their own: `.orbit(2)`.
- Sidechain: the kick carries `duckorbit("2:3:4")` (alias `duck`) + `.duckdepth(.8)` + `.duckattack(.16)` — every listed orbit pumps behind it. Per-orbit values with `':'`: `duckdepth("0.3:0.1")`.

## 10. REPL features

`$: pattern` triggers one lane per line · `register('name', (arg, pat) => …)` — custom chained function, usable as `.name(value)` · `slider(default)` — inline draggable GUI widget · visualizers `._pianoroll()` / `._scope()` / `._punchcard()` · multi-sound stacking with `,` inside `.sound()`.

## 11. Composites — recognizable idioms built from the primitives

Each composite is a genre-ready recipe; combine them like lego.

- **Euclidean groove** — `s("bd(3,8)")`, rotated `s("rim(3,8,2)")`, layered against a straight grid for instant cross-rhythm.
- **Polymeter stack** — `{rim ~ sh}%3` over 4-beat bars (3-beat loop drifting, resolving every 3 bars); or `polymeter("c eb g", "c2 g2")`.
- **Velocity groove** — `s("hh*16").gain("[.2 .5 .2 .35]*4")`: accent patterns make a grid breathe. Same trick on `bd` (kick ghosting) and `note`.
- **Shuffle/triplet feel** — `[4@2 4]*n` inside a scale pattern, or `.swing(.08)` on hats (heavy for 2-step/garage, near-zero for techno).
- **Drum-bank genre kit** — `.bank("RolandTR909")` (house/techno), `"RolandTR808"` (hip-hop), `"RolandTR707"` (vintage), patterned banks to switch feel per section.
- **Supersaw stack** — `s("supersaw")` (the built-in detuned saw stack). Hand-rolled detune via `.add(.04)` on note patterns silently no-ops in current strudel — don't rely on it.
- **Acid/303 line** — `register('acidenv', (x, pat) => pat.lpf(100).lpenv(x*9).lps(.2).lpd(.12))` then `n("...").s("sawtooth").acidenv(slider(.6))` — the macro exposes filter amount as a live slider.
- **Sidechain pump** — kick `s("bd!4").duckorbit("2:3:4").duckdepth(.75).duckattack(.16)`; bass/pads on orbits 2–4.
- **Off-echo** — `.off(1/8, x => x.transpose(-12).gain(.2))`: an octave-down shadow answers every phrase; nest for call-and-response.
- **Stereo mirror** — `.jux(rev)` on arps/leads: left forward, right reversed.
- **Arp engine** — `chord("<Am F C G>").anchor("d5").voicing().arp("[0 1 2 1]*4")`, or scale-play `n("0 1 2 3").chord("<C Am F G>").voicing()`.
- **Voicing engine** — `chord("<Bb^9 G-7>").anchor("bb4").voicing().s("piano")` + `.struct("x ~ x ~")` for comping rhythms; `.rootNotes(1)` shares the same symbols for the bass.
- **Chord-walking roll** — `n("<0 4 0 9 7>*16".add("<0!2 5!2 2!2 6!2>")).scale("a2:minor")`: one 16th-note shape transposed diatonically through the progression (trance's travelling loop).
- **Riser stack** — `s("hh*8").speed("<1 1.5 2 4>").gain("<.1 .2 .3 .45>")` (noise sweep from hats) + `"<sd*4 sd*8 sd*16 sd*16>"` (accelerating roll) + a rising saw pitch figure. Dark variant: low distorted climb `note("<f2 ab2 c3 f3>").s("sawtooth").shape(.5)`.
- **Filter build / breakdown** — `.lpf(saw.range(300, 4000).slow(8))` opening across a section; reverse (`range(hi, lo)`) to close a door.
- **Reverse hit** — `.speed(-1)` or patterned `speed("<1 -1 2 -2>")`.
- **Ply stutter** — `note("~ stab").ply("<1 1 1 4>")`: the 4th hit quadruples into the hook (rave stutter).
- **Coprime ambient drift** — `.slow(9)` + `.every(7, …)` + `perlin.range(...).slow(11)` on different lanes: periods never realign, the loop never audibly repeats.
- **Song form** — `setcpm(bpm/4)` + `arrange([4, intro], [8, verse], [4, silence], …)`, `silence` for pauses, `stack()` inside slots; layers with different section maps need leading `[n, silence]` padding.
- **Frame-accurate hit placement** — nested 16ths to hit exact beats: `[~ ~ ~ [~ ~ ~ db3]]` puts db3 on the last 16th; seconds → slot math: `bar = floor(s ÷ 2)`, `slot = 1 + round((s − 2(bar−1)) ÷ .125)` at 120 BPM.
- **Live rig** — `register` macros + `slider` on the macro amount: the code equivalent of riding a filter for the crowd.

## 12. Engine gotchas (verified against the strudel source)

- `.add(n)` / arithmetic on **note-name** patterns (`note("c4 eb4")`) is a silent no-op — the event passes through untransposed ("Can't do arithmetic on control pattern", known issue). Use `.transpose(n)` instead. `.add()` on `n()` **degree** patterns (numbers, pre-`.scale()`) works — that's the diatonic-transposition tool.
- `.transpose()` silently drops events whose notes are spelled with s/f accidentals (`fs`, `cs`, `gs`, `df`). Respell to flats (`gb`, `db`, `ab`, `eb`, `bb`) in any lane you transpose.
- The default voicing dictionary silences `maj7`/`maj9` chord symbols in `chord()` — write `^7`/`^9` (e.g. `chord("<Db^7>")`). `m9`, `9`, `7`, `m7`, `sus`, `add9` etc. are fine.
- Delay `"a:b:c"` = volume:time:feedback (workshop semantics) — not time:feedback:mix.
- One reverb + one delay per orbit: patterns sharing an orbit overwrite each other's `room`/`roomsize`. Give lush lanes their own `.orbit(n)`.
