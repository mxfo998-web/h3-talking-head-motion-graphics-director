# Generated Voice Direction Without Audio References

Use this reference whenever H3 must generate a visible speaker's voice without runtime driving audio or a voice reference. Do not leave the voice as merely “natural,” “friendly,” “male,” or “female.” Build one coherent voice card and make it agree with the face, body, role, performance, microphone perspective, and room.

## 1. Determine voice presentation responsibly

Use evidence in this order:

1. explicit user instruction;
2. explicit subject wording in the first-frame prompt or character description, such as `成年女性`, `成年男性`, `female presenter`, or `male analyst`;
3. an established character identity from prior approved context;
4. apparent adult vocal presentation consistent with the visible character design, stated as a creative casting choice rather than a factual claim about gender identity.

When an uploaded image alone is ambiguous and choosing male, female, or neutral vocal presentation materially changes the result, ask the user. Do not infer gender identity as fact from facial appearance. If the user has already defined an adult woman or man in the image prompt, use an adult female or male voice respectively without asking again.

Keep one stable voice owner per `(Sx)`. In multi-person work, give each speaker a distinct but non-caricatured voice card.

## 2. Build a complete voice card

Specify only dimensions that improve generation:

- **voice presentation and apparent vocal age:** adult female, adult male, or neutral/androgynous presentation; useful age band rather than an exact biological claim;
- **pitch region and range:** low, low-mid, mid, mid-high, with restrained or expressive range appropriate to the role;
- **resonance and weight:** chest, oral, head, or balanced resonance; light, medium, or grounded vocal weight;
- **texture:** clean, warm, bright, soft, dry, lightly breathy, lightly textured, or gently raspy; avoid contradictory stacks;
- **articulation:** consonant clarity, natural coarticulation, sibilant control, plosive behavior, and vowel openness;
- **pace and phrasing:** target written characters per second, phrase grouping, pause length, stress placement, and whether the pace breathes or stays compact;
- **intonation:** pitch range, question/statement contours, sentence-final fall or partial release, and variation across phrases;
- **emotional stance:** friendly, reassuring, analytical, curious, grounded, urgent, or intimate, with one primary stance and one secondary nuance;
- **capture perspective:** lavalier, desk microphone, boom, phone, or environmental microphone; distance, proximity effect, room reflections, and background bleed;
- **anti-style:** the most likely synthetic failure, such as broadcast announcer voice, sales pitch, customer-service sweetness, trailer voice, monotone TTS, exaggerated breathiness, or metallic reverb.

Do not assign pitch from gender alone. Age, body, role, emotion, health, setting, microphone, and user preference also affect the creative choice. Avoid stereotypes such as making every woman high and sweet or every man low and authoritative.

## 3. Make the voice sound lived-in

Natural speech is organized in phrases, not emitted at perfectly uniform speed.

- Maintain the requested average near 5 written characters per second, while allowing small local accelerations and decelerations around meaning.
- Count punctuation for the user's written-length convention, but render it as phrase grouping, a short pause, breath, or intonational boundary rather than a spoken sound.
- Prepare long phrases with a light inhale. Let demanding clauses resolve with a subtle exhale, swallow, lip reset, or reduced vocal energy.
- Place emphasis through a coordinated change in duration, pitch contour, loudness, and articulation; do not simply make every keyword louder.
- Preserve natural coarticulation and small pitch/energy variation. Avoid identical syllable duration, equal stress on every phrase, fixed sentence-final melody, over-separated characters, or perfectly clean breathless audio.
- Keep breaths quiet and physically synchronized with visible chest, shoulder, jaw, and mouth behavior. Do not add decorative gasps.
- Use slight human imperfection only where plausible: a soft onset, minute breath texture, restrained mouth noise, or tiny timing variation. Never add distracting clicks, excessive saliva noise, or unstable voice identity.

## 4. Match role and environment

### Technology / product studio

- usually close lavalier or controlled boom perspective;
- clear, modern, conversational voice with curious-to-confident phrasing;
- slightly bright or balanced tone, restrained room reflection;
- avoid synthetic futurist vocoder tone, keynote shouting, and customer-service cadence.

### Finance / research office

