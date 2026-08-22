Alternative's equivalent moment is **the swell** — the four bars where the song quietly piles layer onto layer (delay guitar circling, a pad blooming, percussion thickening bar by bar) until the chorus arrives feeling less like a section change and more like a dam giving way. Where grunge flips a switch, alternative **accumulates**: the chorus is simply the place where the texture can no longer contain itself. The genre's other signature is treating meter and texture as the same material — a 6/8 bridge, a 7/8 ostinato drifting against a 4/4 kit — so even the time signature feels like something that grew.

## What the swell actually is

Mechanically: one new layer enters per bar (or per two bars), each louder or brighter or denser than the last — hats, then shaker 16ths, then toms, then snare — while the harmony stays put. Nothing about the chords changes during the swell; the rising is purely orchestration, which is why it feels inevitable rather than manipulated. The chorus that follows is usually **half-time** (`bd ~ ~ ~ sd ~ ~ ~`): the density peak plus the tempo half = enormous. Two other load-bearing moments: **the drop-out bar** — one bar of near-silence (pad only, maybe reversed air) right before the final chorus, the held breath that sizes the landing — and **the dissolve**, an outro where the filter closes (`lpf` sweeping down) as layers fall away. Grunge detonates; alternative tide-changes.

## The layers

- **Clean delay guitar** — `pluck` sus2 arpeggios with `delay(".2:.21:.4")` (high feedback): the figure circles behind itself, one guitarist sounding like three. This is the genre's lead instrument even when a singer exists.
- **Strum guitar** — `gm_overdriven_guitar` at modest gain with `lpf(2500)` and `shape(.3)`: big but rounded, choruses only, sus/triad voicings through a syncopated `.struct()`.
- **Pad** — `gm_synth_strings_1`, `attack(1.2)` or slower, `room(.9)`: the floor that's always almost audible; it blooms, it never attacks.
- **Bass** — `triangle` root pulses, sparse (`a1 ~ ~ a1`), more felt than followed; when it moves, it's an event.
- **Drums** — verses: kick push `bd ~ ~ bd` + rim backbeat + 8th hats. Swells: `sh*16`, tom 8ths, snare 8ths entering bar by bar. Choruses: half-time with open hats and a crash per bar. Bridge: six-pulse bars.
- **Air** — `sound("wind")` through a drifting `lpf(saw.range(300,2400).slow(4))`: the breath that grows; reversed (`speed(-1)`) for the drop-out bar.
- **Voice** — `gm_voice_oohs`, high and wide, entering late; it's a texture that occasionally words.

## Sample kit

- **Clean guitar** — `pluck` + delay (the lead); `gm_electric_guitar_clean` when the arpeggio needs a real electric body.
- **Strum** — `gm_overdriven_guitar` at modest gain under `lpf(2500)`; big but rounded.
- **Pad** — `gm_synth_strings_1`; `gm_pad_warm`/`gm_pad_bowed` for slower, less orchestral blooms.
- **Bass** — `triangle` pulses (felt-not-followed, synth-correct); `gm_electric_bass_finger` for the plugged-in variant.
- **Air** — Dirt `wind` through the drifting filter; `space` for the deeper breakdowns.
- No pack needed — the preloaded tiers cover alternative. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Key of A minor. Vocabulary: sus2 chords (the alternative chord — `[a2,b2,e3]`, `[f2,g2,c3]`, `[c3,d3,g3]`, `[g2,a2,d3]`), add9 color, and modality instead of dominant function: no V7 pulls, just neighbors around a drone.

- **The verse drone: i–bVII** — Am to G (`[a2,e3]` to `[g2,d3]`, arpeggiated `[a2,b2,e3,a3]` / `[g2,a2,d3,g3]`) — two chords, four bars each if necessary; the delay does the movement.
- **The loop: i9–bVI–bIII–bVII** — Asus2, F, C, G (`[a2,b2,e3] [f2,a3,c4] [c4,e4,g4] [g3,b3,d4]`) — the sus2 on the i keeps home unresolved; the loop never cadences, it just cycles.
- **The chorus lift: bVI–bVII–i** — F, G, Am (`[f3,a3,c4] [g3,b3,d4] [a3,c4,e4]`) — stepwise climb into the tonic; use 3 bars each in a 12-bar final chorus so the arrival stretches.
- **The odd-meter vamp** — a 7/8 ostinato on `[e4 d4 c4 b3 c4 d4 b3]` via `.slow(7/8)`: seven eighth-pulses per repetition against the 4/4 kit, realigning every 7 bars — make the section exactly 7 bars so it resolves on the section boundary.

