Punk's equivalent moment is **the shout-along** — the sixteen bars where the room stops watching the band and becomes the band. Where jazz spends its tension in a cadenza, pop in a bridge, and trance in a filter sweep, punk spends it in a chorus yelled in unison: three chords, a hook built out of "whoa-oh"s, and no patience for an intro. The genre's whole engineering problem is arriving at that moment inside fifteen seconds and leaving before the listener's attention does.

## What the shout-along actually is

It is the chorus nobody needs to be taught. The hook is chantable monosyllables — often just the title repeated, or vowel sounds ("whoa-oh", "hey hey") — doubled in octaves so it sounds like a crowd instead of a singer. Structurally, punk front-loads: the chorus either arrives at bar nine or the song opens with it outright, and everything after the first chorus is just verse-chorus again with no decoration except one bridge and one solo that is the vocal melody played faster. The emotional center is participation, not skill — if the audience can't sing it after one hearing, the chorus has failed at its only job, and no amount of chord sophistication will fix that.

## The layers

- **Guitar 1** — power-chord fifth dyads (`[a2,e3]` shapes) on `gm_overdriven_guitar`, straight 8th downstrokes (`note("[a2,e3]*8")`), gain pushed, `room(.12)` or less so it stays dry and in your face. When the riff drops low, barre-chord chugs on the low strings do the same job one register down.
- **Guitar 2** — the identical part an octave up via `.transpose(12)`, panned opposite (`.pan(.75)` against `.pan(.25)`). Width comes from doubling, never from extra notes.
- **Bass** — root 8ths on `sawtooth` with `lpf(700)`, a touch louder than polite. The bass is the engine: it plays straight through every change, pushing the band like a shove in the back.
- **Drums** — the d-beat: `[bd ~ sd ~ bd bd sd ~]`. Kick on 1, snare on 2, kick-kick on 3, snare on 4; the `bd bd sd ~` tail is the fingerprint. Snare gain high with a little `room`, a crash on section downbeats, and a tom fill `[ht mt lt ht]` as the only permitted decoration.
- **Vocals** — `gm_voice_oohs` is the closest gang-vocal approximation: verse is a sneered single line, chorus is the shout, thickened with `.superimpose(x => x.transpose(-12).gain(.5))` so every line sounds like ten people.

## Sample kit

- **Drums** — default kit, no machine bank: punk wants a live room. `bd sd hh oh cr` + `[ht mt lt]` fills; try `sd:1`/`sd:2` for a fatter crack. Trash aesthetic if required: layer `.bank("CasioVL1")` (bd hh sd only).
- **Guitars** — `gm_overdriven_guitar` is the workhorse; `gm_distortion_guitar` for hardcore leanings. The solo uses the same sound, an octave up.
- **Bass** — `gm_electric_bass_pick` with `lpf(700)`: the P-bass-with-pick thud that doubles the guitar roots. Synth fallback: `sawtooth` + `lpf(700)`.
- **Vocals** — `gm_voice_oohs`, gang-doubled an octave down.
- No pack needed — the preloaded tiers cover punk completely. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Vocabulary: major and minor triads stripped to their fifths — dyads, not full chords. Sevenths are a firing offense. Borrowed bVI and bVII do most of the color work, and the ambiguity between relative major and minor lets one chord loop read as hopeless or triumphant depending on how it's shouted.

- **I–vi–IV–V in D** — D, Bm, G, A (`[d3,a3] [b2,fs3] [g2,d3] [a2,e3]`) — doo-wop at double speed, the Ramones chassis. Use it when the song needs to sound like it's having fun anyway.
- **i–bVI–bIII–bVII in A minor** — Am, F, C, G (`[a2,e3] [f2,c3] [c3,g3] [g2,d3]`) — the four-chord axis of '77 and everything after. Two bars each, forever.
- **I–bVII–IV in D** — D, C, G (`[d3,a3] [c3,g3] [g2,d3]`) — the hop. The flattened bVII is the "we are not jazz" badge.
- **i–V in E minor** — Em to B (`[e2,b2] [b2,fs3]`) — the two-chord song. If the chorus can't survive two chords, it can't survive.

## Rhythm & feel

