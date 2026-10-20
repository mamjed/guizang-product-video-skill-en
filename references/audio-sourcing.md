# Score & SFX: Sourcing, Arrangement & Synchronization

## Where the Music Comes From (in order of preference)

1. **User-provided track**, or a licensed library the user has rights to: use it directly. Re-align cut points to its actual beat grid, recording beats via `audio.beatGrid`.
2. **A music generation model actually available locally**: confirm the model weights are truly on disk and the runtime (e.g. torch) is installed before using it. A config-file cache alone does not count as "available." After generation, verify sections against the shot list as usual; splice or layer impacts and risers as needed.
3. **Code-original synthesis** (default fallback): write a synthesis script for this film, keep the source and a fixed random seed so re-running produces the same piece.

Do not download a BGM of unknown provenance, do not rip music from reference videos, and do not rename a demo track and call it a new score. Honor the user's request for silence and record `audioExceptionReason`.

## Code-Original: Arrange First, Then Synthesize

**Arrange from the shot list**: open the shot table in `DIRECTION.md`, write out what the music must do for each section, taking times directly from `plan.json` shot boundaries:

- Does the opening build, create suspense, or drop straight into rhythm?
- Do brand reveals, section transitions, and the end-card need impact hits? Leave a brief silence before the hit?
- Sections with on-screen text or UI walkthroughs must make space: fewer instruments, melody recedes.
- Fast-cut sections tighten rhythm or add risers; the ending has a full harmonic cadence with tail room matching the film length.

**Timbre from product character**: the "voice" axis in [Film Direction](direction.md) sets the type first, then instrumentation — not electronic music every time:

| Character | Possible instrumentation & techniques |
|---|---|
| Calm, premium, technical | Wide supersaw pad, pluck arpeggios, sidechained kick, sub-bass impact |
| Light, friendly | Bright keyboard chords, short melodic motifs, handclaps, marimba-like tones |
| Warm, humanistic | Piano or plucked strings lead, slow tempo, long reverb, minimal percussion |
| Powerful, tight | Percussion-led, bass pulses, dense risers, syncopated rhythm |
| Quiet, focused | Ambient pad, sparse bell tones, almost no drums |

**Two examples** — study the synthesis techniques, do not copy the pieces:

- `assets/audio/score-example-keys.py`: D major, keyboard chords, short melodic motifs, light drums — stdlib + FFmpeg only.
- `assets/audio/score-example-cinematic.py`: F minor, supersaw pad (with filter sweep), harmonic-decay pluck, pitch-dropping kick, noise-based claps and hi-hats, sidechain compression, dotted-eighth delay, noise-sweep riser, sub-bass impact, convolution reverb. Requires numpy/scipy/soundfile in the project's own venv.

**Synthesis key points**:

- Synthesize per bus (drums, bass, pad, arpeggio, effects), then mix. Each bus needs independent envelope, panning, and level control.
- Express all timings in beats and bars. When film length or tempo changes, shift all section times together and check that tails do not overrun.
- Do not bake UI clicks or alert tones into the score — those are independent SFX that need separate synchronization and separate ducking later.
- After export, inspect the spectrogram and per-second loudness (see [Review](review.md)) to confirm section structure and bass weight. Excessive bass is the most common problem with synthesized scores.

## SFX: Find Recorded Samples First, Fill Gaps with Bundled SFX

