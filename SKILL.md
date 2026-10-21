---
name: guizang-product-video-skill
license: "AGPL-3.0; CodePilot fallback assets: BUSL-1.1 (see README.md)"
description: Create code-driven software product promos and release update videos (product promo, release notes video, changelog promo). Derive direction from real features and product design; finish films with real components, GSAP/Three.js motion, original score and action SFX. Every visual device in each film is derived from the product itself — no templates.
---

# Guizang product video skill

Use real components to clearly present a software product or an update, so that visuals, copy, and sound advance together. Terminology used in this document: **fallback style** refers to `assets/fallback/`; **starter project** refers to `assets/starter/`, and its initial output is called a **technical demo**; **direction file** refers to `DIRECTION.md` inside the video project; sound cues are stored collectively in `audio.cues`.

## Workflow

1. **Confirm scope, platform, and style.** For an existing project, keep the brief and user decisions; only handle the current changes. For a new film, fill in: product/repo, distribution channel, duration and aspect ratio, language, whether links are allowed, and whether the user has reference videos. **Scope and product platform surface must be decided by the user** — the repo can only list what versions exist, not what the user wants to promote: all product versions, the latest release cycle, or a specific version range? Which platform surfaces (desktop / CLI·TUI / mobile / server-side API)? If unspecified, ask once; write the answer into `plan.json` under `scope` (e.g. `{"versions":"v0.10.12..v0.11.0","platforms":["cli-tui"]}`) and sync it into BRIEF. If style is undecided, ask once: "Use the codebase's own design style (recommended), or the default warm-white / charcoal-black style?" `repo` uses the product design; `default` wraps content in the fallback style; `hybrid` keeps product identity while adjusting outer layout. Common starting point: landscape, 45–60 seconds, Chinese.
2. **Initialize and check the environment.** Initialize an isolated video directory via the tool entry points below, then run the environment check; load [dependency onboarding](references/onboarding.md) only for reported gaps, and re-check after installing. For existing projects, check directly without re-initializing.
3. **Investigate the product, connect components.** Follow [repo and style audit](references/repo-and-style.md) to determine features, release status, and evidence; note the design language, dark theme, and product elements that can become motifs. Mount real business components in the browser: add providers, use fixtures for APIs, use real clicks and inputs for interactions, and scale up to video dimensions ([starter project](references/starter.md), [component pipeline](references/component-pipeline.md)). Connect one feature shot first and produce a still frame.
4. **Set direction, write `DIRECTION.md`.** Follow [film direction](references/direction.md): deconstruct references, distill product character, propose three directions along different axes, pick one and document the reasoning; list 3–5 product-specific visual devices in "because the product has X, we use Y" form, and avoid devices from the previous film in the same workspace; write the frame design system as concrete numbers; build a shot list down to every second. When the user wants to see direction first, present three directions with 3–6 key still frames and wait for feedback; otherwise continue.
5. **Build shot by shot.** Each shot = view component + builder (GSAP main timeline, `onRender` canvas layer, `onDrive` real interactions); timing is read only from `plan.json`. Choose visual devices from the [visual device vocabulary](references/visual-vocabulary.md) that can be derived from the product; adapt examples from `assets/fx-lab/` before using them. Produce a still frame after each shot and cross-check against the shot list ([review](references/review.md)).
6. **Score and sound effects.** Follow [audio sourcing](references/audio-sourcing.md) to choose a music source (user-provided → locally available generation model → code-synthesized); derive arrangement from shot boundaries, derive timbre from product character; use recorded samples for SFX first, fill gaps with bundled WAV files. Use `sfx_landmarks.py` to measure hit points and levels; synchronize, duck, and mix according to [audio and QA](references/audio-and-qa.md).
7. **Review and deliver.** Export the full film; inspect the 2 fps contact sheet, 10 fps strips for each transition, and full-size frames for information-dense shots; revise per [review](references/review.md) and re-export. Run `check_delivery.py` (`pacing` only suggests which segment to check). Deliver MP4, a reproducible project, and a few previews; state clearly which items passed automated checks, which were actually watched/listened to, and which remain unverified. For publishing, create 3:4 / 4:3 / 16:9 covers per [cover](references/cover.md); if the user hasn't mentioned it, ask with a single sentence. For historical issues, consult [case study](references/case-study.md).

## Hard constraints

