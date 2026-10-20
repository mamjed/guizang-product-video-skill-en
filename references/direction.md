# Film Direction: Define Direction First, Then Write Code

What determines whether a film looks good is the design work done before writing code: what it says, what mood it carries, what each shot's subject is, how large the type is, how many times the interface is zoomed. Write all of this into `DIRECTION.md` (the question template is generated during initialization) before touching any code.

Two comparisons illustrate the weight of this step: a version built only from checklists and metrics hit 100% beat alignment but looked cramped, had tiny type, and resembled a slideshow; a version that started with a visual spec and shot list — same product, same components — looked completely different (see [case study](case-study.md)).

## 1. Deconstruct References (When the User Provides Reference Videos/Images)

1. Extract frames for the full film: `ffmpeg -i ref.mp4 -vf "fps=1,scale=400:-1,tile=6x8" -frames:v 1 sheet.png`, then capture full-size frames for key moments.
2. List each device one by one: what it is, what it expresses (speed? order? connection?), where in the film it appears, how long it lasts.
3. Learn the "method," don't copy the "look": the reference film's colors, shapes, and typeface belong to its brand. State clearly whether this film adopts them, how they are adapted, and the rationale for the adaptation.

## 2. Distill Product Character

Answer from the repo and user input — don't guess:

- **Who uses it, in what context, how does it feel to use**: calm and professional, light, warm, hardcore, quiet…
- **Design language**: color palette, typefaces, border radius, shadows, light/dark themes (if the product has a dark theme, include it as a candidate), icon style. Cite file paths as sources.
- **Motif candidates**: product elements that can be turned directly into visuals.
  - Logo geometry (dot grid, lines, letterforms)
  - The core interface itself (input fields, lists, canvas, timeline)
  - Data shapes the product handles (text streams, charts, file trees, waveforms, maps)
  - Domain metaphors (writing → paper and ink; design → construction lines and control points; music → waveforms; finance → trend lines)
  - Literal imagery from the product name

## 3. Propose Three Directions, Spread Across Different Axes

Each direction picks one option per axis in the table below. They must differ on **at least three axes** from each other, and each must be internally consistent. Options are examples only — add your own:

| Axis | Example Options |
|---|---|
| Base color & light | Black stage + glow; paper white + ink lines; large brand-color blocks; alternating light/dark; real-environment photo feel |
| Typeface voice | Ultra-thin large type; heavy impact; serif editorial; monospace technical; rounded friendly |
| Motif source | Logo geometry; the interface itself; data shapes; domain metaphors; user scenarios |
| Shot language | Flat editorial layout; 3D stage (tilt, orbit, flyover); macro close-up; single continuous take; screen-recording texture |
| Transition vocabulary | Hard cut on beat; zoom-through; mask wipe; shape morph; match cut (element from one shot becomes element in the next) |
| Pacing | Keynote-leisurely; trailer-tight; playful; quiet narrative |
| Sound | Electronic pulses; piano and strings; percussion-led; ambient pad; user-provided music |

Then pick one based on product character, audience, and distribution platform, and write down the reason. When the user wants to see directions first, present the three directions with 3–6 key still frames for selection; otherwise continue directly.

## 4. Film-Specific Devices (3–5)

Every device must be writable as "because the product has X, we use Y." If you can't write the X, delete the device.

Some derivation examples (illustrating the method, not a menu):

| What the Product Has | What It Can Become |
|---|---|
| A logo built from a dot grid | Particles converge from afar, landing in each cell of the grid |
| Many service/plugin integrations | Members orbit around the core interface on a tilted plane |
| Developer-facing, code as material | A character field composed of the product's own code |
| A note-taking/writing product | Characters written stroke by stroke, paper texture, ink bleeding |
| A data analytics product | Real chart paths drawn segment by segment, numbers rolling to rest |
| A design tool | Construction lines, control points, grid snapping |
| A collaboration product | Multiple cursors entering simultaneously, states merging in real time |

[Visual Device Vocabulary](visual-vocabulary.md) lists more devices and their implementation notes; `assets/fx-lab/` has several adaptable examples.

## 5. Anti-Repetition

- **Across films**: Before starting, look at films made previously in the same workspace with this skill (adjacent directories' `DIRECTION.md`, `evidence/contact-sheet.png`) and the [case study](case-study.md). List their openings, chapter treatments, background devices, and score. The new film must differ on at least three axes from the most recent one, and must not reuse its opening device, chapter device, or background effect verbatim.
- **Within a film**: Don't give every element the same entrance. Alternate adjacent shots between framing (wide ↔ close-up ↔ large type) or light/dark. Don't use the same transition more than three times in a row.
- **Case studies are not templates**: The CodePilot film's starfield opening, silver-white light arcs, and Ask/Switch/Extend chapter title cards belong to that product and that derivation. Another product copying them directly produces sameness.

## 6. Narrative Structure, Chosen by Content

The default "hook → brand → feature proof ×3–5 → quick-cut small features → closing" is just one option. Alternatives:

- Problem → turning point → solution (fits updates that solve a clear pain point)
- Completing one real task end to end (fits agent/workflow products)
- A single continuous take through the product's areas (fits spatial interfaces)
- Before/after comparison (fits performance, redesigns)
- Countdown list (fits many small updates)
- A day of use (fits daily tools)

## 7. Frame Design System

Derive from the product, write as concrete numbers:

- Aspect ratio, frame rate, base color, safe area (keep important content clear of the bottom ~13%).
- Type scale: main title, subtitle, description — give font size and weight separately for Chinese and English; typefaces come from the product or licensed fonts, specified separately for Chinese and English.
- Interface on-camera zoom: ensure body text in the interface renders at ≥ 22px in the final film (1080p). Zoom ≈ 22 ÷ product body-text pixel size. Full window views serve only as establishing shots for context.
- Light/dark theme: when the product has a dark theme and the film goes dark, use the product's dark theme directly.
- Motion grammar: entrance methods, easing families, duration ranges, and what this film **does not** use (e.g., "no bounce-back," "no rainbow colors").

## 8. Shot List

For each shot, write: time, subject (only one), visuals and action (with sub-shot timing), on-screen copy, sound. Each shot must contain at least one state change or camera movement; if it's completely still for more than 2.5 seconds, it can only be giving the audience time to read. Shot lengths should vary: opening and quick cuts are short, feature proofs are longer.

Finish the shot list before building any shots. After building each shot, produce a still frame and cross-check it against the shot list (see [review](review.md)).
