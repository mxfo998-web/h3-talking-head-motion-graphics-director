# Motion-Graphics Terminology, Sources, and Production Examples

Researched and audited on 2026-09-16. Prefer these primary, official, or first-party production sources when explaining terminology or revising the type catalog. Do not paste source wording into user prompts.

## 1. Terminology audit

The common labels are not all the same kind of term:

- **Lower third, HUD, and FUI** identify recognizable information or production systems.
- **Kinetic typography, tracked callout, animated infographic, data visualization, animated icons, and particle network** identify motion or content families.
- **Screen-space, surface-attached, subject-tracked, billboarded, tag-along, and world-space** identify coordinate or anchoring behavior.
- **Holographic, glass, neon, editorial, corporate, educational, and social** identify visual style or material.
- **Floating typography** and **floating UI card** are useful production labels but do not have one universal standards-body definition. This skill therefore defines them operationally by container, anchor, coordinate space, and motion behavior.

Applied rule: never ask the user to choose between terms that live on different axes. A design may correctly be `FUI + floating card + world-space billboard + holographic material`.

## 2. Text animation, floating typography, and kinetic typography

- Adobe, **Animating text in After Effects**: https://helpx.adobe.com/after-effects/desktop/animating-text/text-animation/animating-text.html
  - Text can animate as a whole layer or by character, word, or line ranges; position, scale, rotation, opacity, color, spacing, and 3D properties can be controlled independently.
  - Applied rule: state the reveal unit and anchor grouping. Prefer word groups, phrases, or lines when exact H3 text stability matters.

- Adobe, **Creating and editing text layers**: https://helpx.adobe.com/after-effects/desktop/add-text/create-and-edit-text-layers/creating-editing-text-layers.html
  - Point text suits short words and lines; paragraph text suits bounded blocks. Vector text remains crisp when scaled.
  - Applied rule: floating typography should declare whether it is a short point-text phrase or a bounded paragraph/card.

- Adobe Learn, **Animate text in After Effects**: https://www.adobe.com/learn/after-effects/web/creating-animating-text
  - The practical example combines position keyframes and delayed opacity fades to lead attention in a sequence.
  - Applied rule: separate heading and supporting-copy entrances, preserve a clear final layout, and use eased rather than robotic linear motion.

- Adobe Learn, **Keyframe animation**: https://www.adobe.com/learn/after-effects/web/keyframe-animation
  - The example contrasts linear movement with eased movement and editable motion paths.
  - Applied rule: prompts should name entrance direction, path, landing, and easing, not merely say “text animates in.”

## 3. Lower thirds

- Adobe, **Lower third graphics**: https://www.adobe.com/creativecloud/video/discover/lower-third-graphics.html
  - Adobe defines a lower third as a title or graphic overlay placed in the lower region of the screen, usually inside title-safe space, for names, titles, logos, scores, captions, or contextual information.
  - Applied rule: use the lower third for context without pulling focus from the speaker; avoid crowding and conflicting color.

- Adobe Learn, **Animate a lower third**: https://www.adobe.com/learn/after-effects/web/animate-lower-third
  - The production example grows a backing shape first, then adds the name and a tighter text container.
  - Applied rule: prompt the container, primary line, secondary line, hold, and grouped exit in that order.

## 4. Tracking, callouts, and surface attachment

- Adobe, **Tracking and stabilizing motion**: https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-motion/tracking-stabilizing-motion-cs5.html
  - Tracking data can drive another layer or effect point; parallel or perspective tracking can update scale, skew, and corner placement.
  - Applied rule: callouts need a stable source feature, continuous translation/scale/rotation/perspective behavior, and anti-drift instructions.

- Adobe Learn, **Create visual effects — place type into video footage**: https://www.adobe.com/learn/after-effects/web/create-video-visual-effects
  - The example uses camera tracking to make text appear placed on an airport runway.
  - Applied rule: surface-attached graphics inherit the plane’s perspective, camera parallax, local scale, and occlusion.

- Google ARCore, **Working with anchors**: https://developers.google.com/ar/develop/anchors
  - Anchors keep virtual objects at a stable pose as world understanding updates; nearby objects can share an anchor to preserve their relative relationship.
  - Applied rule: nearby callout parts should share one anchor; avoid independent drift between the point, connector, label, and icon.

- Google ARCore, **Augmented Images — tracking optimization**: https://developers.google.com/ar/develop/augmented-images
  - A stable physical image can receive an anchor to improve tracking.
  - Applied rule: when attaching to a poster, display, or product face, explicitly name the tracked surface and keep the graphic inside its boundaries.

## 5. HUD and FUI

- NASA, **Head-up display background**: https://ntrs.nasa.gov/api/citations/19710010277/downloads/19710010277.pdf
  - NASA describes a HUD as presenting information while the operator can still view the outside scene.
  - Applied rule: HUD is a co-visible information layer with an operational purpose, not a synonym for cyan glow.

