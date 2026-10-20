# Real Components to Renderable Frames

## Find the Actual Feature Entry Point First — Not Just a Few Basic Controls

Find the business components and their composition relationships from actual pages/routes for the feature being shown, then trace to the theme, CSS, fonts, icons, providers, and state dependencies. For example, to showcase model switching, reuse the actual model selector and its options; to showcase a file tree, reuse the file tree/node components — don't import a Button and hand-write the rest of the page.

Integration order:

1. Import the original business component or actual composition component directly, and load its complete style chain. Existing Storybook stories, demo routes, or preview harnesses can serve as controlled mount points.
2. Add minimal provider/context, fixed non-sensitive props, and state fixtures. The adapter's job is to make the **original component** run, not to redraw its internal DOM.
3. When dependencies are complex, solve specific issues first: alias resolution, asset paths, CSS compilation, providers, network/IPC stubs. The starter project mounts components in a browser where component effects actually execute: if a provider is missing, add it; if it fetches data, provide fixtures in `fixtures/api.js`; don't hand-replicate because of one error.
4. When it still can't run directly, prefer reusing existing presentational sub-components, preserving the original composition structure and styles. Necessary source extraction must preserve provenance and minimize changes — don't take the opportunity to redesign.
5. Only when a clear platform/technical boundary makes the above infeasible, explain the specific obstacle, methods attempted, and affected shots, and propose controlled screen capture or faithful display adaptation. Continue if existing user authorization covers the alternative; otherwise let the user choose; don't use "saves time, too many dependencies, hard to animate" as a reason to silently replicate. Other reusable shots continue in parallel.

"Abstraction" means reducing the information visible simultaneously in the frame, highlighting key original components, and adjusting framing — it does not mean redrawing the software. The fallback style wraps the promotional frame; it does not replace the software being demonstrated.

## Making Original Components Run in the Film

A tested approach (CodePilot's input field, messages, tool steps, approval modal, model selector, and plugin page all appeared on camera this way):

- **Provider**: Read the product's app shell, fill in the context the component depends on (i18n, tooltip, panel/split state, icon defaults) with static values in `product-context.jsx`. Errors saying `must be used within ...` tell you which one is missing.
- **Data**: Components that `fetch('/api/...')` in effects get fixtures returned by path from `fake-api.js`. Fixtures derive from the product's own constants or catalogs (e.g., generating the model list from the product's built-in service presets) — names and icons are real.
- **Non-determinism**: `fake-api.js` fixes the clock and random seed; components that switch greetings by time period or randomly pick a sentence render identically every time.
- **Real interaction**: Typing uses the native setter to write to the real textarea and dispatches an `input` event — React's onChange fires normally; popups open and close with real clicks; selected items are selected with real clicks. The driver computes expected state from time and only intervenes when the DOM disagrees, so scrubbing forward and backward both work.
- **Popups & 3D**: Radix-style portals mount to `document.body` by default and don't scale with the shot. Write an adapter that points the portal's container to a node inside the shot. While a popup is open, its panel must not have 3D rotation (positioning libraries calculate in 2D).
- **Video scale**: Feature shots zoom the product root node globally (body text ≥ 22px), or use a camera wrapper to push in; don't shrink font sizes to cram into the frame. When the product has a dark theme and the film goes dark, use its dark theme directly.

## Original Component State and Animation

- Expand/collapse, select, switch, load, complete — prefer triggering through original component props, controlled state, or real interaction. Discrete states that change over time (which step is complete, how many characters of a reply are shown) are computed by `useShotState` and passed as props to the original component.
- When original animations aren't seekable, connect time to the main timeline only at the display entry point, preserving original visuals, state semantics, and layout; don't delete the original component and replace it with fake DOM.
- The shot's outer wrapper can add zoom, movement, masking, focus, and choreography. Extra promotional title cards don't impersonate the product interface; bilingual title typography rules don't override fonts inside the component either.
- Choreographed shots can extract and zoom actual sub-components, but must not fabricate states, interactions, or composition relationships that don't exist in the original software.

## Reuse Evidence for Every Feature Shot

Record per shot in `evidence/component-usage.json` or equivalent: `shotId`, `featureEntry`, `components`, `styleEntries`, `stateDriver`, `adapters`, `reuseMode`, `exceptions`. Paths must point to source actually used, not just list component names you hope to use.

