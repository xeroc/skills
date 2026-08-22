Lo-fi hip-hop's equivalent moment is the settle — the bar, usually eight or sixteen bars in, where the loop stops being a pattern and becomes a room you're sitting in. It's the anti-drop: nothing arrives, everything softens, and the song's job switches from going somewhere to being somewhere. That has hard production consequences: information density goes down (few notes, slow harmonic rhythm), texture density goes up (dust, wobble, crackle, room tone), and every "mistake" — a lazy kick, a slightly detuned piano, a missing snare — is kept on purpose because the imperfections are what make it feel found rather than manufactured.

## What the settle actually is

A settle is the audible moment the groove becomes drunken and the listener stops counting bars. Practically, four things converge: the drums shift from quantized to behind-the-beat (deep swing on the hats, the kick landing a touch late around beat 3 rather than on it), a noise floor appears underneath (vinyl crackle, tape hiss — a quiet, filtered noise layer you stop hearing consciously but immediately notice if muted), the keys drift out of perfect tune (tape wobble: slow random pitch movement of a few cents), and the melody starts leaving real space — phrases of two or three notes with whole bars of nothing. After the settle, the arrangement barely moves: layers drift in and out over the same four chords, energy stays inside a narrow band, and the "structure" is really a slow breathing pattern. If a lo-fi track spikes, it has left the genre.

## The layers

- **Crackle bed** — there's no verified `crackle` sound, so build the noise floor from what is: `sound("hh*32").degradeBy(.94).gain(.045).lpf(6000)` gives you sparse, filtered ticks — quiet enough to sit under everything, irregular enough to read as surface noise rather than rhythm. `perlin`-driven gain on a filtered `hh` wash is another route.
- **Drums** — round kick (`bd` with `lpf(400)`, felt more than heard), roomy lazy snare (`sd` with `room(.4)`), ghost `rim` clicks between the backbeats, and swung hats: `hh*8` with a velocity pattern and `swing(.14)` is the core. Dust the hats with `degradeBy(.15)` so they're never identical.
- **Keys** — `piano` is the genre's lead instrument: maj7/9 voicings voiced around `c4`, everything through `lpf(2000)` or so for warmth, and tape wobble via `.speed(perlin.range(.965, 1.035).slow(2))` so the instrument is never quite in tune with itself. `pluck` works for a music-box variation; `gm_music_box` for real twinkle.
- **Bass** — `gm_acoustic_bass`, filtered low (`lpf(500)`), roots plus one passing note per loop, and deliberately simple — the roundness matters more than the notes.
- **Melody** — sparse piano phrases, `@`-elongated notes, long rests, an echo (`delay` with modest feedback) so each phrase decays into the room. Four notes over eight bars is a correct amount.
- **Air** — small `room` on everything except the crackle; the glue is a shared short delay and the fact that everything is filtered. If a layer sounds crisp, `lpf` it until it doesn't.

## Sample kit

- **Drums** — default kit works (round `bd` + roomy `sd` + dusty `hh`). The upgrade is the `crate` pack — dusty, song-named one-shots that sound lifted rather than programmed:
  ```js
  samples('github:eddyflux/crate'); // crate_bd crate_sd(54!) crate_hh crate_cp crate_rim crate_sh crate_clave …
  ```
  First play may be silent while the pack loads — run again. License unknown: fine for playground/foreground, keep default-kit names as the fallback for background beds.
- **Keys** — `piano` standard; `steinway`/`fmpiano` (VCSL) when the room needs a real grand or a felt one; `gm_music_box` for twinkle.
- **Bass** — `gm_acoustic_bass` under `lpf(500)`, roots plus one passing note.
- **Crackle bed** — constructed, not sampled: quiet filtered `hh` ticks (see layers). Works regardless of packs.
- **Trip-hop leanings** — `github:sonidosingapura/rochormatic` carries named breaks (`kompira`, `ritachao`, `karmacoma`) that chop beautifully at 70–85 bpm. Likely sampled material — foreground only.

## Harmony

The vocabulary is jazz 7th/9th chords voiced mid-range and moved slowly — one chord per bar, sometimes one per two bars. The color chords are maj7, m9, and dom9; the emotional move is always a borrowed minor subdominant. In C:

