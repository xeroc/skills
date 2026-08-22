Ambient's equivalent moment is **the shift** — the change you can't timestamp. No drop, no downbeat, no cadence: a piece is a room with slow weather, and the one event it may contain is a harmonic relocation — C^7's field giving way to Am9's — that you only notice after it has finished happening. Eno's doctrine from *Music for Airports* is the spec sheet: "as ignorable as it is interesting." It must survive playing under conversation and reward headphones. Everything technical follows from that one sentence: no pulse you can tap, no bar-line accents, no repeat you can catch.

## What the shift actually is

The composition is a crossfade architecture: three to six layers, each with its own long period, each entering and leaving so slowly that the envelopes smear past every boundary. The single event — one chord field replacing another, one layer blooming once — is placed about two-thirds through, where a drop would be, and it happens *unannounced*: no riser, no roll, just one field fading while another thickens. The test for a shift: scrub the timeline and try to point at the moment it changed. If you can, your envelopes are too short. Attack and release are the rhythm section here; 6–12 second envelopes turning a section change into a crossfade is the core craft of the genre.
The failure modes are all rhythmic in disguise: a loop that repeats, a layer that enters on a barline, a swell with a tempo. Every repair is the same repair — make it slower, make it off-grid, or make it aperiodic.


## The layers

- **Drone** — the floor: `note("c2").sound("sine")` sustained, plus its octave at lower gain. A near-unison neighbor (a semitone away, very quiet) adds slow beating — tension you feel rather than hear.
- **Pad bed** — `gm_synth_strings_1` with `attack(8).release(12).room(1)`; one chord per 4–16 bars, voiced with `.anchor("c4").voicing()`. The harmonic identity of the piece.
- **Synth cloud** — `triangle` for pure and weightless, or `supersaw` blurred by `lpf(800)` for warmer air; notes from a pentatonic scale, sparsely.
- **Sparkle** — `gm_music_box`, `pluck`, or single `piano` notes; very sparse (a handful per minute), `degradeBy(.3)`–`.5)` for grain, one `delay` and lots of `room`.
- **Voices** — `gm_voice_oohs` low in the mix; wordless breath is the genre's human element.
- **Line instrument** — `gm_flute` long tones, one note per minute or slower; the closest thing to a melody the genre allows, and it should never phrase to a barline.
- **Air** — the `wind` sound at gain .04 with `lpf(perlin.range(400, 1800))`: the sound of the room itself, always moving, never repeating.
- **Pulse (optional)** — one soft `triangle` blip every few bars, off the strong beats. Never a kit; the moment it grooves, you've written downtempo.

## Sample kit

- **Drones & pads** — `sine`/`triangle`/`supersaw` + `gm_synth_strings_1`; `gm_pad_warm`/`gm_pad_halo`/`gm_pad_bowed` are preloaded alternatives with slower, softer grains.
- **Sparkle — the VCSL upgrade** — `wineglass` `wineglass_slow` `kalimba` `glockenspiel` `harp` `folkharp`: real resonance instead of synthesized twinkle, pitched multisamples so `note()` stays true.
- **Line instrument** — `gm_flute`; VCSL `recorder_alto_sus` for a breathier, less classical line.
- **Air** — Dirt `wind`/`space`/`crow`: rooms, weather, and the occasional bird, all preloaded.
- No pack needed — the preloaded tiers cover ambient doctrine. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Fields, not progressions: each "chord" holds 16–32 bars, and "movement" means one field replacing another without cadence.

- **The relocation** — **C^7 for 32 bars, then Am9 for 32** (relative minor, no pivot chord). The default ambient move: same pitch collection, new gravity, no announcement.
- **The lydian pair** — **C^7 ↔ D^7**, alternating on a slow period. The raised 4th of D against C's root is weightless tension that never needs resolving — lydian is the ambient mode.
- **The aeolian pair** — **Am9 – F^9**, alternating every 16 bars. Darker, patient; works under a `gm_flute` line.
- **The parallel drift** — **C^7 – Db^7 – B^7**, semitone planing. Reads as the tape speeding up and slowing down; use once per piece at most.

Voice every field with `chord(...).anchor("c4").voicing()`; the anchor matters more than the symbol, because it fixes the register the piece lives in.

## Rhythm & feel

- **Tempo**: pulseless, or nominal 50–70bpm that nothing enforces. `setcpm(60/4)` is a convenient clock, not a beat.
- **The coprime rule** — give every layer its own prime-numbered period: one breathes on `.slow(9)`, another on `.slow(7)`, a pan drifts on `.slow(11)`, sparkle mutates `.every(5)`. Total alignment takes the product of the periods, so the mix never repeats within the piece. This is the single most important rhythm decision in the genre.
- **Envelopes are the groove** — `attack` and `release` times (2–12 seconds) decide when things are heard; note placement barely matters.
- **No bar-line accents** — nothing lands on the downbeat strongly enough to establish one; long `@` elongations and `<a!3 b!2>`-style sparse patterns keep things off the grid.
- **Continuous signals for continuous change** — `perlin.range(lo, hi)` on `gain`/`lpf`/`pan`/`speed` gives motion with no period at all: change you can't timestamp.
- **Long tails as glue** — a shared `delay(".8:.4:.5")` and generous `room` on the sparse layers stitches them into one space; dry ambient layers read as unrelated sound files.

## Structure

Crossfade architecture, thought about in minutes, not bars:

