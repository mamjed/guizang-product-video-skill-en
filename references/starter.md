# Starter Project: Technical Foundation, Not a Production Template

Initialization produces a 10-second, 3-shot **technical demo** that proves only one thing: "real components mount → timeline → screenshot at any moment → MP4" pipeline works end to end. It deliberately has no visual style — the production film's frame design system, shots, and techniques are all written fresh in `DIRECTION.md` for this product.

## Running

Requires Python 3, Node.js, FFmpeg. First run the environment check per SKILL.md; install missing items per [Dependency Installation](onboarding.md).

```sh
python3 <skill-dir>/scripts/init_project.py --output <video-dir> --style repo --repo <repo-dir>
cd <video-dir>
python3 <skill-dir>/scripts/check_environment.py --project . --engine browser
npm run build
node stills.mjs evidence/stills 1.5 5 8.5          # Batch still frames in one session, also prints page errors and API requests
node render.mjs --from 4 --to 7 --output renders/draft.mp4   # Partial draft, no audio needed
node render.mjs --silent-demo --output renders/technical-demo.mp4
npm run preview                                     # Browser console: await seek(4) or playFilm()
node cover.mjs                                      # Export 3:4 / 4:3 / 16:9 covers from cover/cover.html (see references/cover.md)
```

Production export:

```sh
python3 <skill-dir>/scripts/mix_audio.py plan.json
node render.mjs --audio assets/master.wav --output renders/final.mp4
python3 <skill-dir>/scripts/check_delivery.py plan.json --video renders/final.mp4 --mix-report evidence/audio-mix.json
```

Exports frame-by-frame stills (JPEG middle frames, x264 encoding). A 50-second film with WebGL and blur filters typically takes 2–4 minutes; render a few seconds first to estimate. `--silent-demo` is only for the technical demo; for a user-requested silent production film, set `audioRequired:false` and record `audioExceptionReason`.

## Runtime Architecture

```
src/client.jsx        Mounts <Film>, waits for fonts and fixture data, then runs each shot's builder, exposes window.seek / __filmReady
src/engine.js         seek(t): React clock → interaction-driven → GSAP master timeline → shot visibility → onRender canvas
src/film-store.js     useShotState(select): components read discrete state by in-shot time (which step, how many characters typed)
src/fake-api.js       Fixed clock, fixed random seed, path-based fixture fetch, silent EventSource/WebSocket
src/fixtures/api.js   API fixtures; derive from the product's own constants/directories where possible so names and icons are real
src/product-context.jsx  Providers the product shell would normally supply (i18n, theme, tooltip, routing/panel context)
src/kit/              Split + reveal (text split entrance), Cursor + paintCursor, offsetCenter / screenCenterAt, setFieldValue / typed / ensureOpen
src/shots/index.js    plan.json shot id → view component + builder
src/film.css          This film's frame design system (type scale, layout), plus mechanisms required for frame-by-frame rendering
src/adapters/         Static stand-ins for framework runtimes like next/image, next/navigation, etc., aliased as needed
```

`seek(t)` is a pure function of t — seeking forward, backward, or rendering a single frame all produce consistent results:

1. `flushSync` pushes time to React. Components use `useShotState(l => stageAt(l, [...]))` and re-render only when discrete state changes, e.g. a tool step appears or a reply gains characters.
2. Runs drivers registered via `onDrive(id, fn)` — the **real interactions**: typing into real input fields (`setFieldValue` + `typed`), clicking real buttons to open real overlays (`ensureOpen`). Drivers must be idempotent: compute expected state from time first, only touch the DOM when it differs. Return a Promise when overlay positioning needs to settle; `render.mjs` will await it.
3. `master.seek(t)`: all GSAP animations hang on this single paused master timeline, placed using absolute film time.
4. Show/hide shots by time (with 0.8s overlap on each side for transition blending).
5. Calls per-frame drawing registered via `onRender(id, fn)`: Three.js, 2D canvas, time-dependent style calculations.

### Writing a Shot