- **ii9 – V9 – Imaj9 – vi9** — Dm9 – G9 – C^9 – Am9. The canonical loop (the one in the example): starts away from home, resolves, then falls to relative minor so the loop never feels finished. This is the sound most people mean by "lo-fi chords."
- **Imaj7 – vi9 – ii9 – V9** — Cmaj7 – Am9 – Dm9 – G9. The same family rotated to start at home; gentler, better for study-music energy levels.
- **IVmaj7 – iii7 – ii9 – Imaj9** — Fmaj7 – Em7 – Dm9 – C^9. Stepwise descent, each chord a shade darker; ideal when the melody sits still and you want the harmony to do the breathing.
- **The borrowed sigh: Imaj9 – iv9 (– Imaj9)** — C^9 – Fm9 – C^9. I – iv – I. The minor subdominant is lo-fi's single most bittersweet bar; deploy it once per form, usually at the top of the last loop, and let the melody pause on it.

Rhythm of the changes matters as much as the changes: keep one chord per bar, and voice-lead so common tones are sustained — sustained inner voices are what make the loop feel like it floats.

## Rhythm & feel

- **Tempo** — 70–85. Below 70 it becomes ambient; above 85 it starts head-nodding too hard to ignore.
- **Kick skeleton** — `"[bd ~ ~ ~] [~ ~ bd ~]"` with the second kick feeling late (nudge feel via rests around it, not by moving the grid); a busier variant adds a ghost on the and-of-4: `"[bd ~ ~ bd] [~ ~ ~ ~]"` in the last bar of a phrase.
- **Snare** — 2 and 4, `room(.4)`, and occasionally just… absent (`someCycles` dropping or reversing it) — the missed backbeat is a signature, not a bug.
- **Hats** — 8ths, `swing(.1)` to `swing(.16)`, velocity pattern `gain("[.18 .32]*4")` so the ands speak and the downbeats whisper, plus `degradeBy` dust.
- **Feel devices** — no sidechain, no builds. Movement comes from filter drift (`lpf` opened slowly by a `sine`/`perlin` signal), from layers entering/leaving, and from velocity humanity. The bass may sit a hair behind the drums; the piano may wobble; both are features.

## Structure

Lo-fi is loop music wearing a song-shaped coat. A working form:

```
intro 4 (crackle + keys fade in, no drums) | loop A 8 (drums settle) | +melody 8 |
variation 8 (octave sparkle, echo answer, one reversed snare) | strip 4 (drums thin out — the held breath) |
full 8 (everything back, melody darker-filtered) | outro 4 (drums leave, keys ring out)
```

Energy stays inside a narrow band by design — the graph is a ripple, not a mountain range:

```
intro _  loop __  +melody ___  variation ____  strip __  full ____  outro _
```

If you feel the urge to add a drop, a big fill, or a key change, the correct lo-fi move is instead: change one small thing (the melody's octave, the snare's reversal, the filter) and let the loop keep rolling.

## Techniques that actually create "lo-fi"

- **The crackle bed** — a very quiet, filtered, mostly-removed tick layer (`hh` + `lpf` + `gain(.05)` + heavy `degradeBy`). It reads as vinyl because it's sparse, bright-but-quiet, and constant. Without it the track sounds like a quiet clean beat, which is a different genre.
- **Tape wobble** — slow random movement on `speed` around 1.0 (±2–3%) on the keys and sometimes the whole mix. This is the difference between a piano sample and a memory of one.
- **Dust everywhere** — `degradeBy` small amounts on hats and melody; combine with velocity patterns so no two bars are identical.
- **Deep lazy swing** — `.swing(.1)`–`.16)` on hats and light swing even on the snare layer; straight 8ths at 78 bpm sound like a metronome, swung ones sound like a drummer who's comfortable.
- **Warmth as a rule** — `lpf` on every melodic layer, sub-1k on the bass, nothing bright above the crackle's own band. The frequency picture is a blanket with one thin dust layer on top.
- **Sparse melody with real space** — write the melody by removing notes from a phrase until only the ones you'd hum remain, then double the rests.
- **The kept mistake** — one dropped snare, one slightly early piano note, one bar where the melody's echo is louder than the melody. Chosen imperfection is the aesthetic; accidental sloppiness is just sloppiness, so place them deliberately.
- **Slow filter drift instead of builds** — automating `lpf` over 8+ bars with a `perlin` or `sine` signal gives evolution without breaking the settle.

