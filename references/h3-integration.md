# H3 Integration for Talking-Head VFX

Use this as the structural source of truth for H3 prompts produced by this skill.

## 1. Route selection

Choose exactly one route from non-runtime assets:

| Route | Use when | Required alignment |
| --- | --- | --- |
| T2VA | Text only | Describe ratio, composition, speaker, scene, and effects |
| I2VA | One image is the literal first frame | State that Shot 1 begins exactly from the input image |
| FL2VA | Images are literal first and last frames | State both alignments and a continuous bridge |
| L2VA | One image is the literal final frame | Make the performance converge naturally to it |
| Ref2VA | Image/video/audio assets supply reusable identity, scene, style, motion, voice, or sound | Define and track every reference label |

Do not mix Base-mode fields with the Ref2VA schema.

## 2. Exact output shapes

Base modes use these fields in this order:

```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

Ref2VA uses:

```text
subject_definitions:
...

summary:
[task type] ...

retention_analysis:
...

detailed_description:
...

overall_soundscape:
...

non_diegetic_music:
...
```

Ref2VA task types are `keyframe completion`, `reference generation`, `video editing`, `video continuation`, `audio reuse`, and `audio reference`. Use only the types actually supported by the assets.

Visual retention markers are `fully_preserved`, `partially_preserved`, `attribute_transfer`, and `weak_reference`. Audio markers are `fully_copy`, `partially_copy`, `reference`, and `weak_reference`.

## 3. Audio-mode gate

Before route selection, classify the audio role as exactly one of these modes:

| Mode | What the audio does | Prompt consequence |
| --- | --- | --- |
| Runtime audio-driven / 音频驱动 | The platform supplies the final speech waveform and authoritative timing outside the prompt | Do not create `<Audio N>` or any audio task/retention entry; choose the official route from non-audio assets; mention the intended average pace when exact dialogue is supplied |
| Reference timbre / 参考音色 | An uploaded recording guides the timbre, speaking rate, cadence, pause grouping, and delivery of newly generated dialogue | Use Ref2VA; define `<Audio 1>`; add `audio reference`; use the `reference` retention marker |
| No audio reference / 无音频参考 | H3 generates the supplied dialogue without an external driver or voice sample | Choose the route from visual assets; do not invent `<Audio N>`; define adult female/male/neutral voice presentation from explicit character information, then specify vocal age, pitch, resonance, texture, prosody, microphone perspective, and room acoustics near the default 5 written characters per second |

Infer a mode only from explicit wording. An attached audio file by itself is ambiguous. When the user has not stated the role, ask:

```text
这次使用哪种音频方式：① 音频驱动（不引用“音频1”）；② 参考音色（把“音频1”作为音色、语速与表达参考）；③ 无音频参考（根据场景原生生成口播，默认约5字/秒）？
```

Do not generate the final H3 prompt until this material choice is resolved.

### Reference-timbre mode

Use this mode when the user says to reference the timbre, voice quality, cadence, accent, vocal age, or delivery of the supplied recording while speaking new user-supplied dialogue.

- use Ref2VA even when the only reference asset is the voice sample;
- define the binding precisely: `<Audio 1> is the voice-timbre, speaking-rate, cadence, pause-grouping, and delivery reference for <Subject 1> (S1).`;
- include `audio reference` in `summary`;
- write `<Audio 1>: reference` in `retention_analysis` and state that only voice identity and delivery guide generation;
- put the new exact script inside `<d>[Language] ...</d>`;
- do not copy the reference waveform or its spoken words;
- do not claim exact cloning or guaranteed voice identity;
- keep one stable `<Audio N>`-to-speaker binding throughout multi-shot or multi-speaker work.

Minimal binding pattern:

```text
subject_definitions:
<Subject 1> (S1) is the visible speaker.
<Audio 1> is the voice-timbre and delivery reference for <Subject 1> (S1).

summary:
[reference generation + audio reference] Generate a talking-head video in which <Subject 1> delivers the supplied script while motion graphics clarify its semantic beats.