```jsx
// src/shots/agent.jsx (illustrative; names and structure follow this film's needs)
export function AgentView() { /* Real component + this film's layout; GSAP targets use stable wrappers */ }
export const buildAgent = tl => {
  const s = shot('agent');
  // 1. Measure first (layout already exists): offsetCenter(el, root), or screenCenterAt(tl, t, el) for 3D-transformed screen position
  // 2. Then place animations on tl: tl.fromTo(el, from, to, s.start + 0.4)
  // 3. Register per-frame work: onDrive('agent', local => ...), onRender('agent', local => ...)
};
```

- Shot start/end times live only in `plan.json`; code reads them via `shot(id)` — single source of truth for timing.
- GSAP `fromTo` writes start values at build time, so measurement must happen before placing animations.
- GSAP timelines are thenable: `await tl` waits for the timeline to finish, but a paused master timeline never ends. Builders can be async functions, but do not await the timeline itself.
- Nodes that React re-renders or conditionally renders should not be direct GSAP targets: wrap them in a stable container to animate.
- Micro-animations in the product (motion/framer-motion, CSS transitions) compete with the film clock for state: `film.css` freezes CSS animations; products using motion libraries should enable `MotionGlobalConfig.skipAnimations` in `client.jsx`. For things that need to keep moving (spinning loading icons), set transforms by time in `onRender`.
- Background effects can reference and adapt `assets/fx-lab/`, see [Visual Device Vocabulary](visual-vocabulary.md).

### First-Frame Poster

Openings typically start from a blank canvas, but platforms grab the first frame as a thumbnail. The fix: overlay a still frame of the completed opening state on the topmost layer, fully opaque for the first 0.3 seconds (≈ 9 frames), then fade out over 0.3 seconds. The underlying opening animation still starts from 0s — no timeline or audio changes needed.

In the starter project, the same DOM is driven by the GSAP master timeline and cannot simultaneously sit at t=0 and at the completion moment, so the poster uses a real rendered still frame:

1. After the opening is built, pick the moment when the opening section is complete and all titles are visible, export a still frame, and place it in `public/` (`build.mjs` copies it to `dist`):
   ```sh
   node stills.mjs public/poster 5.9 && mv public/poster/t005.90.png public/poster.png && rmdir public/poster
   ```
2. Add `<img id="poster" src="poster.png" alt="" />` at the end of `<main>` in `film.jsx`, styled to fill the frame with `z-index` above all shots, then `npm run build`.
3. In the opening shot's builder, attach the fadeout to the master timeline. Do not use `onRender`: it only runs near the shot — jumping directly to a later section would leave the poster covering everything.
   ```js
   tl.fromTo('#poster', {opacity: 1}, {opacity: 0, duration: 0.3, ease: 'none'}, 0.3);
   ```

When the opening changes, re-export the still frame or the poster and film will not match. For films where the view itself is a pure function of time (renders directly from `t`), you can skip the still frame and instead mount a second `<Opening t={completionTime} />` as a poster layer within 0.6 seconds — same principle.

## Connecting to the Repo

1. In shot views, directly import the feature's original business components and composition layers. Do not wire up just a few basic buttons and hand-write the rest of the UI.
2. Read the product's root layout and app shell; write the providers the components depend on into `product-context.jsx`, all using static values. Missing providers cause immediate runtime errors (`xxx must be used within yyy`) — add them one by one per error.
3. For components that fetch data in effects, provide fixtures in `fixtures/api.js` by path. The `api` list output by `stills.mjs` shows the actual requested paths — use it to find gaps.
4. Compile the product's real styles into `src/product.css` (below), preserving theme, fonts, icons, and state rules. When the product has a dark theme, `ProductContext dark` enables it directly.
5. Place brand assets, fonts, and public icons in `public/` (copied to the web root); fix root-path references in components (e.g. `/provider-icons/...`).
6. The build outputs `evidence/component-imports.json`; record reuse evidence per shot, see [Component Pipeline](component-pipeline.md).

`--style default` / `hybrid` copies fallback style components; `repo` does not. The starter demo is laid out at 1920×1080; changing the aspect ratio requires re-layout.

### Parse Configuration

```js
// integration.config.mjs
import path from 'node:path';
const repo = '/absolute/path/to/product', video = path.resolve('.');
export default {
  repoDir: repo,
  aliases: {
    '@': path.join(repo, 'src'),
    'next/image': path.join(video, 'src/adapters/next-image.jsx'),     // Only add when components actually use it
  },
  external: [], loaders: {}, define: {},
  esbuild: {},   // Other esbuild options, e.g. tsconfigRaw
};
```

