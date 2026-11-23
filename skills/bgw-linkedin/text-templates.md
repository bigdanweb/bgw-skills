# Text templates

Five shapes. They differ in structure, not only in tone. The examples are made up
and generic on purpose: never copy them, and never put real client or project
material from the notes into a post without generalizing it first.

Every template except Micro ends with 3 to 5 hashtags (#nextjs #react
#typescript #frontendarchitecture #softwareengineering #ai #devops #cicd
#security as relevant).

## 1. Decision

A team or personal decision, with the reasons.

1. Hook: one short, confident statement on its own line (not a question).
2. The problem, concrete; one code line is fine.
3. The pivot: the decision in one or two sentences.
4. 3 bullets with `→`, each one short line. Lead-in such as "What you should do
   instead:" for advice, or team voice for team decisions.
5. A concrete example: "For my team, one of those was ..." - what, why, what it
   unlocked.
6. Optional tie-in to AI-assisted development: AI writes code fast; judgment and
   decisions stay human.
7. A question to the reader.

Default layout: Code.

> We banned a whole feature of our framework.
>
> Not because it is bad. Because it hid our API behind a function call.
>
> Our rule is one sentence: every request goes through a route handler.
>
> → One contract we can test and log
> → The backend client never leaves the server
> → Nothing reaches the browser without a DTO
>
> ...
>
> What rule did your team write that sounded too strict at first?

## 2. Story

No lists, no arrows. 5 to 8 short paragraphs in time order.

1. The situation, in one or two lines, with a time or place.
2. What went wrong, concrete.
3. The turn: what I tried, what I noticed, the correction.
4. The lesson as one line, at the very end, on its own.
5. Optional question to the reader, short.

Default layout: Story.

> It was a Friday, 16:40, and the release was "done".
>
> Then the dashboard showed zero errors for an hour. Too quiet.
>
> Nothing was failing because the logger itself had stopped.
>
> ...
>
> A silent system is not a healthy one. Check that the alarm still rings.

## 3. Contrarian

Disagree with a common belief, fairly.

1. "Everyone says X." Name the belief.
2. Why it sounds right. Steelman it in 2 to 3 lines.
3. Why it breaks in practice, with one concrete case.
4. When X is still right. This is what makes the post credible.
5. A question to the reader.

Default layout: Statement.

> Everyone says: never deploy on Friday.
>
> It sounds wise. Fewer people around, longer time to notice a fire.
>
> But a team that cannot deploy on Friday cannot deploy safely on Tuesday either.
> ...
>
> Where the rule still makes sense: ...
>
> Do you deploy on Fridays?

## 4. Numbered lessons

1. Hook: "N things I learned from Y" or "N rules for Y". N is 3 to 5.
2. Numbered `1.` to `5.`: a short title in bold-style wording, then one sentence
   of explanation.
3. One closing line. No question needed.

Default layout: List.

> 5 things I learned from building my own AI workflow.
>
> 1. A skill beats a prompt. A prompt is forgotten; a skill is followed.
> 2. ...
>
> Build the system, not the prompt.

## 5. Micro

3 to 5 lines in total. One sharp observation. No bullets, no question, at most 2
hashtags. It breaks the rhythm of the long posts, so keep it short even when the
idea could be longer.

Default layout: Quote.

> AI writes the code in seconds.
> Deciding what not to build still takes a week.
> That week is the job.

## Layouts outside the defaults

- Timeline: a journey or an evolution (career, tooling, a migration).
- BeforeAfter: a comparison of two ways of working.
Use them with any text template when the content is clearly one of those shapes.
