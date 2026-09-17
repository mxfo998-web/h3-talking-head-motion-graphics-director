# Prompt Patterns

These are structural patterns, not wording templates to copy blindly. Replace bracketed content with observed facts and the selected effect system.

## Single-person I2VA with runtime speech

```text
integrated_multimodal_description:
[Shot 1] 视频从输入图片完全一致的首帧开始。[Preserve adult speaker identity, face, hair, wardrobe, body proportions, hands, props, scene, composition, lighting, and visible text.] [Camera behavior.]

[Speaker] uses lens-first attention and delivers the supplied line: <d>[Language] exact dialogue</d>. State `目标平均口播语速约5个书面字符/秒；本段共[COUNT]字符，统计含标点、不含空格和H3标签；实际动作以平台运行时驱动语音为最终时间轴。` For every semantic beat, write `attention target → internal intent → visible response → recovery`; bind phoneme-level mouth motion, breath, contextual blink, expression onset/peak/release, posture, one motivated gesture, and return to rest to the actual phrase. State explicitly whether the speaker can perceive each graphic; never direct gaze toward an audience-only screen-space overlay.

At the phrase “exact trigger,” [exact visible copy] appears at [anchor] as [effect family]. It follows `preparation → reveal → landing on trigger → readable hold → settle/exit`. [Describe font class, weight, alignment, color, contrast backing, icon, panel material, light response, occlusion, and stability.] [Continue only for meaningful later beats.]

[Lock identity, text spelling, panel geometry, effect anchors, background, exposure, white balance, light sources, and shadows. State anti-flicker and no-occlusion constraints.]

overall_soundscape:
平台运行时驱动音频提供最终口播时间线；口型、呼吸、停顿、表演和画面特效与其同步。不生成重复人声或冲突音层。[Only add explicitly requested compatible sound layers.]

non_diegetic_music:
N/A
```

If no transcript is supplied, remove the `<d>` line and state that no words are invented. Use audible phrase boundaries without naming unknown words.

## Single-person I2VA with generated speech and no audio reference

```text
integrated_multimodal_description:
[Shot 1] 视频从输入图片完全一致的首帧开始。[Preserve identity, wardrobe, scene, composition, lighting, and visible text.] [Camera behavior.]

(S1)面向[attention target]并说：<d>[Language] exact dialogue</d>。

声音设计：无音频参考，由H3原生生成(S1)的[成年女声/成年男声/中性声线]；听感约[age band]，[pitch region]，[resonance]，[weight/texture]。普通话清晰自然，[articulation details]；目标平均口播语速约5个书面字符/秒，本段共[COUNT]字符，统计含标点、不含空格和H3标签，允许按语义轻微快慢变化。[pause grouping, emphasis, pitch contour, and sentence-final release]. 整体[primary stance]并带[secondary nuance]，像真实的[role]面对镜头交流；禁止[announcer/sales/customer-service/monotone TTS failure]. 使用[microphone type]近场收音，距离约[distance]，保留[room tone/reflection]，环境声低于人声且不改变声音身份。

口型、呼吸、眨眼、眼神、表情、姿态和手势与这条原生人声逐句同步并完成恢复。

[Effect event map, exact copy, coordinate spaces, lifecycle, and stability. If dialogue fills the clip, begin final cleanup during the closing clause and finish by the final punctuation.]

overall_soundscape:
由H3原生生成并仅由(S1)拥有的场景内口播；保持上述成年女声/成年男声/中性声线、年龄感、音高、共鸣、质感、语速、节奏、停顿、重音和句尾走势全程稳定。采用上述麦克风距离与空间混响，保留符合画面的克制环境底噪；人声始终清楚并高于环境，不生成第二条人声、画外复述或声音身份漂移。

non_diegetic_music:
N/A
```

## Multiple-person I2VA with runtime speech

Use when one literal first frame contains all speakers.

```text
integrated_multimodal_description:
[Shot 1] 视频从输入图片完全一致的首帧开始。[Preserve each adult identity, wardrobe, body position, eyeline, props, scene, composition, and lighting.] [Camera behavior.]

(S1) owns the first audible turn and (S2) owns the second. When (S1) speaks, (S2) keeps relaxed closed lips, tracks (S1), and gives one restrained backchannel. Before the handoff, (S2) prepares with [gaze/inhale/posture cue]; when (S2) begins, (S1) becomes the silent listener. Mouth motion never transfers between speakers.

For (S1)'s phrase “trigger,” [S1-owned visual] appears at [anchor] without covering either face or the shared eyeline. It settles before (S2)'s turn. For (S2)'s phrase “trigger,” [S2-owned visual] appears with the same design system but a distinct active-state cue. [Shared visual] is used only for shared content.

[Exact visible text, hierarchy, reveal timing, stable anchors, safe zones, lighting, and temporal consistency.]

overall_soundscape:
平台运行时驱动音频提供最终多人口播时间线；每段语音只驱动对应说话者，其他人物保持安静但有自然反应。所有特效按当前说话者和语义触发，不生成重复对白或冲突音层。

non_diegetic_music:
N/A
```

## Ref2VA with reusable visual references and runtime speech

The runtime driver still receives no audio label.

```text
subject_definitions:
<Subject 1> (S1) is [adult speaker identity from visual reference].
<Subject 2> is [reusable environment, product, panel, effect style, or second speaker].
<Picture 1> is [precise visual role when it is a concrete keyframe/composition anchor].
<Video 1> is [motion/effect/camera role when supplied].

summary:
[visual task types only] ...

retention_analysis:
<Subject 1>: [visual marker]
<Subject 2>: [visual marker]
<Picture 1>: [visual marker]
<Video 1>: [visual marker]

detailed_description:
[Shot 1] [Speaker performance, runtime speech synchronization, exact dialogue when supplied, effect event map, camera, layering, stability, and sound ownership.]

overall_soundscape:
平台运行时驱动音频提供最终口播时间线；所有可见发声、人物反应和语义特效与其同步。不生成重复人声或冲突音层。

non_diegetic_music:
N/A
```

