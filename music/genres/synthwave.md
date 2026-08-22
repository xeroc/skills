Synthwave's equivalent moment is the gated-snare chorus — the exact bar where a dry, compressed verse suddenly opens into a cathedral of reverb that a gate slams shut again. The genre's whole emotional promise (night drive, widescreen nostalgia, neon over an empty interstate) is delivered by that one edit: huge space, tight rhythm. Everything else in synthwave — the 16th-note octave bass, the supersaw pads, the arpeggio motor, the melody that sounds like it's wearing a single glove — exists to make the gated snare hit feel like the horizon opening.

## What the gate actually is

Gated reverb is a 1980s drum trick (think big snare on era-defining pop records): snare → enormous reverb → noise gate with a fast threshold, so the reverb blooms for a fraction of a second and is chopped off abruptly. You get the size of a cathedral with the timing of a drum machine. In Strudel there's no dedicated gate, so you build the feel: `sd` (a `RolandTR707` or `RolandTR808` snare) with `room(.9)` or higher and a chopped envelope — `release(.01)`, effectively zero tail on the dry hit while the room blooms — is the signature. The chorus moment stacks that on top of four-on-the-floor kick, 16th-note hats, supersaw chord walls, and the lead melody in the upper register with a dotted-8th delay. The verse, by contrast, is deliberately dry and small: kick, snare, 8th hats, bass, nothing else. The dryness is the setup; the gate is the payoff.

## The layers

- **Kick** — `bd` with `bank("RolandTR808")`. The outrun skeleton is `bd` on 1 and the and-of-3 (`"bd ~ ~ sd ~ bd ~ sd"` as a full bar with snare); choruses go four-on-the-floor. Boomy, round, slightly soft — this genre's kick is a heartbeat, not a punch.
- **Snare with the gate** — `sd` + `bank("RolandTR707")` + `room(.95)` + `release(.01)`. Verses play it dry and small; choruses open the room. This one layer is the genre's name tag — if the budget is one detail, spend it here.
- **Hats** — `hh*8` in verses, `hh*16` with `hpf(5000)` in choruses, `[oh oh]` accents at phrase ends. Light, ticky, never loud.
- **Bass** — the motor: `sawtooth` with `shape(.2)`, `lpf` around 900. Verses play straight 8th roots (`ply(8)` on whole-bar roots); choruses switch to 16th-note octaves — `"[a1 a2]*8"` per bar — which is the single most recognizable synthwave bassline shape.
- **Pads** — `supersaw` chords, slow attack (around a second), wide (`jux(rev)` or drifting pan), filtered around 2200. They enter at the pre-chorus, not before; verses stay dry on purpose.
- **Arp** — 16th-note `triangle` arpeggio, one note per 16th up and down the chord, short decay, dotted delay. It's the motor in the intro and breakdown — often the very first thing you hear, with `lpf` slowly opening via a `saw.range(...).slow(n)` signal.
- **Lead** — `sawtooth` melody, halves and quarters (patient, singable, "daytime glove" phrasing — think thriller-era pop hooks rather than shredding), `lpf` 2600–2800, dotted-8th delay (`delay(".25:.375:.3")`), doubled an octave down in the final chorus.
- **Fills** — `mt lt` tom pairs, `[ht mt lt ht]` runs, accelerating `sd` rolls into the final chorus. Retro banks only: this genre lives in `RolandTR707`/`RolandTR808` territory.

## Sample kit