Cross-check the list against the build import graph, actual JSX/mount entry points, and still frames:

- Did it use the business component for the corresponding feature, not just generic buttons/cards?
- Do styles come from the CSS/theme/font/assets the component actually uses, not just a few color constants?
- Are select, expand, etc. states actually rendered by the original component?
- Does the component in the shot match the original page in shape, hierarchy, spacing, icons, and state detail (framing and proportional zoom allowed)?

An import in the build graph doesn't prove it appeared on camera; similar still frames don't prove source reuse — both pieces of evidence must be combined. Parts not using original components are marked explicitly; don't call the whole film "all native components" in vague terms.

React/Next projects handle `@/` aliases, CSS/Tailwind, Next Image, router, client providers, and icon libraries per project specifics. A successful build doesn't mean styles took effect, nor that data arrived: produce still frames and check.

Vue/Svelte use their own render entry; Electron shells should not start real IPC inside the promo process; when native UI can't be imported directly, explain why controlled screen capture or display-layer adaptation was chosen.

When native apps (e.g., Rust/GPUI, SwiftUI) are faithfully rebuilt with user consent: dimensions come from source code (title bar, tab bar, panel default widths, font sizes and line heights), colors from theme files, fonts/icons/logos from original repo files; write everything that changes on screen (buffer text, cursor, popups, panel state) as a pure function model of film time, and read both the visuals and `plan.json` action timing from this model. In component-usage, state which source files correspond to each interface and note this is a rebuild, not a running app. When the user explicitly requests code-driven animation, don't secretly degrade to screen-capture collage.

## Engineering & Assets

Keep source, assets, evidence, and renders in a separate project. Record dependency versions and lockfile, dimensions, FPS, duration, component sources, font and music sources. Don't bundle the full original repo/node_modules for others.

Asset handling must cover references inside real components:

- Root-relative paths like `/provider-icons/...` often break in standalone players. Copy public assets and fix the base path, or convert small SVGs to data URIs.
- CSS `url(...)`, font files, icon inlines, and image loading strategies also need handling.
- Wait for fonts and images to decode before capturing. A page with no errors doesn't mean images are complete; check `img.complete && img.naturalWidth > 0`.
- A local HTTP server is closer to the export environment than `file://`. Final files should avoid depending on the external network.
- Shared resources need appropriate licensing; music from reference videos cannot be assumed extractable and reusable.

## Determinism & Timeline

All animation is driven by one main timeline or a pure `seek(t)`. Any `t` can reconstruct the complete frame — no dependency on having played previous frames.

- GSAP: paused main timeline; in HyperFrames, register `window.__timelines[compositionId]` per the current project contract; media is framework-managed.
- Remotion: state computed from frame/fps.
- Standalone browser (starter project): `window.seek(seconds)` advances React clock, interaction drivers, GSAP main timeline, and per-frame rendering in sequence; Playwright captures frame by frame + FFmpeg exports.

Define initial/end states for each shot and test forward/backward jumps. The starter project freezes all CSS transitions/animations; motion library micro-animations can jump to end state via a global switch; product dynamics that must be preserved (loading spinners, progress bars) are rebuilt by time in `onRender`. Random numbers, requests, and timers use fixed fixtures.

## Composition & Cropping

CardFrame handles shadow, border radius, and outer space — no cropping; CardSurface handles inner background and cropping. When zooming a component, check the **post-transform** bounds. Don't assume the parent has enough height means it won't clip a zoomed child.

For cards to be centered: outer flex/grid centers, inner transform scales, and reserve space for the transform. Avoid positioning offsets multiplied by CSS zoom causing unexpected downward shift. A page whose total width doesn't overflow doesn't prove text/icons inside a local mask aren't cropped.

Use the product's full official icons, especially app icons with rounded-rectangle backplates. Don't just crop out the inner symbol as a substitute.

## Link Handling

Handle per user's release requirements — don't assume all platforms in a region forbid links. When links must not appear, prefer clearing URLs in fixtures first, using neutral shapes or blurred placeholders in the address bar; if screen masking is necessary, the mask must move and scale with the component. Check end cards, corner badges, screenshots, and exported frames too. Don't blur a URL in one spot only to reveal the full URL in another shot.
