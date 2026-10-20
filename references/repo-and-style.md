# Repo & Style Audit

## Update Facts First

Read the repo rules and relevant directory index first, then search targeted areas. Prioritize release notes, changelogs, version tags, and implementation paths; don't bulk-export logs or environment files.

Build `feature-evidence`, each entry containing:

| Field | Meaning |
| --- | --- |
| feature / benefit | What was implemented / what the user gains |
| status / release | Shipped, merged, or in development; which version |
| source | Repo-relative path + commit/tag, or user-provided docs |
| component | Real reusable component and associated styles |
| demoState | Inputs, state, and fixtures needed for the demo |
| limits | What can't be proven or demo scope limitations |

When the user says "recent weeks," use the current date to set the range, then cross-reference with version records; don't use reference tweet dates. When the range isn't settled yet, suggest the last 2–4 weeks and state clearly this is a proposed range.

## Original Component & Design Dependency Audit

Follow feature pages to find actual business components and composition layers first, then read the tokens / CSS variables / Tailwind config, fonts, icons, and theme context they use. Audit output: business components, composition structure, and their complete design dependencies.

Write in `style-audit.md`:

1. Color palette and semantics: background, surface, text, muted text, stroke, accent — with code sources.
2. Typography: separately determine font, weight, line height, and actual loading result for English titles, Chinese titles/body text. Specific font assignment for promo titles follows [shot list & copy](story-and-copy.md).
3. Spacing and shape: base spacing, border radius, shadows, line widths, density.
4. Brand: full app icon / horizontal logo / monochrome version and their applicable contexts; use existing repo assets.
5. Shot adaptation: which UI details can be reused directly, which need zooming, cropping, or splitting; whether the product has a dark theme that can be enabled directly.
6. Motif candidates: logo geometry, core interface, data shapes the product handles, domain metaphors. These are the raw material for deriving film-specific devices in [film direction](direction.md).
7. Decision: repo / default / hybrid — rationale and preserved brand identity points.

"Doesn't look good" must become actionable judgment: hierarchy confusion, inconsistent font sizes/spacing, insufficient contrast, information density too high, messy borders/shadows. Don't treat your own aesthetic preferences as objective conclusions, and don't swap out the user's brand behind their back.

## Scope of the Fallback Style

The fallback style is extracted/adapted from CodePilot's CardFrame / CardSurface, rounded buttons, tags, and visual tokens. It provides the frame container and typographic foundation; it does not include business features like model lists or browsers, nor does it provide another product's brand.

- `default`: visual tone used for promo title cards, backgrounds, and outer containers; feature shots prefer keeping original business components and their internal styles. Only when the user explicitly requests re-skinning, handle it within that scope.
- `hybrid`: borrows only the frame packaging; the target product's key interfaces, brand colors, and states remain recognizable.
- `repo`: produced from the product design audit results.

Don't copy real conversations, accounts, keys, browsing history, or business data from the user's repo into a shareable project. Fixtures should express real functionality but not impersonate real performance/customer results.