```
0:00 drone + air ─ 1:00 pad bed joins ─ 2:00 sparkle/cloud ─ 4:00 the shift (field A → field B, voices bloom once) ─ 6:00 layers thin ─ 8:00 drone alone
energy ▁▁▂▂▂▃▃▄▄▅▄▄▄▃▃▂▂▁▁  (one gentle swell, centered on the shift)
```

One layer enters (or leaves) per minute at most. The shift sits about two-thirds in. The ending is a release, not a cadence: layers exit by crossfade until the drone and air are left holding the room.

## Techniques that actually create "ambient"

- **Coprime loop lengths** — `.slow(9)` against `.slow(7)` against `.slow(5)`: no two layers realign within the piece, so a five-layer stack of loops behaves like an evergreen texture. Alignment you can hear is the failure mode.
- **Perlin on everything slow** — `gain(perlin.range(.06, .16))`, `lpf(perlin.range(400, 1800))`: aperiodic drift is the genre's sense of life; `sine.slow(n)` is the periodic fallback when you want a swell with a shape.
- **Envelope-as-rhythm** — `attack(8).release(12)` on pads makes section changes crossfades; the boundary disappears into the fade. If a layer's entry is audible as an event, double its attack.
- **Register strata** — sine drone at the bottom, pad bed in the middle, sparkle up top, air everywhere. Each stratum stays sparse; density comes from the stack, not the parts.
- **The near-unison beat** — two sines a semitone apart at very different gains produce slow amplitude beating: motion from physics, not from a pattern. One pair per piece is plenty.
- **The octave shadow** — `superimpose(x => x.transpose(-12).gain(.1))` under a pad deepens it without new harmony; at ambient gain levels it reads as warmth.
- **Silence as material** — minutes where almost nothing happens are content; Eno's tape hiss (your `fx` air layer) is the glue that keeps emptiness from sounding like a mistake.
- **One event per piece** — a single swell (`gain(sine.slow(30).range(0, .12))` is a two-minute bloom-and-recede) placed at the drop position. Two events and it's post-rock.
- **Field voicing discipline** — keep every field anchored in the same octave pocket (`.anchor("c4")` and friends); register leaps between fields read as key changes, which ambient has no use for.

## Practice approach

- Start with a drone and add one layer per minute; resist rhythm the whole way — if you feel the urge to add a kick, slow something down instead.
- Run Eno's own test: play it quietly while doing something else, then on headphones. It must survive both; fix whichever fails.
- Audit for accidental alignment: listen specifically for moments where layers line up, and re-prime one period (9 → 11) to break it.
- Write one piece using only two fields and the relocation; if it holds interest for six minutes, the architecture works.
- Place the shift last: build the whole piece on field A, then choose the relocation point by ear, not by plan.
- Check the ending crossfades — ambient pieces end by releasing layers, never by stopping them.

## Example

```
// ═══ slow glass — ambient, nominal 60bpm, effectively pulseless ═══
// architecture: five layers, each on its own coprime period (9, 7, 13, 11, perlin) so the mix never repeats;
// one event per piece: the harmony relocates from C^7 to Am9 about two-thirds in, unannounced
setcpm(60 / 4) // one cycle = four seconds — slow enough that nothing implies a beat

// ── drone — the floor: c2 and its octave, plus a near-unison neighbor for slow beating ──
$: stack(
  note("c2").sound("sine").gain(.3),
  note("c3").sound("sine").gain(.15),
  note("b2").sound("sine").gain(.04), // a semitone away: a beat you feel, not hear
).attack(6).release(8).room(.6)

// ── pad bed — one chord per four bars, envelopes longer than the chords: the crossfade trick ──
$: chord("<C^7!4 Am9!4>").anchor("c4").voicing()
  .sound("gm_synth_strings_1")
  .attack(9).release(12).room(1)
  .gain(sine.range(.1, .2).slow(9))   // breathing on a 9-cycle period
  .pan(sine.slow(13).range(.35, .65)) // drifting on its own coprime period

// ── mid cloud — triangle notes from c minor pentatonic, a 16-step phrase slowed to 7 cycles ──
$: n("<~ 2 ~ 4 ~ ~ 7 ~ 4 ~ ~ 2 ~ ~ ~ ~>").scale("c5:minor:pentatonic")
  .sound("triangle").attack(2).release(6)
  .slow(7)                            // the phrase spans 7 cycles — never realigns with the pad
  .gain(perlin.range(.06, .16))
  .delay(".75:.35:.4").room(1)

// ── sparkle — music box, degraded, reversed every 7th cycle: never the same twice ──
$: note("<g5 ~ ~ ~ c6 ~ ~ ~ ~ ~ e6 ~ ~ ~ ~ ~>")
  .sound("gm_music_box")
  .every(7, x => x.rev)
  .degradeBy(.4)
  .gain(perlin.range(.05, .15))
  .room(1).delay(".9:.3:.45")

// ── air — the room itself: filtered noise wandering, aperiodic ──
$: sound("wind").gain(.045)
  .lpf(perlin.range(400, 1800))
  .pan(sine.slow(11).range(.2, .8))
  .room(1)

// ── the event — one swell, once: voices bloom toward the Am9 field and recede ──
$: chord("Am9").anchor("a3").voicing()
  .sound("gm_voice_oohs")
  .attack(4).release(10).room(1)
  .gain(sine.slow(30).range(0, .12)) // half a sine period ≈ two minutes up, two minutes down
```