- Territory Studio, **Screen Graphics projects**: https://territorystudio.com/project-category/screen-graphics/
  - The studio frames screen graphics and UI as tools that support narrative and performance, delivered for on-set playback or postproduction.
  - Applied rule: FUI modules must serve story beats, character, and context.

- Territory Studio, **The Martian**: https://territorystudio.com/project/the-martian/
  - Real science and mission context shaped distinct NASA/JPL, biometric, vehicle, and rover interfaces; helmet readability motivated simple white/orange displays.
  - Applied rule: derive data density, palette, and geometry from function and viewing conditions.

- Territory Studio, **Guardians of the Galaxy**: https://territorystudio.com/project/guardians-of-the-galaxy/
  - Character dossiers, ship systems, and environment screens used different visual languages tied to character and world; graphics also explained plot-critical escape information.
  - Applied rule: a coherent project may contain multiple systems, but each scene should use the one appropriate to its owner and task.

- Territory Studio, **Blade Runner 2049**: https://territorystudio.com/project/blade-runner-2049/
  - Interfaces were choreographed with dialogue and actor performance, and different technology cultures received distinct materials and motion.
  - Applied rule: time interface state changes to performance and avoid generic “future UI” detached from the scene.

- Territory Studio, **Ready Player One**: https://territorystudio.com/project/ready-player-one/
  - Production included monitors, visors, HUDs, environmental signage, holographic devices, and volumetric graphics connected to story beats.
  - Applied rule: distinguish screen, visor/camera-space, environmental, holographic, and volumetric placements instead of describing all as overlays.

- Territory Studio, **Miles**: https://territorystudio.com/project/miles/
  - The project combined a robot-view HUD, motion-tracked holographic controls, and screen graphics.
  - Applied rule: HUD, tracking, holographic style, and screen graphics can coexist as separate axes.

## 6. Floating cards, glass material, and containers

- Apple HIG, **Materials**: https://developer.apple.com/design/human-interface-guidelines/materials
  - Materials establish depth, layering, hierarchy, and separation while preserving context; transparent glass needs contrast management and restrained use.
  - Applied rule: state material, background treatment, opacity, blur, edge definition, and contrast; do not stack multiple translucent cards without need.

- Apple HIG, **Windows**: https://developer.apple.com/design/human-interface-guidelines/windows
  - Windows create bounded content regions. In visionOS, glass planes exist in space, adapt to surroundings, and use dynamic scale for legibility.
  - Applied rule: a floating card or panel needs a bounded container, content hierarchy, scale, orientation, and relation to its surroundings.

- Apple Developer, **Applying Liquid Glass to custom views**: https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views
  - Glass can blur, reflect, move, combine, and morph, but remains a functional layer rather than a generic decoration.
  - Applied rule: use shared-container morphs for related card states and keep the material subordinate to readable content.

## 7. Screen space, camera space, and world space

- Unity Manual, **Canvas**: https://docs.unity3d.com/Manual/UICanvas.html
  - Unity distinguishes Screen Space — Overlay, Screen Space — Camera, and World Space. Overlay ignores scene perspective; camera-space sits on a camera plane; world-space behaves like a scene object with angle-, distance-, and occlusion-dependent appearance.
  - Applied rule: every major graphic should explicitly identify its coordinate space.

- Unity Manual, **Canvas render modes**: https://docs.unity3d.com/cn/2021.1/Manual/UICanvas.html
  - The examples show screen overlay, camera plane, and world-space UI as materially different render behaviors.
  - Applied rule: do not request parallax for a screen-space overlay or pixel stability for a fixed world-space panel.

## 8. Spatial UI and AR behavior

- Google ARCore, **Content placement**: https://developers.google.com/ar/design/content/content-placement
  - AR placement should use understandable surfaces, comfortable ranges, stable anchors, visual placement cues, and progressive disclosure.
  - Applied rule: define placement range, scale, anchor, shadow or contact cue, and reveal only the relevant surface or panel.

- Google ARCore, **UI elements**: https://developers.google.com/ar/design/interaction/ui
  - Persistent 2D overlays and sudden pop-ups can reduce immersion; controls should be simple and visual cues should guide attention.
  - Applied rule: spatial UI should avoid unnecessary screen takeover and use gentle, contextual transitions.

- Microsoft Learn, **Billboarding and tag-along**: https://learn.microsoft.com/en-us/windows/mixed-reality/design/billboarding-and-tag-along
  - Billboards rotate to face the viewer; tag-along content remains within a comfortable range or “a glance away.”
  - Applied rule: specify the facing axes, allowed rotation, lag, periphery behavior, and clipping risk.

