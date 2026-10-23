# Tension & Release — harmonic drama (reference)

The emotional engine of Western music: **consonance** (stable, "nice") vs **dissonance** (unstable, "tense"), and the motion from one to the other. Distilled theory + Strudel translations below. **Foreground tool** — background beds deliberately float instead (Background-music core #2 in SKILL.md); only the devices marked *bed-safe* belong under a bed.

## Terminology — say the precise thing

| Phenomenon | Term |
|---|---|
| The umbrella concept | **Tension and release** (consonance/dissonance) |
| Chords with jobs | **Functional harmony** — tonic (I), subdominant (IV), dominant (V); tension = moving away from the tonic toward the dominant |
| The release gesture | **Resolution**; V–I is the **perfect authentic cadence** (PAC) — the definitive tense→relieved move. **Cadence** (cadenza) is the general name for a closing formula |
| One note held over into the next chord, clashing, then dropping | **Suspension** → its **resolution** (e.g. 4–3) |
| Notes/chords from outside the key | **Chromaticism** / **borrowed chords** (♭VI, ♭VII, iv in major) — tension; pivoting back to diatonic = release |
| Whole-piece journey: stable key → distant keys → home | **Tonal journey** / round-trip modulation; sonata form builds it in: exposition (stable) → development (tense, fragmented) → recapitulation (release) |
| Holding out on the resolution | **Delayed resolution** — the longer the delay, the greater the relief |
| Blues practice | dominant 7ths worn as tonics ("the twist") — tension as color, released by the V–IV–I–V turnaround |

## Interval physics — why "nice" vs "tense"

Tension tracks ratio complexity in the overtone series: simple ratio = consonant, complex = dissonant.

| Consonant | ratio | Dissonant | ratio |
|---|---|---|---|
| unison / octave | 1:1 / 2:1 | minor 2nd | 16:15 |
| perfect 5th | 3:2 | major 7th | 15:8 |
| perfect 4th | 4:3 | **tritone** | 45:32 — max instability |
| major / minor 3rd | 5:4 / 6:5 | | |

**Prime rule:** build tension by introducing one dissonant interval _against the bass_; release by moving that dissonant note a **half step** into consonance. Not random wrong notes — one clash, deliberately placed, then resolved.

## The engine: V7 → I

G7 (G–B–D–F) → C (C–E–G): the 3rd (B) and 7th (F) form a **tritone** the ear needs to collapse inward. Voice leading — every voice moves the smallest possible distance:

| G7 voice | moves | becomes in C |
|---|---|---|
| B (3rd) | **up ½** | C (root) |
| F (7th) | **down ½** | E (3rd) |
| G (root) | stays | G (5th) |
| D (5th) | stays | D (9th) — or steps to C/E |

The two opposite-direction half steps (3rd up, 7th down) are the gravitational lock. In Strudel, voice-write both chords explicitly — never trust auto-voicing across a cadence:

```js
note("<[g2,b3,d4,f4] [c3,g3,d4,e4]>") // V7 -> I(add9): b->c up 1/2, f->e down 1/2, d stays
```

## Delay & intensify devices

Relief scales with delay and distance traveled. Ordered small → large:

- **Suspension (4–3):** `C → G7sus4 (G–C–D–F) → G7 → C`. The sus4's C clashes where B "should" be; hold it (`@2` or longer), then drop C→B (`[g2,c4,d4,f4]` → `[g2,b3,d4,f4]`), then cadence. The longer the hang, the bigger the release. *Bed-safe*: sus2/sus4 with no dominant underneath — floats, no pull.
- **Deceptive resolution:** V→vi instead of V→I — tension redirected, not released; the classic section-extender.
- **Augmented color:** raise the 5th (`[c3,e3,gs3]`) — no resolution of its own, forces motion (typically toward IV or vi).
- **♭9:** `[g2,b3,d4,f4,ab4]` — ♭9 against the bass is maximal darkness; the Ab resolves down ½ to G while the tritone resolves normally.
- **Secondary dominant:** the V7 of the chord you're forcing toward — C#7→F#m: `[cs2,f3,gs3,b3]` (spell e# as `f`). Intentionally jarring; the key change it forces _is_ the tension.
- **Borrowed chords:** ♭VI, ♭VII, iv in a major key — chromatic tension released by returning to plain diatonic.

## The long game — 8–16 bar tension arcs

When tension must span a whole section, modulate away, then travel back (example key: C):

| Bars | Move | Effect |
|---|---|---|
| 1–4 | diatonic home: `C – F – Am – G` | stable |
| 5–8 | secondary dominant (C#7) forces **F♯m** — a tritone away | jarring, maximal distance |
| 9–12 | `G7(♭9)` | peak darkness |
| 13–16 | resolve to C | euphoric — distance + alteration + delay pay off together |

Sonata logic miniaturized (exposition → development → recapitulation); the EDM build→drop arc is the same shape.

## Placement rules — 70% of the feeling

1. **Bass is 70% of it.** Root motion down a 5th (G→C) = natural release; motion in 4ths/5ths = satisfying cadences; tritone bass motion (G→C♯) = maximum tension. Plan the bass note at every cadence first.
2. **One-third rule.** Bury dissonance in the **middle voices** (pads, inner strings/guitar); keep bass and top melody consonant and singable. Dissonance in the bass = mud; in the top melody = sounds like a mistake; in the middle = felt subconsciously.
3. **Rhythmic release.** Arrive at the tense chord off the downbeat (beats 2–4); land the **release on beat 1** of the next bar — the downbeat is the most stable psychological place, and syncing the resolution to it doubles the relief. One cycle = one bar in Strudel, so the release is simply the first chord of a cycle.
4. **Hold the release.** After a big resolution, stay put 1–2 bars — let it land before moving on.

## Worked example (delayed resolution, 80 BPM)

Realizes the brief: _"C major area for 4 bars; G7 arrives beat 3 of bar 4; bar 5 G7sus4 held, then dropping to G7; resolve on the downbeat of bar 6; hold the release 2 bars."_

```js
setcpm(20); // 80 BPM, one cycle = one bar
// one element per bar: 1 Cmaj7 | 2 Fmaj7 | 3 Am7
// 4 [Cmaj7@2 G7@2]  -> G7 arrives on beat 3, off the downbeat
// 5 [G7sus4@3 G7]   -> the hang (3 beats), then C drops 1/2 step to B
// 6 C(add9)         -> textbook landing: b->c up 1/2, f->e down 1/2, d stays as 9th, ON the downbeat
// 7 Cmaj7           -> the release blooms and is held
$: note("<[c3,e3,g3,b4] [f3,a3,c4,e4] [a3,c4,e4,g4] [[c3,e3,g3,b4]@2 [g2,b3,d4,f4]@2] [[g2,c4,d4,f4]@3 [g2,b3,d4,f4]] [c3,g3,d4,e4] [c3,e3,g3,b4]>")
  .s("juno").gain(0.35);
// bass: roots, G->C down a 5th into the release = the natural-feeling resolution
$: note("<c2 f2 a2 [c2 g2] g2 c2 c2>").s("sine").gain(0.5);
```
