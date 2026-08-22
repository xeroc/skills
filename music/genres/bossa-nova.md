Bossa nova's equivalent moment is **the hush** — the stretch, usually just before or just after a melody statement, where the arrangement thins back to the nylon-string guitar alone: the thumb walking root and fifth, the chords ticking on the syncopations, everything else gone quiet around it. It is the inverse of salsa's mambo: where salsa answers intimacy with a shout chorus, bossa treats quietness itself as the climax, and the final Imaj7–ii7–V7alt turnaround lands with the emotional weight other genres spend a drop on.

## What the hush actually is

A bossa performance lives at conversational volume, and its dynamics are a terrace, not a curve — the "big" section is one brush layer louder than the small one, and the "quiet" section subtracts players entirely. The hush is that subtraction taken to its limit: guitar alone, or guitar plus a whispered melody, for two, four, eight bars. Because the guitar is self-sufficient — bass note in the thumb, syncopated harmony in the fingers, the clave implied by what it doesn't play — the music never feels empty, only close. When the brushes and the melody return, they arrive with the warmth of a remembered promise.

Structurally, the hush is also where the harmony gets to speak. The genre's signature move is the Imaj7–ii7–V7alt turnaround, voiced with the altered tone (b9, b13) arriving just before the resolution — a small knot tied and untied every eight bars. Placed inside a hush, with nothing masking it, that turnaround is the emotional core of the style; it's the moment in "Corcovado" and "Chega de Saudade" that makes the room lean in.

The other quiet secret is tempo discipline: bossa sits at a walking 120–130 BPM and never rushes, because urgency would break the intimacy. The music only whispers, but it whispers in perfect time.

## The layers

- **Nylon guitar** — `gm_acoustic_guitar_nylon` (or `pluck` for a rounder attack), split into two lanes: the thumb on root and fifth (`note("<[c2 ~ ~ ~ c2 ~ ~ ~] ...>")` on beats 1 and 3) and the chord lane shadowing the bossa clave (hits on 2 and 3, variations on the 2-side). This instrument carries the whole style — build it first and it will survive every subtraction.
- **Brushes/cross-stick** — `rim` doubling the 2-3 bossa clave: `<[~ ~ rim ~ rim ~ ~ ~] [rim ~ ~ rim ~ ~ rim ~]>` (hits on 2, 3 | 1, 2&, 4), quiet, dry.
- **Brush swish** — `sh` on offbeat eighths at whisper gain (`s("[~ sh]*4")`), a little `room` for air. It reads as brush noise, not as a hi-hat — keep it under everything.
- **Surdo-style kick** — `bd` muffled with an `lpf`, on 1 and 3, gain around .2. One pulse per two beats, felt more than heard.
- **Melody** — `gm_flute` for the Getz-lineage breathy phrasing (a voice in the real world). Sparse, starts off the beat, ends phrases early, and leaves bars empty. The melody is a guest in the guitar's home.
- **Color** — optionally `piano` for a counter-line or `gm_synth_strings_1` at very low gain for the bridge's one step up in warmth. Anything more and you've written lounge.

## Sample kit

- **Nylon guitar** — `gm_acoustic_guitar_nylon` (percussive chuck) or `gm_acoustic_guitar_nylon` (warmer, more Jobim); `pluck` as the round-attack fallback. Always two lanes: thumb + chord hand.
- **Percussion** — VCSL latin core is preloaded: `conga` `bongo` `cabasa` `agogo` (the Brazilian agogô) `tambourine` `guiro` — pick `:k` variants for tone/slaps. The cross-stick `rim` clave and the `sh` swish stay default-kit.
- **Brushes option** — the Dirt `jazz` set (`jazz:7` brushed snare, `jazz:0` BD) when the arrangement wants brushes instead of sticks.
- **Melody** — `gm_flute` (Getz-lineage breath) or `gm_tenor_sax` (the actual Getz); soft attacks, early releases.
- **Keys/color** — `piano` counter-lines (`steinway` for a real grand); `gm_synth_strings_1` at whisper gain for the bridge only.
- No pack needed — the preloaded tiers cover bossa. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Sophisticated but unhurried — one chord per bar, changes often anticipated on the "and of 4" before the barline. In C major (turn to F for the Ipanema changes):

- **Imaj7 – ii7 – V7b9 – Imaj7** — Cmaj7 – Dm7 – G7b9 – Cmaj7 — the anchor turnaround. The b9 (ab against g) is the ache; resolve it into the maj7's b natural and the knot unties.
- **iii7 – VI7 – ii7 – V7** — Em7 – A7 – Dm7 – G7 — the circle tail used to extend an A section; the A7 is where a chromatic bassline (a → ab → g) sneaks in under the changes.
- **I – II7 – ii7 – V7 (Ipanema A)** — Fmaj7 – G7 – Gm7 – C7 in F — the signature lateral move: II7 slides up, then melts to its own minor before the V7 walks home.
- **Imaj7 – vi7 – ii7 – V7b9** — Cmaj7 – Am7 – Dm7 – G7b9 — the same turnaround with a melancholy front porch, for second verses and codas.

