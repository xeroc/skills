Gospel's equivalent moment is the vamp — after the last verse, the song narrows to a two- or four-bar loop, the tambourine and handclaps come up, the organ leans in, the drummer starts testifying, and then the key lifts a whole step and the room takes off. Where electro has one arrival (the drop) and K-pop has a chain of cuts, gospel has repeated liftoff: it keeps ascending, sometimes modulating twice, because the point isn't climax — it's escalation of praise. Everything in the idiom (the walking piano, the Hammond growl, the call-and-response, the 6/8-to-4/4 meter flips) serves a music that is built to carry a congregation from verses into a higher and higher place.

## What the vamp actually is

The vamp is a loop, usually I–vi–IV–V or a variation, played at full arrangement weight while the lead repeats the hook's last line and the choir answers. It's where every layer that was rationed during the verses is finally released together: tambourine on every eighth, handclaps on the backbeat, organ stabs doubling in rate, walking bass in constant motion. Then, at a fixed bar (everyone in the room can feel it coming), the whole band modulates up a whole step — same shapes, new key — and the energy ceiling physically rises because the singers have to reach higher. The ending is one of three: a slow-down with a fermata on the tonic, a hard stop on I after one last push bar, or the drums dropping out while the choir holds the final chord. In code terms: the vamp is a loop with growing layers; the modulation is the same pattern constants re-spelled a step up; the ending is an arrangement event, not a fade.

## The layers

