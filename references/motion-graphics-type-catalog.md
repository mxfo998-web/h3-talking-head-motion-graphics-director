# Common Talking-Head Motion-Graphics Types

Use this catalog to classify, combine, and prompt common motion-graphics systems for talking-head and digital-human video. It is a production vocabulary, not a requirement to use every type.

## 1. Use a four-axis taxonomy

Do not place every label in one flat list. Describe a design with four independent axes:

1. **Information format** — what communicates: floating typography, lower third, callout, card, infographic, chart, icon, or particle network.
2. **Motion behavior** — how it changes: fade, wipe, draw, rise, scale, count, fill, trace, replace, pulse, or path travel.
3. **Spatial behavior** — where it exists: screen-space, camera-space, subject-tracked, surface-attached, billboarded, tag-along, or world-space.
4. **Visual style** — how it looks: editorial, corporate, glass, HUD, FUI, holographic, educational, social, warm, or another coherent system.

Examples:

- `lower third + phrase-block wipe + screen-space + documentary/editorial`;
- `tracked callout + line draw + product anchor + clean corporate`;
- `floating UI card + unfold + world-space billboard + holographic FUI`;
- `animated infographic + sequential path trace + surface-attached + education/knowledge`.

## 2. Minimum prompt grammar

For every primary motion-graphics event, define:

```text
type | semantic purpose | exact trigger | exact copy or supplied data | speaker owner |
coordinate space | anchor | plane/orientation | depth | occlusion |
container/material | typography/icon family | entrance | landing |
readable hold | emphasis | settle/exit | tracking behavior |
light response | stability constraints | complexity fallback
```

Compile it into prose rather than exposing the planning row. A useful sentence shape is:

```text
当(S1)说到“[exact trigger]”之前，[coordinate space]中以[anchor]为锚点的[type]开始[entrance]；
在“[payoff word]”的重音处完整落定并显示“[exact copy]”。
它保持[orientation/depth/occlusion]，清晰停留至[semantic end]，然后[settle/exit]，恢复干净画面。
```

## 3. Floating Typography — 悬浮文字

### Definition

Containerless or lightly contained words and short phrases positioned beside the speaker or in negative space. “Floating” describes placement, not a specific glow, 3D effect, or motion. It can be screen-space, camera-space, or world-space.

### Best use

- short hooks, keywords, chapter titles, claims, questions, and conclusions;
- one to three concise phrase blocks that support speech without becoming full subtitles.

### Motion model

- prepare with a subtle line, focus shift, or local contrast field;
- reveal the complete phrase by fade-and-rise, mask wipe, scale settle, or shallow depth emergence;
- land on the stressed word, hold crisp, then dim or leave through the reverse spatial path;
- keep the final phrase stable; do not let it continuously bob or drift.

### Prompt module

```text
当(S1)说到“[trigger]”时，人物[left/right]侧负空间的屏幕平面出现悬浮词组“[copy]”。
完整词组从下方短距离淡入上移，以减速缓动在重音处落定；
最终字形清晰、位置固定，不遮挡人脸和手势，语义结束后降低亮度并停止运动。
```

### Avoid

- treating every spoken word as an independent floating object;
- indefinite float loops, large depth swings, or perspective spins when exact text matters.

## 4. Kinetic Typography — 动态文字

### Definition

Typography whose scale, position, weight, color, spacing, or grouping changes over time to express rhythm and meaning. The defining feature is semantic synchronization, not merely animated entrance.

### Best use

- energetic hooks, contrast, lists, repeated phrases, escalating statements, and social-video emphasis;
- two to five meaningful word groups rather than a full transcript.

### Motion model

- split speech into semantic word groups;
- assign one dominant property change per group, such as scale, weight, color, or position;
- let the active group land on the corresponding vocal stress while completed groups remain stable or dim;
- return to one composed final layout before exit.

### Prompt module

```text
将台词“[exact phrase]”分为“[group 1]”、“[group 2]”和“[group 3]”三个完整词组。
每个词组只在对应语音重音处执行一次明确变化：[scale/weight/color/position]。
新词组激活时，已完成词组降为次要层但保持字形稳定；最后组合为一个清晰终帧。
```

