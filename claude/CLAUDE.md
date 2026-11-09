# Working agreement

## Process
- One step at a time. Stop and confirm before moving to the next.
- Batch clarifying questions into a single message before starting work.
- Use plan mode for anything beyond a single-file change.
- For a full task workflow, run /bgw-task-flow. For debugging, run /bgw-debug-flow. To only analyse a problem, run /bgw-analysis-flow. For code review, run /bgw-review-flow. For an improvement pass on finished work, run /bgw-improve-flow. For browser QA, run /bgw-qa-walk.

## Communication
- Explain for a mid-level developer. Plain language, short sentences, ordinary verbs.
- Define a term the first time you use it. Don't assume I know a flag, option, or concept.
- Mechanism first, then the conclusion. "X happens, so Y" — not "Y, per X".
- Show a small real example — actual code, actual numbers — over an abstract description.
- Say the consequence in human terms: what breaks, who notices, what it costs them.
- No abstract-noun stacking. Quote a doc or ADR by name, then say what it means plainly.
- Plain is not padded. Short and clear beats long and clear.
- Wording only. Never soften a finding, drop a measurement, or hedge to sound gentler.

## Implementation
- Make only the changes required. No drive-by refactors, no unrequested renames.
- Read neighbouring files first. Match their patterns over your defaults.
- Prefer the obvious solution over the clever one. I read this again in 6 months.
- Comments explain why, not what. Max 20 words.
- Check the installed version's docs before using a library API.
  Get the version from package.json or the .csproj, not from memory.
- No `ponytail:` marker comments. Comments follow the repo's own rules.
- Tests follow the repo's own conventions, not ponytail's assert/test_*.py style.

## Tests
- Run the suite before saying you're done.
- Tests failing in areas I didn't touch: report them and stop. Don't fix.

## Honesty
- State plainly what you verified and what you did not.
  Reading the code is not verification.
- If you're unsure, say so before writing code, not after I find the bug.
