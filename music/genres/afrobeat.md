Afrobeat's equivalent moment is **the break** — the point, often ten or more minutes into a Fela Kuti side, when most of the band drops out and two or three interlocking patterns are suddenly exposed, naked, holding the groove by themselves. It is the drop inverted: instead of building density to a climax, afrobeat builds density, subtracts, lets you hear the machinery, and then returns the full weight — and the return is the payoff. The genre's emotional currency is patience distributed over long forms.

## What the break actually is

An afrobeat track is a small democracy of repeating patterns: bell, shakers, congas, two guitars, bass, keys, and a horn section that states riffs rather than melodies. Each part is simple enough to hold for ten minutes; the complexity lives in how they interlock. The arrangement doesn't develop the patterns — it develops their membership. Layers enter one at a time, everything plays together for a long stretch, then comes the break: the horns stop, the guitars stop, maybe only the bass and one percussion voice remain for eight bars while the implied groove keeps ticking in the listener's ear. When the full stack returns, the same patterns you'd stopped noticing arrive as a wall.

The other pillar is the horns: Fela's trumpet and the tenor/baritone saxes play call-and-response riffs — a two-bar figure answered by a second figure or a sustained chord stab, over harmony that barely moves. The riffs are the "vocals" of the instrumental stretches, and they trade with the actual vocals the same way. If your horns are playing through-composed lines, they're wrong for the idiom; a riff you could transcribe in one listen is the correct unit of melody.

## The layers

- **Bells** — `cb` carrying the standard pattern in 16ths: `"cb ~ ~ cb ~ ~ cb ~ cb ~ ~ cb ~ ~ cb ~"` (hits on 1, 1a, 2&, 3, 3a, 4&). This is the 12/8 timeline of West African music flattened onto the 4/4 grid, and it's the layer the whole groove hangs from.
- **Shakers** — `sh*16` with a shaped gain pattern like `[.16 .3 .1 .22 .16 .3 .1 .22 .16 .3 .1 .22 .16 .3 .1 .26]` so the stream swings in threes against the guitars' twos.
- **Congas** — `conga` and `lt` in a two-bar groove like `<[conga ~ lt conga ~ lt conga ~] [conga ~ lt conga ~ lt lt conga]>`, plus `{conga ~ lt}%3` — a three-cycle polymeter — for the deep-water sections where you want the floor to drift and re-sync.
- **Rhythm guitar** — `gm_electric_guitar_muted` on pure offbeat 16ths: `note("a4").struct("~ x ~ x ~ x ~ x ~ x ~ x ~ x ~ x")` with `cut` for the percussive chop. One note, forever — it's a drum that happens to have a pitch.
- **Tenor guitar** — the second guitar, `gm_electric_guitar_muted` or `pluck`, playing a two-bar high ostinato in eighths — a pentatonic cell that winds around the rhythm guitar's offbeats. The interlock of these two parts is the genre's signature texture.
- **Keys** — `piano` stabs, `chord("<Am7 D9>").anchor("a4").voicing()`, hit on a syncopation like `"x ~ ~ x ~ ~ ~ ~"` once or twice a bar. Rhodes in the real world; the piano sample carries the role.
- **Bass** — `triangle` with a touch of `shape` and an `lpf` — the lead instrument. A melodic two-bar ostinato in eighths with syncopated pickups, repeated with total conviction. Fela's basslines sing; write them like a riff, not a root service.
- **Horns** — `gm_trumpet` asking, `gm_tenor_sax` answering (often an octave down). Two-bar riffs and sustained chord stabs traded between them; they play in sections, they rest in sections.

## Sample kit