### Avoid

- random per-character rotations, font cycling, scrambling, or constant pulsing;
- combining large camera movement, broad body gestures, particles, and dense kinetic text simultaneously.

## 5. Lower Third — 人物信息条

### Definition

A title or graphic overlay placed in the lower region of the frame, normally within title-safe margins, to identify a person, place, chapter, or contextual fact without displacing the main action.

### Best use

- name and role, location and date, chapter label, speaker ownership, or source attribution;
- introductions and multi-speaker handoffs.

### Motion model

- reveal the backing shape or rule first;
- reveal the primary line, then the smaller supporting line;
- hold long enough to read; exit as one container in the reverse direction;
- for multiple speakers, activate only the current speaker’s identifier.

### Prompt module

```text
在人物下方[leading/trailing]侧的标题安全区显示下三分之一信息条。
背景形状先以[horizontal wipe/height unfold]展开，随后主行“[name]”和次行“[role]”依次出现。
信息条锁定屏幕平面，不随人物身体晃动，不覆盖手部、麦克风或平台字幕；读取完成后整体退场。
```

### Avoid

- placing identity text over the person’s torso when negative space is available;
- oversized role descriptions, crowded logos, or two equally dominant lower thirds.

## 6. Tracked Callout — 跟踪标注

### Definition

A label connected by a leader line to a specific feature, object, body region, or product point. Its identity depends on a stable anchor and continuous tracking, not on the visual style of the label.

### Best use

- product features, interface parts, anatomy, clothing details, tools, maps, or technical components;
- any phrase that explicitly refers to “this part,” “here,” or a visible property.

### Motion model

- establish the anchor dot on the exact physical point;
- draw the leader line from anchor to label;
- reveal the label after the line reaches its endpoint;
- track translation, scale, rotation, and perspective; recover or hide during occlusion.

### Prompt module

```text
以[physical feature]上的固定点为主锚点，先出现小型标记点，再向[free-space direction]绘制一条折线连接器，
线端完整显示标签“[copy]”。锚点紧贴同一物理特征，连线和标签连续跟随位移、缩放、旋转与透视，
不漂移、不穿过人体；锚点被遮挡时标注降低透明度或暂时隐藏。
```

### Avoid

- tracking a broad low-detail region instead of one stable feature;
- letting the label follow the feature but leaving the connector endpoint behind;
- tracking audience-facing subtitles to a moving subject.

## 7. HUD Overlay — HUD 界面

### Definition

A head-up information display that lets the viewer see status information and the underlying scene at the same time. HUD describes information presentation and viewing function; cyan glow and science-fiction styling are optional.

### Best use

- status, targeting, monitoring, navigation, diagnostics, security, aerospace, sports, or machine vision;
- concise information needed during continuous action.

### Motion model

- boot or acquire only the needed module;
- reveal reticle, grid, gauge, or status row in functional order;
- update one meaningful value or state at a time;
- keep primary view clear and settle nonessential modules to low contrast.

### Prompt module

```text
在[screen-space/camera-space]中建立克制的 HUD 信息层：[reticle/grid/status bar/data tile]。
只显示用户提供的“[exact data/copy]”，按观看任务的先后顺序启动模块。
网格、扫描线和光效只服务于定位或状态变化，不覆盖人物眼睛与口型，不生成随机数据。
```

### Avoid

- decorative pseudo-data, unreadable microtext, full-frame scanning, or constant reticle motion;
- calling every glowing panel a HUD when it has no monitoring or status function.

## 8. FUI — 科幻虚构界面

### Definition

Fantasy User Interface: a fictional interface and motion language created to support story, character, technology, performance, and worldbuilding. It can appear on physical screens, as a hologram, as a visor HUD, or as a post-composited overlay.

### Best use

- speculative technology, AI, science fiction, security, medical scanning, futuristic laboratories, or stylized product narratives;
- situations where interface behavior must reveal narrative meaning, not merely decorate the frame.

### Motion model

- derive a functional metaphor from the story domain;
- build a limited grammar of modules, states, transitions, and colors;
- synchronize interface changes to the speaker’s action or story beat;
- maintain character- and context-specific differences.