1. **User-owned, clearly sourced sample library.**
2. **Locally installed recorded sample library**: e.g. the Pixabay SFX bundled with the media-use skill (clicks, key taps, typing, pops, notifications, dings, whooshes, glitches, sub-bass impacts, etc.). Read its `CREDITS.md` for licensing and record it in the project.
3. **Sample-site search**: e.g. [Pixabay Sound Effects](https://pixabay.com/sound-effects/). Download links must come from real download operations — never fabricate CDN URLs. When a site requires interactive download and current tools cannot retrieve the file, record this honestly and fall through to the next option.
4. **Skill bundled SFX** (`assets/audio/sfx/`, 11 original WAVs): fill only the missing category. Bundled SFX are inherently quiet (peak ≈ −20 dBFS); set gain based on measured peak levels.

| On-screen action | Suitable sound | Selection focus |
|---|---|---|
| Click, select | Short, clear UI click | Not harsh, clean onset |
| Pop, appear | Pop, light toggle | Lightweight, conveys state feedback |
| Typing | Short keyboard burst | Matches on-screen typing rhythm |
| Notification, complete | Two-tone chime, confirmation ding | Recognizable, tail not too long |
| Structural change | Whoosh, glitch | Only for real section changes, not every element |
| Impact, end-card | Sub-bass impact | Layer with or alternate against the score's impact hit — do not clash |

## Synchronization: Land Sounds on the Action

Use `scripts/sfx_landmarks.py` to measure each file's onset, peak time, and peak level:

```sh
python3 <skill-dir>/scripts/sfx_landmarks.py assets/sfx/*
```

- Clicks, key taps, pops: align using the **onset** to the on-screen action.
- Whooshes, impacts, risers: align using the **peak** to the cut point or impact frame — the sound should start before the visual.
- Write into the plan: `syncOffset` = the landing point used, `at` = action time − `syncOffset`.
- Gain: ensure the SFX peak at its onset is no lower than the ducked music peak. Recorded samples sit near 0 dBFS; bundled SFX sit near −20 dBFS — the same gain value sounds very different.

## Record the Provenance

`evidence/audio-selection.json` records:

- `music`: source (user-provided / generation model + model name / `code-original` + script path), duration, BPM, key, section times.
- `sfx[]`: each file's role, source (library name, detail page, or author), license, local path. When falling back to bundled SFX, state the actual reason, e.g. "sample site requires interactive download, current tools cannot retrieve the file." If unknown, write unknown — do not fabricate a search history.

Downloading samples for a finished film and repackaging raw recordings into a redistributable sample library are two different things. This skill does not bundle third-party recordings; samples used in the project follow their existing licenses.

Finally, mix per [Audio Mix & Delivery QA](audio-and-qa.md).


# Audio & Delivery QA

## Score & SFX

First complete sourcing per [Score Creation & SFX Lookup](audio-sourcing.md): music defaults to code-original; SFX starts with recorded samples matching the product/action, filling only missing categories with bundled SFX. Lock down the music character, tempo, and cadence point before arranging actions. The original case study uses 120 BPM; other products choose tempo, melody, and instrumentation from their actual shot list — the same piece is not required.

Build `audio.cues` consistent with `plan.json`: `at / actionId / file / gain / role`. `at` is absolute film seconds; an action's `at` is relative to shot start, so the cue maps to `shot.start + action.at`. SFX lands on the action occurrence point, not mechanically at every shot start. Use light click/pop for selections, whoosh only for structural changes, a recognizable chime for notifications, and one cadence at the end.

Licensing must distinguish "usable in the finished film" from "redistributable as raw audio with the template." This skill does not bundle the original case study's Pixabay recordings or commercial fonts. When downloading audio into the current video project, record source and license; do not assume the project license extends to skill redistribution.

## From "Wrote SFX" to "Can Actually Hear It"

Pick the most feedback-rich state change from each core function group (select, open, complete, notify) and mark the corresponding action `soundRequired: true`. Not every text entrance needs a sound, but you cannot skip all intermediate key actions and only add a sound at the end. Use a recognizable two-tone ding-dong or confirmation chime for completions/notifications — not just whooshes.

Sound verification has three steps: listen to `sfx-stem.wav` alone to confirm key events have SFX; listen to the master to confirm SFX is not drowned by the score; listen to the encoded MP4 to confirm editing/export did not drop anything. Checking only for file existence or track count is insufficient. When playback is possible, verify action by action; when it is not, state this accurately — do not pretend audio passed listening verification.

When a suitable SFX cannot be found, copy the missing type directly from the [bundled SFX directory](../assets/audio/sfx/): click/click-alt, pop, toggle, typing, ding-dong, success, error, resolve, whoosh, or sweep. These are ready-made original WAVs — no generator run needed. Only modify `make_sfx.py` when timbre adjustment is required, outputting to a new directory.

**Set gain from measured levels.** Bundled SFX peak at ≈ −20 dBFS; recorded samples sit near 0 dBFS. At the same gain, the former will be buried by the score. Use `scripts/sfx_landmarks.py` to check each file's peak level and landing point. After mixing, compare per-cue SFX peak against the ducked music at the onset moment: SFX should not be noticeably lower than the music.

```sh
# Output code-original score to assets/music.wav.
# Source SFX per audio-sourcing.md, copy bundled WAVs for gaps; then update plan actions and cues.
python3 <skill-dir>/scripts/mix_audio.py plan.json
```

`mix_audio.py` outputs `assets/sfx-stem.wav`, `assets/music-ducked.wav`, `assets/master.wav`, and `evidence/audio-mix.json`, applying two-pass loudness processing to the mix. When the score is too loud, lower the music gain; when SFX is too quiet, adjust the corresponding cue. Existing HyperFrames/Remotion mixers may also be used, but preserve equivalent evidence of assets, sound cues, mix source, and final output.

Config structure (illustrative; times should come from actual shots):

```json
{
  "audioRequired": true,
  "sfxRequired": true,
  "audio": {
    "music": {"file": "assets/music.wav", "gain": 0.65},
    "cues": [{"at": 12.2, "actionId": "task-finished", "file": "assets/sfx/ding-dong.wav", "gain": 0.7, "role": "sfx"}]
  }
}
```

Corresponding action example: shot starts at 12s, `actions` contains `{"id":"task-finished","at":0.2,"action":"Task complete notification appears","soundRequired":true}`. The cue should align with that action; the auditory landing point vs. action is typically within 1 frame, with a 2-frame check ceiling. When the user explicitly wants no SFX, record `sfxRequired:false` and `audioExceptionReason`; for full silence set `audioRequired:false`. These exceptions follow the user's decision, not the model's.

## Duck the Score When SFX Plays

Enable `audio.ducking` by default. Previously there was only a fixed music gain, and important cues could still be buried; now the music is pre-ducked per cue, then smoothly recovers after the SFX ends. This is not a blanket volume reduction for the whole piece, nor a sudden mute.

The table below is this skill's listening starting point, **not an official audio standard**; adjust based on music density and SFX timbre:

| Sound role | Music ducking | Pre-onset duck / primary hold / release |
| --- | --- | --- |
| Click, toggle, light pop | ≈ 3–3.5 dB | 40ms / 100–120ms / 200–240ms |
| Typing detail | ≈ 2.5 dB | 40ms / 350ms / 250ms |
| Transition | ≈ 4 dB | 40ms / 160–200ms / 300–350ms |
| Complete, notify, important confirm | ≈ 5–6 dB | 40ms / 350–450ms / 350–400ms |
| Brand outro | ≈ 5 dB | 40ms / 550ms / 450ms |

The mix script uses the determined volume envelope; when multiple SFX overlap, take the deepest current duck — do not multiply attenuations cumulatively. Per-cue adjustable:

```json
{"audio":{"ducking":{"enabled":true}},"cueExample":{"kind":"ding-dong","duck":{"db":6,"attack":0.04,"hold":0.45,"release":0.4}}}
```

`cueExample` is a field illustration; in practice it lives in `audio.cues[]`. Global settings override type presets; a cue's `duck` overrides the global. There is no reason to give every sound the same intensity. When the music sounds like it keeps pumping, reduce unnecessary cues, decrease ducking depth, or extend the release. When SFX is still buried, first check timbre conflicts, adjust BGM vs. SFX relative levels, then look at local ducking — do not just raise the final master volume.

If switching to real-time sidechaining, FFmpeg `sidechaincompress` uses a second signal to control compression on the first, requiring threshold/ratio/attack/release tuning; this tool chooses volume automation for known cues, which is easier to pre-duck and repeatedly verify. Filter syntax per [FFmpeg volume](https://ffmpeg.org/ffmpeg-filters.html#volume) and [sidechaincompress](https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress); delay per [adelay](https://ffmpeg.org/ffmpeg-filters.html#adelay).

## Beat Alignment and Sound Variation

1. Listen to / analyze the actual music to determine BPM and downbeat time; when rhythm is not fixed, note actual beat points — do not invent a 120 BPM. Major transitions can align to downbeats; light operations need not all hit downbeats.
2. Adjust image and sound timing together. `cue.at` is the file start; `syncOffset` is the auditory landing point within the file, so `cue.at + syncOffset = shot.start + action.at`. Measure landing points with `scripts/sfx_landmarks.py`: clicks use onset, whooshes/impacts use peak (they must start before the visual).
3. When using a beat grid, fill `audio.beatGrid:{bpm,offset}`; mark cues that need beat alignment with `onBeat:true`, optionally using `beatDivision:1|2|4` for quarter/eighth/sixteenth notes. The mix report will state how many frames each cue deviates from the action and nearest beat — reporting only, not silently shifting SFX and causing audio-visual misalignment.
4. A 30–60 second film typically uses 4–6 sound roles: select/confirm, pop/toggle, typing, spatial transition, complete/notify, outro. Categories serve the visuals — do not invent exceptions or notifications just to hit a count. Shorter films may use fewer.
5. Consecutive clicks can alternate click/click-alt for subtle timbre variation; typing sounds are rhythmic short bursts; transition sounds are reserved for visual structure changes; ding-dong is reserved for noteworthy states. Do not "ding" every text appearance.
6. Finally, listen to the music track alone, SFX track alone, full mix, and final MP4 separately; check whether the first hit of notification sounds is buried, whether tails are cut off, and whether rhythm feels crowded.

## Mixing

Music should be audible but not fatiguing; for narration-free short films, target ≈ −16 LUFS final mix with true peak no higher than −1 to −1.5 dBTP as a starting point, adjusting per platform requirements and listening. Different platforms/subjects do not mandate the same value. With narration, leave space for voice and duck based on listening.

For normalization, use FFmpeg loudnorm two-pass: first measure, read measured_I/TP/LRA/thresh/offset, then feed measurements into the second pass; do not judge loudness by peak normalization alone. Re-measure true peak after final AAC encoding, as encoding may introduce new peaks. Report `normalization.normalization_type` to preserve which mode (linear/dynamic) the second-pass loudnorm actually used. When music exceeds film length by 1 second, the script outputs a warning and writes it to the report; after auto-trim and fadeout, confirm the ending and re-arrange if needed.

Verify music matches picture length, no sudden loud start, natural ending, no SFX clipping, no abrupt silence. Listen to the final file in a player; if the environment only allows measurement, state clearly that listening verification was not completed — do not claim it has been "listened to."

## Automated Checks

```sh
python3 <skill-dir>/scripts/check_delivery.py plan.json --video renders/final.mp4 --mix-report evidence/audio-mix.json > evidence/delivery-check.json
ffmpeg -i renders/final.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=8:print_format=json -f null -
```

In production mode (`demo:false`), the script also rejects missing bilingual titles, missing font assignments, key actions without cues, BGM-only audio, stale mix reports, or changed asset hashes. The script cannot automatically isolate and judge SFX audibility from the MP4; the built-in exporter verifies the hash of the supplied master against the mix report; other exporters must verify track wiring themselves.

The script fails on timing gaps/overlaps, wrong specs, missing audio tracks, or selling points without sources; it warns when reading duration and type are too uniform. It cannot declare selling points truthful, visuals un-cropped, or music pleasant based on these checks alone.

`--video` also reports `pacing` (still-frame ratio, longest still segment, hard-cut count) — only to locate segments worth re-examining. Large solid-color backgrounds with small-area motion can be counted as still; do not add meaningless animation just to improve the number. See [Review](review.md) for visual review methods.

## Final Manual Check

| Check target | What to look for |
| --- | --- |
| Narrative | On first viewing, can state what updates exist and how they are useful |
| Readability | Chinese text alone conveys the object, action, and result; no vague slogans; instructions appear early enough |
| Titles | English has real semantic meaning and is at heading level; Chinese is uniformly sans-serif; fonts for each language load independently |
| Visuals | First frame / middle / last frame / all transitions; no accidental blank screens, cropping, jumping, or tearing |
| Brand | Correct product name, official complete logo, visual identity consistent with the repo |
| Facts | Feature claims have evidence; examples do not impersonate customer results or benchmarks |
| Components | Original business components and styles are actually on camera; build graph, state-driven rendering, source list, and still frames are consistent; no basic-control or token-replica standing in for full feature reuse |
| Audio | BGM and key-action SFX are both audible; completion/notification feedback is clear; actions are aligned; not harsh, no clipping, ending is complete |
| Links | URLs/CTAs hidden per user request; masks do not leak during zoom/pan |
| Consistency | Check both preview and MP4; final changes actually appear in the exported file |

Extract keyframes from the final MP4, not just reuse pre-export screenshots. Deliver with correct file paths and clear production status — do not mistake a technical demo, un-mixed version, or early draft for the final.
