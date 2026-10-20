# CodePilot Original Case Study: Preserve What Worked, Do Not Freeze Accidental Parameters

The final production film is 48 seconds, 1920×1080, 30 FPS, 14 shots, 120 BPM. Real React components bundled via esbuild form the visuals, driven by GSAP, exported by HyperFrames. The music is code-original instrumental; additional recorded SFX sourced from a local library attributed to Pixabay; the earliest first version had even notification tones synthesized by code. The skill's default workflow uses post-production compositing; source and bundled replacement SFX are listed in [Audio Sourcing](audio-sourcing.md). This is one successful instance, not a mandatory tech stack or duration for all products.

## What Worked

- Directly imported the model selector, RuntimeSelector, input fields, tabs, card containers, CLI maintenance rows, buttons, and icons; providers used minimal read-only adapters.
- Shots progressed from large text to selection cards, then to input areas, workspaces, and notifications — never repeating the same layout.
- File trees, diffs, browser content, and system notifications were controlled demonstration data; did not claim the entire business system was running live.
- Music, SFX cues, and visuals shared one timeline. Actions of ≈ 0.3–0.6 seconds, plus enough explanation dwell time.

## Issues Actually Fixed During Iteration

| Problem | Root cause | Reusable check |
| --- | --- | --- |
| Visuals good but feels silent | Early music too quiet; tracks exist but still feel insufficient | Measure loudness and listen to the final film |
| Rhythm feels stuck | Repeated layouts; animation and still holds too long | Explain early, intersperse title cards and close-ups; make every pause carry information |
| Direction draft diverged from user intent | Generating concept art cannot replace real component animation | Wire in code components early; still frames come from actual renders |
| GLM 5.3 card bottom edge cropped | Position offset compounded by zoom magnification, exceeding local mask | Check transformed component bounds; center and leave room |
| TokenDance icon tearing | Component references site root path; standalone preview assets missing | Inline the original SVG or copy correctly; verify images in both preview and export |
| Few words but unclear | Small text has only phrases, no function and result | Complete sentences, appear earlier, time shots to reading speed |
| Logo incomplete | Only used the icon's center symbol | Use the official rounded-rectangle app icon |
| Frame extraction missing components | CSS transition/visibility competing with master timeline for state | Hook original animations to the master clock; when necessary, disable only the specific conflicting elements; seek forward and backward to verify |
| Does not meet this release's requirements | URLs in browser and end credits | Remove URLs from fixtures, neutralize the address bar, remove end-credit links and their animations |

Still-frame checks cannot replace rhythm review; framework checks passing cannot replace final film review. Social covers are made per user request; method see [Cover](cover.md); when not mentioned, ask at delivery rather than expanding scope by default.

## Lessons from the Second Project

Chinese Song-typeface titles, decorative English labels, vague complete sentences, and a BGM-only audio track exposed default-value problems. Specific practices are in [Shot List & Copy](story-and-copy.md) and [Audio Mix QA](audio-and-qa.md) respectively; this file retains the case background.

## The Third Project: Why Checklist Iteration Got Worse

The same CodePilot repo had three versions — the comparison is instructive:

| Version | Approach | Result |
|---|---|---|
| Model builds directly (HyperFrames) | First wrote `frame.md` visual spec (type scale, UI scaled to 22px, margins, safe area), then wrote a detailed shot description for each shot, finally orchestrated shot by shot with GSAP | Good rhythm, refined components, text motion done right |
| After iterating the skill with "12 blueprints + motion primitives + beat-hit/still-frame metrics" | Each shot mapped to a blueprint name, uniform data-attribute entrances, metric-based acceptance | 29/29 actions on beat, all cuts on bar lines; but the visuals were cramped, text small, titles colliding with icons, large blank areas in the UI |
| This skill's current workflow | First write `DIRECTION.md` (reference teardown, product character, three directions, frame design system, shot table), real components on camera at video scale, GSAP master timeline + Three.js/canvas background layer, still frames per shot, full-film contact sheet and transition strip | See next section |

Lesson: **The model will satisfy what can be quantized.** Compressing "looks good" into blueprint names and metrics yields a film with perfect numbers and mediocre visuals. What lands quality is the design done before writing code: specs written as concrete numbers, shots written down to every second.

## CodePilot Film: How Techniques Were Derived from the Product

50 seconds, dark stage. Two reference videos (Hero UI brand film, Talis launch film) yielded techniques, not copies: starfield flythrough, construction lines drawing the logo, product rising behind a glowing horizon, section title cards, slice offsets, pseudo-3D. Colors were not copied because CodePilot is charcoal monochrome.

| Technique | Because CodePilot has… |
|---|---|
| Stream-line field opening with "Use Claude / GPT / Gemini today…" rotation | Users switch between multiple models — that is the pain point it solves |
| Particles converging into each cell of a 5×5 dot matrix | The logo itself is a fading dot matrix — taken from the real SVG's geometry and opacity |
| Silver-white light arcs with only the faintest color fringe | Monochrome brand with a dark theme |
| Dark real UI scaled 1.6–2× with slight perspective | The product has a complete dark theme; Agent conversations, approvals, model selection are all real interactions in real components |
| Provider icons orbiting the input field | Presets include 17+ providers (count from README, icons from product dependencies) |
| Plugin page laid flat as a kanban board, camera flies over, skill cards lift along the Z axis | Skills and MCP are a full page of cards |
| Character field composed of product source code | A developer-facing tool |
| Section words Ask / Switch / Extend | Three core capabilities that happen to be three verbs |

Score is code-synthesized F minor electronic music (`assets/audio/score-example-cinematic.py`), sections arranged per shot boundaries; SFX uses Pixabay recordings from the local media-use library, landing points measured individually.

**This table is one derivation example, not a template.** For a different product, most of these techniques would not hold: no dot-matrix logo means no particle convergence; a light, paper-textured product should not use a glowing horizon; a product integrating only one or two services should not do an orbit. Derive fresh from the new product following [Film Direction](direction.md); when making films consecutively in the same workspace, change the opening, section, and background techniques.

Specific pitfalls encountered making this film (overlay portals, zoom landing points under 3D, gray flash on light-to-dark cuts, orphaned punctuation on line breaks, GSAP timeline being thenable) have been written into [Component Pipeline](component-pipeline.md), [Starter Project](starter.md), and [Review](review.md).