The builder outputs a browser IIFE bundle: resolves dependencies from the product's `node_modules` first; React/ReactDOM both point to the video project's copy (two React instances cause `Cannot read properties of null (reading 'useContext')`). When product dependencies are missing, install only pinned display dependencies in the video project. Resolve paths for strictly isolated layouts like pnpm according to the actual workspace mapping. Dependencies with top-level await cannot be bundled into the IIFE: switch to their synchronous entry point, or change the build to ESM.

Monorepo workspace packages that export TS source directly: alias the package name to its `src`; for packages with subpath `exports`, read their `package.json` to generate a subpath → source file alias table. When the product has `verbatimModuleSyntax` enabled, type imports are preserved as-is and may drag server-side runtime into the browser bundle; use `esbuild: {tsconfigRaw: {compilerOptions: {verbatimModuleSyntax: false}}}` to relax only this display build.

When an alias needs to "replace one export in a module, keep everything else" (e.g. redirecting an overlay portal into the shot), the adapter can first `export * from '<real file absolute path>'`, then separately export the same-named replacement.

### Next / Tailwind Style Chain

Tailwind source CSS must be compiled first. Tailwind v4: create `src/product.input.css`, import the product's real CSS entry, and scan both product and video source:

```css
@import "/absolute/path/to/product/src/app/globals.css";
@source "/absolute/path/to/product/src";
@source "./";
```

```sh
npx @tailwindcss/cli -i src/product.input.css -o src/product.css   # Version matches the product
npm run build
```

When shot code adds new Tailwind classes, recompile. Tailwind v3 uses the matching version's CLI and a config inheriting the product's theme/plugins; `content` includes both product and video source. `url(...)` fonts/images in the product CSS must be findable in `dist/`. Sources: [esbuild nodePaths](https://esbuild.github.io/api/#node-paths), [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli).

## Plan Fields

- `demo`: true for the technical demo; set to false once production content is ready.
- `product / width / height / fps / duration / style / audioRequired`: project specs.
- `typography`: default `mode:bilingual`, specify `zhFont / enFont` separately, `zhStyle:sans-serif`; when the user specifies monolingual or other fonts, record the rationale in `exceptionReason`.
- `shots[]`: `id, start, end, type, headlineEn, headline, plainExplanation, description, descriptionAt, claim, source, component, actions`. Shot implementation in code follows the shot table in `DIRECTION.md`; the plan records timing, facts, and audio — the two must be consistent.
- Shots with `claim` true must provide `source`. Format: `file:docs/release.md` (relative to video project) or `repo:src/features/panel.tsx` (relative to `plan.repo`), supporting `:line-number` / `#Lline-number`; bare paths check the video project first then `plan.repo`; URLs, version tags, commit references are for fact-checking. Brand openings do not need fabricated sources.
- `component`: actual source path or adapter; can be null for title cards.
- `actions`: unique `id`, `at` relative to shot start, action description, `soundRequired`.
- `audio.music / audio.cues`: cue `at` is the film-absolute time of file start; `syncOffset` is the auditory landing point within the file, satisfying `at + syncOffset = action time`. Measure landing points with `scripts/sfx_landmarks.py` — do not guess. Optional `onBeat` / `beatDivision` references `audio.beatGrid`.
- `descriptionAt`: time relative to shot start when the description text appears, used for reading-time hints.

Re-mix when the shot list or score changes; production export verifies the hash of plan vs. master. Generic placeholder components carry `data-skill-placeholder`; in production mode the build rejects placeholder content still visible on screen.

## Integration Regression

After modifying the builder, engine, or kit, run:

```sh
python3 -m unittest discover -s <skill-dir>/tests
node <skill-dir>/tests/integration.mjs --modules <video-dir>/node_modules
```

The integration test constructs a product repo in a temp directory and verifies: dependencies and aliases that exist only in the product resolve, CSS assets copy, component effects receive data through fixture APIs, GSAP state is correct when seeking forward and backward, and WebGL renders in headless export. It does not auto-install dependencies.
