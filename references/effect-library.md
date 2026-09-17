# Talking-Head VFX Library

Select a small coherent subset. The library is a decision vocabulary, not a checklist.

## 1. Text effects

### Primary message

- **Phrase-block fade and rise:** complete phrase moves a short distance upward while opacity increases; safest general-purpose reveal.
- **Masked wipe:** text is revealed by a horizontal or vertical matte; suitable for corporate, news, education, and technology.
- **Scale settle:** phrase begins slightly smaller, approaches final scale, and decelerates without a large bounce; suitable for hooks and conclusions.
- **Split reveal:** two halves or two lines enter from related directions; use for contrast, before/after, or dual concepts.
- **Line-by-line build:** complete lines appear sequentially; suitable for longer statements and stable Chinese copy.
- **Word-group kinetic type:** two to five meaningful word groups receive size, weight, or position changes; suitable for energetic social content.
- **Tracking expansion:** letter spacing settles from wide to normal; use for premium, restrained headings, not dense body copy.
- **Blur-to-sharp focus:** phrase resolves from slight optical softness to crisp type; use sparingly for insight, memory, or reveal.
- **Depth emergence:** text moves from a slightly recessed plane to its final screen plane; suitable for spatial or high-end technology design.

### Emphasis and annotation

- animated underline or bracket draw;
- highlight bar traveling behind a keyword;
- color or weight change on the currently spoken phrase;
- circled keyword, marker stroke, arrow, connector, or callout line;
- number counter, percentage, unit, or statistic card;
- quote card with quotation glyph and speaker attribution;
- label chip, tag, badge, or lower third;
- checklist row with checkmark completion;
- progress bar, step indicator, timeline marker, or chapter label;
- subtitle chunking with selected keyword emphasis.

Avoid random per-character rotation, scrambling, glitching, or continuous scale pulsing when exact text matters.

## 2. UI panels and information graphics

- **Glass card:** translucent panel, controlled blur, restrained border, and stable contrast; good for modern business, technology, lifestyle, and product explanations.
- **Solid information card:** opaque or semi-opaque shape behind text; best for busy backgrounds and mobile readability.
- **HUD panel:** fine grid, corner brackets, small nodes, scanning accent, and limited glow; use only for technology, science, security, aerospace, or data themes.
- **Dashboard:** metric tiles, line/bar/donut charts, counters, status dots, and compact labels; numbers must come from supplied facts.
- **Process stepper:** numbered nodes connected in one direction; reveal one step at a time.
- **Comparison panel:** two aligned columns, split screen, balance scale, versus marker, or before/after labels.
- **Timeline:** ordered points with one active segment; use for history, schedules, stages, or development.
- **Map or location panel:** map silhouette, route line, pin, compass, distance, or region label; never invent geographic facts.
- **Diagram:** nodes, arrows, concentric rings, flowchart, anatomy, hierarchy, or cause-effect chain; reveal in reading order.
- **Product callout:** tracked line from product feature to label; the anchor must remain attached to the same physical point.
- **Chat or social card:** message bubble, comment, reaction, follow, subscribe, notification, or profile card; use only when content concerns communication or creator platforms.
- **Document/browser card:** simplified page, search bar, file, table, or interface window; use supplied text and avoid tiny unreadable UI.

## 3. Icon effects

Choose icons by semantic meaning, not decoration. Use one consistent family and compatible stroke weights.

Useful icon motions:

- **Appear/disappear:** gradual introduction or removal.
- **Draw on/off:** path traces the symbol; good for arrows, routes, checkmarks, ideas, links, and process.
- **Scale:** small controlled growth for emphasis or state confirmation.
- **Low-bounce feedback:** one damped bounce for success, welcome, or playful confirmation.
- **Pulse:** restrained opacity or scale pulse for a temporary active state; do not pulse indefinitely.
- **Variable fill/color:** outline fills or color changes to show state transition.
- **Replace/morph:** related icon changes while preserving position, such as lock to unlock or play to pause.
- **Rotate:** reserved for loading, settings, refresh, orbit, or actual rotation concepts.

Common semantic families:

