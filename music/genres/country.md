Country's equivalent moment is **the break** — the instrumental verse after the second chorus, 8 or 16 bars with no vocal, where the fiddle or the pedal steel takes the melody and the band quietly shows off behind it. It's the genre's solo section, but it's also its identity card: you can tell what kind of country song you're listening to entirely by who takes the break and how the rhythm section behaves under it.

## What the break actually is

After chorus two, instead of a third verse the band plays one: the fiddle states a double-stop-heavy melody, or the steel sings a bending line that quotes the vocal hook, or — in bluegrass-adjacent territory — the banjo takes it at double energy. Under the break the rhythm section usually **simplifies**: the train beat drops to a half-time lumber (`bd` on 1 only, one soft snare), the bass keeps booming but the chick guitar gets sparser, so the solo instrument sits in a frame that's suddenly roomier than anything the verses allowed. The break ends on a **signature lick** — a bent note into the downbeat, a walk-up everybody hears coming — that hands the microphone back to the singer for the last verse. Structure it as relief, not as climax: the final chorus after the break is always the loudest thing in the song, and the break's job is to clear space so that landing works.

## The layers

- **Rhythm guitar, the tick-tack chick** — `gm_electric_guitar_muted` (General MIDI has no acoustic-muted; the muted electric is exactly this sound anyway) playing chord stabs on beats 2 and 4: `.struct("~ x ~ x")` over one chord per bar. This plus the bass is the boom-chick engine.
- **Acoustic strum** — `gm_acoustic_guitar_steel`, full-quarter strums at low gain with a little `room`; it's glue, not foreground.
- **Bass** — `gm_electric_bass_pick` (modern) or `gm_acoustic_bass` (older, western): alternating root and fifth in quarters. In A, an A bar is literally `note("a2 e3 a2 e3")` — boom, chick, boom, chick.
- **Pedal steel** — no GM steel patch exists, so fake it: `gm_electric_guitar_clean` with half-step **grace-pair bends** — a quick `[gs4 a4]` where gs4 snaps into a4 reads as a string bend. Long release, some `room`, fills at the ends of vocal lines.
- **Fiddle** — `gm_fiddle`, answering vocal lines with double stops (mini-notation chords like `[d4,gb4]`) and taking the break in the fiddle variant.
- **Banjo** — `gm_banjo` when the song tips bluegrass: rolling 8ths, huge forward drive, usually reserved for one section so it reads as a gear change.
- **Drums** — the **train beat**: kick on 1 and 3, snare galloping in 8ths with the accents landing on 2 and 4. In strudel: `stack(sound("bd ~ bd ~"), sound("sd*8").gain("[.16 .1 .55 .12 .16 .1 .55 .12]"))`. Ballads swap to a soft 4/4 with `rim` instead of the snare backbeat.

## Sample kit

- **Tick-tack** — `gm_electric_guitar_muted` ✓ (GM has no acoustic-muted; the muted electric is the sound anyway).
- **Strum & bass** — `gm_acoustic_guitar_steel` glue; `gm_electric_bass_pick` (modern) / `gm_acoustic_bass` (western); `gm_slap_bass_1` when it tips rockabilly.
- **Pedal steel fake** — `gm_electric_guitar_clean` + grace-pair bends, as layered; there is no steel patch anywhere in the preloaded sets — don't go looking.
- **Fiddle & banjo** — `gm_fiddle` ✓, `gm_banjo` ✓, both exactly right.
- **Drums** — default kit train beat; VCSL `cowbell`/`woodblock` for the novelty-number percussion, `tambourine` for the two-step variant.
- No pack needed — the preloaded tiers cover country. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Country harmony is honest to a fault: **plain triads on I, IV and V**, major keys, few sevenths (and a seventh is a hint, not a function). In A the whole vocabulary is A, D and E; in G it's G, C and D. Canonical progressions, roman and spelled in A:

- **Verse** — I I IV I | I V I I → A A D A | A E A A (the workhorse 8-bar)
- **Chorus** — IV I V I, twice → D A E A | D A E A (lift from the first change being IV)
- **Turnaround walk-up** — the bass walks the scale into the next section: `note("a2 b2 cs3 d3")` at the end of a verse leading into a D chorus. This walk is the genre's punctuation mark.
- **Ballad cadence** — I vi IV V I → A F#m D E A, used slowly, one chord per bar at 4/4 ballad tempo.

Two color chords exist and get used sparingly: the vi (F#m in A) for a beat of ache, and the bVII in the truck-driver context below. The one big harmonic event in the genre is the **truck-driver modulation** — the final chorus moves up a whole step (A to B): `transpose(2)` on every lane, no apology, no preparation. It's cheesy, it's beloved, it works.

## Rhythm & feel

**Honky-tonk train beat, 2/4**: older and faster material counts in two; set the cycle to the 2/4 bar with `setcpm(bpm/2)` and the patterns halve — `"bd sd"` per bar, bass `"a2 e3"` per bar, chick on the second beat only. **4/4 train beat, 140–170 bpm**: kick 1 and 3, snare 8ths with accents on 2 and 4 (the gallop above), hi-hat none or a tight `hh` on the off-8ths. **4/4 ballad, 72–92 bpm**: `rim` or a soft `sd` with `room(.4)` on 2 and 4, kick on 1 (and a ghost on 3), everything played like it's apologizing. **Western swing, 120–150, swung**: `swing(.1)` on the 8ths, walking bass, jazz chords trying to sneak in — keep them out unless you mean swing specifically. The feel devices that matter: bass alternation is law (root, fifth, root, fifth — never a walking line except the walk-up into a chorus), the snare gallop is lighter than you think (the accents carry it, the ghosts are brushes), and fills land at the end of every second bar — the grid is call-and-response even when nobody sings.

## Structure

The standard up-tempo song: intro 2–4 | verse 8 | chorus 8 | verse 8 | chorus 8 | **break 8** | verse 8 | final chorus 8 + tag 2 | outro 2. The final chorus carries the truck-driver modulation (up a whole step) and the tag repeats its last line with a walk-up under it. Ballads stretch the sections (verses 16) and skip the break's energy spike — the fiddle plays a solo over a thinner band instead. Energy graph: intro mid | verses steady-low with fills creeping in | choruses +1 | break steps back to clear | final chorus (transposed) is the peak | tag snaps it shut. The breaks-then-peak shape is the whole arrangement trick; if the break is the loudest section, the form falls backwards.

## Techniques that actually create "country"

- **Boom-chick** — bass alternating root-fifth in strict quarters (`note("a2 e3 a2 e3")`) with the muted-guitar chick on 2 and 4. If these two lanes are right, everything else is decoration; if they're wrong, nothing saves it.
- **Train-beat ghosts** — the snare plays all the 8ths but only 2 and 4 are loud: `sound("sd*8").gain("[.16 .1 .55 .12 .16 .1 .55 .12]")`. The quiet notes are the gallop; keep them quieter than feels natural.
- **Steel bends as grace pairs** — `[gs4 a4]`, `[b4 cs5]`: a fast chromatic snap onto a chord tone. Long `release`, place them at the ends of vocal phrases, never on the downbeat — the steel answers, it doesn't lead.
- **Fiddle double stops** — two-stop mini-chords (`[d4,gb4]`, `[a4,cs5]`) instead of single lines. One stopped double-stop answer per two bars reads more authentic than a whole fiddle melody.
- **The walk-up** — `note("a2 b2 cs3 d3")` into every chorus and the tag. It's the genre's comma; use it so consistently the listener starts anticipating it.
- **Truck-driver modulation** — final chorus `.transpose(2)` on every pitched lane at once, unannounced. The lack of preparation is the style; smoothing it out makes it pop. One engine gotcha: `transpose()` silently fails on `s`/`f` accidentals (`fs`, `gs`, `df`), so respell anything inside a transposed lane as b-flats (`gb`, `db`, `ab`) — untransposed lanes can keep the s-spellings.
- **Half-time under the break** — kit drops to `bd` on 1 and one soft snare; the band makes room, the solo breathes, and the final chorus gets to be the loud one.
- **Tag** — repeat the last chorus line over the walk-up and end on a single accent: band hit on the downbeat, ringing chord, done. `sound("<[bd sd sd sd] [bd ~ ~ ~]>")` is a complete ending.

## Practice approach

- Program boom-chick and train beat alone and listen to them for a minute straight; if they don't hypnotize you, fix them before adding anything.
- Transcribe one Merle Haggard verse-chorus and one Ray Price shuffle by ear; count where the fills land — it's always bar 4 and bar 8.
- Write a whole song section using only A, D and E triads; only add a seventh or a vi when the plain version genuinely hurts.
- Practice the grace-pair bends until a handful of `[gs4 a4]` snaps read as steel rather than as fast notes.
- Arrange the break last: decide what drops out, then what the solo instrument plays. The drops matter more.

## Example

```
// ═══ break in a — honky-tonk train beat, 152 bpm ═══
// form: intro 2 | V1 8 | chorus 8 | V2 8 | chorus 8 | steel break 8 | V3 8 | final chorus 8 (up a step) | tag 2
// energy: verses steady | choruses +1 | break clears room | final chorus (B, transposed) peaks | tag snaps shut
setcpm(152 / 4) // one cycle = one bar of 4/4

// train drums — kick 1 & 3, snare gallops in 8ths, accents land 2 & 4
const train = stack(sound("bd ~ bd ~").gain(.85), sound("sd*8").gain("[.16 .1 .55 .12 .16 .1 .55 .12]").room(.25))
const breakBeat = stack(sound("bd ~ ~ ~").gain(.7), sound("~ sd ~ ~").gain(.35).room(.25)) // under the steel: the train slows to a walk
const drums = arrange(
  [2, train], [8, train], [8, train], [8, train], [8, train],
  [8, breakBeat], // the break: half-time, suddenly roomy
  [8, train], [8, train],
  [2, sound("<[bd sd sd sd] [bd ~ ~ ~]>").gain(.75)], // the tag
)

// changes — honest triads, one per bar
const verseCh = "<A A D A A E A A>"
const chorusCh = "<D A E A D A E A>"
const breakCh = "<A A D D A E A A>"

// boom-chick bass — root and fifth in strict quarters, walk-up into each chorus
const verseBass = "<[a2 e3 a2 e3] [a2 e3 a2 e3] [d3 a3 d3 a3] [a2 e3 a2 e3] [a2 e3 a2 e3] [e2 b2 e2 b2] [a2 e3 a2 e3] [a2 b2 cs3 d3]>"
const chorusBass = "<[d3 a3 d3 a3] [a2 e3 a2 e3] [e2 b2 e2 b2] [a2 e3 a2 e3] [d3 a3 d3 a3] [a2 e3 a2 e3] [e2 b2 e2 b2] [a2 e3 a2 e3]>"
const breakBass = "<[a2 e3 a2 e3] [a2 e3 a2 e3] [d3 a3 d3 a3] [d3 a3 d3 a3] [a2 e3 a2 e3] [e2 b2 e2 b2] [a2 e3 a2 e3] [a2 e3 a2 e3]>"
const bass = arrange(
  [2, note("<[a2 e3 a2 e3] [a2 e3 a2 e3]>")], [8, note(verseBass)], [8, note(chorusBass)],
  [8, note(verseBass)], [8, note(chorusBass)], [8, note(breakBass)], [8, note(verseBass)],
  [8, note(chorusBass).transpose(2)], // truck-driver modulation: A → B, no warning
  [2, note("<[b2 cs3 ds3 e3] [e2 ~ ~ ~]>")], // tag walk-up in the new key
).sound("gm_electric_bass_pick").gain(.6).room(.1)

// the chick — muted electric stabs on 2 & 4: with the bass, this is the whole engine
const chick = changes => chord(changes).anchor("a3").voicing().sound("gm_electric_guitar_muted").struct("~ x ~ x").gain(.28)
const guitarChick = arrange(
  [2, chick("<A A>")], [8, chick(verseCh)], [8, chick(chorusCh)], [8, chick(verseCh)],
  [8, chick(chorusCh)], [8, chick(breakCh).struct("x ~ x ~")], [8, chick(verseCh)], // sparser under the break
  [8, chick(chorusCh).transpose(2)], [2, chick("<B B>").struct("<[x ~ ~ ~] [x ~ ~ ~]>")],
)

// acoustic strum — glue at low gain, every beat
const strum = changes => chord(changes).anchor("d3").voicing().sound("gm_acoustic_guitar_steel").struct("x x x x").gain(.15).room(.35)
const guitarStrum = arrange(
  [2, silence], [8, strum(verseCh)], [8, strum(chorusCh)], [8, strum(verseCh)],
  [8, strum(chorusCh)], [8, strum(breakCh)], [8, strum(verseCh)],
  [8, strum(chorusCh).transpose(2)], [2, strum("<B B>").struct("<[x ~ x x] [x ~ ~ ~]>")],
)

// steel — no gm patch: clean guitar, bends as grace pairs, answers at the ends of lines
const steelV = "<[~ ~ ~ ~] [~ ~ [gs4 a4] ~] [~ ~ ~ ~] [~ ~ [b4 cs5] ~] [~ ~ ~ ~] [~ [e5 fs5] ~ ~] [~ ~ ~ ~] [~ [gs4 a4] ~ ~]>" // untransposed: s-spellings fine
const steelCh = "<[~ ~ ~ ~] [~ ~ [db5 d5] ~] [~ ~ ~ ~] [~ ~ [e5 gb5] ~] [~ ~ ~ ~] [~ ~ [db5 d5] ~] [~ ~ ~ ~] [[ab5 a5] ~ ~ ~]>" // b-flats only: transpose(2) breaks on s/f spellings
const steelBreak = "<[[a4,cs5] e5 ~ ~] [[gs4 a4] b4 cs5 ~] [[fs4,a4] d5 ~ ~] [[fs4,a4] [g4,b4] [fs4,a4] ~] [e5 d5 [cs5 a4] ~] [gs4@2 b4 e5 ~] [[a4,cs5] a5 ~ ~] [[gs4 a4] ~ ~ ~]>"
const steel = arrange(
  [2, silence], [8, silence], // V1 is plain: no steel until the song earns it
  [8, note(steelCh)], [8, note(steelV)], [8, note(steelCh)],
  [8, note(steelBreak).gain(.5)], // the break itself: double stops and bends
  [8, note(steelV)], [8, note(steelCh).transpose(2)],
  [2, note("<[[as5 b5] ~ ~ ~] [b5 ~ ~ ~]>")], // one last bend in B, ringing
).sound("gm_electric_guitar_clean").gain(.38).room(.4).release(.8)

// fiddle — double-stop answers in the back verses, silent elsewhere
const fiddleV = "<[~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ [d4,gb4]] [~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ ~] [~ ~ ~ [a4,db5]]>" // gb4/db5: transposed lane, b-flats only
const fiddle = arrange(
  [2, silence], [8, silence], [8, silence], [8, note(fiddleV)], [8, silence], [8, silence], // chorus 2 belongs to the steel
  [8, note(fiddleV)], [8, note(fiddleV).transpose(2)], [2, silence],
).sound("gm_fiddle").gain(.35).room(.35)

$: drums
$: bass
$: guitarChick
$: guitarStrum
$: steel
$: fiddle
```
