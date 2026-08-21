Techno's equivalent moment is **the sweep** — not a drop but a long morph. Where other genres spend their energy on the bar where everything lands, techno spends it on the sixteen bars where a single loop slowly opens: a filter crawling upward, a rumble thickening, one muted stab surfacing every eighth bar. The equivalent of the breakdown-into-drop arc is a *filter journey* — the same pattern heard through a closing filter, then through an opening one, so the return of clarity feels like the event. If nothing changes over 32 bars except one parameter, you're doing it right.

## What the sweep actually is

Pick one loop — kick, rumble, one percussion figure, maybe one stab — and keep the notes identical for minutes. The composition lives in slow parameter change: a lowpass opening over 16 bars (`lpf(saw.range(300, 4000).slow(16))`), a mute that pulls the hats for 8 bars, a stab that gains an octave flicker at the peak. Hypnosis mechanics are strict: a dead-straight grid, exactly one displaced or syncopated layer, and one change at a time — never two. The breakdown is the only drama: kick out, drone and the stab's minor third exposed, then the kick returns *before* the full loop does, so the peak is the loop reassembling rather than a new thing arriving.

## The layers

- **Kick** — `bd` from `.bank("RolandTR909")`, gain up to 1, `shape(.3)` for baked-in grit. Heavier and shorter-toned than the house kick; it is both the rhythm and the bass fundamental.
- **Rumble** — the kick's own reverb tail, lowpassed into a bassline: `s("bd*2").bank("RolandTR909").room(1).lpf(140)`. The defining techno low end — the room plays the bass part.
- **Sub drone** — `note("a0").sound("sine")`, sustained, gain around .2: felt not heard, the floor under the floor.
- **Hats** — offbeat 8ths `"[~ hh]*4"` plus flat, quiet 16ths `hh*16`. Zero swing. Open hats only at the peak.
- **One perc loop** — `rim(3,8)` euclid, or a `{cb ~ sh}%3` polymeter. This is the *only* syncopated element in the whole track; everything else is grid.
- **The one stab** — a single note (`a3`) or a minor-third pair (`[a3,c4]`), `sawtooth`, `lpf(500)`, short decay, appearing every 4–8 bars. Discipline: one stab. A second melodic idea is a different genre.
- **Noise and air** — the `fx` sound at low gain with a perlin-filtered sweep, or hats sped up as a riser. Techno's "melody" is usually filtered noise.

## Harmony

Almost no harmony — drones, one- and two-chord loops, minor and phrygian. Movement comes from filters, not chord changes.

- **The drone** — **Am** forever. A aeolian: no progression at all; the pitch content of the track is one root, and the filter journey is the development.
- **The phrygian pivot** — **Am – Bbm** (i – bII in A phrygian). The half-step slide is the darkest two-chord move in dance music; one bar each, once per 8.
- **The hypnotic loop** — **Am – F** (i – bVI), or extended **Am – F – G** (i – bVI – bVII). Diatonic, weightless, loops forever without asking a question.
- **The rave ghost** — a single **Dm** stab or the bare minor-third `[a3,c4]`. A memory of hardcore, one hit at a time.

## Rhythm & feel

- **Tempo**: 125–140 — hypnotic/melodic techno 125–130, peak-time 132–138, harder gear up to 140.
- **Kick**: `bd*4` — dead straight, no ghost kicks, no syncopation. Ever.
- **Hats**: `"[~ hh]*4"` offbeat 8ths; 16ths `hh*16` flat or with a 2-step velocity pattern; `"[~ oh]*4"` reserved for the peak.
- **The funk budget**: `rim(3,8)` or `{cb ~ sh}%3` — one euclid/polymeter carries *all* the groove. Two syncopated layers and it stops being techno.
- **Rumble**: `bd*2` through `room(1)` + `lpf(140)` — continuous, offbeat-agnostic; it glues the kick to the room.
- **Builds**: double the hat density (`every(4, x => x.fast(2))` on hats) and run snare rolls `<sd*4 sd*8 sd*16 sd*16>` — but the melodic material never changes during a build.
- **Feel**: zero swing. The shuffle you hear in good techno comes entirely from the one displaced perc layer over the straight grid.

## Structure

Filter-journey form — 16-bar arcs, DJ-legal intro and outro (drums and rumble only), one element entering or leaving every 8 bars:

```
intro 8 | perc 8 | hats 8 | stab 8 | journey 16 | breakdown 8 | build 4 | peak 16 | outro 8
energy ▂▂▃▃▄▄▅▅▅▅▆▆▆▆▂▂▁▂▇▇▇▇▇▇▅▄▃
```

The journey is the center: the same loop with `lpf` opening over 16 bars. The peak is not new material — it is the identical loop with everything unmuted, which is the whole thesis of the genre.

## Techniques that actually create "techno"

- **Rumble bass** — reverb the kick, lowpass the reverb at ~140Hz, layer it under the dry kick. One sound does kick, bass, and room.
- **One-stab discipline** — a single muted note every 4–8 bars reads as enormous; two competing riffs read as trance. The stab's power is its scarcity.
- **The filter journey** — automate one `lpf` across 16 bars (`saw.range(lo, hi).slow(16)`) on the perc loop or hats. Slow enough to be hypnotic, fast enough to be felt once per section.
- **Subtractive arrangement** — mute and unmute identical loops; write no new patterns after bar 8. The arrangement is the mixer, not the sequencer.
- **Euclid as the only syncopation** — `rim(3,8)` over `bd*4` gives the 3-against-4 drift without touching the grid.
- **Slow signals for slow change** — `perlin.range(400, 1800)` on a noise layer's `lpf`, `sine.slow(8)` on a pan: change you can't timestamp, which is what "hypnotic" means technically.
- **Loop mutation at the edges** — `.every(8, ...)`, `.someCycles(...)`: small mutations on long periods, never bar-to-bar.
- **Breakdown economy** — kick out, keep the drone, expose the stab's minor third, bring the kick back one section *before* the rest. The peak assembles itself.

