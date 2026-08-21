---
name: music
description: "Compose music as paste-ready Strudel code from a project MUSIC.md brief — background beds, loops, jingles, or full foreground tracks in any genre. Use when the user wants music for a video, product, lobby, app, animation, a beat, a track, or names a genre directly (house, techno, punk, funk, bossa nova, gospel, …) and wants Strudel code in that style. Differentiator: reads and writes a per-project MUSIC.md (like DESIGN.md, but for music), deconstructs artist/genre references into technique-based sonic DNA (how, not who), keeps a 33-genre reference library, and outputs exactly one self-contained code block to paste into strudel.cc — no encoded URLs, no HTML scaffold, no audio setup."
---

# Music — MUSIC.md-driven Strudel composition

Compose music as Strudel code, in any genre, for background or foreground listening. The brief lives in a per-project `MUSIC.md` file — the same idea as DESIGN.md for visual identity: a persistent, structured description of the sound, so iterations stay consistent across sessions. Output is code the user pastes into <https://strudel.cc> — nothing else.

## Output contract (non-negotiable)

- Deliver **exactly one** self-contained fenced ```js code block.
- It must run on paste into the <https://strudel.cc> workshop: press **ctrl+enter** (or the play button) to hear it. The REPL preloads default samples — no setup code needed.
- Never emit encoded URLs, `initStrudel`, HTML scaffolds, or "click this link".
- After the code block, add a short plain-text note: what to listen for (2–3 bullets tied to the brief) and 1–2 obvious dials to tweak (tempo, gain of a layer, filter).
- On iteration: if the _sound_ changes, update the code block only. If the _brief_ changes (new key, new mood, new structure), update `MUSIC.md` first, then the code.

## Workflow

1. **Locate the brief.** Read `MUSIC.md` from the working directory (or the path the user gives). If it exists: compose from it. If not: run the interview below, then read `references/MUSICMD-SPEC.md` and write the `MUSIC.md` before composing anything.
2. **Interview** (only when no `MUSIC.md` exists). Ask, waiting for answers:
   1. What does this accompany, and where does it play? (video, lobby, app, on-hold…)
   2. Give one _specific_ reference — a song, artist, album, or a place-and-moment ("hotel lobby at 7am"). Reject adjective-only answers; adjectives describe a region, a reference describes a point.
   3. Mood and energy in one sentence each.
   4. Loop forever, or fixed duration? If fixed: how many seconds and what sections?
   5. Constraints: must it sit under a voice-over? Any sound to absolutely avoid?
      Then draft `MUSIC.md` per the spec, show it, save it after approval.
3. **Research the sound.** Real composers don't memorize all theory — they research what each piece needs. If the brief (or the user) names a genre, read `genres/<slug>.md` from the library below **first** — it carries that genre's sound palette with concrete Strudel sound names, canonical harmony, groove skeletons, song form, and a worked paste-ready example. If a user names an artist or song, deconstruct it into sonic DNA (next section) before composing. If neither source answers what the brief needs, research the web (playbook at the bottom).
4. **Extract 2–4 principles.** Before writing any code, write the composition brief: key, BPM, feel, and the 2–4 principles that define this piece (chord language, rhythmic feel, texture, form). More than 4 over-constrains into mechanical output; fewer than 2 is vague. Simple genres (punk, ambient) need only 2; complex ones (jazz, progressive) may need 4. Worked examples:
   - **Lo-fi hip-hop**: (1) jazz-influenced chords — m9, m7♭5, 7♭9 — with Dorian color; (2) laid-back drums at 70–90 BPM, ghost snares, slightly-behind-the-beat feel; (3) sparse pentatonic melody with lots of space, drenched in reverb/delay.
   - **EDM drop**: (1) four-on-the-floor kick with off-beat hats at 128 BPM; (2) minor key, often just two chords, heavy bass; (3) energy contrast — stripped breakdown into full drop.
   - **Jazz ballad**: (1) extended harmony (maj7, m9, 13) with smooth voice leading; (2) rubato feel, brushes, walking or pedal bass; (3) melody uses chromatic approach tones and tells a story with dynamics.
5. **Compose bottom-up**, each layer informed by the brief: harmony (chord progression) → rhythm (pulse/drums) → bass (roots) → melody → texture. Then arrange: assign frequency lanes, pan, section maps (see Composition craft).
6. **Evaluate** against the principles: does it match the genre feel — would a listener recognize the genre unprompted? Does the rhythm groove when you imagine it bar by bar? Is it musical (space, dynamics, contour), not just correct notes? Does every principle from step 4 show up somewhere audible? Fail anything → back to the relevant step.
7. **Validate** with the checklist below. **Deliver** per the output contract.

## Deconstruct references into sonic DNA

**How, not who.** An artist name is a pointer for humans, a black box for composition: it means different things to different people and invites copying. Unpack every reference (artist, song, or genre label) into technique-based descriptions before composing, and write those phrases into `MUSIC.md` — the Overview and Sound Palette should carry the DNA, not just the name.

Six dimensions — force through all of them; musical identity lives in their interaction, not in any one:

| Dimension | Ask |
|---|---|
| Rhythmic foundation | Drum character (kit composition, backbeat placement, ghost notes, fill style), tempo, subdivision (8ths/16ths/triplets), swing amount, bass technique and its relationship to the kick (locked / complementary / independent). |
| Harmonic architecture | Chord density (triads → 7ths → 9ths/11ths/13ths), modal inflections (Dorian 6th, Mixolydian ♭7), harmonic rhythm (bars per chord), melodic contour and range, dissonance tolerance. |
| Instrumental techniques | Playing styles per layer (fingerpicked, muted chank, slapped, brushed), effects chains (drive type, delay, modulation), timbre choices (neck vs bridge brightness). |
| Production aesthetics | Room/reverb depth (dry-intimate to cavernous), stereo width, dynamic range (compressed vs live), frequency balance (scooped, bass-forward, airy), which element sits loudest. |
| Genre fusion | Primary base (≈60%), secondary influence (≈30%), accent flavor (≤10%) — and which layers carry which influence (drums from A, harmony from B), or temporal split (genre X verses, genre Y choruses). |
| Energy architecture | Section map, dynamic range, peak placement (early / late / multiple), build-and-release pattern, emotional trajectory (single state / journey / oscillation). |

Conservative default sound names (safe in the REPL): drums `bd sd hh cp oh hc rim perc`, melodic `piano pluck juno moog pad sawtooth triangle sine square supersaw`, texture `fx misc`. If a name errors in the REPL, swap it — don't ship unverified names.

One-sentence DNA, when a quick summary is needed: `[rhythmic approach] + [harmonic character] + [instrumental signature] + [production aesthetic]` — e.g. "syncopated post-punk drumming over minor modal progressions, angular clean guitar with chorus effect, dry room recording with bass-forward mix".

Anti-patterns: **name-drop** ("sounds like X" instead of techniques) · **single dimension** (identity emerges from interaction) · **genre substitute** (labels are contested categories — unpack what the label means here) · **one-track trap** (analyze 3–5 tracks across eras, not just the famous one) · **technical overdose** (distill to 5–10 essential phrases; more is noise).

Ethics: combine elements from multiple analyses into something new; never replicate a signature riff or melody; never treat "reproduce artist X" as the goal.

## Composition craft (all genres)

Universal constraints first: **all pitched parts in the same key** (verify against the written-out scale); **bass lands on chord roots at strong beats** (the minimum harmonic anchor); **velocity/gain must vary** (never flat); **leave space** (rests are musical; don't fill every beat).

### Harmony

- **Registers** (MIDI): bass 36–71 (octaves 2–3; octave 1 disappears on small speakers), pads 55–80, melody 67–84.
- **Keys**: write out the scale before composing. C major: c d e f g a b. C natural minor: c d eb f g ab bb. Minor keys use the natural minor _except_ V is major (harmonic minor's raised 7th) when dominant pull is wanted — background music usually avoids that pull entirely.
Gotchas that break patterns: `<a b>` is alternation, never a chord; chords use commas inside brackets. Sharps are `fs4` / `cs4` — never `f#4`. Flats are `bb4` / `eb4`. Octave numbers: `c4` = middle C = MIDI 60. Engine bugs to design around: `.add(n)` / arithmetic on note-name patterns silently no-ops (known issue — use `.transpose(n)` instead); `.transpose()` silently drops events for sharp-spelled notes (`fs`, `cs`, `gs`, `df`) — respell to flats (`gb`, `db`, `ab`) in lanes you transpose; the default voicing dictionary silences `maj7`/`maj9` chord symbols — write `^7`/`^9` (e.g. `chord("<Db^7>")`).
- **Scale and mode colors** (offsets vs major):

