Funk's equivalent moment is **the One** — beat one of the bar after a bar of everyone playing around it. Jazz has the cadenza, pop has the bridge; funk has the landing: the whole band hits beat one together, having spent the previous bar fragmenting, syncopating, and ghost-noting their way as far from it as possible without losing it. The One isn't a chord change or a drop — it's gravity.

## What the One actually is

James Brown's directive ("on the One") means the downbeat is the anchor of an otherwise syncopated texture. The groove is a one-chord vamp: instead of harmony moving the music forward, rhythm does — 16th-note guitars, ghost snares, slap bass, horn stabs placed against the beat, all pointing at the next downbeat. Space is still the secret: between every two hits there's a rest, and the interlocking patterns of bass, drums, and guitar form a lattice you could read three ways. When the arrangement suddenly strips down — breakdown: just kick, claps, and ghosts — the tension isn't a rest, it's a coiled spring, because everyone can hear exactly where the One will land.

## The layers

- **Drums** — `.bank("AkaiLinn")` for that dry 80s Linn snare and snap. Kick syncopated but always on 1 (`bd ~ ~ ~ ~ ~ bd ~ …`), snare on 2 and 4, and the real engine: ghost snares at gain `.1` filling the 16th grid between backbeats.
- **Hats & percussion** — straight 16ths with a velocity pattern accenting the offbeat 8ths, `cb` cowbell on the offbeats, `tb` tambourine 8ths joining the full sections, `sh` for the top sheen.
- **Bass** — `pluck` with `.lpf(1300)`, playing a 16th-note figure around the root with octave pops (`superimpose` an octave up at low gain = the slap). The bass is the second lead; it answers the kick.
- **Guitar (the chank)** — `gm_electric_guitar_muted` playing one note (the root) on a syncopated 16th pattern full of holes, `.cut(1)` so each stroke chokes the last. This is the metronome of the band.
- **Clav** — `gm_clavinet`, `.decay(.06).sustain(0)`, playing staccato 16th dyads on the 9th and b7 — the percussive keyboard layer that answers the guitar. (`square` synth + short envelope is the lo-fi fallback.)
- **Horns** — `gm_trumpet` section stabs (a `D9` `chord()` anchored high) landing on the One with answers on the pushes, an octave-down double for the tenor weight. `gm_tenor_sax` takes single-note answers where the trumpets leave space.

## Sample kit

- **Kit** — `.bank("AkaiLinn")` (dry 80s snap); `.bank("EmuSP12")`/`.bank("AkaiMPC60")` for the grittier golden-age variants, `.bank("RolandTR707")` for the boogie edge.
- **Clav — the genre's keyboard** — `gm_clavinet`, always; no synth argument beats the real soundfont for "Superstition" duty.
- **Bass** — the slap: `gm_slap_bass_1` for genuine thumb-and-pluck attack, `gm_slap_bass_2` for the brighter set; the `pluck` + octave-`superimpose` trick remains the rounder, less cartoony fallback.
- **Chank guitar** — `gm_electric_guitar_muted` ✓; add `vowel("<a e>")` for the wah dialect.
- **Horns** — `gm_trumpet` stabs + `gm_tenor_sax` answers; `gm_brass_section` when the section plays as one body, `gm_muted_trumpet` for the sly answers.
- No pack needed — the preloaded tiers cover funk. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Funk is a one-chord music with a blues accent. The dominant 9th is the default chord; the 7♯9 ("Hendrix chord," spelled D–F♯–C–E♮) is the grittier sibling. In D:

- **One-chord vamp: I9** — D9 (D–F♯–A–C–E) for the entire tune: the Meters/JB default. All development is rhythmic and textural.
- **The move: I9–IV9** — D9 | A9: the single harmonic event of many tunes, hit maybe twice. IV9 spelled A–C♯–E–G–B.
- **I7♯9 vamp** — D7♯9 (D–F♯–C–E): darker, city funk; in code spell it `[d3,fs3,c4,f4]`.
- **Blues box** — D9 | G9 | A9: when funk borrows the 12-bar, it reduces it to riffs over those three 9th chords.
- **bVII color** — C9 over a D vamp: the flat-seventh stab that makes one chord sound like two.

