# Visual Device Vocabulary

Common devices grouped by function. Each entry states what it expresses, what product aspect it should derive from, implementation notes, and common pitfalls. **This is a vocabulary, not a menu**: a film picks 3–5 devices derivable from the product; the rest are unused. Read [film direction](direction.md) before choosing.

All devices must satisfy the same technical constraint: the frame is determined only by time (seek-safe). GSAP animations are attached to the main timeline; canvas/WebGL is written as a `render(t)` pure function registered to `onRender`; random numbers use fixed seeds. `assets/fx-lab/` has adaptable examples for devices marked ★.

## Opening & Hook

| Device | Expresses | Derive From | Implementation | Pitfall |
|---|---|---|---|---|
| Flow lines / fly-through ★ | Speed, entering a world | Product's "fast" or "many" | Three.js line segments, position = integral of velocity | Looks grandiose on a calm product |
| Slot rotation | Repetition of pain points (today A, tomorrow B) | What users actually swap out | Hard cut or very short blur cut, intervals progressively faster | Crossfade loses the rhythmic feel |
| Real interface macro | Entering the product directly | The most representative single control | Real component zoomed 3–4×, depth of field blurs the rest | Text wraps/overflows after zoom |
| Sentence written character by character | Quiet, weighty | Writing/conversation products | Character by character or stroke by stroke, with cursor | Sentence too long — audience loses patience |
| Data first | Opening with the result | Provable numbers available | Number roll + chart path drawn | Numbers without a source |

## Brand & Logo

| Device | Expresses | Derive From | Implementation | Pitfall |
|---|---|---|---|---|
| Particle convergence ★ | Scattered things coming together | Logo itself is geometric | Extract cells from rendered SVG (`targetsFromSvg`), swap to crisp SVG once particles settle | Forcing it when the logo isn't geometric |
| Construction lines & control points | Precision, designed | Design products, or logo has a grid | SVG lines drawn with `strokeDashoffset`, square nodes pop in | Too many lines, too bright — steals from the subject |
| Wordmark stroke to fill | From sketch to finished | Distinctive wordmark | Stroke path drawn then filled | Chinese font paths too complex |
| Extrusion / isometric blocks | Structure, stability | Logo has 3D potential | CSS 3D layered or Three.js extrude geometry | Excessive glossy materials look cheap |
| Shape morph | One thing becoming another | Logo and product UI share shapes | SVG path interpolation (point counts must match) or mask | Morph intermediate states look ugly |

## Stage & Background

| Device | Expresses | Derive From | Implementation | Pitfall |
|---|---|---|---|---|
| Glowing horizon ★ | Entrance, ceremony | Dark, premium products | CSS multi-layer radial gradients + dark body occlusion | Used in consecutive shots; clashes with light products |
| Gradient field | Mood, brand colors | Products with rich brand colors | Slow-moving large color blobs (canvas or CSS), low contrast | Placed behind a dense interface — can't see it |
| Character field ★ | Code, data, the underlying layer | Technical products, using its own code or data | 2D canvas character grid + noise brightness, center kept empty | Feels cold for non-technical audiences |
| Paper & ink | Writing, warmth | Writing/note-taking products | Paper texture + ink diffusion mask | Texture too heavy — looks dirty |
| Grid & dot matrix | Order, tool-like feel | Design/data tools | Very faint dots or lines, parallax with camera | Fights with the interface grid |
| Environmental depth of field | Real usage scenarios | Hardware, mobile | Device mockup + blurred background | Fabricating hardware the product doesn't have |

## Product On Camera

