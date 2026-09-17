# Composition, Timing, and Quality

## 1. Attention hierarchy

Maintain this default order:

1. active speaker's eyes and mouth;
2. primary on-screen message;
3. supporting icon, chart, or callout;
4. decorative particles, light, and texture;
5. background.

An effect may briefly approach the speaker's visual weight at a major reveal, then recede. Decorative layers never remain brighter, sharper, larger, or faster than both the face and primary copy.

## 2. Safe composition

- Keep essential text and graphics inside a title-safe region. As a robust video heuristic, reserve roughly the outer 10% for action and a larger inset for essential text when delivery crops are unknown.
- Respect platform overlays, captions, profile controls, and mobile notches when a target platform is known.
- Protect face, mouth, eyes, hands, products, microphones, logos, and eyelines.
- Give text a stable container or contrast treatment when placed over imagery.
- Use consistent margins, baselines, alignment, corner radii, line weights, and internal padding.
- When adapting ratios, redesign the layout rather than merely scaling every element.

## 3. Readability

- Use a clear type hierarchy: headline, supporting line, metadata.
- Prefer one or two typefaces and a small number of weights.
- Avoid thin weights for small text or bright translucent backgrounds.
- Maintain strong text/background contrast; use a solid or translucent backing, shadow, outline, or local blur when the image is busy.
- Target at least 4.5:1 contrast for normal text and 3:1 for large text as a conservative accessibility goal when colors can be controlled.
- Keep line length and copy density appropriate to viewing distance and platform.
- For 480P or small mobile delivery, enlarge type, thicken lines, simplify cards, and reduce particle density.

## 4. Timing lifecycle

Every effect has five states:

1. **preparation:** optional subtle anticipation before the trigger;
2. **entrance:** the element becomes visible;
3. **landing:** its final readable form coincides with the spoken keyword or payoff;
4. **hold/emphasis:** the viewer can read it while speech continues;
5. **exit/recovery:** it visibly collapses, moves out, dissolves, retracts to its source, or transforms into the next state, then leaves the intended clean resting frame.

Start a reveal slightly before the target word when necessary so the landing, not the first motion, coincides with semantic stress. Hold the final readable state through the relevant phrase. Do not remove information before the speaker finishes referring to it.

The default lifecycle is bounded inside the clip: every dynamic graphic that enters must also complete an observable exit. Reduced brightness, lower priority, or indefinite stable persistence is not an exit. Persistence is allowed only when the user asks for it or when the same information group still needs the element; state that reason and its eventual exit explicitly.

Before an independent information group begins, the previous group must either fully clear or visibly replace/morph into the new state inside one continuing container. Do not stack completed titles, cards, icons, connectors, and particles as historical layers. Keep no more than one primary information group active unless a comparison, list, or overview genuinely requires simultaneous visibility.

Name the semantic endpoint, exit motion, exit destination, and recovered frame for each event. When the final graphic should disappear, reserve roughly 0.5–1.0 seconds after the last spoken word when duration permits. If dialogue is intentionally budgeted near 5 written characters per second and fills nearly the whole clip, begin the final exit during the closing clause and complete it by the final punctuation; never schedule cleanup beyond the clip endpoint.

Introduce independent elements sequentially. Parallel motion is appropriate only when elements form one perceptual group, such as a card and its border or a chart line and its active value.

## 5. Motion grammar

- Use easing that accelerates and decelerates. Constant linear speed usually feels mechanical.
- Use ease-out for entrances and emphasis landings.
- Use ease-in for clean exits.
- Use ease-in-out for continuous lines, tracks, or camera-independent moves.
- Use low-bounce spring motion for playful feedback; use critical or overdamped settling for corporate, news, medical, finance, and premium work.
- Preserve current velocity and direction when one state transitions into another.
- Keep overshoot small enough that text does not become unreadable or cross safe boundaries.
- Apply restrained motion blur to moving text or shapes, but keep the final hold crisp.
- Avoid persistent oscillation and perpetual floating unless the amplitude is small, the layer is decorative, and it does not compete with reading.

## 6. Text animation stability in generative video

H3 must synthesize both content and motion, so typography requires explicit stabilization:

- quote exact visible copy;
- reveal complete words, phrases, or lines;
- define final line breaks and alignment;
- state that glyphs, punctuation, numbers, and spacing remain unchanged after appearing;
- keep text attached to one plane or tracked surface;
- avoid scrambling, rapidly cycling fonts, per-character 3D spins, perspective flips, and repeated retyping;
- avoid very fine grids and one-pixel strokes at low resolution;
- keep completed rows dim but stable instead of deleting and recreating them;
- if exact copy is critical, reduce simultaneous body, camera, particle, and background motion.