| Scale/mode | Notes vs major | Color | Home |
|---|---|---|---|
| Ionian (major) | 1 2 3 5 6 (all natural) | bright, resolved | pop, country |
| Aeolian (natural minor) | ♭3 ♭6 ♭7 | sad, serious | pop/rock minor |
| Dorian | ♭3 ♭7 (natural 6) | cool minor, hopeful | funk vamps, modal jazz, lo-fi |
| Mixolydian | ♭7 | bright with an edge | rock, blues, funk |
| Lydian | ♯4 | floating, dreamy | film, ambient |
| Phrygian | ♭2 ♭3 ♭6 ♭7 | dark, Spanish | flamenco, metal |
| Harmonic minor | ♭3 ♭6, ♮7 | exotic, dramatic | classical, neoclassical metal |
| Major pentatonic | 1 2 3 5 6 | open, safe | folk, country, melodies |
| Minor pentatonic | 1 ♭3 4 5 ♭7 | raw, riff-ready | blues, rock, soul |
| Blues | minor pent + ♯4/♭5 | the cry | blues, rock |

  Formulas if you need them: major W-W-H-W-W-W-H; natural minor W-H-W-W-H-W-W.
- **Progression vocabulary by genre** (numerals; spell in the target key):
  - Pop: `I–V–vi–IV` and rotations (`vi–IV–I–V`, `I–vi–IV–V` "50s"). One chord per bar, four-chord loop.
  - Jazz: `ii–V–I` (the sentence of jazz); chains `iii–vi–ii–V–I`; tritone-sub the V (♭II7 → I) for chromatic pull.
  - Blues: 12-bar `I(4) IV(2) I(2) V(1) IV(1) I(2)` with a `V–IV–I–V` turnaround; dominant 7ths throughout; quick-change to IV in bar 2 optional.
  - Rock: `I–♭VII–IV`; minor epic `i–♭VI–♭VII` or `i–♭VI–III–♭VII`; or riffs over one–two chords.
  - Background-safe (no strong dominant): major `Imaj7 – IVmaj7 – iii7 – vi7`, `Imaj7 – vi7 – IVmaj7 – iii7`; minor `i9 – VImaj7 – iv9 – VII`, `i9 – III – iv9 – VI`.
