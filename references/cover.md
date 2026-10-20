# Cover: 3:4, 4:3, 16:9

Only produce when the user is about to publish the film, or explicitly asks for a cover; otherwise ask with one sentence at delivery time. The cover extends the film — its visual language comes from that film's `DIRECTION.md`, not a universal template: a dark-stage film's cover and a light-editor film's cover should look obviously different at a glance.

## Three Aspect Ratios

| Ratio | Design Size (CSS px, export at 2×) | Common Use | Layout Approach |
|---|---|---|---|
| 3:4 | 1080×1440 | Xiaohongshu, WeChat Moments, vertical feeds | Top-to-bottom stack: title on top, hero image in middle, tags and credit at bottom |
| 4:3 | 1440×1080 | X / Threads / WeChat article images | Left-right split: left ~40% for title and tags, right for hero image |
| 16:9 | 1920×1080 | Video platform thumbnails, Bilibili, YouTube | Hero image dominates, title larger with fewer words; avoid the duration badge in the bottom-right and the progress bar area at the bottom |

## Process

1. **Pick the frame.** Use the contact sheet to view the full film first, then select 1 hero image and 0–2 supporting images. Use only frames actually rendered by this film: `node stills.mjs cover/frames <moment…>` produces PNGs — sharper than extracting from MP4.
   - The hero must remain readable when shrunk: large shapes, a clear product interface, a recognizable moment (e.g., CodePilot's service orbit, Zed's cursor drawing the logo).
   - Frames that are mostly pure black or pure white look like empty boards as supporting images — swap them.
2. **Set the copy.**
   - Main title: user's original post wording takes priority; otherwise take the film's core claim. Chinese main title ≤ ~12 characters; can pair with one short English line.
   - One subtitle line. Up to 4 tags.
   - Claims are either the user's own opinion in the user's own words, or sourced from the repo. Comparisons with other products appear on the cover only when the user wrote them, keeping the user's original wording.
3. **Set the design.** Base color, typeface, and motif carry over directly from the film's frame design system: if the film's titles are code comments, the cover title can be a code comment too; if the film uses a glowing horizon, the cover can too. All three ratios share the same element set — reflow only, never just scale proportionally.
4. **Typeset and export.** Write `cover/cover.html` in the video project, one element per ratio, tagged with `data-cover="3x4"`, `"4x3"`, or `"16x9"`, sized per the table above. Reference fonts and images with relative paths (e.g., `../public/fonts/…`, `frames/…`). Then run:

   ```sh
   node cover.mjs            # Outputs covers/cover-3x4.png etc., 2× pixel resolution
   ```

   The script verifies each element's dimensions; it fails directly on page errors or resource load failures.
5. **Thumbnail test.** Shrink each cover to 320px wide and check: is the title still readable? Is the hero still recognizable? In feeds, 3:4 and 4:3 often appear at roughly this size.

## Common Issues

| Symptom | Fix |
|---|---|
| Supporting image almost entirely hidden by hero | Move the supporting image outward — at least one-third visible, showing content |
| Title overlaps hero image | Separate the title zone from the hero zone, or give the title a background color; don't overlay title on interface text |
| Title too small in 16:9 | At thumbnail size, title height should be ≥ 1/8 of frame height; halve the word count |
| Three ratios look like the same image scaled | Reflow per each ratio's layout approach — hero size and position must change |
| Code/monospace text loses spaces (`fnname`, `1//`) | Line container uses `display:flex`, text nodes containing only whitespace are dropped; change lines to block elements with `white-space:pre` |
| Font didn't load (falls back to system font) | Check `@font-face` relative paths; `cover.mjs` waits for `document.fonts.ready` |

Don't make covers that impersonate platform interfaces (fake view counts, fake platform buttons, others' brands). Play icons on the cover must be neutral shapes only.
