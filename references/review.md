# Review: Watch as You Build, Then Watch the Final Film

Automated checks prove only that structure and files are correct. Whether it looks good requires watching the picture — this page covers how to watch efficiently and recurring issues that surface during actual production.

## Three Checkpoints

1. **After building each shot**: `node stills.mjs evidence/stills <3–4 moments within this shot>`, compare still frames against the shot table in `DIRECTION.md`: is the protagonist immediately obvious? Is the font size large enough? Is anything overlapping? `stills.mjs` also prints page errors and API paths actually requested by components — missing fixtures can be caught here.
2. **After the first full export**:
   - 2 fps contact sheet for rhythm and composition: `ffmpeg -i final.mp4 -vf "fps=2,scale=384:-1,tile=6x9" -frames:v 1 sheet.png` (one sheet per half).
   - 10 fps strip for each transition: `ffmpeg -ss <0.4s before cut> -t 1 -i final.mp4 -vf "fps=10,scale=320:-1,tile=10x1" -frames:v 1 cut.png`.
   - Full-size frames for information-dense shots to confirm UI text is legible.
3. **After modifications**: re-watch only the changed shot and its surrounding transitions, then do one final full pass.

## Common Issues

| What you see | Typical cause | Fix |
|---|---|---|
| Title and UI overlap, text crammed in corner | No type scale or safe area, or title column too narrow | Go back to the frame design system; give the title column a fixed width and font size; shorten copy instead of shrinking font |
| Last Chinese character or punctuation drops alone to the next line | Text width exceeds by just a bit | Shorten by a word or two, or adjust column width; do not rely on `nowrap` to let text overflow |
| UI on camera shows tiny text, panels have large blank areas | Product shown at desktop size; panel height set for fullscreen | Scale up the product root node; fit panel height to content; tighten blank areas |
| Zoom landing point is off | Manually calculating landing point under 3D tilt/perspective | Use `screenCenterAt` to measure the real screen position at the corresponding moment |
| Shot targets the wrong row, or targets the top of the frame | When matching text to find the target row, matched an earlier similar row, or searched before that row finished typing | Search only after the row appears completely; use a unique marker (e.g. status field) to find the row; if not found, report an error directly — do not let −1 become coordinates |
| Gray flash when cutting from light to dark | Long crossfade | Hard cut, or blur-out the previous shot's protagonist before cutting |
| Overlay position broken, cannot follow zoom | Portal mounted on body; panel is in 3D rotation when opening | Point the portal container inside the shot; no 3D rotation during opening |
| 3+ seconds of complete stillness | No follow-up after the last action | Add a slow push-in or state continuation (e.g. new message arriving), or shorten the shot |
| All elements use the same entrance | Only one reveal type used | Design separate entrances for protagonist, supporting info, and background; vary between adjacent shots |
| First frame is blank background color; social platform thumbnail is all white or all black | Opening starts from blank canvas, first frame has nothing yet | Show the opening's completed state as the poster frame for the first 5–10 frames, then fade out and enter normally; `check_delivery.py`'s `firstFrames` reports blank frames |
| Every film looks the same | Directly reusing the case study or previous film's techniques | Go back to sections 3–5 of `DIRECTION.md`, re-derive from the product |
| Background effect steals focus from the UI | Atmosphere layer contrast too high, or placed behind a dense UI | Keep backgrounds quiet during feature shots; save effects for title cards, brand, and transitions |

## Metrics Are Only Hints

`check_delivery.py --video` reports still-frame ratio, longest still segment, and hard-cut count (`pacing`). These are meant to prompt "go look at that section": reading pauses are necessary, and small motion on large dark backgrounds also counts as "still." **Do not add meaningless motion to improve the numbers, and do not treat hitting the numbers as the film looking good.**

## Sound

- When playback is possible, listen section by section: `sfx-stem.wav` alone, then the master, then the encoded MP4.
- When playback is not possible, state this honestly and verify structure with visible evidence: spectrogram (`ffmpeg -i music.wav -lavfi showspectrumpic=s=1600x500:scale=log:fscale=log music-spec.png`) and per-second loudness to confirm impact points, pauses, builds, and cadences land at the right times. Whether bass is too heavy is obvious on the spectrogram.