- **Congas** — VCSL `conga` over the tom simulation: `:0–:9` conga (mid), `:10–:19` quinto (high), `:20+` tumba (low); probe neighboring indices for stroke characters. `{conga:10 ~ conga:20}%3` keeps the polymeter trick with real skins.
- **Bells & shakers** — `cb` carries the standard pattern; `agogo` (VCSL) is the West African-derived alternative; `cabasa` reads as shekere when `sh` feels too hissy.
- **Keys — the organ upgrade** — `gm_percussive_organ` is Fela's bubble; `gm_drawbar_organ` for the full-spectrum version. Piano stabs work, but organ is the idiom.
- **Bass** — `gm_electric_bass_finger`: Fela's bass was electric, melodic, and mixed forward. Synth fallback: `triangle` + `shape(.25)` + `lpf`.
- **Guitars** — `gm_electric_guitar_muted` for both interlocking parts.
- **Horns** — `gm_trumpet` asks, `gm_tenor_sax` answers, `gm_baritone_sax` adds the low weight on repeats.
- No pack needed — the preloaded tiers cover afrobeat. (Full options: `references/SAMPLE-CATALOG.md`.)

## Harmony

Modal and static — one or two chords, vamps that run for entire sections. The motion comes from the bass ostinato and the riff phrasing, not from functional progressions. In A minor:

- **One-chord vamp** — Am7 for an entire section — the "Zombie" discipline. If the groove is right, nothing is missing; if it's wrong, no chord change will save it.
- **i7 – IV9** — Am7 – D9 — the classic dorian uplift: four bars of i, four bars of IV9, with the bass ostinato transposed rather than rewritten. The 9th on the IV is what keeps it bright instead of pop-flat.
- **bVII7 – i7** — G9 – Am7 — the mixolydian pull back home; works as a two-chord shuffle between horn statements.
- **i7 – iv7** — Am7 – Dm7 — the darker alternative to i–IV when the track wants weight instead of lift.

## Rhythm & feel

100–115 BPM (`setcpm(108/4)`), straight 16ths, no swing. The feel is the interlock, and the interlock is 2-against-3: the bell and shakers phrase in threes (the 12/8 ghost inside the 4/4 grid) while the guitars phrase in twos, so the floor subtly drifts and locks every bar or three. The skeletons:

- **Bell, standard pattern** (one bar of 16ths) — `cb ~ ~ cb ~ ~ cb ~ cb ~ ~ cb ~ ~ cb ~` — hits on 1, 1a, 2&, 3, 3a, 4&.
- **Rhythm guitar** (one bar of 16ths) — `~ a4 ~ a4 ~ a4 ~ a4 ~ a4 ~ a4 ~ a4` — offbeats only, forever.
- **Tenor guitar** (two bars of 8ths) — `[a4 c5 d5 c5 a4 c5 d5 g4] [a4 c5 d5 e5 d5 c5 a4 c5]`.
- **Bass ostinato** (two bars of 8ths) — `[a2 ~ a2 ~ ~ a2 c3 ~] [a2 ~ e2 g2 a2 ~ g2 e2]`.
- **Keys stab** (one bar of 8ths) — `x ~ ~ x ~ ~ ~ ~`.

Feel devices: the bass states the downbeat more than anyone else (everything else syncopates around it); the guitars never land where the bell lands; horn riffs begin on offbeats so they lean into the groove; and the polymeter layer (`{conga ~ lt}%3`) is a spice for late sections, not a base layer — add it once the straight interlock has fully hypnotized.

## Structure

Fela's sides run 10–20 minutes; the proportions below compress one to 56 bars — keep the proportions, stretch the repeats. The form runs `perc intro 8 → groove 8 → full + horns 8 → break 4 → horns talk 8 → full 8 → solo 8 → outro 4` with energy `3 · 5 · 6 · 4 · 7 · 6 · 7 · 5`.

## Techniques that actually create "afrobeat"