### Prompt module

```text
创建一套与[story domain/character]一致的 FUI 视觉语言：[palette]、[geometry]、[material]、[icon family]和[motion grammar]。
当(S1)说到“[trigger]”时，只启动支持该语义的[module]，用“[exact copy]”呈现剧情信息。
界面状态与人物手势、视线和语义发生因果关系，不填充无意义代码或随机数据。
```

### Avoid

- combining unrelated cyberpunk, medical, military, luxury, and cartoon interface languages;
- copying proprietary film UI, logos, fictional alphabets, or exact branded layouts.

## 9. Floating UI Card — 悬浮信息卡

### Definition

A bounded information container that groups related copy, icons, lists, buttons, or metrics. The card may use solid, translucent, glass, or holographic material and can exist in screen space or world space.

### Best use

- definitions, feature summaries, lists, quotes, steps, chat messages, documents, and compact comparisons;
- busy backgrounds where text needs a stable contrast container.

### Motion model

- materialize or unfold the container first;
- reveal heading, body, and icon in hierarchy order;
- use shared-axis or container morphs when changing state;
- collapse or dim the entire card as one object.

### Prompt module

```text
在[anchor]生成一张[solid/translucent/glass/holographic]悬浮信息卡，其坐标空间为[screen/world]。
容器边框先闭合，然后依次显示标题“[heading]”、说明“[body]”和[icon/list]。
背景材质保持足够局部对比度，不叠加多层玻璃，不让背景纹理穿过字形影响可读性。
```

### Avoid

- glass-on-glass stacking, excessive refraction, or using high transparency over a bright busy background;
- treating unrelated information as one crowded card.

## 10. Spatial UI / AR UI — AR 空间界面

### Definition

Virtual interface content placed into the perceived physical scene with explicit position, orientation, scale, depth, anchoring, occlusion, and viewer relationship. It is not defined by holographic glow.

### Positional behaviors

- **world-locked:** fixed to one world pose;
- **surface-anchored:** welded to a wall, desk, screen, or detected plane;
- **billboarded:** fixed in position but rotates to face the viewer;
- **tag-along:** follows the viewing region with controlled lag;
- **subject-tracked:** follows a moving person or object feature.

### Motion model

- establish or confirm the anchor;
- materialize at a comfortable scale and distance;
- preserve parallax, occlusion, and perspective during camera movement;
- use gentle transitions and avoid large peripheral movement.

### Prompt module

```text
将[panel/object]放置在场景中的[world pose/surface/subject anchor]，明确其大小、朝向、景深层和遮挡关系。
镜头或人物移动时，内容保持正确视差和相对位置；若使用 billboard，只绕[vertical/full]轴平滑转向镜头，
不突然翻面；若使用 tag-along，内容以柔和滞后跟随而不粘死在视野中心。
```

### Avoid

- undefined “floating in air” behavior with no coordinate system;
- sliding against the background, broken occlusion, or scale changes unrelated to camera distance.

## 11. Animated Infographic — 信息图动画

### Definition

A sequential visual explanation of relationships, process, hierarchy, comparison, time, cause, or flow. Its success depends on reading order and semantic structure more than decorative style.

### Best use

- workflows, numbered steps, timelines, before/after, cause/effect, hierarchy, maps, and educational explanations.

### Motion model

- reveal the frame or first node;
- reveal nodes one at a time in reading order;
- draw connectors only after their source exists;
- keep completed nodes dim but stable; highlight only the active step;
- settle on a complete overview before exit.

### Prompt module

```text
将“[topic]”编排为[stepper/timeline/comparison/flowchart]，包含精确节点“[item 1]”、“[item 2]”、“[item 3]”。
按口播顺序逐个显现节点，连接线只在源节点完成后向目标绘制。
已完成节点降低亮度但不删除，当前节点在对应重音处落定；最后保留完整可读的总览。
```

### Avoid

- revealing every node and connector simultaneously;
- arrows with no defined source and destination;
- tiny explanatory text that cannot be read during the hold.

## 12. Data Visualization — 数据可视化

### Definition