- **Real features.** A production film must have at least one traceable claim; record release status, source, and a plain-language explanation for each. Demo data may be fixed, but feature behavior and numbers must have evidence. Scope and platform follow `plan.scope`; at delivery, declare which platform surfaces are not covered so the audience does not assume the film represents the entire product.
- **Real components, video scale.** Feature shots connect to actual business components with original styles and states; interface body text must be ≥ 22px (1080p) in the final film. Abstraction is used only for framing, layout, and outer animation. When a platform genuinely cannot be connected, document the obstacle and the substitute approach, respecting existing authorization.
- **Direction first, code second.** A production film must have `DIRECTION.md`: the chosen direction and reasoning, product-derived visual devices, frame design system, and shot list.
- **No templates.** Every visual device must be traceable to a specific product attribute. Case studies and fx-lab are derivation examples, not style packs; when making consecutive films in the same workspace, do not reuse the previous film's opening, chapter, or background devices verbatim. Within a film, also avoid giving all elements the same entrance or the same transition.
- **Clear typography.** Promo titles default to one English span and one Chinese span, each with its own font; Chinese uses sans-serif. Chinese copy states the object, action, and result. Fonts inside the product keep their original design; user-specified language/font takes priority.
- **First frame is a complete image.** When no separate cover is uploaded, platforms like X / Threads grab the first frame as the thumbnail. Therefore the first 5–10 frames of the film must show a complete image, typically the finished state of the opening segment; then fade out and let the opening animation play normally. The first frame must not be a blank background or a waiting-to-animate backdrop. `check_delivery.py` tests the first 5 frames.
- **Complete sound.** Default music and individual action SFX both go into the audio track; key feedback is audible and synchronized with visuals. When the user requests silence or omits SFX, record `audioExceptionReason`.
- **Isolated project.** Source code adaptation, display dependencies, and build config go in the video project; the original product code and dependencies are untouched.
- **Licensing and honest QA.** Assets retain their source and license. The fallback style is governed by the [BSL license](assets/fallback/SOURCE.md). Automated checks only prove structural and file consistency; visual, semantic, and auditory quality depend on actual review — if no listening test was performed, state so honestly.

## Tool entry points

Confirm the style first, then initialize; all three styles accept `--repo`, which is required for repo/hybrid:

```sh
python3 <skill-dir>/scripts/init_project.py --output <video-dir> --style repo --repo <repo-dir>
python3 <skill-dir>/scripts/check_environment.py --project <video-dir> --engine browser
# Missing items → install per references/onboarding.md → re-check with --force.
```

Use `--engine hyperframes` for HyperFrames projects. A new project includes a 10-second technical demo (deliberately unstyled, only to verify the pipeline) and a `DIRECTION.md` containing only questions.

- [Film direction](references/direction.md): reference deconstruction, product character, three directions with differentiation axes, product-specific device derivation, anti-repetition, frame design system, shot list.
- [Visual device vocabulary](references/visual-vocabulary.md): devices grouped by function, stating what they express, where they are derived from, how to implement them, and when not to use them.
- [Starter project](references/starter.md): runtime structure (seek, GSAP main timeline, onRender, onDrive), repo connection, style chain, plan fields.
- [Review](references/review.md): three review checkpoints, contact sheet and transition strips, common-issue reference table.
- [Cover](references/cover.md): layout approach for 3:4 / 4:3 / 16:9 ratios, image selection, copy, and export (`cover.mjs` in the starter project).
- `assets/fx-lab/`: adaptable examples — flow fields, particle convergence, character fields, glowing horizon, slices, orbiting elements.
- `assets/audio/score-example-keys.py`, `score-example-cinematic.py`: two code-synthesized score examples with different character; borrow techniques, do not copy the music verbatim.
- [Bundled SFX](assets/audio/SOURCE.md): 11 original WAV files; when timbre changes are needed, run `scripts/make_sfx.py --output <new-sfx-dir>`.
- `scripts/sfx_landmarks.py <files>`: measure attack point, peak time, and peak level of SFX.
- `scripts/mix_audio.py <plan.json>`: mixing, music ducking, separate audio tracks, and evidence report.
- `scripts/check_delivery.py <plan.json> [--video <final.mp4>] [--mix-report <audio-mix.json>]`: structure, files, timeline, direction file, media, and visual pacing hints.
- `python3 -m unittest discover -s <skill-dir>/tests` and `node <skill-dir>/tests/integration.mjs --modules <video-dir>/node_modules`: run when maintaining this skill; daily film production does not require reading test source code.