- **Interlocking ostinati** — every layer is a pattern a child could clap, and the ensemble is a machine no one player understands alone. Compose each part against the others: a new layer must avoid doubling any existing layer's attacks, or it collapses the texture instead of thickening it.
- **Subtractive arrangement** — sections are defined by who is absent. Write your full groove first, then create the form by muting lanes; the break is a section, not an effect.
- **2-against-3 as the ground state** — bell/shakers phrasing in threes against guitars in twos. You don't need to write a polymeter; the flattened 12/8 standard pattern does it automatically against any straight duple layer.
- **Call-and-response horns** — trumpet states a two-bar riff, tenor answers with a second figure or a sustained stab. Never overlap them; the gap between statement and answer is where the groove shows through.
- **The bass as lead voice** — melodic, syncopated, mixed forward. If your bassline could be sung, it's right; if it could be replaced by a root-note kick, rewrite it.
- **Repetition as hypnosis** — hold a pattern 16 bars before you're bored, not 4. The genre trusts the listener to hear a loop morph via context; earn that trust before changing anything.
- **Minor pentatonic riff vocabulary** — guitars, horns, and solos all draw from A minor pentatonic (a, c, d, e, g) with occasional dorian color (fs over D9). Chromaticism reads as foreign; the mode is the dialect.

## Practice approach

- Loop the bell pattern alone and clap a different simple pattern against it every minute — offbeats, threes, downbeats — until you feel which combinations lock and which smear.
- Transcribe one Fela bassline ("Water No Get Enemy" or "Gentleman") and note how few notes it uses and how syncopated the pickups are; then write your own two-bar ostinato with the same economy.
- Build the two-guitar interlock first, percussion second, and only add horns once the floor grooves without them — horn riffs written over a static floor always work; written first, they always need rescuing.
- Take a finished 32-bar groove and create the form only by muting lanes for stretches; resist the urge to write anything new for the transitions.
- Listen to Antibalas next to Fela's Africa '70 to hear the same architecture at Western track lengths — the proportions survive, the patience doesn't have to.

## Example