Visual encoding of supplied quantitative or categorical data through position, length, area, angle, color, or connection. It must communicate a real relationship and must not invent values.

### Selection guide

- comparison: bar, grouped bar, lollipop;
- trend: line, area, sparkline;
- part-to-whole: stacked bar, donut only for few categories;
- progress toward a goal: meter, bullet, gauge;
- correlation: scatter or heat map;
- connections: network or flow diagram;
- one key value: KPI or big-number card.

### Motion model

- establish axes, baseline, or container;
- animate marks from a meaningful origin to supplied values;
- land labels and units with the data marks;
- highlight the one insight referenced by speech;
- freeze final values and scale for reading.

### Prompt module

```text
仅使用用户提供的数据[exact dataset]生成[chart type]。
先建立标题、轴、单位和基线，再让数据标记从[meaningful origin]平滑到真实数值。
当(S1)说到“[insight trigger]”时，只强调[relevant series/value]；所有数字、单位、颜色编码和坐标比例保持稳定。
```

### Avoid

- invented values, fake precision, mixed scales, 3D chart distortion, or decorative gauges with no target;
- changing the axis or color meaning during animation.

## 13. Animated Icons — 图标动画

### Definition

Semantic symbols animated to introduce an idea, confirm an event, show state change, or represent ongoing activity. The motion must reinforce the icon’s meaning.

### Motion vocabulary

- appear/disappear: introduction or removal;
- draw on/off: routes, arrows, checks, links, handwriting;
- bounce: one playful confirmation;
- scale: selection or emphasis that persists briefly;
- pulse: temporary active or ongoing state;
- variable fill/color: strength, progress, connection, broadcast;
- replace/morph: related state change;
- rotate: loading, refresh, orbit, or real rotation.

### Prompt module

```text
在说到“[trigger]”时，以统一[outline/filled]风格的[icon]表达[semantic meaning]。
图标只执行与含义匹配的[appear/draw/fill/replace/rotate]动画一次，在重音处达到清晰终态。
与同片其他图标保持一致线宽、圆角、透视和光强。
```

### Avoid

- indefinite rotation or pulsing when no ongoing state exists;
- unrelated icon morphs, mixed icon families, or trademarked platform symbols without permission.

## 14. Particle Network — 粒子与连线

### Definition

A system of particles, nodes, trails, and edges used to represent connection, data movement, energy, diffusion, or emergence. It may carry meaning or act as a restrained accent; the prompt must say which.

### Required system properties

- emission source and start condition;
- node placement rule and connection rule;
- trajectory, velocity, drag, turbulence, and depth range;
- color, size, opacity, trail length, and glow;
- lifetime, decay, collision or occlusion behavior, and stop condition;
- local-space or world-space simulation.

### Motion model

- emit from one motivated source or region;
- form only the needed connections;
- send a limited pulse or data packet along the path;
- decay and stop after the semantic event.

### Prompt module

```text
从[source]在“[trigger]”时发射少量[data/energy]粒子，沿[defined path]移动并按[connection rule]连接到[target nodes]。
粒子具有明确的速度、阻力、景深、寿命和衰减；只有一次信号脉冲抵达目标，随后连线降亮并完全停止。
粒子不从人脸前方穿过，不形成全局无来源漂浮。
```

### Avoid

- “random particles everywhere” with no source, path, decay, or stop state;
- using particle density to compensate for weak information design.

## 15. Screen-Space Overlay — 屏幕叠加

### Definition

Graphics locked to the viewer’s frame rather than to the photographed scene. Their pixel position and orientation remain stable regardless of camera perspective or scene motion.

### Best use

- lower thirds, captions, chapter labels, broadcast graphics, audience-facing HUD, CTA, and framing devices.

### Motion model

- use frame edges, title-safe margins, or a fixed grid as anchors;
- animate independently of the camera;
- keep pixel-stable during camera movement;
- redesign for aspect-ratio changes instead of scaling blindly.

### Prompt module

```text
该图形为屏幕空间叠加层，锁定在画面[corner/edge/safe-zone coordinate]，不参与场景透视和镜头视差。
镜头、人物和背景移动时，图形保持像素稳定，不跟随人物身体，并始终避开人脸、手势和平台字幕区。
```