## Rhythm & feel

95–125 bpm; the example runs 104. The verse pushes (kick on 1 and the "and" of 3), the chorus halves (snare on 3), and the contrast between push and sprawl is the genre's groove signature. One cycle = one bar of 4/4 unless stated; the 6/8 bridge reinterprets the same cycle as six eighth-pulses — the clock never changes, only the internal subdivision, which is exactly how rock bands fake a meter change without a conductor.

- **Verse push** — `bd ~ ~ bd` + `~ rim ~ rim` + `hh*8`
- **The swell ladder** — `<sh*16 [sh*16 ht*8] [ht*8 sd*8] sd*16>` with gain `"<.08 .12 .18 .28>"`: one rung per bar
- **Half-time chorus** — `bd ~ ~ ~ sd ~ ~ ~` + `[~ oh]*4` + crash per bar
- **6/8 bridge** — `[bd ~ ~ sd ~ ~]`: six pulses per cycle, kick on 1, snare on 4; guitar arps become `[a3 ~ c4 ~ e4 ~]`
- **7/8 ostinato** — `note("e4 d4 c4 b3 c4 d4 b3").slow(7/8)` over straight `bd*4` + `hh*8`: the realignment is the drama

## Structure

intro (figure alone) 4 | verse 8 | swell 4 | chorus 8 | verse 8 | swell 4 | chorus 8 | 6/8 bridge 8 | 7/8 break 7 | drop-out 1 | final chorus 12 | dissolve 4 — 76 bars, just under three minutes at 104. The odd numbers are on purpose: the 7-bar break realigns exactly at its end, and the 1-bar drop-out sizes the 12-bar finale.

```
// energy: 2 - 3 - 5 - 8 - 3 - 5 - 8 - 4 - 6 - 0 - 9 - 3
// the 0 before the 9 is the whole trick: the drop-out sizes the landing
```

## Techniques that actually create "alternative"

- **Accumulation dynamics** — one layer per bar with rising gains during the swell; if you change chords mid-swell you've written a pre-chorus, which is a different genre's move.
- **Dotted-8th delay circles** — `delay(".2:.21:.4")` with high feedback on the clean guitar; melodies are written *to the echo*, landing between the repeats rather than on them.
- **Push verse, half-time chorus** — `bd ~ ~ bd` versus `bd ~ ~ ~ sd ~ ~ ~`: the tempo never changes but the chorus arrives sprawling.
- **The 6/8 bridge** — six pulses per cycle on every layer at once (`[bd ~ ~ sd ~ ~]`, `[a3 ~ c4 ~ e4 ~]`); because the cycle duration is unchanged, the shift reads as texture, not math.
- **The 7/8 ostinato** — `.slow(7/8)` on a 7-note figure over straight 4/4 kit; they realign every 7 bars, so a 7-bar section ends resolved. One per song.
- **sus2/add9 modal vocabulary** — `[a2,b2,e3]` shapes and no dominant sevenths; home stays provisional, which is the mood.
- **Filter drift as emotion** — `lpf(saw.range(300,2400).slow(4))` or `perlin.range(...)` on pads and air; the same chord opens and closes like weather.
- **The drop-out bar** — one bar of pad (and reversed `wind`) before the final chorus: silence as the cheapest amplification there is.

## Practice approach

- Arrange a single chord loop with six layers entering one per bar and no gain ride; if it doesn't swell, reorder the layers (brighter later), don't add any.
- Write a melody that lands in the gaps of its own delay echo, not on the beats.
- Build the 6/8 bridge by re-subdividing the existing cycle (six pulses) while the pad plays what it already played — feel how little has to change.
- Give yourself one 7-bar odd-meter window per song and make the realignment land on the section boundary.
- Audit dynamics by counting simultaneous layers per section: intro 1, verse 3, swell 6, chorus 8 is a working curve.

## Example