## Rhythm & feel

- Tempo 90–110. Below that it's a slow grind, above it you're tipping into disco.
- Kick skeleton (16th grid): `bd ~ ~ ~ ~ ~ bd ~ ~ ~ ~ ~ bd ~ ~ bd` — beat 1, the and-of-2, beat 4, and the a-of-4 push so the next One lands harder.
- Backbeat: `~ ~ ~ ~ sd ~ ~ ~ ~ ~ ~ ~ sd ~ ~ ~` — 2 and 4, dead center, every bar.
- Ghost engine: `~ ~ sd ~ ~ sd ~ sd ~ ~ sd ~ ~ sd ~ sd` at gain `.1` — the 16th grid made audible without being loud.
- Guitar chank, 16ths with holes: `[d3 ~ d3 d3] [d3 d3 ~ d3] [d3 ~ d3 d3] [d3 ~ d3 ~]`.
- No swing: funk 16ths are straight — the looseness comes from velocity variation and ghost placement, not timing.

## Structure

```
intro 4 | vamp 8 | horns 8 | breakdown 4 | build 2 | full 8 | out 4
   3         5        6         4         5 -> 7      8        2    (energy 0-10)
```

Intro: kick, ghosts, hats — the backbeat hasn't been earned yet. Vamp: bass and chank join. Horns: the section enters, still the same chord. Breakdown strips to kick, claps, and ghost snares — the naked 16th grid. Build: claps double, then everything returns for the full stack (cowbell, tambourine, clav, horns). The outro removes elements one at a time, like the band leaving the stage mid-bar.

## Techniques that actually create "funk"

- **Everything points at the One** — pushes (a-of-4 kick, 16th chromatic walks in the bass, horn answers on `&4`) are tension aimed at the downbeat; without them the vamp is just a loop.
- **One chord, total commitment** — resist new harmony; when you need change, move the voicing an octave, stab a bVII, or drop the bass out for two bars.
- **Ghost snares at gain .1** — the 16th-note engine; they make the groove feel twice as fast without adding volume.
- **The chank** — one muted note on a holey 16th grid, choked with `cut(1)`; it is both percussion and harmony.
- **Call and response** — horns ask on the One, bass or tenor answers on the push; every layer phrases in the gaps the others leave (the lattice).
- **The breakdown** — strip to kick, claps, and ghosts; the sparser texture reads as more tension, not less, because the One is still implied.
- **Velocity, not swing** — accent patterns on straight 16ths (`[.5 .14 .3 .14 .46 .14 .3 .14]`) create the looseness; timing stays on the grid.
- **Octave-pop bass** — `superimpose` the bass an octave up at low gain for the slap articulation without changing the line.

## Practice approach

- Play one note on muted guitar for two minutes at 16th resolution, varying only which slots you rest on; that's the whole chank education.
- Program the kick first, then place every other layer's hits only where the kick isn't — the lattice appears by itself.
- Play along with the J.B.'s or the Meters and notice you can hear each part as "the melody"; write parts that survive that test.
- Break your own groove down to kick and ghosts for four bars, then bring it back; notice the return feels like the hook.
- Write a bass line that walks chromatically into the One (`~ bb2 a2 ~` resolving to `d2`) and build the bar around it.

## Example