- Apple HIG, **Designing for visionOS**: https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos
  - Spatial interfaces should use the minimum immersion appropriate to the task and prioritize comfort.
  - Applied rule: avoid large fast motion in peripheral space and use bounded panels for ordinary information tasks.

## 9. Animated infographics and data visualization

- Adobe Learn, **Create an animated infographic**: https://www.adobe.com/learn/animate/web/animated-infographic
  - The example separates symbols, motion paths, looping environmental elements, arrows, and pop-up content.
  - Applied rule: reveal infographic components in reading order and treat connectors and pop-ups as dependent states.

- Adobe Learn, **Animate graphics with data**: https://www.adobe.com/learn/after-effects/web/create-data-driven-animations
  - JSON keys and values drive reusable charts, graphs, weather visuals, and localized graphics.
  - Applied rule: tie chart marks, labels, and animation endpoints to supplied data; never fabricate values.

- IBM Carbon Design System, **Chart anatomy**: https://carbondesignsystem.com/data-visualization/chart-anatomy/
  - A chart uses coordinated titles, axes, ticks, units, legends, labels, graph frame, and optional interaction; excess elements reduce interpretation.
  - Applied rule: prompt the chart structure, units, direct labels, and one main insight before decorative motion.

- IBM Carbon Design System, **Chart types**: https://carbondesignsystem.com/data-visualization/chart-types/
  - Chart choice follows purpose: comparison, trend, part-to-whole, correlation, connection, or geospatial relationship.
  - Applied rule: select the chart from the rhetorical job, not from visual novelty.

- Microsoft Learn, **Power BI dashboard design tips**: https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboards-design-tips
  - Dashboards should show essential information at a glance, use appropriate chart types, maintain scale and color consistency, and avoid unnecessary 3D or precision.
  - Applied rule: prioritize one key metric or insight per beat and remove nonessential labels.

## 10. Animated icons

- Apple HIG, **SF Symbols — Animations**: https://developer.apple.com/design/human-interface-guidelines/sf-symbols
  - The official vocabulary includes appear, disappear, bounce, scale, pulse, variable color, replace, wiggle, rotate, and draw on/off, each suited to different feedback or state meanings.
  - Applied rule: choose one icon motion by semantic purpose and avoid excessive combinations.

- Google Developers, **Material Symbols guide**: https://developers.google.com/fonts/docs/material_symbols
  - Fill, weight, grade, and optical size support consistent symbol states; fill can communicate state transition.
  - Applied rule: keep icon family, optical weight, and scale compatible with the text and use fill changes for meaningful state transitions.

## 11. Particle networks

- Unity Manual, **Visual Effect Graph**: https://docs.unity3d.com/Manual/com.unity.visualeffectgraph.html
  - Node-based GPU simulation supports large and highly customizable particle systems.
  - Applied rule: “particles” must be described as a system with a source, simulation space, behavior, and lifecycle.

- Unity Visual Effect Graph, **Systems**: https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@10.5/manual/Systems.html
  - Systems can include spawn, particle, strip, mesh, and event-driven interactions, with local or world simulation space.
  - Applied rule: define emission, connection or trail behavior, local/world space, event trigger, decay, and stop condition.

## 12. Cross-cutting motion and accessibility

- Apple HIG, **Motion**: https://developer.apple.com/design/human-interface-guidelines/motion
  - Motion should be purposeful, brief, precise, spatially logical, and optional where possible; large peripheral motion and sustained oscillation can cause discomfort.
  - Applied rule: one semantic reveal at a time, no perpetual motion, and no motion as the only carrier of meaning.

- W3C, **WCAG 2.2 Contrast Minimum**: https://www.w3.org/TR/WCAG22/#contrast-minimum
  - 4.5:1 for normal text and 3:1 for large text are conservative readability targets when colors are controllable.

- W3C, **Three Flashes or Below Threshold**: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold
  - Avoid flashing or keep it below defined general and red-flash thresholds.
  - Applied rule: replace strobe with a single sweep, draw, fill, or damped pulse.

## 13. Research conclusions used by this skill

1. Start from semantic purpose, not style.
2. Separate information format, motion behavior, spatial behavior, and visual style.
3. Name exact copy and supplied data before describing motion.
4. Define coordinate space and anchoring for every primary element.
5. Use one reveal lifecycle: preparation, entrance, landing, hold, emphasis, settle/exit, recovery.
6. Treat tracking, perspective, occlusion, and camera-facing behavior as explicit prompt variables.
7. Make FUI and HUD functional or narrative, not pseudo-technical decoration.
8. Keep data truthful, chart encodings stable, and final values readable.
9. Give particles a physical or semantic system and a stop condition.
10. Preserve the speaker’s face, mouth, gaze, identity, and performance above all graphics.