# Guizang product video skill

**Software updated — time to make the promo video too.**

[![GitHub stars](https://img.shields.io/github/stars/mamjed/guizang-product-video-skill-en?style=flat-square)](https://github.com/mamjed/guizang-product-video-skill-en/stargazers)
[![License](https://img.shields.io/github/license/mamjed/guizang-product-video-skill-en?style=flat-square)](LICENSE)
![Agent Skill](https://img.shields.io/badge/Agent-Skill-252525?style=flat-square)
![Claude Code](https://img.shields.io/badge/Claude-Code-D97757?style=flat-square)
![Codex](https://img.shields.io/badge/Codex-supported-252525?style=flat-square)

Hand your codebase to an AI, tell it what changed in this update or that you want to introduce the whole product, and start making a promo video: organize selling points, write copy, connect real components, animate, compose a score, add sound effects, then export the video and a project you can keep editing.

I distilled the workflow I refined while making CodePilot promo videos into this skill. The focus is three things: **it looks like your product, people understand what you're saying, and it doesn't feel sluggish when it's over.**

![Guizang product video skill: software updated — where's the promo video?](assets/readme/hero.jpg)

<!-- Paste the video attachment URL uploaded to GitHub here. The intro video is not distributed with the skill package. -->

## Start in 30 seconds

Install in the terminal:

```bash
npx skills add https://github.com/mamjed/guizang-product-video-skill-en --skill guizang-product-video-skill
```

Then open your product codebase and tell your AI coding tool that supports skills:

> Use guizang-product-video-skill to make a promo video from the major updates in this project over the last three weeks. Landscape, 45–60 seconds, Chinese. First look at the codebase's own components and design style, show me a few key frames, then continue with animation and sound.

Or send the repo URL directly:

> Install this skill for me: https://github.com/mamjed/guizang-product-video-skill-en, then use it to make a release update promo video for the current project.

First use checks Node.js, Python, FFmpeg, and rendering dependencies; installs whatever is missing via the official method. System software installation still follows your tool and system permission settings.

## What can it do for you?

| What you have | What it does with it |
| --- | --- |
| Recent commits, release notes | Finds changes worth presenting, organizes them into selling points the audience can understand |
| The software's components and pages | Prioritizes connecting real components with original styles and demo states, then drives animation with code |
| An existing design system | Keeps the product's colors, fonts, border radius, layers, and interaction language |
| No mature promo visuals yet | Uses the bundled CodePilot warm-white / charcoal-black style to organize outer visuals |
| A few very technical update descriptions | Rewrites them as complete plain-language sentences so people know what changed and how it feels to use |
| A video with only visuals | Writes a code-synthesized score for the film, adds individual action SFX, and ducks the music when key sounds play |

Visuals are rendered by code and can keep being edited. Titles, feature close-ups, full workspace shots, and detail shots alternate — there's large copy and also time to see what's happening.

![Real components and bilingual typography](assets/readme/components.jpg)

## Three styles — pick what fits

On the first film, the AI confirms the style first. Choices already made carry over; you don't need to answer every time.

| Mode | When to use it |
| --- | --- |
| **Use product style `repo`** · recommended | The product already has a complete design; you want the promo to look like your software at a glance |
| **Fallback style `default`** | You want to start with CodePilot's warm-white, charcoal-black, card layers, and bilingual typography |
| **Hybrid `hybrid`** | Keep the real interface inside the software; make the outer copy, framing, and pacing more shareable |

All three modes use real product components for feature shots. The fallback style handles outer layout and visual packaging; when a platform or framework limits connection, it explains why and what the substitute is.

English titles and Chinese descriptions specify fonts separately. English handles rhythm and typography; Chinese makes things clear; you can also request all-Chinese or all-English directly.

## How to brief it for a good first pass?

You don't need a long brief — just say **what to introduce, who it's for, and where it goes**.

**Make a release update video**

> Introduce the major updates from v2.1 to v2.4, prioritizing multi-model switching, file preview, and browser actions. Post to Bilibili, landscape, about 50 seconds. Use our product design; keep the copy conversational, don't just read out commit messages one by one.

**For overseas users**

> Make an English changelog promo, 45 seconds, mainly for first-time users. Explain what problems these updates solve first, then show the actions. Keep the original product components and fonts.

**See the direction before the full film**

> First organize selling points, storyboard, and four real-rendered key frames. Use the default CodePilot style, Chinese with English titles, wait for my confirmation before doing the full animation.

**Modify an existing film**

> The model selection segment is too slow, compress it to three seconds. Add a clear ding-dong sound when the notification appears, and duck the music. At the end, remove the website URL and cover any place in the browser where a link is visible.

You don't need to fill in everything at once; existing context carries over — it only asks about what's missing and affects production.

## From codebase to finished film

1. **Set the scope first.** Confirm the product, update range, audience, distribution platform, aspect ratio, language, and style; share reference videos if you have them.
2. **Find real content.** Check versions and code, verify feature status, mount real components, and scale them up for video.
3. **Set direction first.** Deconstruct references, distill product character, propose three clearly different directions and pick one; every visual device must answer "because the product has what"; write font sizes, interface scale multiples, and the shot list as concrete numbers before building.
4. **Build shot by shot.** GSAP main timeline arranges animation; Three.js / canvas handles the background layer; real components use real clicks and inputs to drive them; produce a still frame after each shot for comparison.
5. **Get the sound right.** Arrange the score from the storyboard, choose timbre from the product character; use recorded samples for SFX first, measure hit points, align to actions, mix, and handle music ducking.
6. **Review, then export.** Check the contact sheet, check every transition, check full-size frames for information-dense shots; fix and re-export.
7. **Make a cover if needed.** 3:4, 4:3, 16:9 — the visual language follows this film; only use frames actually rendered in the project.

Each film's devices are derived from the product itself, not from the same template: the same workflow should produce completely different films for a note-taking app vs. a developer tool.

## Same workflow, three different films

The three films below use the same workflow but look and sound completely different: each one first answers "what does this product have" then decides "so how do we present it visually."

| Product | What we found in the product | So the film does this | Sound |
| --- | --- | --- | --- |
| **CodePilot** (desktop AI coding client) | Connects to multiple model providers; dark, textured desktop app | Dark stage with silver-white light arcs; particles form the logo; providers orbit the product; kanban flyover | 120 BPM cinematic electronic |
| **Zed** (multiplayer code editor) | The editor itself is the star; teammate cursors appear in real time | Light-colored single take, the camera moves through the editor the whole time; titles are typed-out code comments; teammate cursors lead, then draw the logo | 128 BPM marimba percussion |
| **T3 Code** (open-source coding agent console) | Positioned as a "control plane"; ships with 5 built-in themes; each harness has its own login command | The entire film is a 3×3 console panel; the camera pushes into whichever card to enter that chapter; each chapter switches to a different built-in product theme; five terminals type five login commands at the opening, then get absorbed into the panel | 96 BPM lo-fi electric piano |

When making consecutive films in the same workspace, the opening, transitions, and background devices also change from the previous film.

The default starting point is **45–60 seconds, landscape, Chinese**. You can adjust duration and aspect ratio; portrait needs different framing and text layout — it usually doesn't just crop the sides.

## Where does the music and sound come from?

**Music is chosen in order: the track you provide → a music generation model that actually runs locally → code-synthesized original.** Code synthesis keeps the source code, arranges sections by this film's shot boundaries, and chooses timbre by product character. The repo has two character examples (bright keyboard, cinematic electronic) — borrow the techniques, not the music.

**SFX: find suitable ones first, then use bundled assets to fill gaps.** First search available asset libraries and record source, license, and suitable actions; for categories with no suitable asset, use the 11 code-synthesized WAV files included, or adjust synthesis parameters.

**Music and SFX mix separately.** Clicks, pop-ups, toggles, completion alerts — each has its own sound cue event. When key feedback plays, the music briefly ducks so the ding, confirmation, and transition sounds are actually audible.

![Score, action SFX, and music ducking](assets/readme/audio.jpg)

## What do you get at the end?

- A publishable **MP4**.
- A **video project** you can keep editing and re-rendering.
- A few key frames for confirming direction or making covers later.
- Component sources, asset sources, sound cue events, and check records for future reference and adjustments.

Automated checks catch some structure, file, and timeline issues; whether the copy is clear, the visuals are comfortable, and the sound is right still requires actually watching and listening. The project distinguishes what has been verified from what still has limitations.

## Install and update

### Install with the skills CLI

```bash
npx skills add https://github.com/mamjed/guizang-product-video-skill-en --skill guizang-product-video-skill
```

Follow the prompts to choose your AI tool and install scope. To update, ask the AI to check this repo and update the installed skill; if you've changed files locally, keep your changes first.

### Manual install

**Codex:**

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/mamjed/guizang-product-video-skill-en.git \
  ~/.agents/skills/guizang-product-video-skill
```

**Claude Code:**

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/mamjed/guizang-product-video-skill-en.git \
  ~/.claude/skills/guizang-product-video-skill
```

Install directories follow the [Codex official docs](https://learn.chatgpt.com/docs/customization/overview#skills) and [Claude Code official docs](https://code.claude.com/docs/en/skills#choose-where-skills-load). The universal install command above uses the [skills CLI](https://github.com/vercel-labs/skills).

Reopen the session so the tool reads the newly installed skill. When cloned manually without local changes, run `git pull --ff-only` in the install directory to update.

You can also download the repo ZIP, extract it, and put the folder containing `SKILL.md` into the corresponding skills directory, naming the folder `guizang-product-video-skill`.

## What environment is needed?

The bundled starter project uses React, esbuild, and Playwright for visuals, then FFmpeg for encoding. Existing HyperFrames projects can also be reused.

| Dependency | Purpose |
| --- | --- |
| Node.js ≥ 22, npm | Build components, run browser rendering tools |
| Python ≥ 3.9 | Project initialization, environment check, score and mix scripts |
| FFmpeg / ffprobe | Audio processing, video encoding, file inspection |
| Playwright Chromium | Still-frame and frame-by-frame rendering in the built-in browser pipeline (WebGL via SwiftShader) |
| React, GSAP, Three.js | Mount real components, main timeline animation, background effect layers (installed in the video project) |
| Product repo and its dependencies | Connect real components and styles directly |

Dependency installation instructions load on demand; see [onboarding and dependency check](references/onboarding.md). No extra video service purchase is needed for the built-in browser pipeline; the AI coding tool itself and any external services you choose follow their own rules.

Different component frameworks require different connection effort. React codebases have ready examples; monorepo workspace packages and special TypeScript compiler options can be mapped and relaxed in the video project's `integration.config.mjs` without changing product code. Components that need a server, native runtime, or complex context may still need a display adaptation layer; interfaces that truly cannot be connected are faithfully rebuilt from source and marked item by item in the evidence.

## What's in the repo?

```text
LICENSE                  GNU AGPL-3.0 main license
COMMERCIAL_LICENSING.md   Separate commercial licensing entry point
SKILL.md                 Workflow, hard constraints, and tool entry points
agents/                  Codex display information
references/              Film direction, visual device vocabulary, component connection, storyboard copy, audio, review, cover, onboarding, and acceptance methods
scripts/                 Initialization, environment check, SFX hit-point measurement, SFX synthesis, mixing, delivery check
assets/starter/          Runnable starter project (technical foundation, no style)
assets/fx-lab/           Adaptable visual device examples (flow fields, particle convergence, character fields, horizon, slices, orbit)
assets/fallback/         CodePilot fallback style and display components
assets/audio/            Two character score synthesis examples, 11 bundled SFX with source documentation
assets/readme/           Intro video frames used on this page
tests/                   Script regression tests and component connection tests
```

When maintaining this skill, run:

```bash
python3 -m unittest discover -s tests
node tests/integration.mjs --modules <some-video-project>/node_modules
```

For connection and rendering details, see [starter project](references/starter.md); for the full production entry point, see [SKILL.md](SKILL.md).

## FAQ

**Can it only make videos for CodePilot?**

It works for other software. CodePilot provides the fallback style and a case study of this workflow; normal use prioritizes connecting your own product components.

**Does it generate a video with a model?**

The main visuals are rendered by code, components, and a timeline; the score is also code-synthesized. You can keep editing text, layout, duration, animation, and sound, then re-export.

**Can I just give it a repo URL and get a video?**

Sometimes you still need to download the repo, install dependencies, and confirm demo state. It's a production workflow that lets the AI complete the work step by step, not a one-click converter that ignores the project environment.

**Can the fallback style be used commercially?**

Components and styles adapted from CodePilot in the fallback style retain their original BSL license; read the [source documentation](assets/fallback/SOURCE.md) and [LICENSE.CodePilot](assets/fallback/LICENSE.CodePilot) before use to determine applicability. The fallback style is not re-licensed as MIT here.

**Can I use my own music, logo, or reference video?**

Yes — give the assets and requirements to the AI. Reference videos are used to understand rhythm and expression; introduced assets need an applicable usage license, and sources must be retained.

## Feedback and improvements

Share your work, issues, and improvement suggestions on [Issues](https://github.com/mamjed/guizang-product-video-skill-en/issues). When reporting, include the AI tool used, product tech stack, failure stage, and redacted logs or frames.

If you also want AI to help with image and text content, check out the [Guizang social media card skill](https://github.com/op7418/guizang-social-card-skill).

## License

GNU AGPL-3.0 © 2026 [op7418](https://github.com/op7418)

Except for content explicitly separately licensed below, the workflow, documentation, scripts, starter project, and original audio assets in this repository use **GNU AGPL-3.0**; see [LICENSE](LICENSE) for full terms.

- Preserve copyright, license, and relevant notices when copying or distributing; describe changes when publishing a modified version.
- When distributing modified versions or derivative programs under this license, comply with AGPL-3.0 requirements for licensing and corresponding source code.
- When a modified program supports remote network interaction, provide users interacting with it a way to freely obtain the corresponding source code of that version per Section 13.
- AGPL-3.0 allows commercial use and paid distribution; charging does not exempt you from applicable license and source-provision obligations.

**Separately licensed content:** Components and styles adapted from CodePilot in [assets/fallback/](assets/fallback/SOURCE.md) continue to use the [Business Source License 1.1](assets/fallback/LICENSE.CodePilot), including its Additional Use Grant and Change Date. They do not change to AGPL because of the main license. When using, modifying, or distributing projects containing these components, you must also check the relevant terms; you cannot claim the combined work is solely under AGPL or unrestricted for commercial use.

Connected product components, logos, fonts, third-party music, or sound effects are used under their respective applicable licenses. Generated videos also do not automatically become AGPL works solely because this tool was used; if the output contains protected components, assets, or code, their applicable terms must still be retained and followed.

For closed-source integration, white-labeling, platform built-in, distribution partnership, or separate licensing not covered by AGPL, see [commercial licensing](COMMERCIAL_LICENSING.md). This section is a reading guide; specific rights and obligations are governed by the applicable license or a written agreement between the parties.


# Guizang product video skill — commercial licensing

This project uses GNU AGPL-3.0 as its main license; the CodePilot fallback style has a separate BSL license; see the [README](README.md#license) for scope.

Commercial use that complies with the applicable open-source license does not need a separate commercial license just because it charges money. If you want closed-source integration, white-labeling, additional support, or licensing terms different from the public license, you can negotiate a separate written agreement with the author.

## Partnership models

Following the [Guizang Skill Series commercial licensing framework](https://github.com/op7418/guizang-social-card-skill/blob/main/COMMERCIAL_LICENSING.md), the following models can be discussed:

- **Deep built-in licensing**: Integrate the software promo video capability into your own product; negotiate product adaptation, effect optimization, attribution, and white-label scope.
- **Distribution and visibility partnership**: List on agent, plugin, or workflow platforms; negotiate support scope, brand visibility, and version update arrangements.
- **Revenue sharing**: For platforms charging per-use, points, or subscription; negotiate billing metrics, usage data, and settlement terms.

Specific fees, product lines, term, support content, whether the CodePilot fallback style is included, attribution, and sublicense scope are governed by the final signed agreement between the parties; reference project pricing does not automatically constitute a quote for this project.

## How to contact

Contact the author through [Guizang's X profile](https://x.com/op7418) and include:

1. Product or platform name, integration method, and target users.
2. Expected usage volume, pricing model, and desired launch timeline.
3. Whether closed-source, white-label, fallback style, or custom adaptation is needed.

This document provides a partnership entry point; it does not replace the [LICENSE](LICENSE) and does not additionally restrict rights already obtained under the applicable license. Commercial licensing cannot substitute for the separate licenses that third-party components, fonts, sound effects, and brand assets may each require.