160–200 bpm; one cycle = one bar of 4/4, so `*8` is 8ths and that is genuinely all you need. Straight as a plank — no swing, no pulls. The grid is stiff on purpose, because the slop is supposed to live in the vocals, not the drums.

- **D-beat skeleton** — `[bd ~ sd ~ bd bd sd ~]` (hardcore and everything it touched)
- **Early punk skeleton** — `bd ~ sd ~ bd ~ sd ~` with 8th hats: kick 1 and 3, snare 2 and 4
- **Guitar skeleton** — `[a2,e3]*8` downstrokes locked to the kick
- **The fill** — `[ht mt lt ht]` in the last bar of a section; nothing else is licensed

The kick sits ON the beat, the snare cracks a hair late, and the crash marks section changes the way a chapter heading does — entrance, not decoration.

## Structure

The 90-second form at ~180 bpm (a bar is about 1.3 seconds): count-in 1 | verse 8 | chorus 8 | verse 8 | chorus 8 | bridge 8 | chorus 8 | stamp 1 — fifty bars, roughly 67 seconds, with room for one repeat of the back half before anyone gets bored.

```
// energy: 9 - 8 - 10 - 8 - 10 - 7 - 10 - 11
// it starts at 9 and never once gets polite
```

## Techniques that actually create "punk"

- **Downstroke 8ths at the tempo limit** — the physical strain of all-down strumming at 178 bpm is the genre's feel; switch to a picked pattern and it instantly becomes a different genre.
- **Power dyads, not triads** — `[a2,e3]` and nothing else. Dropping the third makes the harmony ambiguous and leaves sonic space for the vocal to define major or minor.
- **Three chords and the truth** — build verse and chorus from the same four chords with different rhythms; if you need a fifth chord the song is not finished being written.
- **The count-in** — `sound("rim!4")` for "1-2-3-4!". The only intro the genre needs, and the fastest possible way to announce what this is.
- **Gang-vocal octave doubling** — `.superimpose(x => x.transpose(-12).gain(.5))` on the vocal line: one voice becomes a mob.
- **The solo is the melody** — punk solos quote the vocal line an octave up on `gm_overdriven_guitar`; virtuosity is a firing offense second only to sevenths.
- **Crash as punctuation** — `sound("<cr ~ ~ ~>")` at section starts; fills are for exits, not entrances.
- **End on the stamp** — one chord held (`note("[a2,e3]@4")`), no ritard, no fade: the song stops because it's done, not because it got tired.

## Practice approach

- Transcribe three Ramones songs' chord loops in twenty minutes — they are all I–vi–IV–V and they are all two minutes long.
- Write a verse and chorus from the same four chords, differentiated only by rhythm and layer count.
- Get the d-beat sitting tight at 190 bpm with nothing but kick and snare before adding a single hat.
- Sing your chorus melody out loud: if you can't shout it in monotone after one listen, rewrite the hook, not the chords.
- Cut any section over eight bars; a twelve-bar bridge is an album-track bridge and this is not an album track.

## Example