- **Kit** — `RolandTR808` + `RolandTR707` ✓ (the era's actual machines); `.bank("LinnLM1")`/`.bank("LinnDrum")` for the early-80s variant, `.bank("SimmonsSDS5")` toms for the arena fills.
- **Snare gate** — 707 snare + `room(.95).release(.01)`: the genre's name tag, unchanged.
- **Bass & leads** — synths, correctly: `sawtooth` motor, `triangle` arps, dotted delays.
- **The DX color** — `gm_epiano1` for the one electric-piano ballad moment every synthwave album owes itself; `gm_lead_5_charang` for the sharper sync-lead variant.
- No pack needed — the preloaded tiers cover synthwave. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Synthwave is minor-key diatonic with almost no borrowed anything — the neon comes from the sounds, so the chords stay clean and loop. In A minor:

- **i – VI – III – VII** — Am – F – C – G. The genre's default loop: the "neon minor" progression. Functions like a circle-of-fifths that refuses to cadence; loops forever without feeling like it needs to resolve.
- **i – VII – VI – VII** — Am – G – F – G. The stepwise rock variant; more drive, slightly darker — good for verses under the main loop's choruses.
- **i – VI – iv – V** — Am – F – Dm – E. Introduces a real dominant, so it pulls; use it when a section genuinely needs to arrive somewhere (pre-chorus, or a chorus with an actual cadence).
- **i – IV dorian vamp** — Am – D (or Dm to stay diatonic: Am – Dm). The two-chord vamp for breakdowns; modal and static, perfect for half-energy moments with the arp alone.

Harmonic rhythm is slow — one chord per bar, or two bars per chord in choruses — and the bass arpeggiates the current chord rather than playing changes, which is why four chords can carry six minutes.

## Rhythm & feel

- **Tempo** — 85–118: 85–95 for dreamy, 100–110 for the classic drive, 110–118 for darksynth aggression.
- **Verse skeleton** — `bd ~ ~ sd ~ bd ~ sd` (kick 1 and and-of-3, snare 2 and 4) over `hh*8`. Straight, machined, zero swing — the grid is a feature; the 80s drum computers didn't sway.
- **Chorus skeleton** — `bd*4` + gated `~ sd ~ sd` + `hh*16`. The four-on-the-floor lift is what makes the gate land like a horizon.
- **The bass motor** — 16th octaves: `[a1 a2]*8` per bar, root per chord. Verses: 8th roots via `ply(8)`. The constant 16th pulse is the "driving at night" sensation itself.
- **Feel devices** — dotted-8th delay on the lead (0.375 cycles at 100 bpm); slow filter openings as arrangement (`lpf(saw.range(500, 4000).slow(8))` on the intro arp); tom fills only at major section ends; `jux(rev)` width on pads.

## Structure

```
intro 8 (arp alone, filter closed, hats ticking) | verse 16 (dry: kick/snare/bass/8th hats) |
pre 8 (pads enter, hats double to 16ths) | chorus 8 (gate + supersaw + octave motor) |
verse2 8 | chorus 8 | breakdown 8 (kick 1+3, small gate, rims, pads at half gain) |
build 4 (snare roll, bass pedal + chromatic walk-up) | final chorus 8 (lead doubled at the octave) | outro 4 (one held note outlives the drums)
```

Energy holds low and flat for 24 dry bars on purpose — that's the runway — then alternates full/half with the breakdown as the only valley:

```
intro __  verse ____  pre _____  CHORUS █████  verse2 ____  chorus2 █████  breakdown ___  build ▄▄▄  FINAL ██████  outro ▂
```

## Techniques that actually create "synthwave"

- **The gated snare** — `sd` + retro bank + `room(.95)` + `release(.01)`, deployed only in choruses. Huge bloom, chopped tail, tight grid. Dry verse snare versus gated chorus snare is the arrangement in miniature.
- **The 16th-note octave bass motor** — root/octave alternation at 16ths (`[a1 a2]*8`), filtered, lightly shaped. Switching the bass from 8th roots to 16th octaves is the verse→chorus energy flip without changing tempo.
- **Supersaw wall with slow attack** — chords a second-long attack, wide voicing around `a3`, filtered. It should feel like fog with streetlights in it, not a punch.
- **The arp as motor and intro** — a 16th `triangle` arp with a slowly opening filter is the strongest possible synthwave intro; bring it back alone in the breakdown.
- **Dotted-8th delay on the lead** — the classic 80s echo: melody note, then two fading repeats per beat. It makes patient melodies sound enormous.
- **Dry-verse discipline** — no pads, no delay wash, small snare for 16+ bars. The gate only feels like sunrise because the verse was night.
- **Retro banks only** — `RolandTR707`/`RolandTR808` (or `RolandTR909`/`AkaiLinn`/`CasioRZ1` for adjacent flavors). Modern punchy kits read as 2020s electronic, not 1985 memory.
- **Patient melody** — halves and quarters, mostly stepwise, one peak note per phrase, `@`-held final notes. If the melody gets busy, it stops sounding like a night drive and starts sounding like a demo.

## Practice approach

- Reference tracks: Kavinsky "Nightcall," The Midnight "Days of Thunder," Timecop1983 "On the Run" for the dreamy side; Gunship and Carpenter Brut for the dark, faster side. Note each one's gate: how big, how chopped, and in which sections it appears.
- Program the bass motor first and live with it for two minutes — if the 16th octaves alone don't feel like motion, fix tempo or register before adding anything.
- Build the gated snare as its own experiment: same bar, sweep `room` from .2 to 1 and `release` from .3 to .01, and find the exact bloom-to-chop ratio you want.
- Write the melody last, away from the track, then sing it over the loop — if you can't, it's too busy.
- A/B your verse against your chorus with everything else muted: kick, snare, bass only. The switch should still be unmistakable.

## Example

```
// ═══ palm mall at midnight — synthwave, 100 bpm ═══
// the moment is bar 33: after 32 dry bars, the verse opens into gated snare + supersaw widescreen.
// form: intro 8 | verse 16 | pre 8 | chorus 8 | verse2 8 | chorus 8 | breakdown 8 | build 4 | final 8 | outro 4
setcpm(100 / 4) // one cycle = one bar of 4/4

// ── drums: tight and dry in verses; cathedral room chopped by a short envelope in choruses ──
const verseKit = stack(
  sound("bd ~ ~ sd ~ bd ~ sd").bank("RolandTR808").gain(.5), // kick 1 + and-of-3: the outrun skeleton
  sound("hh*8").gain(.22).hpf(5000),
)
const chorusKit = stack(
  sound("bd*4").bank("RolandTR808").gain(.6),
  sound("~ sd ~ sd").bank("RolandTR707").room(.95).release(.01).gain(.6), // THE GATE: huge room, tail chopped
  sound("hh*16").gain(.2).hpf(5000),
  sound("<~!7 [oh oh]>").gain(.3),
)
const drums = arrange(
  [8, sound("hh*8").gain(.15).hpf(5000)], // intro: just the ticking under the opening arp
  [16, stack(verseKit, sound("<~!15 [mt lt]>").gain(.35))], // one tom fill, at the end of all 16
  [8, stack(verseKit, sound("hh*16").gain(.16).hpf(5000))], // 16th hats arrive with the pad
  [8, chorusKit],
  [8, verseKit], [8, chorusKit], // verse2 + chorus2: same fight, one round shorter
  [8, stack(
    sound("bd ~ ~ ~ bd ~ ~ ~").bank("RolandTR808").gain(.45), // half energy: kick 1 and 3
    sound("~ sd ~ sd").bank("RolandTR707").room(.8).release(.01).gain(.4), // gate stays, smaller room
    sound("rim*8").gain(.12), // rims motor — the city recedes
  )],
  [4, sound("<sd*4 sd*8 sd*16 sd*16>").gain("<.2 .3 .45 .6>")], // the roll
  [8, stack(chorusKit, sound("<~!7 [ht mt lt ht]>").gain(.45))],
  [4, sound("hh*8").gain(.12).hpf(5000)],
)

// ── bass: 8th roots in verses, the 16th octave motor in choruses — Am F C G throughout ──
const bass = arrange(
  [8, silence],
  [16, note("<a1 f1 c2 g1>").ply(8).lpf(800)], [8, note("<a1 f1 c2 g1>").ply(8).lpf(1000)], // straight 8ths on the roots
  [8, note("<[a1 a2]*8 [f1 f2]*8 [c2 c3]*8 [g1 g2]*8>").lpf(1000)], // the octave motor
  [8, note("<a1 f1 c2 g1>").ply(8).lpf(800)],
  [8, note("<[a1 a2]*8 [f1 f2]*8 [c2 c3]*8 [g1 g2]*8>").lpf(1000)],
  [8, note("<a1 f1 c2 g1>").lpf(700).sustain(.9).release(.4)], // breakdown: whole-bar roots, let them ring
  [4, note("<a1 a1 a1 [a1 b1 c2]>").lpf(700)], // build: pedal, then the walk-up into the final chorus
  [8, note("<[a1 a2]*8 [f1 f2]*8 [c2 c3]*8 [g1 g2]*8>").lpf(1100)],
  [4, note("<a1@4>").lpf(600)], // outro: one note that outlives the drums
).sound("sawtooth").decay(.1).sustain(0).gain(.55).shape(.2)

// ── harmony: neon minor — supersaw pads + the 16th arp as motor ──
const pads = chord("<Am F C G>").anchor("a3").voicing().sound("supersaw").attack(1).release(2).lpf(2200).gain(.18).room(.5).jux(rev)
const arp = note("<[a3 e4 a4 c5 e5 c5 a4 e4]*2 [f3 c4 f4 a4 c5 a4 f4 c4]*2 [c3 g3 c4 e4 g4 e4 c4 g3]*2 [g3 d4 g4 b4 d5 b4 g4 d4]*2>")
  .sound("triangle").decay(.06).sustain(0).gain(.3).delay(".15:.2:.25")
const harm = arrange(
  [8, arp.lpf(saw.range(500, 4000).slow(8))], // intro: the filter IS the arrangement
  [16, silence], // verses stay dry — the chorus needs somewhere to arrive
  [8, pads],
  [8, stack(pads, arp.lpf(3500))],
  [8, silence],
  [8, stack(pads, arp.lpf(3500))],
  [8, stack(pads.gain(.14), arp.lpf(2200))], // breakdown: half the gain, half the light
  [4, arp.lpf(3000).gain(.2)],
  [8, stack(pads, arp.lpf(4000))],
  [4, pads.release(3).gain(.14)],
)

// ── lead: patient halves-and-quarters melody, dotted-8th delay, doubled at the octave at the end ──
const leadA = note("<[a4 c5 e5 d5] [c5@2 a4] [g4 a4 c5 e5] [d5@4]>").sound("sawtooth").lpf(2600).gain(.4).delay(".25:.375:.3").room(.3)
const leadB = note("<[c5 e5 a5 g5] [e5@2 d5] [c5 d5 e5 g5] [a5@4]>").sound("sawtooth").lpf(2800).gain(.42).delay(".25:.375:.3").room(.3)
const lead = arrange(
  [8, silence], [16, silence], [8, silence],
  [8, leadA],
  [8, silence],
  [8, leadA.superimpose(x => x.transpose(-12).gain(.2))],
  [8, silence], [4, silence],
  [8, stack(leadB, leadA.transpose(-12).gain(.2))], // final: the answer climbs, the octave double carries it
  [4, note("<e5@4 ~ ~ ~>").sound("sawtooth").lpf(2600).release(1).gain(.3)],
)

$: drums
$: bass
$: harm
$: lead
```