## 7. Layering and compositing logic

Define each element as one of:

- **screen-space overlay:** audience-facing and locked to the frame;
- **world-space panel:** exists beside or behind the subject with stable perspective and occlusion;
- **surface-attached graphic:** tracked to a display, wall, product, desk, or card;
- **subject-linked callout:** follows one stable point without drifting;
- **background effect:** remains behind the subject;
- **foreground accent:** crosses in front only when explicitly intended and never hides key anatomy.

State which layers can occlude others. Localize masks and glows to the intended region. A screen effect should not spill onto the face unless the design requests a subtle, physically consistent light response.

## 8. Realistic light and particles

- Give emitted light a source, falloff, color, affected surfaces, and maximum extent.
- Keep exposure, white balance, practical lights, shadow direction, and background bokeh stable.
- Confine scanning lights and particle systems to a panel, path, or source.
- Particles need emission, trajectory, drag, depth, decay, and stop behavior.
- Use glow as edge support, not a white bloom that destroys text or skin detail.
- Avoid global exposure breathing, drifting light orbs, unexplained lens flares, flashing bokeh, and color contamination of skin.

## 9. Flash and motion safety

- Never create more than three flashes in any one-second period.
- Prefer no repetitive flashing at all for large, bright, high-contrast, or saturated-red areas.
- Replace strobing with a single sweep, opacity settle, color fill, line draw, or damped pulse.
- Keep rapid motion small and peripheral; do not use it as the only carrier of meaning.
- Avoid sustained large oscillations, aggressive camera shake, and repeated zoom punches in ordinary talking-head work.

## 10. Camera and effects

For fixed camera:

- lock position, focal length, horizon, framing, exposure, and depth of field;
- let overlays animate independently within the frame;
- keep screen-space graphics pixel-stable;
- keep world-space graphics attached to their plane;
- do not introduce a hidden digital push-in unless requested.

For moving camera:

- specify whether effects are screen-locked, tracked, or world-space;
- preserve parallax and occlusion consistently;
- reduce simultaneous overlay motion during rapid camera movement.

## 11. Complexity budget

Reduce overload in this order:

1. remove decorative particles and ambient loops;
2. remove secondary icons and redundant borders;
3. simplify entrances and exits;
4. reduce the number of visible cards;
5. shorten on-screen copy without changing required words only when the user permits;
6. simplify camera motion;
7. preserve the speaker, primary message, and exact text last.

At low resolution or under 15 seconds, one strong effect system usually outperforms many unrelated effects.

## 12. Human-performance timing

- Treat the person and graphic as one causal sequence: attention preparation, spoken trigger, graphic landing, one motivated human response, readable hold, graphic exit, then gaze/body recovery.
- Default Mandarin speech planning to about 5 written characters per second, counting punctuation but excluding whitespace and H3 tags. Report the actual count, and align phrase groups, breaths, gestures, and effect landings to this pace without mechanical uniformity.
- Keep lens engagement alive without unwavering staring. Name any temporary gaze target and the return target; eyes lead modest head movement.
- Place isolated blinks near breath, phrase boundary, gaze shift, cognitive release, or environmental stimulus, never at a fixed rate.
- Match phoneme closures, vowel shapes, jaw amplitude, inhalation, pause, exhalation, swallowing, and lip reset to the speech timeline; silence stops speech mouth motion.
- Expressions use onset, peak, and partial release. Gestures use preparation, semantic peak, settle, and a stable rest pose.
- Fixed camera locks the camera only; breathing, weight, posture, gaze, and restrained performance continue inside the frame.
- Reduce particles, secondary icons, decorative light, and UI density before reducing face, mouth, eyes, breath, posture, hand continuity, or the primary message.

## 13. Final quality audit

Verify frame-to-frame continuity of:

- speaker identity, face, mouth, teeth, eyes, hair, clothing, hands, and props;
- exact text, icon shape, chart values, logo, spelling, line breaks, and alignment;
- panel size, perspective, anchor, opacity, and glow;
- background objects, practical lights, exposure, white balance, and shadows;
- active-speaker ownership, phoneme-level lip states, breath, contextual blinks, gaze targets and returns, expression onset/peak/release, posture support, gesture preparation/peak/rest, and turn handoffs;
- reveal order, readable holds, quiet intervals, and effect exits.

If the prompt asks H3 to control detail that is invisible in the framing, either revise the framing or lower the precision claim.