- **Voicing**: 4–5 note chords with extensions (`[c3,e3,g3,b4,d5]` = Cmaj9) beat triads at the same gain — warmer, more cinematic. Voice-lead by common tones between chords; keep the top note moving stepwise. If the bass covers the root, upper chords may go rootless.
- **Harmonic rhythm**: decide bars-per-chord and hold it per section — 1–4 bars for ambient/funk vamps/loops, 1 bar for pop, 2 chords per bar for bebop. Changing it is itself an arrangement move.
- **Modulation** (foreground): relative major/minor is free; lift to IV for a final chorus; swap aeolian for its parallel Dorian to brighten a minor vamp.

### Melody

- **Motif first**: compose a 2–4 note cell, then develop it — repetition, transposition, inversion, rhythmic displacement (shift it a beat later), augmentation/diminution (double/halve durations), sequence (same shape up the scale). Development of one idea beats a stream of new ones.
- **Contour**: arch, descending, oscillating — pick one and let the phrase be a question (rise, tension) answered by a fall (resolution). Follow a leap with a step in the opposite direction; singable melodies stay within ~an octave.
- **Chord tones on strong beats**; passing and neighbor tones on weak beats; chromatic approach from a semitone below or above into a chord tone (the jazz move).
- **Space**: rests do half the work. For beds: pentatonic subsets of the key, a note every 1–2 bars. For foreground: still leave a bar of rest every 4–8.
- In Strudel: `n("…").scale("C:minor")` is the guaranteed-in-key tool (degrees 0–6); `.off(1/8, x => x.transpose(-12).gain(.2))` gives an octave-down answer for call-and-response.