### Avoid

- describing it as physically floating beside the speaker;
- adding parallax, surface reflections, or scene occlusion that contradict screen locking.

## 16. Surface-Attached Graphics — 场景附着图形

### Definition

Graphics planar-tracked or conceptually welded to a visible surface such as a blackboard, wall, display, desk, page, floor, or product face. They inherit the surface’s perspective, scale, motion, and occlusion.

### Best use

- blackboard explanations, product labels, projected diagrams, screen replacements, document animation, and environmental signage.

### Motion model

- identify the plane and its corners, texture, and viewing angle;
- reveal within the surface boundary;
- preserve corner perspective and local scale through camera movement;
- allow foreground objects to occlude the graphic naturally.

### Prompt module

```text
将“[copy/diagram]”附着在[surface]的同一平面上，与表面四边、法线和纹理保持一致透视。
镜头或表面移动时，图形同步跟随位移、缩放和角点变形，不滑动、不漂移。
人物手部从表面前方经过时形成正确遮挡，图形不穿过手掌。
```

### Avoid

- attaching to a textureless or repeatedly occluded area without a stable plane;
- mixing surface-attached and screen-space behavior in the same element.

## 17. World-Space Panel — 世界空间面板

### Definition

A panel treated as an object or plane inside the scene. Its apparent size, perspective, parallax, depth of field, and occlusion depend on its 3D placement relative to the camera and subject.

### Orientation options

- fixed world orientation;
- fully camera-facing billboard;
- vertical-axis billboard that preserves upright orientation;
- subject-facing panel;
- surface-offset panel floating a defined distance from a wall, desk, or product.

### Motion model

- emerge from a motivated source or bounded region;
- settle at an explicit world pose and depth;
- preserve parallax and occlusion;
- if billboarded, rotate smoothly within defined axes;
- exit toward its origin or collapse into its container.

### Prompt module

```text
面板是场景中的世界空间对象，位于[subject/surface]的[direction]侧，距离[relative distance]，朝向[fixed/billboard/subject-facing]。
面板从[source]展开后在明确位姿上停止；镜头移动时产生正确视差、透视、景深和前后遮挡，
不滑向屏幕边缘，不突然改变大小。
```

### Avoid

- unspecified depth or orientation;
- keeping a world-space panel pixel-stable during a moving-camera shot unless it is intentionally camera-space.

## 18. Combination recipes

### Presenter introduction

`lower third + screen-space + phrase-block wipe + editorial/corporate`

### Product feature explanation

`tracked callout + subject anchor + line draw + solid label card`

### Classroom or blackboard explainer

`animated infographic + surface-attached + sequential draw + education/knowledge`

### Futuristic digital-human explainer

`floating UI cards + world-space billboard + HUD/FUI style + restrained holographic material`

### Data-led business explanation

`KPI card + chart + screen-space or surface-attached + clean corporate`

### High-energy social hook

`kinetic typography + screen-space + scale settle + social energetic`

### Machine-vision point of view

`HUD overlay + camera-space + tracked callouts + limited particle paths`

## 19. Selection and audit rules

- Choose the information format from meaning, not from visual fashion.
- Choose the spatial behavior from what the graphic is attached to.
- Choose the style from story, brand, scene, and audience.
- Use one primary family per semantic beat and at most one supporting family.
- A secondary accent may inherit the primary container and motion grammar; it must not create a second competing system.
- If the camera moves, explicitly state whether each element is screen-locked, camera-space, tracked, surface-attached, billboarded, or fixed in world space.
- If the source image has no safe negative space, reduce effect density before shrinking text.
- When exact copy or data is critical, reduce camera, body, background, particle, and typographic motion.
- Preserve a clean resting frame after every major reveal.
- Every dynamic graphic needs a paired entrance and observable in-clip exit. Dimming or lowering priority is not an exit.
- Clear each independent group before the next group appears, or visibly morph the existing container into the next state; never accumulate completed historical layers until one global cleanup at the end.
- Reserve a short clean-tail interval after the final spoken word when the last graphic must retract or disappear.