retention_analysis:
<Subject 1>: fully_preserved - Preserve the supplied visual identity and wardrobe when a visual reference is present.
<Audio 1>: reference - Its vocal timbre, pitch region, cadence, accent, vocal age, texture, and delivery guide newly generated dialogue; do not copy its waveform or source words.
```

## 4. Runtime audio-driven overlay

If the platform supplies the driving speech outside the prompt:

- do not create `<Audio N>`;
- do not add `audio reuse` or `audio reference`;
- do not add an audio retention row;
- call it `平台运行时驱动音频`, `输入驱动语音`, or `驱动语音` only when synchronization must be stated;
- choose the H3 route from the remaining visual assets;
- do not invent a transcript when none is supplied;
- when preparing or describing the supplied driver, target an average near 5 written characters per second including punctuation unless the user specifies otherwise; once supplied, treat its actual timing as authoritative for phonemes, breaths, pauses, emphasis, laughter, interruptions, and effect triggers;
- do not request a duplicate voice, dialogue, narration, or sound layer.

Recommended Base-mode sound fields:

```text
overall_soundscape: 平台运行时驱动音频提供最终口播时间线；所有可见口型、呼吸、停顿、表情、手势和画面特效与其同步。不生成重复人声或冲突音层。

non_diegetic_music: N/A
```

If the driver already contains music or ambience, it remains part of that input signal. Do not request regeneration unless the user explicitly describes a separate product behavior.

## 5. Speech-rate and written-length budget

- Default Mandarin talking-head planning to about 5 written characters per second. Count punctuation, exclude whitespace and H3 tags, and count Latin letters and digits individually.
- Report the exact counted dialogue length with the prompt. A 15-second clip targets about 75 characters; approximately 72–80 is a practical default band when articulation remains natural.
- In reference-timbre mode, `<Audio 1>` guides speaking rate, cadence, pause grouping, stress, and delivery as well as timbre. If reference pace, text length, and duration conflict, revise the copy or duration rather than compressing speech unnaturally.
- In runtime audio-driven mode, mention the intended average pace, but let the supplied waveform control actual mouth, breath, pauses, gesture, and effect timing.
- In no-audio-reference mode, infer voice energy and phrasing from the scene and script while keeping the average near the benchmark.
- Punctuation counts toward the written budget but becomes phrase grouping or a natural pause, not a spoken phoneme.
- If speech fills nearly the entire duration, begin final graphic cleanup during the closing clause and complete it by the final punctuation.

## 6. Generated voice without an audio reference

When H3 creates the voice natively, define a stable voice identity and acoustic world rather than writing only “自然亲切的声音.”

- Follow explicit character wording first. `成年女性` maps to an adult female voice; `成年男性` maps to an adult male voice. If a standalone image is ambiguous, ask or describe an apparent vocal presentation as a casting choice rather than claiming gender identity.
- Specify apparent vocal age band, pitch region and usable range, resonance, vocal weight, restrained texture, consonant/vowel articulation, average pace, cadence, pause grouping, stress, pitch contour, sentence-final behavior, and emotional stance.
- Keep the voice friendly, real, and role-appropriate without stereotypes. Do not make every female voice high and sweet or every male voice low and commanding.
- Preserve natural phrase-level speed variation around the 5-character-per-second average, coordinated breath, small pitch/energy variation, coarticulation, and imperfect but clean human onset/release. Avoid equal syllable duration and fixed TTS melody.
- Name microphone perspective, distance, proximity, room reflection, ambience, and environmental bleed. The voice and room tone share one space; dialogue remains dominant and intelligible.
- State one likely anti-style: no broadcast announcer, sales pitch, customer-service sweetness, trailer voice, monotone TTS, vocoder color, excessive breathiness, or metallic reverb.
- Put the voice card in the active shot and restate capture perspective and ambience in `overall_soundscape`. Do not add `<Audio N>`.

Read [generated-voice-direction.md](generated-voice-direction.md) for domain profiles, prompt pattern, and audit.

## 7. Dialogue and visible copy

- Put exact supplied speech inside `<d>[Language] ...</d>`.
- Put exact on-screen text in double quotation marks outside `<d>`.
- Preserve wording, punctuation, numbers, capitalization, line breaks, and language.
- If a displayed phrase duplicates spoken words, define the displayed copy separately and state how it reveals in relation to the spoken phrase.
- Prefer phrase blocks or complete words. Character-by-character morphing increases spelling instability and should be used only when the user explicitly wants it.
- Keep displayed copy attached to one stable layer or surface. State position, alignment, scale, font class, weight, color, background treatment, entry, hold, and exit.
- Do not silently shorten user-supplied copy. If it cannot be read within the duration, report the conflict or reduce the number of simultaneous elements.

## 8. Human performance

Every meaningful beat follows `attention target → internal intent → visible response → recovery`. Start from a neutral living baseline instead of adding generic constant movement.

For direct-to-camera speech:

- maintain lens-first gaze with brief motivated departures; name the target and return target, and let the eyes lead modest head movement;
- place isolated blinks near breaths, gaze shifts, phrase boundaries, cognitive release, or environmental causes; never set a metronomic blink rate;
- build expressions through eyes, lids, brow, cheeks, lip corners, jaw, nostrils, swallow, and breath as `onset → peak → partial release`, with restrained asymmetry where useful;
- synchronize consonant closures, rounded vowels, brief lip seals, tongue/cheek support, jaw amplitude, pauses, inhalation, exhalation, and swallowing to the actual speech; lips relax during silence;
- maintain subtle continuous breathing and believable seated or standing support, center of gravity, forearm pressure, shoulder balance, and post-gesture inertia;
- give both hands asymmetric resting states; gestures use `prepare → semantic peak → settle → rest`, respect furniture and props, and preserve fingers, grip, contact, and hand dominance;
- let emphasis drive one primary response, not a simultaneous nod, blink, brow lift, hand wave, and torso lean;
- keep face, skin texture, teeth, tongue, eye highlights, hair, clothing, hands, and props continuous without waxy skin, tooth flicker, drifting lips, or joint deformation.

Only world-space, surface-attached, or plausibly perceptible subject-linked graphics can motivate a gaze or pointing response. The speaker does not look at audience-only screen-space overlays. Effects never replace speaking behavior: a perfectly animated card beside a frozen or mechanically nodding person still fails.

## 9. Multiple speakers

- Assign `(S1)`, `(S2)`, and so on by first vocal event.
- State the active speaker for every turn.
- A silent listener keeps relaxed closed lips, tracks the speaker or referenced visual, and uses only a restrained backchannel.
- Place nameplates, captions, or callouts so ownership is obvious.
- During a handoff, allow a cue such as eye contact, inhale, posture lift, or card emphasis before the next voice starts.
- Avoid identical gestures, synchronized blinking, simultaneous mouth movement, or two equally dominant overlays.

## 10. Shots and timing

- `[Shot 1]` has no timestamp.
- Later cuts use `[Shot N] At MM:SS.mmm, ...`.
- A continuous one-shot video uses only `[Shot 1]`.
- If the user requests a fixed camera, lock position, focal length, horizon, framing, and exposure while performance and overlays develop within the shot.
- Effects may have internal relative timing tied to speech without adding unnecessary absolute timestamps.

## 11. Sound layer ownership

Keep dialogue and synchronized vocal events in the active shot. In no-audio-reference mode, the active shot also owns the stable generated voice card; `overall_soundscape` restates speaker ownership, microphone perspective, room reflections, ambience, and noise floor. Use `overall_soundscape` for continuous diegetic ambience and physical sounds. Use `non_diegetic_music` only for audience-only score, otherwise `N/A`.

Visual UI effects are silent by default in runtime audio-driven work. Add clicks, sweeps, impacts, notification tones, or whooshes only when the user requests them and the audio workflow can support an additional layer without duplication.

## 12. H3 continuity priorities

When complexity must be reduced, preserve in this order:

1. speaker identity, face, mouth, eyes, and vocal ownership;
2. exact visible text and primary effect;
3. hands, products, microphones, and physical contacts;
4. composition, safe areas, exposure, and background stability;
5. secondary icons and supporting accents;
6. particles, decorative light, and ambient motion.

The prompt must never sacrifice face or mouth stability to keep decorative effects.
