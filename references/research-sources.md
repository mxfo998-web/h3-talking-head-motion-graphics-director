# Research Sources and Applied Rules

This skill distills the following primary or official sources. Use them for rationale, not as text to paste into a prompt.

## MiniMax H3

- MiniMax-AI, **MiniMax H3 Skills**: https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/README.md
  - Confirms the official prompt-writing skill and the five routes T2VA, I2VA, FL2VA, L2VA, and Ref2VA.
  - Applied rule: preserve exact route-specific field structures and reference labels.

## Adobe After Effects

- Adobe, **Animating text**: https://helpx.adobe.com/after-effects/desktop/animating-text/text-animation/animating-text.html
  - Text can animate as a whole layer or by selected characters/ranges; motion blur smooths moving edges.
  - Applied rule: define reveal unit and use restrained motion blur while keeping final text crisp.

- Adobe, **Creating and editing text layers**: https://helpx.adobe.com/after-effects/desktop/add-text/create-and-edit-text-layers/creating-editing-text-layers.html
  - Text layers support independent animation of source text, color, size, and position; vector text remains crisp when scaled.
  - Applied rule: treat copy as a stable independent layer with explicit properties rather than an incidental background texture.

- Adobe, **Track Mattes and Traveling Mattes**: https://helpx.adobe.com/after-effects/desktop/work-with-transparency-and-compositing/work-with-track-mattes-and-traveling-mattes/track-mattes-and-traveling-mattes.html
  - Alpha/luma mattes can reveal footage, graphics, text, or shapes and should travel with their target when linked.
  - Applied rule: use mask/wipe reveals and keep overlays attached to one container or surface.

- Adobe, **Compositing and transparency overview**: https://helpx.adobe.com/after-effects/desktop/work-with-transparency-and-compositing/compositing-in-after-effects/compositing-transparency-overview-resources.html
  - Layers combine through transparency, masks, mattes, keying, and blending modes.
  - Applied rule: specify overlay depth, opacity, masking, and occlusion instead of asking for generic “cool effects.”

- Adobe, **Mask Tracker**: https://helpx.adobe.com/after-effects/using/rigid-mask-tracking.html
  - Tracking must be checked for drift and corrected when shape or perspective changes.
  - Applied rule: tracked callouts need one stable point, continuous scale/perspective, and explicit anti-drift direction.

- Adobe, **Safe Margins**: https://helpx.adobe.com/after-effects/desktop/get-started/preferences-and-settings/preferences.html
  - Title-safe and action-safe guides protect essential content across crops and displays.
  - Applied rule: keep important text and actions away from edges and redesign layouts for aspect-ratio changes.

## Motion behavior

- Apple, **Motion**: https://developer.apple.com/design/human-interface-guidelines/motion
  - Motion should be purposeful, brief, precise, spatially logical, and not excessive or persistently oscillating.
  - Applied rule: one semantic reveal at a time, coherent direction, short feedback, quiet recovery.

- Android Developers, **Customize animations**: https://developer.android.com/develop/ui/compose/animation/customize
  - Easing controls acceleration/deceleration; spring, tween, keyframes, and spline paths suit different motion behaviors.
  - Applied rule: avoid linear robotic motion, match easing to entrance/exit, and use damped springs selectively.

## Icons and symbols

- Google Developers, **Material Symbols guide**: https://developers.google.com/fonts/docs/material_symbols
  - Symbols support adjustable fill, weight, grade, and optical size; fill can communicate state transitions.
  - Applied rule: keep icon family and stroke weight consistent and use state animation semantically.

- Apple, **SF Symbols**: https://developer.apple.com/design/human-interface-guidelines/sf-symbols
  - Official effects include appear, draw, bounce, scale, pulse, variable color, replace, and rotate; excessive symbol animation distracts.
  - Applied rule: use icon effects as a semantic vocabulary with one clear purpose.

## Typography and readability

- Apple, **Typography**: https://developer.apple.com/design/human-interface-guidelines/typography
  - Legibility depends on size, weight, contrast, typeface count, hierarchy, and viewing context.
  - Applied rule: use few typefaces, avoid thin small text, and establish headline/supporting/metadata hierarchy.

- Apple, **Image views**: https://developer.apple.com/design/human-interface-guidelines/image-views
  - Text over imagery can reduce clarity; contrast, shadow, or a backing layer can improve readability.
  - Applied rule: give overlay text a deliberate contrast container on busy footage.

- W3C, **WCAG 2.2 Contrast Minimum**: https://www.w3.org/TR/WCAG22/#contrast-minimum
  - Normal text targets 4.5:1 contrast and large text 3:1, with defined exceptions.
  - Applied rule: use these ratios as conservative design targets when colors are controllable.

## Flash safety

- W3C, **Understanding SC 2.3.1 Three Flashes or Below Threshold**: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold
  - Avoid flashing or keep it within defined general/red flash thresholds; no more than three flashes per second is the simple safe rule.
  - Applied rule: replace strobe with a sweep, fill, draw-on, or single damped pulse, especially for large bright or red regions.

## Reference-video handling

The user-supplied reference video was technically verified as 3840×2160, 24 fps, approximately 15.04 seconds, H.264 video with AAC stereo audio. Those facts support a short high-resolution talking-head use case. Visual motifs must only be claimed after successful frame-level inspection; the skill therefore contains general effect-selection logic rather than hard-coding unverified motifs from that file.