## Practice approach

- Live with reference loops: Nujabes, J Dilla (the *Donuts* era of timing decisions), Knxwledge, Tomppabeats, Idealism. Listen specifically for where the snare lands relative to the grid — it's later than you think.
- Build a two-bar loop with just drums + crackle first; if that doesn't feel like a room, no chord will fix it.
- Add imperfections one at a time (swing, then dust, then wobble, then a dropped snare), listening after each — the goal is a few chosen flaws, not soup.
- Filter challenge: get every melodic element under 3 kHz and make the mix still interesting using only rhythm and space.
- Record the melody as a single take over the loop and keep the take's accidents — quantizing it afterwards reliably kills the genre.

## Example

```
// ═══ corner window — lo-fi hip-hop, 76 bpm ═══
// the settle: a four-bar loop that becomes a room. dust, wobble, and space do the arranging.
// form: intro 4 | loop 8 | +melody 8 | variation 8 | strip 4 | full 8 | outro 4 — energy never spikes
setcpm(76 / 4) // one cycle = one bar of 4/4
samples('github:eddyflux/crate'); // dusty one-shot kit; first play may be silent while it loads — run again

// ── the loop: Dm9 G9 C^9 Am9, one chord per bar, warm and closed ──
const keys = chord("<Dm9 G9 C^9 Am9>")
  .anchor("c4").voicing()
  .sound("piano")
  .lpf(2200).gain(.5)
  .speed(perlin.range(.965, 1.035).slow(2)) // tape wobble: never quite in tune with itself
  .room(.35)

// ── bass: roots plus one passing note (g walks up to c), round and unhurried ──
const bass = note("<[d2 ~ ~ ~] [g2 ~ ~ a2] [c2 ~ ~ ~] [a2 ~ ~ ~]>")
  .sound("gm_acoustic_bass").gain(.7).lpf(500)
  .swing(.05)

// ── drums: kick around 1 and 3, roomy snare on 2 and 4, swung dusty hats ──
const kick = sound("[crate_bd ~ ~ ~] [~ ~ crate_bd ~] [crate_bd ~ ~ crate_bd] [~ ~ ~ ~]").gain(.75).lpf(400) // round, felt more than heard
const snare = sound("~ crate_sd ~ crate_sd").gain(.45).room(.4)
const ghosts = sound("~ crate_rim ~ ~ ~ crate_rim ~ crate_rim").gain(.12) // side-stick ghosts between the backbeats
const hats = sound("crate_hh*8").gain("[.18 .32]*4").swing(.14).hpf(5000).degradeBy(.15) // dust in the hats

// ── melody: four notes a minute — the space is the part ──
const melody = note("<[e5@3 ~] [d5 ~ b4] [~ c5@3] [~ ~ a4 ~]>")
  .sound("piano").gain(.34).lpf(2000)
  .speed(perlin.range(.97, 1.03).slow(3)) // its own, slower wobble
  .delay(".25:.28:.3").room(.4)
  .degradeBy(.1)

// ── vinyl crackle: quiet filtered ticks, mostly nothing — the noise floor ──
const crackle = sound("hh*32").degradeBy(.94).gain(.045).lpf(6000)

// ── arrangement: the loop is the song; layers drift in and out, nothing arrives ──
$: arrange(
  [4, stack(crackle, keys.gain(.3))], // fade into the room
  [8, stack(crackle, keys, bass, kick, snare, hats.gain(.25))], // the settle happens in here
  [8, stack(crackle, keys, bass, kick, snare, hats, ghosts, melody)],
  [8, stack(
    crackle,
    keys.superimpose(x => x.transpose(12).gain(.12)), // octave sparkle above the voicings
    bass, kick,
    snare.someCycles(x => x.rev), // one reversed snare, whenever it feels like it
    hats,
    melody.off(1/16, x => x.transpose(-12).gain(.15)), // the melody's echo answers itself an octave down
  )],
  [4, stack(crackle, keys, bass, hats.gain(.18))], // drums thin out — the held breath
  [8, stack(crackle, keys, bass, kick, snare, hats, ghosts, melody.lpf(1600))], // back, slightly darker
  [4, stack(crackle, keys.gain(.35).release(2), melody.gain(.2))], // keys ring out under the dust
)
```