Voice the final tonic with a non-root note on top (9th or 5th) and let the guitar's thumb supply the root a beat before the chord settles — a slightly staggered landing reads as breathing.

## Rhythm & feel

120–130 BPM (`setcpm(124/4)`), and crucially: straight. The famous bossa "lilt" is not swing — it comes from velocity shaping, the anticipated changes, and melody phrases that start on offbeats. The skeletons:

- **Bossa clave 2-3** (two bars of 8ths) — `[~ ~ rim ~ rim ~ ~ ~] [rim ~ ~ rim ~ ~ rim ~]` — hits on 2, 3 in bar one, 1, 2&, 4 in bar two.
- **Guitar thumb** (per bar) — `c2 ~ ~ ~ c2 ~ ~ ~` — root and fifth on 1 and 3.
- **Guitar chords** (per bar) — `~ ~ [chord] ~ [chord] ~ ~ ~` — hits on 2 and 3, shadowing the clave.
- **Anticipation** (change bars) — `~ ~ ~ ~ ~ ~ ~ [next-chord]` — the 4& pushes the new chord in early.
- **Swish** (per bar) — `~ sh ~ sh ~ sh ~ sh` — offbeat air, quieter than you think.

Feel devices: chords land on the 2-side of the clave and never double the thumb; harmonic changes anticipate on the "and of 4" so the barline is crossed, not landed on; melody phrases begin on 1& or 2& and end a beat early — rushing the tail of a phrase is how machines play bossa; and dynamics step in small terraces (add the swish, add the stick, add the kick — never all at once).

## Structure

The form runs `intro 4 → A 8 → A' 8 → B 8 → A 8 → coda 2` with energy `3 · 4 · 4 · 5 · 4 · 1`.

The form is songbook-shaped (AABA in spirit, ABACA in practice) but the energy never exceeds one terrace of difference. The intro starts with guitar plus air (no pulse), the bridge adds a single layer of warmth, and the coda is the hush resolved — one held chord, one sighing note, nothing else. If your arrangement's energy graph looks like anything other than a table top with a doily on it, pull layers back off.

By convention both ends of the form belong to the guitar alone: the intro establishes the two-lane cell before anyone else is allowed to play, and the coda returns to it because nothing else can end a bossa quietly enough. Everything you add in between is borrowing from that frame — plan the returns, not just the departures.

## Techniques that actually create "bossa nova"

- **The thumb/finger split** — the guitar is two instruments: a walking bass (root, fifth, occasional passing tone, always beats 1 and 3) and a comping hand that never plays on 1. Write them as two lanes and the style is 80% done; merge them into block chords and it dies.
- **Clave shadowing** — the chord lane and the cross-stick both shadow the 2-3 bossa clave without ever stating it as a fixed ostinato. Vary which hits sound; the clave is the reference frame, not a part.
- **Anticipated changes** — the new chord's voicing (and often the bass root) arrives on the "and of 4" before its bar. This constant early crossing of the barline is the genre's rhythmic signature at the harmonic level.
- **Terrace dynamics** — sections are layer-count changes of one. The hush is a section: plan it in the arrangement, don't improvise it.
- **Breathy sparse melody** — phrases start off the beat, end early, and leave whole bars empty; notes are long with soft attacks (`attack(.02)`, generous `release`). The space between notes is where the style lives.
- **The altered-V knot** — G7b9 or G7b13 voicings right before the tonic resolution, especially inside a hush. One altered tone, not a stack — the ache is surgical, not dramatic.
- **Intimate mixing** — small `room`, low gains, the guitar pair slightly panned apart, the melody close and dry-ish. Reverb wash reads as elevator; intimacy reads as a room with two people in it.
- **The non-root ending** — land the last chord voiced with the 3rd or 9th on top while the thumb alone supplies the root. A root-on-top ending is a period; this is an ellipsis.
- **Countermelody in the gaps** — when the melody rests for two or more bars, let the chord lane add one passing tone between its usual hits. It answers the singer the way a second conversation answers the first across a small table — quieter, and never at the same time.

## Practice approach

- Loop the two-lane guitar cell (thumb + chord lane) over Imaj7–ii7–V7b9–Imaj7 in C until you can leave out random clave hits and it still grooves — the implied hits are the feel.
- Play the "Girl from Ipanema" A changes in F with only the thumb, then only the chord lane, then both; notice the changes anticipate at 4& and copy that everywhere.
- Write an 8-bar melody using six notes, all phrases starting on offbeats, then delete every note that doesn't hurt to remove.
- Record your full arrangement, then play it back while muting one layer at a time — bossa arrangements are finished when removing any layer still works and adding any layer doesn't.
- Sing the melody against a metronome at 124 BPM and deliberately end each phrase a half-beat early; that early release is the phrasing fingerprint of the style.
- End on a tonic voiced with the 9th on top and no root above the octave; if it sounds finished like a pop ending, revoice it until it sounds like a sentence trailing off.
- Learn the "Corcovado" intro by ear and notice it is nothing but the two-lane cell with one added 9th — the whole style's promise delivered before the band enters.

