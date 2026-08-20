---
name: music
description: "Compose music as paste-ready Strudel code from a project MUSIC.md brief. Use when the user wants background music, elevator music, ambient beds, a seamless loop, a beat, a track, a jingle, or music to accompany a video, product, lobby, app, or animation. Differentiator: reads and writes a per-project MUSIC.md file (like DESIGN.md, but for music) and outputs exactly one self-contained code block to paste into strudel.cc — no encoded URLs, no HTML scaffold, no audio setup."
---

# Music — MUSIC.md-driven Strudel composition

Compose music as Strudel code. The brief lives in a per-project `MUSIC.md` file — the same idea as DESIGN.md for visual identity: a persistent, structured description of the sound, so iterations stay consistent across sessions. Output is code the user pastes into <https://strudel.cc> — nothing else.

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
3. **Extract 2–4 principles.** Before writing any code, write down the composition brief: key, BPM, feel, and the 2–4 principles that define this piece (chord language, rhythmic feel, texture, form). More than 4 over-constrains into mechanical output; fewer than 2 is vague. If the genre/reference in `MUSIC.md` is unfamiliar, research it first: web-search `{genre} chord progressions`, `{genre} typical BPM`, `{reference song} key BPM`.
4. **Compose bottom-up**, each layer informed by the brief: harmony (chord progression) → rhythm (pulse/drums) → bass (roots) → melody → texture.
5. **Validate** with the checklist below.
6. **Deliver** per the output contract.

## Background-music core

When `purpose: background` (the default mode of this skill), these constraints rule — grounded in functional-music practice (Muzak programming) and Eno's ambient doctrine:

1. **As ignorable as it is interesting.** The music must not demand attention: no vocals, no earworm hooks, no melody that pulls focus, no sudden changes or drops.
2. **Unobtrusive harmony.** Consonant extensions (maj7, m9, add9, sus). Avoid strong dominant→tonic resolution and aggressive dominant chords — float instead. Slow harmonic rhythm: 1 bar per chord or slower.
3. **Soft dynamics, soft transients.** Pads 0.2–0.4 gain, melody 0.3–0.5, pulse 0.3–0.5, nothing above ~0.6. Choose soft onsets (pads, sine, filtered samples) over percussive attacks. `.shape(0.1–0.3)` reads as warmth; more becomes distortion. 4. **Endlessness.** The loop must never audibly repeat and the seam must be invisible: no downbeat accent that exposes bar 1. Use coprime variation periods — `.slow(9)` on one layer, `.every(7, …)` on another, `.slow(13)` on a third — so layer periods never realign (Eno's differing-tape-loop-lengths technique), plus continuous modulation (`perlin.range(400, 1800).slow(11)` on a filter, `cosine.range(0.3, 0.7).slow(13)` on pan) so the texture breathes. 5. **Frequency-lane discipline.** Mid-register warmth: bass soft and subby (octave 2), highs rolled off (`.lpf`), and if the bed sits under a voice-over, keep the total energy out of the 1–4 kHz presence region and the overall gain low — leave headroom.
4. **Tempo sweet spots.** Lobby / retail / elevator: 70–95 BPM. Spa / meditation: 60–75. Focus / productivity: 50–70, ambient and pulseless. Upbeat retail: 100–115. Music that must energize is foreground music — a different brief.

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

Gotchas that break patterns: `<a b>` is alternation, never a chord; chords use commas inside brackets. Sharps are `fs4` / `cs4` — never `f#4`. Flats are `bb4` / `eb4`. Octave numbers: `c4` = middle C = MIDI 60.

Tempo — 4/4 math: `setcps(BPM/120)` or `setcpm(BPM/4)`. Set it once at the top.

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
- **fixed**: `arrange([cycles, pattern], …)` with intro / body / outro. Cycle math in 4/4: seconds-per-cycle = 240/BPM, so `cycles = seconds × BPM / 240` (30s at 80 BPM → 10 cycles).

Key tools:

```js
.lpf(800).hpf(100).gain(0.3).room(0.4).delay(0.25).pan(0.5).shape(0.2)
.every(7, rev) .sometimes(x => x.fast(2)) .off(1/4, x => x.add(12).gain(0.1))
perlin.range(400, 1800).slow(9)   // continuous, organic
sine.range(0.2, 0.8).slow(13)     // continuous, mechanical
.add(-5) .rev() .jux(rev) .slow(2).fast(2)
```

## Theory quick kit

- **Registers** (MIDI): bass 36–71 (octaves 2–3; octave 1 disappears on small speakers), pads 55–80, melody 67–84. Bass lands on chord roots at strong beats.
- **Keys**: write out the scale before composing. C major: c d e f g a b. Minor keys use the natural minor _except_ V is major (harmonic minor's raised 7th) when dominant pull is wanted — background music usually avoids that pull entirely.
- **Roman numerals**: I/i vi/VI iii/III = tonic (rest), IV/iv ii/ii° = subdominant (motion), V vii° = dominant (tension). Function first, then voicing.
- **Voicing**: 4–5 note chords with extensions (`[c3,e3,g3,b4,d5]` = Cmaj9) beat triads at the same gain — warmer, more cinematic. Voice-lead by common tones between chords.
- **Background-safe progressions** (no strong dominant): major `Imaj7 – IVmaj7 – iii7 – vi7`, `Imaj7 – vi7 – IVmaj7 – iii7`; minor `i9 – VImaj7 – iv9 – VII`, `i9 – III – iv9 – VI`.
- **Melody**: for beds, pentatonic subsets of the key, sparse (a note every 1–2 bars), with rests doing half the work. Velocity/gain must vary — never flat.
- `n()` + `.scale()` is the guaranteed-in-key tool: degrees 0–6 of the given scale.

## Validation checklist (run before delivering)

**Theory**

- [ ] Every pitched note listed against the scale — none foreign (or intentional color, noted).
- [ ] Bass register 36–71, roots on strong beats.
- [ ] Chord voicings 4–5 notes, common-tone voice leading.
- [ ] Gain varies per layer and per note; rests present; not every beat filled.

**Syntax**

- [ ] Mini-notation in double quotes; brackets/parens balanced.
- [ ] Chords use commas (`[c,e,g]`); no `<…>` used as a chord.
- [ ] Sharps written `fs4` not `f#4`; sound names from the conservative list.
- [ ] One tempo setting at top; `$:` on every layer (or one `stack()`).

**Structure & brief**

- [ ] loop: seam invisible, coprime periods present, continuous modulation present.
- [ ] fixed: `arrange()` cycle math matches the duration in MUSIC.md.
- [ ] purpose background: no hooks/transients/sudden changes; headroom left;
      constraints from Context & Mix section honored.

Fail anything → fix, re-check. Then deliver per the output contract.

## References

- `references/MUSICMD-SPEC.md` — the MUSIC.md format specification. **Read before creating or editing any MUSIC.md.**
- `references/MUSICMD-EXAMPLE.md` — one fully annotated worked example (background loop): brief, MUSIC.md, and the Strudel code it produced.