- **Piano** — `piano`, and it's the engine, not a comping instrument. Left hand walks in octaves: dotted-beat roots in 6/8 (`[c2 ~ ~]`), stride octaves on the quarters in 4/4 (`[c2 c3]` per bar). The right hand either doubles the organ's stabs or plays answer figures. If the piano stops driving, the whole style collapses into slow jam.
- **Organ — the Hammond** — `gm_drawbar_organ` is the real thing: chord stabs with `shape(.3)` for the growl and `lpf` around 1700. (`gm_percussive_organ` is the brighter, gospel-rock variant; a sustained `sawtooth` stab is the lo-fi fallback.) Stabs sit on the beats in verses and push onto the ands (`struct("x ~ ~ x ~ x")`) in shouts; in the vamp the stab rate doubles.
- **Bass** — `gm_acoustic_bass`, walking quarters in 4/4 (roots, fifths, and scale approaches into the next chord), dotted whole-bar roots in 6/8. It walks into every section change — the last two quarters before a new section are a walk-up.
- **Drums** — `bd` pocket with pushes, `sd` backbeat with ghost figures, and the two congregation sounds: `tb` tambourine on every eighth (the genre's name tag — it can enter as early as bar 1 and never leaves) and `cp` handclaps stacked on 2 and 4 in shouts and vamps. `oh` opens when the spirit moves, `rim` ghosts in ballad verses.
- **Choir** — `gm_voice_oohs`: sustained chords in verses, backbeat answer hits in shouts (`struct("~ x ~ x")`), and call-and-response in the vamp — the leader's line high and exposed, the choir's chord answer on beat 3.
- **Optional preacher line** — `gm_trumpet` for a lead line that speaks in short phrases between choir answers; use it once, or not at all.

## Sample kit

- **Piano** — `piano` driving ✓; VCSL `steinway` for the real sanctuary grand.
- **Organ** — `gm_drawbar_organ` (the Hammond), `gm_percussive_organ` for shouts; crescendo via `attack` and full-manual `room`.
- **Bass** — `gm_acoustic_bass` walking ✓; `gm_electric_bass_finger` when the band modernizes.
- **Congregation** — `tb` tambourine (the name tag) + `cp` claps; VCSL `tambourine` and `clap` are the human round-robin upgrades for close-up mixes.
- **Choir & preacher** — `gm_voice_oohs` call-and-response ✓, `gm_trumpet` preacher line, `gm_choir_aahs` for the full-bench moment.
- No pack needed — the preloaded tiers cover gospel. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Gospel harmony is extended-function church harmony: major-key loops of I, vi, IV, V with sevenths and ninths, chromatic passing chords between them, and a modulation built into the form. In C:

- **Imaj7 – vi7 – IVmaj7 – V7** — Cmaj7 – Am7 – Fmaj7 – G7. The core loop; this is the verse cycle, the shout cycle, and the vamp cycle. Extend the tops (add the 9th) for warmth, but keep the functions this plain — the style's complexity lives in rhythm and arrangement, not reharmonization.
- **I – #i°7 – ii7 – V7 (passing diminished)** — Cmaj7 – Dbdim7 – Dm7 – G7. The signature walk-up: a diminished chord on the raised tonic connecting I to ii. Spelled Dbdim7 (enharmonic C#dim7) to keep flats in the chord symbols. Use it in verse cycles to signal motion without changing the loop.
- **iii7 – vi7 – ii7 – V7** — Em7 – Am7 – Dm7 – G7. The circle-of-fifths variant for a verse that wants more motion; resolves back to I with extra momentum.
- **Backdoor arrival: bVII7 – Imaj7** — Bb9 – Cmaj9. The flat-seventh dominant slides into I from behind — standard gospel color for section endings and the setup into a shout chorus.
- **The modulation: I – vi – IV – V, then the same a whole step up** — Cmaj7 – Am7 – Fmaj7 – G7, then Dmaj7 – Bm7 – Gmaj7 – A7. The whole-step lift for the final vamp. Re-spell, re-voice, keep every rhythm identical — the familiarity of the loop plus the new key is precisely the effect.

## Rhythm & feel

- **Tempo** — 60–140, and the range is two worlds: 6/8 ballad verses at dotted-quarter 54–72, 4/4 shout sections and vamps at 120–140.
- **The 6/8 skeleton** — `[bd ~ ~] [~ sd ~]` per bar (kick on dotted beat 1, snare on 2), `tb*6` tambourine on all six eighths, piano dotted roots `[c2 ~ ~] [g2 ~ ~]`. One cycle = one bar of 6/8: six even events.
- **The 4/4 shout skeleton** — `bd ~ ~ sd ~ bd ~ sd` (kick 1 and the and-of-3), `tb*8`, claps `~ cp ~ cp` with the snare, organ pushing on the ands. Endings add the push bar `bd ~ sd ~ bd bd sd bd` — kicks on 3, the and-of-3, and the and-of-4 into the final hit.
- **Meter flips as arrangement** — switching 6/8 verse to 4/4 shout is a section change in itself. In Strudel, run one cycle = one bar in both meters at a single `setcpm`: at `setcpm(33)` a cycle lasts ~1.8 s, which is a 6/8 bar at dotted-quarter 66 and a 4/4 bar at quarter 132 simultaneously — the meter switch needs no tempo machinery, just patterns of six versus patterns of eight.
- **Feel** — straight but loose: velocity variance on the tambourine, ghost snare figures, bass walks that lean into the next bar. The pocket is relaxed even at 132; if it starts sounding military, humanize velocities before touching anything else.

## Structure

```
intro 4 (6/8: organ + tambourine setting up) | verse 1 8 (6/8) | verse 2 8 (6/8, passing dim appears) |
shout chorus 8 (4/4: full kit, claps, organ pushes) | bridge 8 (6/8 returns — the breather) |
shout 2 8 | vamp in C 8 (call-and-response, layers stacking) | vamp in D 8 (the lift) | ending 4 (push bar + fermata)
```

Energy climbs in steps and never comes all the way back down — the bridge is a breather, not a valley:

```
intro _  v1 ___  v2 ____  SHOUT ████  bridge __↓  SHOUT2 █████  VAMP ██████  VAMP+1 ████████  END █▄
```

## Techniques that actually create "gospel"

- **The vamp** — narrow to a I–vi–IV–V loop at full weight, repeat the hook line over it, and stack a new layer on each pass (tambourine, then claps, then ghost snares, then doubled organ rate). Arrival by accumulation, not by addition of new material.
- **The whole-step modulation** — identical loop shapes re-spelled +2 at a fixed bar. Do it once as the final lift; doing it twice is for when the room is really with you. Re-voice upward so the top line physically climbs.
- **Call-and-response** — every layer can do it: leader melody answered by choir chord (`gm_voice_oohs` answer on beat 3), organ stab answered by piano figure, kick figure answered by clap. Phrase lengths of 2 bars, answers landing on the strong beat after the call ends.
- **Passing diminished walk-ups** — the #i°7 (spelled Dbdim7) between I and ii; also usable walking into IV. It's the fastest single chord to make functional harmony sound like church.
- **Tambourine as the congregation** — `tb` on every eighth from the first shout onward, gain riding with section energy. It's the layer that says people are in the room.
- **The driving piano** — stride octaves in the left hand, constant; gospel piano is a rhythm instrument first. When in doubt, more left hand, not more right hand.
- **The Hammond stand-in** — no verified organ GM sound, so `sawtooth` + `shape(.3)` + `lpf(1700)` chord stabs; push the stabs onto the ands in shouts and double their rate in the vamp to mimic the Leslie speeding up.
- **6/8 ↔ 4/4 flips** — use the meter change itself as the verse-to-shout transition; one bar of fill (`[sd sd rim]`) is enough runway.
- **Everything ascends** — arrangement philosophy: layer count, register, stab rate, and key all only go up (except one bridge breather). The opposite of a build-and-drop arc.

## Practice approach

- Listen with a bar counter: Edwin Hawkins "Oh Happy Day" (the original vamp-and-modulate architecture), Andraé Crouch, Richard Smallwood for the 6/8 ballads, Kirk Franklin "Revolution"/"Stomp" and Tye Tribbett for modern shout grooves. Find the exact bar where each modulation lands — it's earlier than you expect and everyone hears it coming.
- Practice the I–vi–IV–V loop with the passing diminished in every key, left-hand octaves only, at 132 — that alone should sound like gospel before any other layer.
- Transcribe one walking bass verse from a 6/8 ballad; notice how the last two quarters of each section walk into the next section's first chord.
- Run the meter-flip drill: two bars of `[bd ~ ~] [~ sd ~]`, one fill bar, then `bd ~ ~ sd ~ bd ~ sd` at the same cpm until both feel like one tempo.
- Write one call-and-response pair per section maximum — the device is powerful precisely because it isn't constant.

## Example

```
// ═══ sunday morning — gospel, 6/8 verses at dotted-quarter 66, 4/4 shouts at 132 ═══
// one cycle = one bar in both meters: setcpm(33) gives a 6/8 bar of six eighths (dotted beat = 66) and a 4/4 bar of 8ths/16ths (quarter = 132) — the meter flip is itself the arrangement.
// form: intro 4 | v1 8 (6/8) | v2 8 (6/8) | shout 8 (4/4) | bridge 8 (6/8) | shout2 8 | vamp C 8 | vamp D 8 (+2) | ending 4
// energy: intro _  v1 ___  v2 ____  SHOUT ████  bridge __↓  SHOUT2 █████  VAMP ██████  VAMP+1 ████████  END █▄
setcpm(33)
// ── organ: the Hammond stand-in — sawtooth stabs with shape() growl (no verified gm organ) ──
const organTone = p => p.sound("sawtooth").shape(.3).lpf(1700).sustain(.5).release(.3).gain(.22)
const v68 = "<Cmaj7 Am7 Dm7 G7 Cmaj7 Dbdim7 Dm7 G7>" // verse: passing dim walks I -> ii in the back half
const sh44 = "<Cmaj7 Cmaj7 Fmaj7 G7 Cmaj7 Cmaj7 F G7>" // shout cycle
const vampC = "<Cmaj7 Am7 Dm7 G7>", vampD = "<Dmaj7 Bm7 Em7 A7>" // the 1/bar vamp loop, and the same a whole step up
const og68 = organTone(chord(v68).anchor("c4").voicing().struct("x ~ ~ x ~ ~")) // 6/8: stabs on the dotted beats
const ogSh = organTone(chord(sh44).anchor("c4").voicing().struct("x ~ ~ x ~ x")) // 4/4: pushes land on the ands
const organ = arrange(
  [4, organTone(chord(vampC).anchor("c4").voicing())],
  [8, og68], [8, og68], // v1 + v2
  [8, ogSh], [8, og68], // shout, then the 6/8 bridge breathes
  [8, ogSh], [8, organTone(chord(vampC).anchor("c4").voicing().struct("x ~ x ~ x ~"))], // shout2, then the vamp's doubled stab rate
  [8, organTone(chord(vampD).anchor("d4").voicing().struct("x ~ x ~ x ~"))], // same rhythm, new key
  [4, chord("<D^9>").anchor("d4").voicing().sound("sawtooth").shape(.3).lpf(1600).attack(.05).release(2).gain(.26)], // the fermata
)

// ── piano: the engine — left hand walks in octaves and never stops driving ──
const lh68 = note("<[c2 ~ ~] [a1 ~ ~] [f2 ~ ~] [g2 ~ ~] [c2 ~ ~] [c2 ~ ~] [d2 ~ ~] [g2 ~ ~]>") // 6/8 dotted roots
const lh44 = note("<[c2 c3] [a1 a2] [f2 f3] [g2 g3] [c2 c3] [c2 c3] [f2 f3] [g2 g3]>") // 4/4 stride octaves
const piano = arrange(
  [4, note("<[c2 ~ ~] [g2 ~ ~]>")],
  [8, lh68], [8, lh68], [8, lh44], // v1, v2, shout
  [8, lh68], [8, lh44], // bridge, shout2
  [8, note("<[c2 c3] [a1 a2] [f2 f3] [g2 g3]>")], // vamp loop
  [8, note("<[d2 d3] [b1 b2] [g2 g3] [a2 a3]>")], // the same stride in D
  [4, note("<[d2 d3 ~ ~] ~ ~ ~>")], // one last push, then silence for the fermata
).sound("piano").gain(.55).room(.3)

// ── bass: dotted roots under 6/8, walking quarters through everything in 4/4 ──
const roots68 = note("<c2 a1 f2 g1 c2 c2 d2 g1>")
const walk44 = note("<[c2 e2 g2 e2] [a1 c2 e2 c2] [f2 a2 c3 a2] [g1 b1 d2 b1] [c2 e2 g2 e2] [c2 e2 g2 a1] [f2 a2 c3 c2] [g1 b1 d2 f2]>")
const bass = arrange(
  [4, note("<c2 g1>")],
  [8, roots68], [8, roots68], [8, walk44], // v1, v2, shout
  [8, roots68], [8, walk44], // bridge, shout2
  [8, note("<[c2 e2 g2 a2] [a1 c2 e2 f2] [f2 a2 c3 b2] [g1 b1 d2 e2]>")], // vamp walk, loops back to c2
  [8, note("<[d2 fs2 a2 b2] [b1 d2 fs2 g2] [g2 b2 d3 cs3] [a1 cs2 e2 fs2]>")], // same walk in D — fs/cs, never sharps
  [4, note("<d2@4>")],
).sound("gm_acoustic_bass").gain(.7).room(.15)

// ── choir + call-and-response: the leader sings, the room answers ──
const oo = p => p.sound("gm_voice_oohs").attack(.4).release(1).gain(.2).room(.6)
const oo68 = oo(chord(v68).anchor("f4").voicing())
const ooSh = chord(sh44).anchor("f4").voicing().sound("gm_voice_oohs").attack(.05).release(.3).gain(.24).struct("~ x ~ x") // answers on the backbeat
const resp = (cs, a) => chord(cs).anchor(a).voicing().sound("gm_voice_oohs").attack(.05).release(.4).gain(.22).struct("~ ~ x ~") // response hits on 3
const call = (n, g = .32) => note(n).sound("gm_voice_oohs").gain(g).room(.5) // the leader's line
const choir = arrange(
  [4, oo(chord(vampC).anchor("f4").voicing())],
  [8, oo68], [8, oo68], [8, ooSh], // v1, v2, shout
  [8, oo68], [8, ooSh], // bridge, shout2
  [8, stack(resp(vampC, "f4"), call("<[e5@2 d5] [c5@4 ~] ~ ~>"))], // vamp: call bars 1-2, the room answers on 3
  [8, stack(resp(vampD, "g4"), call("<[fs5@2 e5] [d5@4 ~] ~ ~>", .34))], // the call lifts with the key
  [4, chord("<D^9>").anchor("g4").voicing().sound("gm_voice_oohs").attack(1).release(3).gain(.26).room(.8)], // the room lands
)

// ── drums: 6/8 pocket for verses, 4/4 shout with tambourine 8ths and claps ──
const d68 = stack(sound("[bd ~ ~] [~ sd ~]").gain(.5), sound("tb*6").gain(.24)) // kick 1, snare 2, tambourine on every eighth
const d44 = stack(sound("bd ~ ~ sd ~ bd ~ sd").gain(.55), sound("tb*8").gain(.28), sound("~ cp ~ cp").gain(.4)) // shout kit + handclaps
const drums = arrange(
  [4, stack(sound("[bd ~ ~] [~ sd ~]").gain(.45), sound("tb*6").gain(.18))],
  [8, d68], [8, stack(d68, sound("<~!7 [sd sd rim]>").gain(.35))], // v2, fill into the meter flip
  [8, d44], [8, d68], // shout, bridge
  [8, stack(d44, sound("oh*8").gain(.18))], [8, d44], // shout2: hats open up; then the vamp begins
  [8, stack(d44, sound("sd*16").gain(.28).degradeBy(.4))], // vamp D: the drummer testifies — busy, dusty ghosts
  [4, stack(sound("<[bd ~ sd ~ bd bd sd bd] ~ ~ ~>").gain(.5), sound("cr ~ ~ ~").gain(.3), sound("tb*8").gain(.25))], // push bar, then stop
)

$: organ
$: piano
$: bass
$: choir
$: drums
```
