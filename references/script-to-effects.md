# Script-to-Effects Selection

The core task is not choosing the prettiest effect. It is choosing the smallest visual system that makes the spoken idea easier to understand and remember.

## 1. Parse the content

For each sentence or turn, extract only supported facts:

- topic and domain;
- speaker intent;
- emotional valence and urgency;
- concrete nouns, actions, numbers, dates, names, places, products, and relationships;
- rhetorical role: hook, setup, problem, cause, mechanism, example, proof, benefit, warning, conclusion, or CTA;
- exact visible words worth showing;
- what must remain voice-only.

Do not put every spoken word on screen. Prefer keywords, claims, numbers, names, process steps, or one short quotation unless the user explicitly requests full subtitles.

## 2. Inspect the image and reserve space

Determine:

- face and body bounding region;
- mouth, eyes, hands, props, microphones, and products that must remain unobstructed;
- gaze direction and likely gesture reach;
- existing screens, walls, desks, windows, signs, or empty regions that can host graphics;
- foreground, subject, midground, background, and screen-plane depth;
- background complexity and local contrast;
- whether the composition is symmetric, person-left, person-right, centered, or multi-person.

Placement defaults:

- person on left: primary panel on right;
- person on right: primary panel on left;
- centered close-up: use lower third, shoulder-side callout, top corner, or background plane, never the mouth and eyes;
- two speakers: use shared center panel only when both refer to it; otherwise anchor lower thirds or callouts near the owning speaker without covering hands or eyelines;
- existing display: attach content to that display's perspective and border;
- no safe negative space: reduce effect density before shrinking text.

## 3. Semantic mapping table

| Spoken meaning | Preferred primary visual | Supporting accent | Avoid |
| --- | --- | --- | --- |
| greeting / welcome | name or channel title, warm card, gentle phrase reveal | small wave/spark icon, soft border activation | explosion, aggressive glitch |
| identity / introduction | lower third, portrait label, role chip | line draw or restrained icon | large panel covering torso |
| question / hook | large short headline, question mark, focus ring | scale settle or blur-to-sharp | full transcript dump |
| definition | term card plus one-line explanation | underline, bracket, book/info icon | multiple competing cards |
| number / percentage | large numeral or counter | compact chart, unit label | invented values or fake precision |
| list | sequential chips, checklist, numbered stack | check/dot icons | revealing all rows at once |
| steps / process | stepper, timeline, flow diagram | arrow or progress line | disconnected icons |
| comparison | split card, two columns, before/after | versus marker, color coding | unrelated left/right meanings |
| cause and effect | two nodes with directional connector | ripple or line travel | decorative arrows with no source |
| benefit / success | concise benefit card | check, target, upward arrow | constant green pulsing |
| warning / risk | alert card with restrained red/amber | triangle or shield | large saturated-red flashing |
| proof / trust | quote, certification, source, metric | check/shield/document icon | unsupported badges |
| location / route | map, pin, route line | compass or distance tag | fabricated geography |
| time / history | date card or timeline | clock/calendar icon | rapid date cycling |
| technology / system | glass HUD, node graph, data card | scan line, chip/network icon | random sci-fi gibberish |
| finance / trend | chart, ticker, comparison tile | arrow, gauge, currency icon | misleading invented market data |
| education / explanation | diagram, label, highlighted term | pointer, bracket, draw-on icon | dense tiny text |
| emotion / personal story | restrained quote, soft color field | subtle line or slow light | busy data UI |
| CTA | one clear action card | button state or arrow | several calls to action at once |

## 4. Match style to context

Choose one dominant style:

- technology, AI, data, software: realistic technology or clean corporate;
- finance, news, policy: news/finance with disciplined data treatment;
- education, tutorial, science: education/knowledge with sequential diagrams;
- beauty, fashion, luxury: premium minimal;
- lifestyle, wellness, relationships: warm lifestyle;
- social creator or entertainment: social energetic, moderated by subject age and tone;
- testimony, interview, documentary: documentary/editorial;
- user-supplied brand system: follow it instead of defaults.

Infer palette from clothing, background, logo, product, and scene illumination. Avoid choosing an accent color that merges with skin, hair, clothing, or the background. If no brand is available, derive one main accent and a neutral support palette from the image.

## 5. Effect density

### Low

Use for interviews, testimony, premium brands, emotional monologues, legal/medical/financial seriousness, or busy images.

- one lower third or headline;
- occasional keyword or icon;
- minimal particles;
- long readable holds.

### Medium

Default for explainers, product introductions, education, and corporate social content.

- one primary visual per sentence or semantic beat;
- supporting icon or connector only when useful;
- periodic quiet beats;
- consistent cards and transitions.

### High

Use only for energetic creator content, short hooks, entertainment, rapid product features, or explicit user requests.

- short word groups, counters, stickers, or fast cards;
- still one new information group at a time;
- shorter holds but no unreadable text;
- fewer background particles than foreground information elements.

If duration is short, resolution is low, the speaker moves broadly, or exact Chinese text is long, reduce density by one level.

## 6. Build the event map

For each effect write an internal planning row:

```text
speaker | exact trigger phrase | purpose | visible copy/data | effect family | anchor/layer | entrance | landing | hold | exit/recovery | linked gaze/gesture | risk
```

`exit/recovery` is mandatory for every dynamic graphic. Record the exact semantic endpoint, exit motion, destination, and resulting clean state. If an element must continue, mark it as an intentional persistent member of the same information group and define the later event that removes or transforms it. Never leave the field implicit and never substitute “dim” or “stable” for a real exit.

Example:

```text
S1 | “三个关键步骤” | process setup | “01 识别 / 02 判断 / 03 执行” | stepper | right-side glass panel | border draw then rows reveal sequentially | active row lands on each spoken step | completed rows remain dim and stable | panel settles after step 3 | one brief open-palm cue | text length and hand overlap
```

Do not expose this table unless the user asks for a storyboard or effect plan. Compile it into the final H3 description.

## 7. Single-person choreography

- Maintain lens engagement while overlays appear in peripheral space.
- Use at most one motivated glance toward a major panel per short beat.
- A pointing gesture begins before the referenced visual emphasis, peaks with the keyword, then returns to rest.
- If the effect appears behind or beside the speaker, keep its light response subtle and physically consistent.
- Avoid making the speaker react to purely audience-facing subtitles.

## 8. Multi-person choreography

- Keep speaker ownership obvious through mouth state, gaze, lower third, or active color.
- Use one shared graphic when both people discuss the same object; otherwise localize visuals near the active speaker.
- During turn handoff, dim or settle the previous speaker's graphic before revealing the next.
- Preserve clear eyelines and face separation.
- Do not animate identical captions or icons beside both speakers unless the content explicitly compares them.

## 9. Text selection

Priority for on-screen copy:

1. exact names, titles, dates, numbers, units, and product terms;
2. central claim or keyword;
3. steps, comparison labels, and CTA;
4. supporting explanation;
5. full subtitles only when requested.

If copy is long, split at semantic boundaries into stable lines or successive cards. Do not compress until it becomes tiny. Preserve the exact wording across every appearance.

## 10. Reference media

When a reference video is supplied, extract reusable grammar rather than blindly copying:

- effect categories and density;
- spatial anchors and safe areas;
- motion direction, easing, and overlap;
- text hierarchy and line grouping;
- icon behavior and material style;
- trigger timing relative to speech;
- how effects enter, hold, and clear;
- what remains still.

Do not claim to have inspected a video if it could not be decoded or viewed. Use verified technical metadata and user-described visual traits only.