## Example

```
// ═══ tarde em ipanema — bossa nova, 124 bpm ═══
// form: intro 4 | A 8 | A' 8 | B 8 | A 8 | coda 2
// energy: 3        4      4      5      4      1
// straight 16ths, no swing — the lilt is velocity, anticipation, and space
setcpm(124 / 4) // one cycle = one 4/4 bar

// ── the guitar: thumb on 1 and 3, chords shadowing the 2-3 bossa clave (2, 3 | 1, 2&, 4) ──
// A sections: Cmaj7 – Dm7 – G7b9 – Cmaj7 (x2) | B section: Em7 – A7 – Dm7 – G7
const gtrBass = note("<[c2 ~ ~ ~ c2 ~ ~ ~] [d2 ~ ~ ~ d2 ~ ~ ~] [g1 ~ ~ ~ g1 ~ ~ c2] [c2 ~ ~ ~ c2 ~ ~ ~]>").sound("gm_acoustic_guitar_nylon").gain(.6)
const gtrTop = note("<[~ ~ [e4,g4,b4] ~ [e4,g4,b4] ~ ~ ~] [~ ~ [f4,a4,c5] ~ [f4,a4,c5] ~ ~ ~] [~ ~ [f4,ab4,b4] ~ [f4,ab4,b4] ~ ~ [e4,g4,b4]] [~ ~ [e4,g4,b4] ~ [e4,g4,b4] ~ ~ ~]>").sound("gm_acoustic_guitar_nylon").gain(.48).cut(2)
const gtrBassB = note("<[e2 ~ ~ ~ e2 ~ ~ ~] [a1 ~ ~ ~ a1 ~ ~ ~] [d2 ~ ~ ~ d2 ~ ~ ~] [g1 ~ ~ ~ g1 ~ ~ c2]>").sound("gm_acoustic_guitar_nylon").gain(.6)
const gtrTopB = note("<[~ ~ [g4,b4,e5] ~ [g4,b4,e5] ~ ~ ~] [~ ~ [e4,g4,cs5] ~ [e4,g4,cs5] ~ ~ ~] [~ ~ [f4,a4,c5] ~ [f4,a4,c5] ~ ~ ~] [~ ~ [f4,a4,b4] ~ [f4,a4,b4] ~ ~ [e4,g4,b4]]>").sound("gm_acoustic_guitar_nylon").gain(.48).cut(2)

// ── brushes: cross-stick on the clave, swish on the offbeats, muffled kick on 1 and 3 ──
const stick = s("<[~ ~ rim ~ rim ~ ~ ~] [rim ~ ~ rim ~ ~ rim ~]>").gain(.3)
const swish = s("[~ sh]*4").gain(.13).room(.3)
const surdo = s("bd ~ bd ~").gain(.22).lpf(300)

// ── comp book: who plays when — subtraction is the arrangement ──
const compA = stack(gtrBass, gtrTop, stick, swish, surdo)
const compB = stack(gtrBassB, gtrTopB, stick, swish, surdo, s("oh ~ ~ ~ ~ ~ ~ ~").gain(.14))
const comp = arrange(
  [4, stack(gtrBass, gtrTop, swish)],   // intro: guitar and air, no pulse yet
  [8, compA],
  [8, compA],
  [8, compB],                           // bridge: one terrace warmer
  [8, compA],
  [2, stack(gtrBass, gtrTop, s("[~ sh]*4").gain(.08))], // coda: the hush
)

// ── melody: breathy, sparse, lands off the beat and stops early ──
const melA = note("<[g4 ~ ~ ~ ~ ~ b4 ~] [d5 ~ ~ ~ ~ ~ ~ ~] [~ ~ a4 ~ ~ ~ c5 ~] [b4@2 ~ ~ ~ ~ ~ ~ ~] [~ ~ g4 ~ e4 ~ ~ ~] [~ ~ ~ ~ a4 ~ c5 ~] [d5@2 ~ ~ ~ ~ ~ ~ ~] [~ ~ b4 ~ g4 ~ ~ ~]>")
const melB = note("<[e5 ~ ~ d5 ~ ~ b4 ~] [~ ~ ~ ~ ~ cs5 ~ ~] [d5 ~ ~ ~ a4 ~ ~ ~] [b4 ~ ~ ~ ~ ~ ~ ~]>")

const mel = arrange(
  [4, silence],
  [8, melA],
  [8, melA],
  [8, melB],
  [8, melA],
  [2, note("<[~ ~ g4 ~ ~ ~ ~ ~] [e4@6 ~ ~ ~ ~ ~ ~ ~]>")], // the sigh: 3rd of the tonic, not the root
).sound("gm_flute").gain(.4).attack(.02).release(.35).room(.45)

$: comp
$: mel
```