```
// ═══ the electric pocket — funk, 102bpm, one-chord D9 vamp ═══
// form: intro 4 | vamp 8 | horns 8 | breakdown 4 | build 2 | full 8 | out 4
// energy: 3 5 6 4 5->7 8 2 — the breakdown is a coiled spring, not a rest
setcpm(102 / 4) // one cycle = one bar of 4/4

// ── kit — Linn snap: kick on the One plus syncopes, ghosts at .1 between backbeats ──
const bdFunk = sound("bd ~ ~ ~ ~ ~ bd ~ ~ ~ ~ ~ bd ~ ~ bd").bank("AkaiLinn").gain(.9) // 1, &2, 4, a-of-4 push
const sdFunk = sound("~ ~ ~ ~ sd ~ ~ ~ ~ ~ ~ ~ sd ~ ~ ~").bank("AkaiLinn").gain(.55)
const sdGhost = sound("~ ~ sd ~ ~ sd ~ sd ~ ~ sd ~ ~ sd ~ sd").bank("AkaiLinn").gain(.1) // the engine
const hatFunk = sound("hh*16").gain("[.5 .14 .3 .14 .46 .14 .3 .14]*2")
const cpFunk = sound("~ ~ ~ ~ cp ~ ~ ~ ~ ~ ~ ~ cp ~ ~ ~").bank("AkaiLinn").gain(.3)
const kitCore = stack(bdFunk, sdFunk, sdGhost, hatFunk)
const kitFull = stack(kitCore, cpFunk, sound("cb ~ cb ~ cb ~ cb ~").gain(.18), sound("tb*8").gain(.12))
const drums = arrange(
  [4, stack(bdFunk, sdGhost, hatFunk)], // no backbeat yet — it hasn't been earned
  [8, kitCore],
  [8, kitCore],
  [4, stack(bdFunk.gain(.7), cpFunk, sdGhost)], // breakdown: the naked 16th grid
  [2, stack(bdFunk, sdFunk, sound("<cp*4 cp*8>").bank("AkaiLinn").gain(.35))], // build: claps double
  [8, kitFull],
  [4, stack(bdFunk, sdFunk, sdGhost, hatFunk.gain(.2))], // out: elements leave one at a time
)

// ── bass — one chord, so the rhythm IS the part: 16ths, octaves, chromatic walk to the One ──
const bassFunk = note("<[[d2 ~ ~ d2] [~ ~ d2 ~] [~ d3 ~ d2] [~ ~ a2 c3]] [[d2 ~ d2 ~] [~ d2 ~ ~] [d3 ~ d2 ~] [~ bb2 a2 ~]]>")
  .sound("pluck").lpf(1300).superimpose(x => x.transpose(12).gain(.18)) // the slap pop, an octave up
const bass = arrange(
  [4, bassFunk.gain(.5)], [8, bassFunk.gain(.65)], [8, bassFunk.gain(.7)],
  [4, bassFunk.gain(.55)], // breakdown keeps the bass — the coil needs it
  [2, bassFunk.gain(.6)], [8, bassFunk.gain(.72)], [4, note("d2").gain(.6)],
)

// ── guitar — the chank: muted D on a holey 16th grid, choked every stroke ──
const chank = note("<[[d3 ~ d3 d3] [d3 d3 ~ d3] [d3 ~ d3 d3] [d3 ~ d3 ~]] [[d3 ~ d3 d3] [d3 d3 ~ d3] [d3 ~ d3 d3] [a3 ~ bb3 ~]]>")
  .sound("gm_electric_guitar_muted").cut(1).pan(.6)
const guitar = arrange(
  [4, silence], [8, chank.gain(.22)], [8, chank.gain(.28)], [4, chank.gain(.15)],
  [2, silence], [8, chank.gain(.32)], [4, chank.gain(.12)],
)

// ── clav — square-wave stabs answering the guitar in the gaps ──
const clav = note("<[[e4 d4] [e4 bb4] [a4 e4] [d4 e4]] [[e4 d4] [e4 c4] [a4 e4] [c4 a3]]>")
  .sound("square").decay(.06).sustain(0).pan(.4)
const keys = arrange([30, silence], [8, clav.gain(.22)], [4, clav.gain(.22)])

// ── horns — section stabs: call on the One, answer on the push, tenor shadow below ──
const horns = chord("<D9 D9 D9 G9>").anchor("d5").voicing().struct("x ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ x x")
  .sound("gm_trumpet").room(.3).superimpose(x => x.transpose(-12).gain(.5))
const section = arrange([20, silence], [8, horns.gain(.4)], [4, silence], [2, silence], [8, horns.gain(.45)], [4, silence])

$: drums
$: bass
$: guitar
$: keys
$: section
```
