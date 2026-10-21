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

> Use guizang-product-video-skill to make a promo video from the major updates in this project over the last three weeks. Landscape, 45–60 seconds, English. First look at the codebase's own components and design style, show me a few key frames, then continue with animation and sound.

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

Titles and descriptions specify fonts separately. The headline font handles rhythm and typography; the body font keeps things clear. You can also request a single font for everything or separate fonts for headings and body.

## How to brief it for a good first pass?

You don't need a long brief — just say **what to introduce, who it's for, and where it goes**.

**Make a release update video**

> Introduce the major updates from v2.1 to v2.4, prioritizing multi-model switching, file preview, and browser actions. Post to YouTube, landscape, about 50 seconds. Use our product design; keep the copy conversational, don't just read out commit messages one by one.

**For overseas users**

> Make an English changelog promo, 45 seconds, mainly for first-time users. Explain what problems these updates solve first, then show the actions. Keep the original product components and fonts.

**See the direction before the full film**

> First organize selling points, storyboard, and four real-rendered key frames. Use the default CodePilot style, English copy with bold headlines, wait for my confirmation before doing the full animation.

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

The default starting point is **45–60 seconds, landscape, English**. You can adjust duration and aspect ratio; portrait needs different framing and text layout — it usually doesn't just crop the sides.

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
| Playwright (Chromium or CLI) | Still-frame and frame-by-frame rendering via the built-in browser pipeline or Playwright CLI (WebGL via SwiftShader) |
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