- idea: bulb, spark, brain, star;
- proof/trust: check, shield, certificate, lock;
- warning: triangle, exclamation, alert bell;
- time/process: clock, calendar, timeline, progress;
- data/growth: chart, arrow, gauge, target;
- communication: message, microphone, phone, mail, share;
- location: pin, globe, compass, route;
- people: profile, group, handshake, community;
- commerce: cart, bag, tag, coin, receipt;
- technology: chip, cloud, network, code, database.

Do not use trademarked platform icons, logos, or proprietary interface assets unless the user supplies or authorizes them.

## 4. Graphic accents

- lines, corner brackets, grids, crosshairs, dots, rings, arcs, waves, chevrons, and connectors;
- soft gradient fields, mesh gradients, restrained noise, halftone, paper texture, or film grain;
- blob or organic shape morphs for lifestyle/playful content;
- geometric blocks and modular tiles for corporate/technology content;
- sticker, doodle, marker, torn paper, or stamp motifs for casual/education content;
- contour lines, map lines, orbit paths, or data streams for science and geography.

Accents should form a hierarchy around the information. Never let decorative shapes compete with the face or copy.

## 5. Particles, light, and atmosphere

- localized dust, spark, data particle, bokeh, streak, trail, ripple, or energy point;
- edge light, rim glow, light sweep, scan line, volumetric ray, holographic shimmer, or subtle lens response;
- shadow, reflection, refraction, translucency, depth blur, parallax, or atmospheric haze;
- localized distortion, displacement, chromatic split, glitch, or digital breakup for a motivated transition.

Rules:

- confine particles and glow to a defined region or path;
- give particles a source, trajectory, decay, and stop condition;
- keep glow subordinate to text contrast;
- do not create unexplained moving light blobs, global exposure pulses, floating bokeh in front of faces, or random lens flare;
- glitch and chromatic split are short transition accents, not a continuous texture;
- preserve the source image's real light directions and color temperature.

## 6. Reveal and transition patterns

- fade, slide, wipe, mask, scale, crop, unfold, draw, dissolve, blur focus, depth move, card expand, shape morph, icon replace, and tracked callout;
- match direction to spatial logic: elements introduced from the right should usually settle from the right or emerge within their right-side container;
- use shared-axis or container transforms when one state becomes another;
- transition related elements through continuity; remove unrelated elements before introducing a new group;
- pair every independent entrance with an explicit, visible exit inside the clip; do not depend on one end-of-video cleanup to remove several accumulated groups;
- treat dimming as hierarchy control, not removal; when the information is finished, collapse, retract, wipe, dissolve, draw off, or morph the complete group into its successor;
- a one-shot H3 prompt may animate overlays without moving the camera or cutting the scene.

Avoid simultaneous entrances from every edge, persistent oscillation, repeated full-screen flashes, unmotivated zooms, and transitions that change direction arbitrarily.

## 7. Style systems

### Clean corporate

Neutral sans-serif type, solid or lightly translucent cards, blue/teal accent, thin connectors, restrained fades and wipes, almost no particles.

### Realistic technology

Dark or cool glass, fine grid, cyan/blue accents, tracked nodes, line draws, compact data cards, localized scan light, controlled depth and glow.

### Premium minimal

Large negative space, one elegant headline, restrained serif or refined sans serif, slow mask reveal, minimal line work, subtle light sweep.

### Education and knowledge

Clear hierarchy, colored labels, diagrams, arrows, step cards, highlights, checklists, friendly icons, sequential reveal.

### Social energetic

Bold type, short word groups, stickers or simple icons, punchy scale settles, fast but damped transitions, high contrast, limited palette.

### News and finance

Lower thirds, name/role cards, tickers, maps, charts, data labels, red only for genuine alerts or losses, disciplined motion.

### Warm lifestyle

Soft rounded cards, warm accents, gentle fades, handwritten accent used sparingly, organic shapes, low-amplitude float with a defined settle.

### Documentary/editorial

Subtle captions, dates, places, quotes, archival frames, clean lines, restrained parallax, soft fades, low effect density.