```
// ═══ no agreement with status — afrobeat, 108 bpm ═══
// form: perc 8 | groove 8 | full 8 | break 4 | horns talk 8 | full 8 | solo 8 | outro 4
// energy: 3       5         6        4       7            6        7       5
// a ten-minute Fela side folded into 56 bars — keep the proportions, stretch the repeats
setcpm(108 / 4) // one cycle = one 4/4 bar

// ── percussion floor: the bell carries the 12/8 feel flattened into 16ths ──
const bell = s("cb ~ ~ cb ~ ~ cb ~ cb ~ ~ cb ~ ~ cb ~").gain(.3) // 1, 1a, 2&, 3, 3a, 4& — the standard pattern
const shekere = s("sh*16").gain("[.16 .3 .1 .22 .16 .3 .1 .22 .16 .3 .1 .22 .16 .3 .1 .26]")
const congas = s("<[conga ~ lt conga ~ lt conga ~] [conga ~ lt conga ~ lt lt conga]>").gain(.4)
const pmeter = s("{conga ~ lt}%3").gain(.3) // 3-cycle polymeter for the deep-water section

const perc = arrange(
  [8, stack(bell.gain(.22), shekere.gain(.12))],                            // intro: skeleton only
  [8, stack(bell, shekere, congas)],
  [8, stack(bell, shekere, congas, s("rim ~ ~ ~ ~ ~ ~ ~").gain(.25))],       // full: one more click
  [4, stack(bell.gain(.15), shekere.gain(.1))],                             // the break: almost nobody home
  [8, stack(bell, shekere, congas)],
  [8, stack(bell, shekere, congas, pmeter, s("rim ~ ~ ~ ~ ~ ~ ~").gain(.25))], // drift + re-sync
  [8, stack(bell, shekere, congas)],
  [4, stack(bell.gain(.25), shekere.gain(.12))],
)

// ── bass: the lead instrument — a two-bar ostinato you could repeat for ten minutes ──
const bassA = note("<[a2 ~ a2 ~ ~ a2 c3 ~] [a2 ~ e2 g2 a2 ~ g2 e2]>")
const bassB = note("<[d2 ~ d2 ~ ~ d2 fs2 ~] [d2 ~ a1 c2 d2 ~ c2 a1]>") // same shape, moved to the IV9
const bass = arrange(
  [8, silence],
  [8, bassA],
  [8, bassA],
  [4, bassA.gain(.7)],                    // the break: bass is the melody now
  [8, cat(bassA, bassA, bassB, bassB)],   // horns talk section: i7 → IV9, four bars each
  [8, bassA],
  [8, bassA],
  [4, note("<[a2 ~ ~ ~ ~ ~ ~ ~] [~ ~ ~ ~ ~ ~ ~ ~]>")], // step off on the tonic
).sound("gm_electric_bass_finger").lpf(900).gain(.7)

// ── guitars: the interlocking pair — offbeat 16ths vs a high two-bar ostinato ──
const rGtr = note("a4").struct("~ x ~ x ~ x ~ x ~ x ~ x ~ x ~ x").sound("gm_electric_guitar_muted").gain(.28).cut(3).pan(.35)
const tGtrA = note("<[a4 c5 d5 c5 a4 c5 d5 g4] [a4 c5 d5 e5 d5 c5 a4 c5]>").sound("gm_electric_guitar_muted").gain(.32).cut(4).pan(.65)
const tGtrB = note("<[d4 fs4 a4 fs4 d4 fs4 a4 c4] [d4 fs4 a4 b4 a4 fs4 d4 fs4]>").sound("gm_electric_guitar_muted").gain(.32).cut(4).pan(.65)

const gtrs = arrange(
  [8, silence],
  [8, stack(rGtr, tGtrA)],
  [8, stack(rGtr, tGtrA)],
  [4, tGtrA.gain(.3)],                    // the break: one guitar, bass, skeleton bell
  [8, stack(rGtr, cat(tGtrA, tGtrA, tGtrB, tGtrB))],
  [8, stack(rGtr, tGtrA)],
  [8, stack(rGtr, tGtrA)],
  [4, rGtr],                              // outro: the chop outlasts everything
)

// ── keys: Am7 stabs answering the guitars, D9 when the bass goes there ──
const keys = arrange(
  [8, silence], [8, silence], [8, silence], [4, silence],
  [8, chord("<Am7 Am7 Am7 Am7 D9 D9 Am7 Am7>").anchor("a4").voicing().struct("x ~ ~ x ~ ~ ~ ~")],
  [8, chord("<Am7 Am7 Am7 Am7>").anchor("a4").voicing().struct("x ~ ~ x ~ ~ ~ ~")],
  [8, silence],
  [4, silence],
).sound("gm_percussive_organ").gain(.3).room(.3)

// ── horns: trumpet asks, tenor answers — riffs and stabs, never through-composed lines ──
const riffAsk = note("<[a4 ~ c5 d5 ~ e5 ~ d5] [c5 ~ a4 ~ g4 ~ a4 ~]>")
const riffAnswer = note("<[~ ~ ~ ~ ~ ~ ~ ~] [e5 ~ d5 ~ c5 ~ a4 ~]>")
const stab = note("<[[a4,c5,e5]@2 ~ ~ ~ ~ ~ ~ ~] [~ ~ ~ ~ ~ ~ ~ ~]>")
const hornsBook = arrange(
  [8, silence], [8, silence],
  [8, stack(riffAsk, riffAnswer)],
  [4, riffAnswer.gain(.5)],               // break: one last answer falls into the silence
  [8, cat(riffAsk, stab, riffAsk, riffAnswer)], // talk: riff, stab, riff, answer
  [8, stack(riffAsk, riffAnswer)],
  [8, silence],                           // the solo owns this section alone
  [4, silence],
)
const trumpet = hornsBook.sound("gm_trumpet").gain(.45).room(.35)
const tenor = hornsBook.transpose(-12).sound("gm_tenor_sax").gain(.36).room(.35).pan(.6)

// ── the solo: A minor pentatonic as degrees 0 3 5 7 10 of the A minor scale ──
const solo = arrange(
  [8, silence], [8, silence], [8, silence], [4, silence], [8, silence], [8, silence],
  [8, n("<[0 3 5 7] [5 7 10 7] [5 3 0 3] [~ 0 ~ ~]>").scale("A2:minor")],
  [4, silence],
).sound("gm_tenor_sax").gain(.42).room(.45)

$: perc
$: bass
$: gtrs
$: keys
$: trumpet
$: tenor
$: solo
```