- close lavalier or desk-microphone perspective with soft room tone;
- grounded low-mid or mid voice, disciplined dynamics, deliberate stress, concise pauses;
- friendly credibility rather than cold authority;
- avoid television-news cadence, trading-floor shouting, and ominous trailer bass.

### Medical / consultation room

- clean close speech with soft room ambience and minimal hard reflection;
- calm, warm, intelligible delivery with empathy and steady breath;
- risk language is measured, not cheerful; reassurance arrives only after explanation;
- avoid sterile robotic flatness, advertising warmth, and whispered intimacy.

### Property / showroom

- conversational near-field voice with mild natural room reflection;
- open, warm, confident phrasing and a small smile only where semantically earned;
- avoid repetitive sales intonation, exaggerated enthusiasm, and pressure-selling cadence.

### Industrial / control room

- protected lavalier or close boom perspective with low control-room hum and limited equipment bleed;
- grounded, clear, physically supported delivery with moderate vocal weight;
- friendly competence rather than command shouting;
- avoid metallic filtering, radio distortion, alarm masking, and military cadence.

## 5. Couple voice, body, and mouth

- The visible speaker owns exactly one voice. No off-screen duplicate repeats the line.
- Mouth shapes follow phonemes; breath preparation, vocal effort, loudness, and phrase release match the chest, jaw, cheeks, and posture.
- A warmer or more reassuring phrase may soften the eyes and release brow tension; an analytical warning may narrow emphasis and reduce smile. Do not animate emotion independently from the voice.
- Microphone distance and head turns affect acoustic perspective only slightly in a fixed talking-head setup. Avoid sudden dry/wet changes, volume pumping, or timbre swaps.
- Environmental noise remains below dialogue and shares the same room. Do not generate studio-isolated narration for a visibly reverberant or industrial space unless a concealed lavalier is specified.

## 6. Prompt pattern

```text
声音设计：无音频参考，由H3原生生成(S1)的[成年女声/成年男声/中性声线]；听感约[age band]，[pitch region]，[resonance]，[weight/texture]。普通话清晰自然，[articulation details]；平均语速约5个书面字符/秒，本段共[COUNT]字符，允许按语义轻微快慢变化。[pause grouping, emphasis, and sentence-final contour]. 整体[primary emotional stance]并带[secondary nuance]，像真实的[role]面对镜头交流；禁止[announcer/sales/customer-service/monotone TTS failure]. 使用[visible/hidden microphone type]的近场收音，距离约[distance]，保留[room tone/reflection]，环境声低于人声且不改变声音身份。
```

Put the stable voice identity and delivery profile in `integrated_multimodal_description`. Restate capture perspective, ambience, and ownership in `overall_soundscape` without creating an audio reference label.

## 7. Audit

Verify:

- voice presentation follows explicit user or character information; ambiguity was not silently converted into a factual gender claim;
- apparent vocal age, pitch, resonance, texture, articulation, pace, cadence, intonation, and emotional stance form one coherent person;
- the voice fits the role without relying on gender stereotypes;
- average rate and reported character count match the planned duration;
- pauses, breaths, emphasis, and sentence-final contour align with visible performance;
- microphone type, distance, room reflection, ambience, and noise floor match the visible environment;
- no broadcast, sales, customer-service, trailer, vocoder, monotone TTS, or metallic-reverb failure appears unless explicitly requested;
- voice identity, volume, acoustic perspective, and speaker ownership remain stable throughout.

## 8. Primary-source basis

- MiniMax H3 official repository: native synchronized 32 kHz stereo audio, Chinese dialogue support, Base and Ref2VA workflows, and examples that jointly describe voice timbre, visible speaking, room tone, physical sounds, and soundtrack layers: https://github.com/MiniMax-AI/MiniMax-H3
- W3C Speech Synthesis Markup Language 1.1: voice selection, emphasis, breaks, pitch, speaking rate, volume, and prosodic contour as core speech controls: https://www.w3.org/TR/speech-synthesis11/
- Microsoft Speech SSML overview: voice, language, role, style, pronunciation, speaking rate, pitch, volume, sentence structure, and pauses as practical synthesis controls: https://learn.microsoft.com/azure/ai-services/speech-service/speech-synthesis-markup

These sources provide design vocabulary and capability evidence. Do not claim that H3 directly supports SSML tags; compile the concepts into natural-language H3 direction.