Do not include empty subject, picture, video, or retention rows.

## Speech-rate clause by audio mode

```text
音频驱动：目标平均口播语速约5个书面字符/秒；本段共[COUNT]字符，统计含标点、不含空格和H3标签。平台运行时驱动语音以此基准准备，实际口型、呼吸、停顿、表演和特效仍以输入波形为最终时间轴。

参考音色：<Audio 1>同时作为音色、平均语速、节奏、停顿分组、重音和表达参考；新台词共[COUNT]字符，目标时长[DURATION]秒。尽量复现参考录音的口播速度与停顿逻辑；若参考速度与文本时长冲突，先调整文案或时长，不做不自然压缩。

无音频参考：根据人物身份、场景和文案原生生成口播；平均语速约5个书面字符/秒，本段共[COUNT]字符，统计含标点、不含空格和H3标签。保持自然短停顿、清楚辅音和句末完整收束。
```

## Generated-voice card clause

```text
声音设计：无音频参考，由H3原生生成(S1)的[成年女声/成年男声/中性声线]；听感约[age band]，[pitch region and range]，[resonance]，[weight and restrained texture]。普通话清晰自然，[articulation]；平均语速约5个书面字符/秒，本段共[COUNT]字符，允许按语义产生细微快慢变化；[pause grouping]，[stress and intonation]，[sentence-final release]。整体[primary emotional stance]并带[secondary nuance]，像真实的[role]与观众交流；禁止[likely synthetic or genre failure]. 使用[microphone type]近场收音，距离约[distance]，保留[room tone and reflection]；环境声低于人声，声音身份、响度和声学距离全程稳定。
```

## Effect event sentence pattern

```text
当(S1)说到“[exact trigger]”之前的一小段准备时间，[anchor]处的[container/icon/line]以[entrance and easing]开始出现；在“[payoff word]”的语义重音处完整落定并显示“[exact visible copy]”。[supporting accent]只执行[one motivated action]，文字保持清晰稳定至[exact semantic endpoint]；随后整个信息组以[explicit exit motion]进入[exit destination or zero-opacity state]并完全消失，恢复[clean frame state]后，下一组信息才开始出现。
```

## Human-realism clause

```text
真人表演始终优先于动态图形。人物以镜头为主要注意目标，保留自然微眼跳和细微重新聚焦；只有世界空间、场景附着或人物可感知的图形才能引发短暂注视，眼睛先于头部轻微转动，确认信息后回看镜头。眨眼为非周期性的自然单次眨眼，只落在换气、短暂停顿、视线转移、认知释放或环境刺激附近。

口型按真实音素变化：辅音闭合、圆唇元音、短暂闭唇和下颌开合幅度与语音重音一致；停声时嘴唇停止发音运动并回到自然状态。长句前有轻微吸气，句末允许细微呼气、吞咽、嘴唇复位或姿态释放。胸廓、肩部和衣料保留符合景别的细微连续呼吸。

表情遵循“出现—峰值—部分释放”，保持适度不对称；手势遵循“准备—语义峰值—回落—休息”，双手具有自然且不完全对称的休息姿态。动作尊重桌面、麦克风、产品和画幅边界，不连续点头、不机械眨眼、不持续微笑、不重复挥手，不让点头、眨眼、抬眉、手势和身体前倾同时机械触发。面部、皮肤纹理、眼球高光、牙齿、舌头、发丝、衣褶、手指、关节、握持和道具接触全程连续稳定。
```

Use this as a baseline, then replace generic phrasing with phrase-specific attention, intent, response, and recovery whenever exact dialogue is available.

## Paired entrance and exit clause

```text
每一个动态图形都必须在片内完成“进入—落定—可读停留—退出—恢复”的完整生命周期。凡是通过淡入、上升、展开、绘制、缩放或组装进入的元素，都必须写明对应的淡出、下降、折叠、反向擦除、缩回源点、溶解或变形替换。降低亮度、退为次要层或保持稳定不等于退出。上一组独立图形完全消失，或明确变形成同一容器的下一状态后，下一组才可出现；禁止历史标题、卡片、图标、连线和粒子持续累积。最后一个动态图需要在最后一句说完后预留清场时间，并在视频结束前恢复干净画面。
```

## Text stabilization clause

```text
所有可见文字使用准确、完整、稳定的[language]，保持字形、字序、标点、数字、单位、行距和对齐不变；文字附着在同一屏幕平面或容器中，不漂移、不重写、不乱码、不随机换字体。采用完整词组或整行显现，不使用高速逐字变形。
```

## VFX stability clause

```text
特效严格限制在指定区域和景深层，具有明确源点、运动路径、衰减和停止状态；不遮挡人物眼睛、嘴唇、手部、麦克风或产品。人物身份、面部、文字、图标、面板、背景、曝光、白平衡、光源和阴影全程连续稳定，不出现漂移光球、随机镜头炫光、全局亮度脉动、彩色闪烁或无原因粒子。
```

## Fixed-camera clause

```text
固定机位、固定焦距、固定水平线、固定构图和固定曝光；全程不推镜、不拉镜、不摇镜、不平移、不变焦、不切镜。人物在画面内部自然表演，屏幕空间特效保持像素稳定，世界空间特效保持正确透视和遮挡。
```
