# Image

Every image is a 1080x1350 artboard on the canvas, built from a layout template
and one of four monochrome themes.

Canvas: https://claude.ai/artifact/HYktiJudfBwwCRD7JG4Re4
- Page "Templates": the layout files in `project/templates/`.
- Page "Teme": one preview row per theme (`templates/Teme-<theme>.dc.html`), every
  layout in it, shrunk. These are previews, not layouts: never copy them.
- Page "Posts": finished posts. Never edit an existing post unless I ask.

## Layouts

| File | Use it for | Default for text template |
| --- | --- | --- |
| `templates/Code.dc.html` | a decision with a do/don't code contrast + 3 reasons | Decision |
| `templates/Story.dc.html` | a key moment as a big quote + 3 scenes (before, the break, after) | Story |
| `templates/Statement.dc.html` | one big sentence + a grey twist, three label/value columns | Contrarian |
| `templates/List.dc.html` | up to 5 numbered rows | Numbered lessons |
| `templates/Quote.dc.html` | one huge sentence, nothing else | Micro |
| `templates/Timeline.dc.html` | 3 dated stages + Now | any, for a journey |
| `templates/BeforeAfter.dc.html` | two rows of pills, the old way vs the new way, + a code card | any, for a comparison |

## Themes

All four are strictly black, white and grey. No accent colour, no emoji, no
gradient washes. Never imitate a brand's or a game's visual identity; carry a
theme of the topic in the copy.

| Id | Looks like | Headline |
| --- | --- | --- |
| `noapte` | black ground, grey lower panel, faded code texture (the original look) | Inter 600, uppercase |
| `hartie` | off-white paper, thin black rules, no texture, editorial | Instrument Serif 400, as written |
| `terminal` | dark grey, everything in JetBrains Mono, `$` prompt, dashed frames | JetBrains Mono 600, lowercase |
| `grila` | light grey with a visible grid, black solid lower block, brutalist | Inter 800, uppercase |

Constant in every theme: "Bogdan Dimoiu" top left, "<Topic> · <Area>" in mono
top right, a mono closing line bottom left, "bigdan.dev" bottom right.

Forbidden combinations: none yet. Add a line here for each layout x theme pair
that looks weak on the "Teme" page.

The theme colours live in a `THEMES` object in each layout's script. The seven
copies must stay identical: change all of them together.

## Copy limits

Write headlines in sentence case. In Code, List, Timeline and BeforeAfter the
theme sets the case. Statement, Story and Quote show the copy as written in every
theme, so keep it in sentence case.
- `noapte`, `grila`, `terminal`: at most ~10 characters per line at 128px, ~11 at
  112px, 2 to 3 lines.
- `hartie`: up to ~14 characters per line.
- 3-point descriptions about 10 words; list items one sentence.
- Story: the quote at most ~70 characters; each scene a short title + one
  sentence.
- Quote: at most ~60 characters in total.

## Build steps

1. `read` `project/canvas.json`, then `read` the chosen layout file.
2. Copy it to a new artboard `project/<PascalSlug>.dc.html` (top level, not under
   `templates/`). Keep `<script src="./support.js"></script>` exactly.
3. Set the theme in BOTH places in the copy: the `"default"` of `theme` in
   `data-props`, and the fallback in `renderVals()`
   (`this.props.theme ?? 'noapte'`). The default alone only seeds the editor; the
   artboard renders the fallback.
4. Replace every [bracketed placeholder] with real copy. Nothing in brackets may
   remain except facts I must still supply (tell me which). Escape `<` and `>` in
   code as `&lt;` `&gt;`; avoid `{{` in copy.
5. In themes with texture (`noapte`, `terminal`), replace the background code
   texture with 3 to 5 short code lines about the topic.
6. Add the artboard to `canvas.json`: a `boards` entry `{"x": <next free x on the
   Posts page, step 1160>, "y": 0, "w": 1080, "h": 1350, "title": "LinkedIn post ·
   <topic>", "page": "posts"}`, and append it to `order`. Keep every other key
   untouched.
7. Publish to the canvas url with `root` = the folder holding `project/`,
   `file_path` = canvas.json, `files` = the new artboard. Do not render,
   screenshot or re-read to verify unless I ask.