```
// ═══ glass cathedral — alternative in A minor, 104bpm, texture-first ═══
// form: intro 4 | verse 8 | swell 4 | chorus 8 | verse 8 | swell 4 | chorus 8 | 6/8 bridge 8 | 7/8 break 7 | drop-out 1 | final chorus 12 | dissolve 4
// energy: 2 - 3 - 5 - 8 - 3 - 5 - 8 - 4 - 6 - 0 - 9 - 3. the chorus arrives like a dam giving way
setcpm(104 / 4) // one cycle = one bar of 4/4

// ── clean guitar — sus2 arpeggios, circling in high-feedback delay ──
const vArp = note("<[a2,b2,e3,a3]!2 [f2,g2,c3,f3]!2 [c3,d3,g3,c4]!2 [g2,a2,d3,g3]!2>").gain(.4) // i bVI bIII bVII, 2 bars each
const arp6 = note("<[a3 ~ c4 ~ e4 ~]!2 [f3 ~ a3 ~ c4 ~]!2 [g3 ~ b3 ~ d4 ~]!2 [a3 ~ c4 ~ e4 ~]!2>") // bridge: six pulses per cycle = 6/8

const clean = arrange(
  [4, note("<[a2,b2,e3,a3]!4>").gain(.35)], // intro: the figure, alone, circling
  [8, vArp],
  [4, vArp.gain(.45)], // swell: same figure, brighter — the layers do the rising
  [8, vArp.gain(.3)],  // chorus: tucked under the strums
  [8, vArp],
  [4, vArp.gain(.45)],
  [8, vArp.gain(.3)],
  [8, arp6.gain(.42)], // 6/8 bridge: same clock, six pulses
  [7, silence],        // the 7/8 break belongs to the ostinato alone
  [1, silence],        // drop-out: only pad and reversed air breathe here
  [12, vArp.gain(.3)],
  [4, vArp.gain(.25).lpf(1800)], // dissolve: the door closes
).sound("pluck").room(.35).delay(".2:.21:.4")

// ── strums — overdriven but rounded, choruses only ──
const chorusStrum = note("<[a3,c4,e4]!2 [f3,a3,c4]!2 [c4,e4,g4]!2 [g3,b3,d4]!2>").struct("[x ~ ~ x ~ x ~ x]").gain(.55)
const finalStrum = note("<[a3,c4,e4]!3 [f3,a3,c4]!3 [c4,e4,g4]!3 [g3,b3,d4]!3>").struct("[x ~ ~ x ~ x ~ x]").gain(.6) // 3 bars per chord = the stretched 12

const swells = arrange(
  [16, silence],
  [8, chorusStrum],
  [12, silence],
  [8, chorusStrum],
  [16, silence], // bridge + break + drop-out: texture only
  [12, finalStrum],
  [4, note("[a3,c4,e4]@4").gain(.5)],
).sound("gm_overdriven_guitar").lpf(2500).shape(.3).room(.4)

// ── pad — the floor that never attacks; it blooms ──
const padArp = note("<[a3,c4,e4]!2 [f3,a3,c4]!2 [c4,e4,g4]!2 [g3,b3,d4]!2>").attack(1.2).release(1.5)
const pad = arrange(
  [4, note("[a3,c4,e4]@4").attack(1.5).release(2).gain(.12)],
  [8, padArp.gain(.14)],
  [4, padArp.gain(.2)],
  [8, padArp.gain(.24)],
  [8, padArp.gain(.14)],
  [4, padArp.gain(.2)],
  [8, padArp.gain(.24)],
  [8, note("<[f3,a3,c4]!4 [g3,b3,d4]!4>").attack(1.5).release(2).gain(.18)],
  [7, silence],
  [1, note("[a3,c4,e4]@4").attack(2).release(3).gain(.2)], // the drop-out: only the pad breathes
  [12, padArp.gain(.26)],
  [4, note("<[a3,c4,e4] [g3,b3,d4]>").attack(1.5).release(3).gain(.18)],
).sound("gm_synth_strings_1").room(.9)
$: pad

// ── bass — triangle pulses, sparse; when it moves, it's an event ──
const bassV = note("<[a1 ~ ~ a1]!2 [f1 ~ ~ f1]!2 [c2 ~ ~ c2]!2 [g1 ~ ~ g1]!2>").gain(.55)
const bass6 = note("<[f1 ~ ~ c2 ~ ~]!2 [g1 ~ ~ d2 ~ ~]!2 [a1 ~ ~ e2 ~ ~]!2 [a1 ~ ~ e2 ~ ~]!2>").gain(.55)
const bassF = note("<[a1 ~ ~ a1]!3 [f1 ~ ~ f1]!3 [c2 ~ ~ c2]!3 [g1 ~ ~ g1]!3>").gain(.6)

const bass = arrange(
  [4, note("[a1 ~ ~ ~]").gain(.5)],
  [8, bassV],
  [4, bassV],
  [8, bassV],
  [8, bassV],
  [4, bassV],
  [8, bassV],
  [8, bass6],
  [7, silence],
  [1, silence],
  [12, bassF],
  [4, note("a1@4").gain(.5)],
).sound("triangle").gain(.55)
$: bass

// ── drums — push verses, ladder swells, half-time choruses, six-pulse bridge ──
const kitV = stack(sound("bd ~ ~ bd").gain(.45), sound("~ rim ~ rim").gain(.3), sound("hh*8").gain(.15))
const swellPerc = sound("<sh*16 [sh*16 ht*8] [ht*8 sd*8] sd*16>").gain("<.08 .12 .18 .28>") // one rung per bar
const kitC = stack(sound("bd ~ ~ ~ sd ~ ~ ~").gain(.6), sound("[~ oh]*4").gain(.28), sound("<cr ~ ~ ~>").gain(.35))
const kit6 = stack(sound("[bd ~ ~ sd ~ ~]").gain(.5), sound("rim ~ rim ~ rim ~").gain(.2)) // one cycle = one bar of 6/8
const kit7 = stack(sound("bd*4").gain(.5), sound("hh*8").gain(.2)) // straight 4 under the 7/8 ostinato: the drift you came for
const kitFin = stack(
  sound("bd ~ ~ ~").gain(.6).duckorbit("2:3").duckdepth(.45).duckattack(.2), // the kick breathes everything else
  sound("~ ~ ~ sd ~ ~ ~").gain(.5),
  sound("[~ oh]*4").gain(.3),
  sound("<cr ~ ~ ~>").gain(.35),
)

const drums = arrange(
  [4, silence],
  [8, kitV],
  [4, stack(kitV, swellPerc)],
  [8, kitC],
  [8, kitV],
  [4, stack(kitV, swellPerc)],
  [8, kitC],
  [8, kit6],
  [7, kit7],
  [1, silence], // the drop-out: the drums sit out the held breath
  [12, kitFin],
  [4, sound("hh*8").gain(.1)],
)
$: drums

// ── air — wind noise through a drifting filter; reversed for the drop-out ──
const air = arrange(
  [12, silence],
  [4, sound("wind").gain(.1)],
  [8, sound("wind").gain(.06)],
  [8, silence],
  [4, sound("wind").gain(.1)],
  [8, sound("wind").gain(.06)],
  [8, silence],
  [7, silence],
  [1, sound("wind").speed(-1).gain(.12)], // the inhale before the final chorus
  [12, sound("wind").gain(.08)],
  [4, sound("wind").gain(.05)],
).lpf(saw.range(300, 2400).slow(4))
$: air

// ── the 7/8 ostinato — seven eighth-pulses per repetition over the 4/4 kit; realigns every 7 bars ──
const sev8 = arrange(
  [52, silence],
  [7, note("e4 d4 c4 b3 c4 d4 b3").slow(7/8).gain(.5)],
  [17, silence],
).sound("gm_overdriven_guitar").lpf(1800).room(.3)
$: sev8

// ── vocals — oohs, high and wide, arriving late ──
const vox1 = note("<[e5@3 ~] [c5 d5 e5] [d5@3 ~] [b4 c5 d5] [c5@2 d5] [e5@2 g5] [e5@4] [~ c5]>").gain(.3)
const voxFin = note("<[e5@3 ~] [c5 d5 e5] [g5@3 ~] [e5 d5 c5] [d5@2 e5] [g5@2 e5] [c5@4] [~ a4] [c5@2 d5] [e5@2 d5] [b4@4] [a4@4]>").gain(.32)

const vox = arrange(
  [36, silence],
  [8, vox1],
  [8, note("<c5@4 ~ [e5 d5] ~>").gain(.2)], // bridge hum
  [8, silence],
  [12, voxFin],
  [4, note("<e5@4 ~>").gain(.2)],
).sound("gm_voice_oohs").room(.6).jux(rev)
$: vox

$: clean
$: swells
```