```
// ═══ dead end kids — three-chord punk, 178bpm, d-beat ═══
// form: count-in 1 | verse 8 | chorus 8 | verse 8 | chorus 8 | bridge 8 | chorus 8 | stamp 1
// 50 bars ≈ 67 seconds: the whole argument, made before attention runs out
setcpm(178 / 4) // one cycle = one bar of 4/4

// ── guitar 1 — power dyads, straight 8th downstrokes: no thirds, the vocal owns the key ──
const vGtr = note("<[a2,e3]*8 [a2,e3]*8 [g2,d3]*8 [g2,d3]*8 [f2,c3]*8 [f2,c3]*8 [e2,b2]*8 [e2,b2]*8>").gain(.55) // Am G F E
const cGtr = note("<[a2,e3]*8 [a2,e3]*8 [f2,c3]*8 [f2,c3]*8 [c3,g3]*8 [c3,g3]*8 [g2,d3]*8 [g2,d3]*8>").gain(.68) // i bVI bIII bVII
const bGtr = note("<[f2,c3]*8 [f2,c3]*8 [g2,d3]*8 [g2,d3]*8 [e2,b2]*8 [e2,b2]*8 [e2,b2]*8 [e2,b2]*8>").gain(.5) // the run at E

const gtr = arrange(
  [1, note("[a2,e3]*8").gain(.35)], // the song starts mid-sentence, under the count-in
  [8, vGtr], [8, cGtr], [8, vGtr], [8, cGtr], [8, bGtr], [8, cGtr],
  [1, note("[a2,e3]@4").gain(.9)], // the stamp: one chord, let it feed
).sound("gm_overdriven_guitar").pan(.25).room(.12)

// ── guitar 2 — the same part an octave up, hard right: width by doubling, not extra notes ──
$: gtr.transpose(12).gain(.45).pan(.75)

// ── bass — roots in 8ths, straight through every change, pushing the band ──
const vBass = note("<a1*8 a1*8 g1*8 g1*8 f1*8 f1*8 e1*8 e1*8>")
const cBass = note("<a1*8 a1*8 f1*8 f1*8 c2*8 c2*8 g1*8 g1*8>")
const bBass = note("<f1*8 f1*8 g1*8 g1*8 e1*8 e1*8 e1*8 e1*8>")

const bass = arrange(
  [1, note("a1*8")],
  [8, vBass], [8, cBass], [8, vBass], [8, cBass], [8, bBass], [8, cBass],
  [1, note("a1@4")],
).sound("gm_electric_bass_pick").lpf(700).gain(.6)
$: bass

// ── drums — the d-beat: kick 1, snare 2, kick+kick 3, snare 4. "bd bd sd ~" is the fingerprint ──
const dbeat = sound("[bd ~ sd ~ bd bd sd ~]")
const tomfill = sound("~ ~ ~ ~ [ht mt lt ht]")
const verseKit = stack(dbeat, sound("hh*8").gain(.2))
const chorusKit = stack(dbeat, sound("[~ oh]*4").gain(.28), sound("<cr ~ ~ ~>").gain(.4))
const bridgeKit = stack(sound("bd ~ ~ sd ~ bd ~ sd").gain(.5), sound("hh*8").gain(.15))

const drums = arrange(
  [1, sound("rim!4").gain(.5)], // "1-2-3-4!" — the only intro the genre needs
  [8, verseKit.every(8, x => tomfill)],
  [8, chorusKit.every(8, x => tomfill)],
  [8, verseKit.every(8, x => tomfill)],
  [8, chorusKit.every(8, x => tomfill)],
  [8, bridgeKit.every(8, x => tomfill)], // the bridge thins to a strut
  [8, chorusKit.every(8, x => tomfill)],
  [1, sound("[cr,sd] ~ ~ ~").gain(.5)], // the last hit
)
$: drums

// ── vocals — verse sneers a two-bar phrase; chorus is the gang whoa-oh everyone came for ──
const vVox = note("<[a4@3 ~] [c5 b4 a4 g4] [a4@3 ~] [g4 a4 b4 ~] [f4@3 ~] [a4 c5 b4 a4] [ab4 a4 b4 ~] [e4@4]>")
const cVox = note("<[e5@2 d5] [c5@2 d5] [e5@2 d5] [e5@4] [c5@2 d5] [e5@2 f5] [g5@4] [e5@4]>")
const bVox = note("<f4@4 g4@4 [b4 a4] [b4 a4] ab4@4 e4@4 b4@2 c5 b4@2 a4 ab4@4>")

const vox = arrange(
  [1, silence],
  [8, vVox.gain(.34)], [8, cVox.gain(.5)], [8, vVox.gain(.34)], [8, cVox.gain(.5)],
  [8, bVox.gain(.3)], [8, cVox.gain(.55)],
  [1, note("a4@4").gain(.5)],
).sound("gm_voice_oohs").room(.25).superimpose(x => x.transpose(-12).gain(.5)) // the gang: an octave below, always
$: vox

// ── solo — the verse melody on guitar, an octave up: punk solos are the tune, faster ──
const solo = arrange(
  [41, silence],
  [8, vVox],
  [1, silence],
).sound("gm_overdriven_guitar").transpose(12).gain(.45).pan(.6).room(.2)
$: solo
```
