# Shot List, Copy & Pacing

## From Update List to Story

The structure is chosen first in [film direction](direction.md): claim → proof per section is the most common; alternatives include "problem → solution," "complete one task end to end," "single continuous take," "before/after," chosen by content. 45–60 seconds typically fits 3–5 update groups, ~10–14 shots; this is a capacity reference, not a template to fill. A small release can be 20 seconds; a complex feature can be longer.

Each shot is recorded in `plan.json`: start/end time, type, main copy, explanation, selling point source, real component/adapter, primary action, sound cue. Estimate reading and demo time first, then fit to music beats — don't lock 48 seconds first and stuff copy in afterward.

Using the "claim → proof" structure as an example, reference sections:

| Section | Visual Role | Pacing Reference |
| --- | --- | --- |
| Opening | One direct statement of change, large type or brand | 2–4 seconds |
| Core capability | Title card states the capability → component close-up proves it → workspace provides context | 7–12 seconds per group |
| Small improvements | 2–3 independent, clear details | 2–4 seconds each |
| Closing | Product identity and one closing line; CTA follows release requirements | 2–3 seconds |

Shot variety comes from "where should the audience look": single component zoomed, left-right dialogue, focus on input area, workspace expanding, pure large type, a few parallel cards. Not from random transitions creating a sense of busyness.

## Copy Should Sound Human

- Titles can be short; small text must not be reduced to just keywords.
- Small text should have subject/action/result so the audience understands the change on first read.
- Use words the product's users recognize; avoid explaining build scripts, SSR, or technical compatibility in a promo film.
- Feature names must match the real interface; don't replace them with unverifiable vague words like "smarter, smoother, freer."

Examples:

| Too Abbreviated | Clearer |
| --- | --- |
| Context, kept up. | After switching models, you can continue working with the previous conversation carried over. |
| Preview and browse, right there. | Open web pages in the built-in browser to check project results at any time. |
| Task notifications. Less waiting. | You'll receive a notification when the task completes — no need to watch the conversation window. |
| CLI maintenance. | Check CLI status in settings and update directly when needed. |

These sentences are writing examples for CodePilot only — they cannot be applied directly to products without these features.

## Division of Labor Between Headline and Body Copy

Default: short headline + clear body sentence; both sit at the primary visual level. The headline distills the capability/action; the body ensures immediate comprehension. Headlines use meaningful phrases chosen per feature.

- Body text uses a unified sans-serif system; weight/size distinguish hierarchy.
- Headlines in a separate span with `--film-font-headline`; body in a separate span with `--film-font-body`. Headlines can use a distinctive serif; body uses a clean sans-serif; or pick two matching sans-serifs per brand. **Assigning fonts to headlines and body separately does not mean letting font fallback randomly assign glyphs.**
- Main title cards can use large headline + medium body title; component pages can place short headline above the body — it should still be prominent enough. Not every small button needs a label.
- Headlines must fit the feature; don't mechanically pad short descriptions, don't force unrelated slogans for layout. Body copy must stand alone and be immediately understandable.
- Font choices come from product design or available licensed fonts; system fonts are for technical preview only. Production projects freeze font assets and verify actual glyphs. Don't judge font loading by CSS font-family name alone.

| Headline | Body Copy | Description (when the feature genuinely exists) |
| --- | --- | --- |
| Switch models | Switch models, keep chatting | After switching models, the previous conversation carries over — no need to re-explain everything. |
| Browse here | Web pages open right beside you | Open web pages inside the app — chat and view page content side by side. |
| You're notified | Done — we'll let you know | A notification pops up when the task completes — go handle something else. |

Don't reuse these three copy pairs as a fixed template for every product; check facts first, then rewrite. When the user explicitly specifies monolingual/font choices, respect them and record the reason in `typography.exceptionReason`.

## Copy Read-Aloud Test: Periods Don't Guarantee Substance

Execute per feature, write results to `evidence/copy-review.md`:

1. Write the plain-language fact first: "what you had to do before, what you do now, how the result differs." Write only what has a source; don't fabricate a before/after comparison if you don't know the previous behavior.
2. Distill a title from it, then write the description. The description must state **target + action + observable result**, adding usage context when needed; length is whatever it takes to be clear.
3. Cover the screenshots and read only the body copy to someone who has never used the product. If you still need to ask "what connected? Where do you see it? What happens?" — rewrite.
4. Check whether the title and description are just synonymous repetition; the description should add action or result, not praise the product again.
5. Read aloud in natural conversational tone, then check subtitle display time. Don't substitute "enough characters" or "has a period" for content review.

Additional counter-examples:

| Fails | Why It's Unclear | How to Say It (assuming the feature is real) |
| --- | --- | --- |
| Let the workflow flow naturally. | Doesn't say which action changed | After submitting changes, you can view the check results in the same window. |
| From inspiration to launch, all in one go. | Generic praise, provides no information | After writing requirements, AI generates the code and you can preview the updated page directly. |
| Results, at your fingertips. | What "results," where to see them | When a task completes, click the notification to return to the corresponding conversation. |

`plainExplanation` holds the fact-based plain-language explanation; `description` is the final on-screen text. They can be identical, but don't compress a concrete explanation back into an abstract phrase for "sophistication." Scripts can only detect missing fields or suspicious phrasing — whether the semantics are clear still requires the read-aloud test above.

## Action, Dwell Time & Music

- Entrance/select/switch actions typically 0.25–0.6 seconds; give actions a clear start and end.
- Each shot generally follows "establish frame → core action → readable result → cut away." Don't have everything float in together then sit still for 5 seconds.
- Description text appears early so reading time overlaps with the component demo. Don't solve long sentences by shrinking font size — prefer cutting filler, splitting sentences, or adding dwell time.
- ~150–200 words per minute as a rough warning threshold for on-screen text readability. Leave additional margin when the UI has complex changes happening simultaneously; this is a human-reading starting point, not a pass threshold.
- Start composing at 110–125 BPM; beat interval ≈ `60 / BPM` seconds. Main actions land on strong beats, small actions offset by half a beat. Don't force-quantize every clip to the same length.
- Blank or completely still frames aren't inherently wrong: brief pauses serve emphasis/reading. Beware long pauses with no information; don't add meaningless motion just to defeat stillness detection.
- The ending needs a complete logo lockup and sound resolution. When there's no website link, leave just the product name/logo and one closing line.

## Still Frame Review

Capture representative shots from actual code, arrange them in playback order as a contact sheet. Check for: variation in visual scale, whether the hierarchy is immediately clear, whether descriptions remain readable when shrunk to phone width, and whether any word or punctuation has wrapped awkwardly to the next line. Passing still-frame review only proves layout direction; pacing, motion continuity, and sound still require watching the finished film — see [review](review.md).