| Device | Expresses | Derive From | Implementation | Pitfall |
|---|---|---|---|---|
| Zoom framing + push/pull | Letting the audience see one thing clearly | All feature shots | Camera wrapper animates x/y/scale with GSAP; landing positions measured on the timeline first (`screenCenterAt`) | Manual landing calculation under 3D tilt will be off |
| Perspective-tilted panels | Spatial depth, premium feel | Dark interfaces with clear hierarchy | Parent sets `perspective`, panels use small `rotationX/Y`, slowly changing over time | Portals misposition under 3D transforms — return to flat when opening |
| Flat board + camera flyover | Overview, system | Pages with many cards or modules | Entire page `rotationX 50–60°` raised to 10–20° | Raising too fast causes disorientation; card text too small |
| Lift detail along Z axis | Highlighting within the overview | Key items in a list/card | Add `translateZ` and shadow to a duplicate in the same `preserve-3d` container, dim the background | The lifted element is hand-drawn, not the real component |
| Orbit ★ | Many things connected to one core | Integrations, services, plugin count | Manual projection: depth controls size, opacity, blur, and layering | Fabricating members just to fill the circle |
| Cursor interaction | This is a real clickable thing | Interactive features | Cursor moves in product coordinate space, click lands on the beat, real click triggers state | No state change after clicking |
| Real typing & streaming output | Agent/conversation at work | Conversation/generation products | Write to the real input using native setter; truncate reply characters by time | Entire block appears at once |

## Chapters & Text

| Device | Expresses | Derive From | Implementation | Pitfall |
|---|---|---|---|---|
| Chapter large text | Section break, rhythm | Features groupable into verbs | One word fills the frame, 1–1.5 seconds | Meaningless words (UPDATE, NEW) |
| Slice offset ★ | Signal, interruption | Need a strong section break | Text sliced into horizontal strips, spring back from different offsets; paired with thin light bars | Used as the default title entrance |
| Character-by-character blur entrance | Refined, breathing | Most titles | `Split` + `reveal`, stagger 0.02–0.05 seconds | Every element uses it — becomes monotonous |
| Word quick-cut | Many small features | Small features not worth a full shot | One word per beat, rotating entrance methods, with counter | Each word held too long — becomes subtitles |
| Light beam sweep | Emphasis, completion | End of film or key word | A horizontal line with glow sweeps across quickly | Frequent use loses weight |
| Serif editorial title | Taste, content products | Content/reading products | Serif English + sans-serif Chinese, tightened tracking | Chinese in serif looks dated |

## Transitions

| Transition | Used For | Implementation |
|---|---|---|
| Hard cut on beat | Impact, sudden light change | Cut point lands on the beat; previous shot blurs its subject first for a cleaner cut |
| Zoom-through | Moving from concept into the product | Previous shot's subject zooms in and fades out; next shot starts slightly large and pulls back |
| Push-in continuation | An element from one shot is the next shot's subject | Push in to that element; next shot starts from the same position, same size |
| White flash / black | Between major sections | 0.15–0.25 seconds, paired with impact sound |
| Mask wipe | Between parallel features | Shape comes from the product (rounded rectangle, logo shape) |

Don't do long cross-dissolves between light and dark shots: a gray patch appears mid-transition. Use a hard cut, or blur the previous shot's subject out first.

## Technical Notes

- **Three.js in headless export**: The starter project's `render.mjs` / `stills.mjs` already include SwiftShader parameters; set `preserveDrawingBuffer: true` on the renderer, pixel ratio 1. **Load `threejs-animation` for keyframe, morph-target, and procedural motion patterns.**
- **One WebGL canvas per scene**, keep the whole film to 2–4 contexts; use CSS or 2D canvas for background layers instead of WebGL when possible.
- **GSAP**: The main timeline is paused, driven by `seek`. `fromTo` writes start values at build time — build only after layout measurement is complete. Don't target nodes React will re-render; attach animations to a stable wrapper. **Load `gsap-core` for API details, `gsap-timeline` for sequencing, `gsap-performance` for optimization rules.**
- **CSS filters** (blur) and 3D transforms both work correctly in frame-by-frame capture, but large-area blur slows export; render a few frames first to estimate cost.