### Rhythm & groove

- **Build order**: pulse → kick map → backbeat (snare/clap on 2 & 4, or genre equivalent) → subdivision layer (hats: 8ths, 16ths, triplets) → ghost notes → fills.
- **Swing scale**: 0 = straight (techno, funk 16ths — looseness comes from velocity, not timing); ~.05–.08 = light shuffle (house, lo-fi); heavy = triplet feel (blues shuffle, 2-step/garage). `.swing(.08)` on hats, or write swung 8ths as `[4@2 4]`.
- **Velocity groove**: accent patterns on straight grids make them breathe — `s("hh*16").gain("[.2 .5 .2 .35]*4")`. Ghost hits at gain ~.1 make a groove feel twice as fast without adding volume.
- **Syncopation**: hits on off-8ths/16ths, pushes on the "and" of 4 aimed at the next downbeat (funk's the-One gravity).
- **Cross-rhythm**: Euclidean `"bd(3,8)"` (rotate with a third arg) for world/afro pulses; `{rim ~ sh}%3` polymeter drifting against 4/4, resolving every 3 bars.
- **Call-and-response**: every layer phrases in the gaps the others leave; ask on the downbeat, answer on the push.
- **Analyzing a reference's groove**: find where you tap your foot, map kick, map snare, map hat subdivision, note ghost notes, note swing amount — then rebuild that skeleton in mini-notation.

### Bass

- **Roles**: rhythmic anchor (roots on strong beats — the minimum), melodic counterpoint (answers the melody), or rhythmic engine (funk: the second lead, answering the kick).
- **Register**: octave 2 (MIDI 36–47) for sub weight; octave-pop via `.superimpose(x => x.transpose(12).gain(.2))` for slap articulation.
- **Kick relationship**: locked (techno — bass on off-8ths between four-on-the-floor kicks), complementary (funk — bass fills where the kick isn't), independent (jazz walking: quarter notes through root–3–5 with chromatic approaches into the next root).
- **Movement vocabulary**: root–5th, root–octave, chromatic walk into the One (`~ bb2 a2 ~` resolving to `d2`), arpeggios.

### Arrangement & mix

- **Frequency lanes**: one element per lane — sub <80 Hz (kick _or_ bass, never both), 80–250 bass warmth, 250–500 body/mud risk, 500 Hz–2 kHz core/harshness risk, 2–4 kHz presence (voice-over territory — stay out if one plays), >4 kHz air. Two layers fighting → filter or pan one away.
- **Contrast between sections** via density, register, and timbre — not just volume. Cheapest move: add or remove one layer per section.
- **Dynamics tiers** (gain): foreground drums 0.3–0.9 (ghosts low, accents high), pads/chords 0.3–0.5 (sit back), melody 0.5–0.8 (expressive). Background caps ~0.6. ppp→fff maps roughly 0.05→1.0; use the full range rather than four notches of mf.
- **Tension curve**: build by adding layers, opening filters (`.lpf(saw.range(300, 4000).slow(8))`), rising lines, accelerating rolls; release by stripping to a breakdown or resolving harmony. Silence right before the loudest hit.
- **Spatial depth**: dry = forward, more `room` = further back; pan answering phrases opposite each other; give lush lanes their own `.orbit()` so reverbs don't fight.

### Humanization

Machine-perfect patterns sound dead. Vary: **gain per note** (accent patterns or `?` probability, ±.05–.1), **note lengths** (`.clip()`), **timing** (`.late(0.01)` / `.early()` micro-shifts), **events** (`.sometimes()`, `.someCycles()`, `perlin.range()` drift on gain/pan/filter). Avoid quantize-everything: a small constant lag on one layer reads as a live player sitting behind the beat (lo-fi, soul).

### Form & energy architecture

Write a section map with bar counts **and an energy rating (0–10) per section** before coding — the genre files use this notation. Common forms:

- **Verse–chorus** (pop/rock): `intro 4 | verse 8 | chorus 8 | verse 8 | chorus 8 | bridge 8 | chorus 8 | outro 4`.
- **AABA** (jazz standard): four 8-bar sections, B is the bridge.
- **12-bar blues**: `I(4) IV(2) I(2) V(1) IV(1) I(2)` — one chorus per section, solo over repeated choruses.
- **Dance arc**: `intro | build | drop | break | drop | outro` in 8/16-bar multiples (DJ-usable).
- **Strophic** (folk): same music every verse. **Through-composed** (ambient/cinematic): evolves, never returns.

Section characters: intros are atmospheric, punchy, or cold-start; the chorus lifts via density + register + timbre together; the bridge contrasts (new chord, stripped texture, meter change); outros fade, stop dead, or evolve past the loop. Peak placement: late for ballads, early-and-repeated for EDM, none for background. Verse–chorus contrast via density rather than volume is often the classier move.

In Strudel: `arrange([4, intro], [8, verse], [4, silence], …)` builds the form; `silence` is a section; layers with different section maps need leading `[n, silence]` padding.

## Background-music core

When `purpose: background` (the default assumption if MUSIC.md omits purpose), these constraints rule — grounded in functional-music practice (Muzak programming) and Eno's ambient doctrine. They override the foreground instincts above:

1. **As ignorable as it is interesting.** The music must not demand attention: no vocals, no earworm hooks, no melody that pulls focus, no sudden changes or drops.
2. **Unobtrusive harmony.** Consonant extensions (maj7, m9, add9, sus). Avoid strong dominant→tonic resolution and aggressive dominant chords — float instead. Slow harmonic rhythm: 1 bar per chord or slower.
3. **Soft dynamics, soft transients.** Pads 0.2–0.4 gain, melody 0.3–0.5, pulse 0.3–0.5, nothing above ~0.6. Choose soft onsets (pads, sine, filtered samples) over percussive attacks. `.shape(0.1–0.3)` reads as warmth; more becomes distortion.
4. **Endlessness.** The loop must never audibly repeat and the seam must be invisible: no downbeat accent that exposes bar 1. Use coprime variation periods — `.slow(9)` on one layer, `.every(7, …)` on another, `.slow(13)` on a third — so layer periods never realign (Eno's differing-tape-loop-lengths technique), plus continuous modulation (`perlin.range(400, 1800).slow(11)` on a filter, `cosine.range(0.3, 0.7).slow(13)` on pan) so the texture breathes.
5. **Frequency-lane discipline.** Mid-register warmth: bass soft and subby (octave 2), highs rolled off (`.lpf`), and if the bed sits under a voice-over, keep the total energy out of the 1–4 kHz presence region and the overall gain low — leave headroom.
6. **Tempo sweet spots.** Lobby / retail / elevator: 70–95 BPM. Spa / meditation: 60–75. Focus / productivity: 50–70, ambient and pulseless. Upbeat retail: 100–115. Music that must energize is foreground music — a different brief.

## Strudel essentials (strudel.cc REPL edition)

Sound sources — every pitched pattern needs a sound; drums use `sound()`:

```js
note("c4 eb4 g4").s("juno"); // pitched: note() + .s(soundname)
s("bd ~ sd ~"); // drums
n("0 2 4 6").scale("C:minor").s("pluck"); // scale degrees -> guaranteed in key
```

Conservative default sound names (safe in the REPL): drums `bd sd hh cp oh hc rim perc`, melodic `piano pluck juno moog pad sawtooth triangle sine square`, texture `crackle` (built-in). If a name errors in the REPL, swap it — don't ship unverified names.

Mini-notation (always in **double quotes**):

| Syntax      | Meaning                                      | Example                   |
| ----------- | -------------------------------------------- | ------------------------- |
| space       | sequence                                     | `"bd hh sd hh"`           |
| `[a b]`     | subdivide one slot                           | `"bd [hh hh] sd"`         |
| `[a,b,c]`   | **chord** (comma!)                           | `"[c3,e3,g3,b4]"`         |
| `<a b c>`   | alternation, one per cycle — **NOT a chord** | `"<cmaj fmaj>"`           |
| `*n` / `/n` | repeat / slow                                | `"hh*8"`, `"[c d e f]/2"` |
| `~`         | rest                                         | `"bd ~ sd ~"`             |
| `@n`        | elongate                                     | `"c@3 e"`                 |
| `x?`        | 50% mute                                     | `"hh*8?"`                 |
| `(p,s)`     | Euclidean                                    | `"bd(3,8)"`               |

Gotchas that break patterns: `<a b>` is alternation, never a chord; chords use commas inside brackets. Sharps are `fs4` / `cs4` — never `f#4`. Flats are `bb4` / `eb4`. Octave numbers: `c4` = middle C = MIDI 60; one octave = 12 semitones.

Tempo — 4/4 math: `setcps(BPM/120)` or `setcpm(BPM/4)` (one cycle = one bar). Set it once at the top. Other meters: 3/4 → three beats per cycle with `setcpm(BPM/3)`; 6/8 → six eighth-events per cycle.

```js
setcpm(18.5); // 74 BPM
```

Layering — in the REPL, `$:` prefixes stack patterns, one layer per line:

```js
setcpm(19);
$: sound("bd ~ ~ ~").gain(0.4);
$: note("<[c3,e3,g3,b4] [a2,c3,e3,g3]>").s("juno").gain(0.25);
```

(A single `stack(a, b, c)` expression also works; `$:` lines read better for beds.)

Structure — `structure` in MUSIC.md decides:

- **loop** (default for background): a steady generative bed — no `arrange()`. Variation comes from coprime periods + continuous signals (see background core #4).
- **fixed**: `arrange([cycles, pattern], …)` with the section map from Form. Cycle math in 4/4: seconds-per-cycle = 240/BPM, so `cycles = seconds × BPM / 240` (30s at 80 BPM → 10 cycles).

Key tools:

```js
.lpf(800).hpf(100).gain(0.3).room(0.4).delay(0.25).pan(0.5).shape(0.2)
.every(7, rev) .sometimes(x => x.fast(2)) .off(1/4, x => x.transpose(12).gain(0.1))
perlin.range(400, 1800).slow(9)   // continuous, organic
sine.range(0.2, 0.8).slow(13)     // continuous, mechanical
.transpose(-5) .rev() .jux(rev) .slow(2).fast(2) .swing(.08) .late(0.01)
```

For anything else (drum machines, chord symbols, voicing engine, filter envelopes, sidechain ducking, risers, arp engines), read `references/STRUDEL-COMPONENTS.md` — every idiom there is verified.

## Transposition

When moving a piece to a different key: compute the interval in semitones (C→E♭ = +3), shift every note by it, keep enharmonic spelling consistent (flat keys use flats: `eb`, `bb`; sharp keys use sharps: `cs`, `fs`), then re-verify every note belongs to the target scale. Roman-numeral progressions transpose for free — that's why briefs use them.

## Validation checklist (run before delivering)

**Theory**

- [ ] Every pitched note listed against the scale — none foreign (or intentional color, noted).
- [ ] Bass register 36–71, roots on strong beats.
- [ ] Chord voicings 4–5 notes, common-tone voice leading.
- [ ] Gain varies per layer and per note; rests present; not every beat filled.

**Genre & craft**

- [ ] Genre recognizable unprompted; each of the 2–4 brief principles audible somewhere.
- [ ] Melody has a motif and develops it; chord tones on strong beats; leaps recover by step.
- [ ] Groove has a skeleton (pulse → kick → backbeat → subdivision → ghosts) and a decided swing amount.
- [ ] Every layer owns a frequency lane and a pan; sections contrast by density/register/timbre.
- [ ] Humanization present: accent patterns or `?`, varied lengths, no wall of equal notes.

**Syntax**

- [ ] Mini-notation in double quotes; brackets/parens balanced.
- [ ] Chords use commas (`[c,e,g]`); no `<…>` used as a chord.
- [ ] Sharps written `fs4` not `f#4`; sound names from the conservative list (or verified in the components catalog).
- [ ] One tempo setting at top; `$:` on every layer (or one `stack()`).

**Structure & brief**

- [ ] loop: seam invisible, coprime periods present, continuous modulation present.
- [ ] fixed: `arrange()` cycle math matches the duration and section map in MUSIC.md.
- [ ] purpose background: no hooks/transients/sudden changes; headroom left; constraints from Context & Mix section honored.

Fail anything → fix, re-check. Then deliver per the output contract.

## Genre library (`genres/`)

Each genre file follows the same shape — the genre's "equivalent moment" (its emotional centerpiece), layers with concrete Strudel sound names, harmony with spelled progressions, rhythm & feel with mini-notation skeletons, structure with bar counts and energy ratings, technique list, and one complete worked Strudel example. Read the matching file before composing in that genre; steal its example as the starting skeleton.

| Family | Genres (`genres/<slug>.md`) |
|---|---|
| Electronic/Dance | `house` · `techno` · `dubstep` · `drum-and-bass` · `ambient` · `electro` · `trance` |
| Rock | `punk` · `metal` · `grunge` · `indie-rock` · `alternative` |
| Rhythmic/Groove | `hip-hop` · `randb` · `funk` · `soul` · `reggae` |
| Traditional/Roots | `jazz` · `blues` · `folk` · `country` · `classical` · `minimal` |
| Latin/World | `salsa` · `reggaeton` · `afrobeat` · `bossa-nova` · `flamenco` |
| Other | `pop` · `k-pop` · `lo-fi` · `synthwave` · `gospel` |

When composing in a genre whose file doesn't exist yet, research it (playbook below) and build the brief from the same five elements every genre file answers: key/scale conventions, chord language, rhythmic feel, texture/instrumentation, and form/energy curve.

## Research playbook (when you don't know — don't guess)

| Missing | Search |
|---|---|
| Genre's typical chords | `"{genre}" common chord progressions` |
| Scale/mode the genre uses | `"{genre}" scales modes used` |
| Drum pattern | `"{genre}" drum pattern programming` |
| BPM range | `"{genre}" typical BPM tempo` |
| A specific reference song | `"{song}" chords key BPM analysis` |
| Strudel feature | `strudel.cc {feature}` — then the components catalog |
| A voicing | Reason from intervals: root + semitone offsets |

## References

- `references/MUSICMD-SPEC.md` — the MUSIC.md format specification. **Read before creating or editing any MUSIC.md.**
- `references/MUSICMD-EXAMPLE.md` — one fully annotated worked example (background loop): brief, MUSIC.md, and the Strudel code it produced.
- `references/STRUDEL-COMPONENTS.md` — the complete Strudel component catalog by category: sound sources (drum map, banks, synths, gm instruments), pitch/tonal (scales, chord symbols, voicings), full mini-notation, time ops, conditionals, pattern effects, audio effects, signals, mixer/ducking, REPL features — plus a composites section of 20+ genre-ready idioms (Euclidean grooves, polymeter stacks, supersaw, acid envelope macro, sidechain pump, off-echo, arp engine, chord-walking roll, riser stack, coprime ambient drift, song form, frame-accurate placement). **Read when you need a component and the genre file doesn't name it.**