## Practice approach

- Build an 8-bar loop of kick + rumble + hat + one euclid, then mutate exactly one parameter per 16 bars and listen back to 4 minutes of it.
- Apply the removal test: every 8 bars, take one thing out before you add anything.
- Run the one-stab test: if your stab would still feel special arriving every 8th bar, it's right; if you're bored, the problem is the loop, not the stab rate.
- Map the energy on paper every 8 bars — techno's graph should be long arcs, not spikes.
- Check intro/outro discipline: 8 bars of drums-only at both ends, mixable into another track without rearranging anything.

## Example

```
// ═══ turbine hall — hypnotic techno, 132bpm ═══
// form: intro 8 | perc 8 | hats 8 | stab 8 | journey 16 | breakdown 8 | build 4 | peak 16 | outro 8
// one loop; the music is the slow change — filters, mutes, one event at a time
setcpm(132 / 4) // one cycle = one bar of 4/4

// ── kick — 909, heavy, dead straight; ducks the rumble and stab orbits, gently ──
const kick = arrange(
  [8, s("bd*4").bank("RolandTR909").gain(.7).lpf(500)],  // muffled: the mix-in
  [40, s("bd*4").bank("RolandTR909").gain(1).shape(.3)], // full weight, slight grit
  [8, silence],                                          // breakdown: the floor is pulled
  [4, s("bd*4").bank("RolandTR909").gain(.8)],           // build: it returns before you're ready
  [16, s("bd*4").bank("RolandTR909").gain(1).shape(.3)], // peak: same kick, that's the point
  [8, s("bd*4").bank("RolandTR909").gain(.85).lpf(600)], // outro: the mix-out
).duckorbit("2:3").duckdepth(.6).duckattack(.12)

// ── rumble — the kick's reverb tail, lowpassed into a bass: the room plays the low end ──
const rumble = s("bd*2").bank("RolandTR909").room(1).lpf(140).gain(.5)
const lowend = arrange(
  [8, rumble.gain(.4)],
  [40, rumble],
  [12, note("a0").sound("sine").gain(.32)], // breakdown + build: the drone is what's left
  [16, rumble],
  [8, rumble.gain(.35)],
).orbit(2)

// ── perc — the only syncopated thing in the track: euclid 3s over the straight grid ──
const rim = sound("rim(3,8)").bank("RolandTR909")
const perc = arrange(
  [8, silence],
  [8, rim.gain(.3)],
  [16, rim.gain(.32)],
  [16, rim.gain(.34).lpf(saw.range(300, 4000).slow(16))], // the journey: same loop, opening
  [8, sound("{cb ~ sh}%3").bank("RolandTR909").gain(.16)], // breakdown: 3-over-4, weightless
  [4, rim.gain(.2)],
  [16, stack(rim.gain(.36), sound("{cb ~ sh}%3").bank("RolandTR909").gain(.2))], // peak
  [8, rim.gain(.28)],
)

// ── hats — offbeat tick first, 16ths later, open hats only at the peak ──
const off = sound("[~ hh]*4").bank("RolandTR909")
const hats = arrange(
  [16, silence],
  [8, off.gain(.22)], // enters alone: the offbeat tick
  [8, stack(off.gain(.24), sound("hh*16").bank("RolandTR909").gain(.08))],
  [16, stack(off.gain(.26), sound("hh*16").bank("RolandTR909").gain(.1)
     .lpf(saw.range(1500, 9000).slow(16)))], // the journey, on the hats too
  [8, silence], // breakdown: air
  [4, sound("hh*16").bank("RolandTR909").gain(.1)], // the build belongs to the roll
  [16, stack(sound("[~ oh]*4").bank("RolandTR909").gain(.3), // peak: open hats = the release
     sound("hh*16").bank("RolandTR909").gain(.1))],
)

// ── the one muted stab — a single a every 8th bar; a minor third only in the breakdown ──
const stabPat = note("<a3 ~ ~ ~ ~ ~ ~ ~>").lpf(500)
const stab = arrange(
  [24, silence],
  [8, stabPat.gain(.45)],                             // first appearance, no announcement
  [16, stabPat.gain(.5).someCycles(x => x.lpf(800))], // journey: the one thing that changes
  [8, note("<[a3,c4] ~ ~ ~ ~ ~ ~ ~>").lpf(600).gain(.4)], // breakdown: the third exposed
  [20, stabPat.gain(.55).someCycles(x => x.transpose(12))], // peak: octave flicker, still one note
).sound("sawtooth").decay(.25).sustain(0).orbit(3)

// ── the build — a snare roll and a noise riser; nothing melodic ──
const riser = arrange(
  [56, silence],
  [4, stack(sound("<sd*4 sd*8 sd*16 sd*16>").bank("RolandTR909").gain("<.2 .3 .45 .6>"),
     sound("hh*8").bank("RolandTR909").speed("<1 1.5 2 4>").gain("<.12 .2 .3 .45>"))],
)

$: kick
$: lowend
$: perc
$: hats
$: stab
$: riser
```
