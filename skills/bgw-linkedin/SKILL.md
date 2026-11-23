---
name: bgw-linkedin
description: Turn a story, description or rough text from me into a LinkedIn post plus its 1080x1350 monochrome image on my design canvas. Finds the idea in my NOTES vault or on the web, rotates five text templates, seven image layouts and four monochrome themes. Use for /bgw-linkedin or any request for a new LinkedIn post.
---

# /bgw-linkedin

Input: a story, a description or rough text from me. Output: the post text and a
matching image on my design canvas. Runs only from Claude Code on my machine,
because the notes live on disk.

Files next to this one:
- `text-templates.md`: the five text templates, with examples.
- `image.md`: the seven layouts, the four themes and how to build the image.

Canvas (Design artifact): https://claude.ai/artifact/HYktiJudfBwwCRD7JG4Re4
Notes vault: `C:\Users\dimoi\Desktop\NOTES`
Post log: `C:\Users\dimoi\Desktop\NOTES\LinkedIn\log.md`

## 1. Find the idea

1. Read `log.md`. Note the text template, layout and theme of the last 2 posts,
   and every source note already used.
   Compare the core idea of my input with the Topic column of every row, not only
   the last 2. Same idea already posted: say which post in one line, and make
   every angle in step 4 take a side of the input that post did not cover. If no
   such side exists, say so and ask before going on.
2. Pull 3 to 6 keywords out of my input. Grep them (case-insensitive) in
   `NOTES/Sessions/` and `NOTES/Summaries/`.
3. Read the top 3 to 5 matching notes, and from each only "Pe scurt",
   "De reținut" and any correction ("am spus X, apoi am corectat").
   Skip notes already listed as a source in `log.md`, and notes about writing
   LinkedIn posts (sessions of this skill).
4. Nothing matched: read the last 7 files in `Summaries/` and look for a link to
   my input.
5. Still nothing, or the post needs a current fact (a release, a version, a
   number): search the web. Rules below.
6. Folder missing: say so in one line and go straight to the web.

## 2. Web rules

- The web gives facts and context, never the idea. Look for what happened
  (release notes, official docs, news), not for other people's LinkedIn posts.
  The angle comes from my input.
- Every number, date or technical claim from the web goes in your reply to me with
  its link and a tag: [Certain] / [Likely] / [Guessing].
- A fact with no source stays a `[PLACEHOLDER]`. Never invent numbers, timings,
  incidents or stack details.
- Current topics: sources from the last ~3 months. Official docs beat blogs.
- No links in the post itself. If one is needed, tell me to put it in the first
  comment.

## 3. Privacy: generalize everything

The notes hold client work and work for my employer. Nothing that identifies
them reaches the post or the image:
- No client, company, colleague or project names, mine included: "a small
  business", "an internal tool", "a side project", "my team".
- No employer or internal details. The exact banned names (employer, products,
  domain, stack, tools) are in `C:\Users\dimoi\Desktop\NOTES\LinkedIn\private-terms.md`,
  kept out of this public repo. Read it every run; if it is missing, stop and ask.
- No URLs, keys, tokens, contract sums, prices from a client deal,
  infrastructure details or exact internal numbers.
- If removing the detail kills the story, drop the angle and say why.

## 4. Propose 3 angles

Unless my input says "direct", stop here and give me 3 angles, each on one line:

> 1. *Contrarian*: "<the hook>" (source: Sessions/<project>/<file>.md)
> 2. *Story*: <one-line summary> (source: web, <link>)
> 3. *Micro*: "<the whole line>" (source: your input only)

Each angle names its text template and its source. Respect the rotation rule
(section 5) and the topic check (step 1.1) when you propose. Wait for my pick. With "direct", pick the best one
yourself and say which in one line.

## 5. Rotation rule

Pick the text template, layout and theme that fit the content, with one limit:
none of the three may repeat one used in either of the last 2 posts in `log.md`.
If I name one ("make it micro", "terminal theme"), my choice wins over the rule.

## 6. Write the post text

Follow the chosen template in `text-templates.md`.
Language: English (my profile audience), unless I ask for Romanian. Talk to me in
Romanian.

Voice:
- Team voice for work decisions ("we", "my team and I"); second person for
  general advice; first person for personal experience.
- Short sentences, plain words; a mid-level developer must follow it.
- Light self-irony is welcome; at most one emoji.
- Technical claims must be correct.

Deliver the text in one fenced `text` block, ready to copy, with nothing else
inside it.

## 7. Build the image

Follow `image.md`.

## 8. Log it

Append one row to `log.md`: date, topic, text template, layout, theme, source
note (or "web: <link>", or "input"), artboard file. Create the file with its
header row if it is missing.

## 9. Reply

In Romanian, concise. Tag claims [Certain] / [Likely] / [Guessing]. Say:
- which template, layout and theme you picked, and why, in one line;
- which placeholders remain and which facts I must supply;
- that the image is not checked visually: look at it and export the PNG from
  Share > Export (select the artboard first).
No URL pasting unless asked.
