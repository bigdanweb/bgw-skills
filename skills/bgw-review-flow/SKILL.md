---
name: bgw-review-flow
description: Structured code review - orient, analyse what the diff touches, grade findings by evidence, checkpoint, then deliver. Works on someone else's PR (link or number) or on my own changes (branch, staged, last commit), and re-reviews after fixes. Use when asked to review code or a PR.
---

# Review flow

Read around the diff, report only on the diff.
Runs in phases. Stop and wait for confirmation between every phase.
Never touches the code under review, and never posts anything without my yes.

## Repo rules win

If the repo has its own review rules (severity labels, comment format, review
plans, area skills), use them on top of this flow. This flow adds the process.
Without repo rules, use the defaults below.

## 1. Target

Pick the target from the argument:
- A PR link or number: someone else's PR. Diff with `gh pr diff`, base from the PR.
- No argument: the current branch against its base.
- `staged`: `git diff --cached`. `commit`: the last commit.

Branch base: the nearest branch this one was cut from, not the repo default by
reflex. If the commits span more than one ticket, or the nearest parent differs
from the default, show both candidates and ask.

Re-review: an analysis file for this target already exists. Go to "Re-review".

Code written in this session: run phases 2 and 3 in a fresh sub-agent,
so the author does not grade its own work.

## 2. Orient and analyse

Someone else's PR: run /bgw-pr-brief first for purpose and reading order.
Read the CI status, read-only (`gh pr checks`). A red run is a blocker.

Then run /bgw-analysis-flow with the diff as the problem. Its analysis file is
~/.claude/analyses/<repo>/<target>.md, target being `pr-<n>` or the branch name.
Focus its lenses on what the diff touches: who calls the changed code, which
contracts and data it changes, which business rules, processes and tests depend on it.

## 3. Findings

Review the diff against these criteria, plus any area skills or plans the repo has:
1. Correctness: does it do what it claims, on every path.
2. Contracts and types: callers and consumers still hold.
3. Security and personal data: input, auth, secrets, what reaches logs.
4. Errors and edge cases: empty, null, failure, concurrency, retries.
5. Tests: they exist, and they fail if the logic breaks.
6. Performance: only on hot paths or a stated requirement.
7. Readability: matches the patterns in neighbouring files.
8. Complexity: run `ponytail:ponytail-review` as a lens.

A finding belongs in the review only if the diff causes it, even when it shows
up in another file. Everything else goes under "Out of scope".

Evidence bar, using the labels from /bgw-analysis-flow:
- `blocker`: needs `verified`. Something was run that shows the problem.
- `warning`: needs at least `read`, with the exact path (file:line → file:line).
- `nit`: `read` is enough.
- `assumed`: never a finding. It becomes a question for the author.
A finding below its bar drops one severity, or becomes a question.

Each finding: severity, label, file:line, problem, why it matters, suggested fix
as code plus a short explanation. Write them all to the analysis file.

## 4. Checkpoint

In chat, short:
- Severity counts: n blockers, n warnings, n nits.
- Each finding in one line, with its label.
- Questions for the author, or for me on my own code.
- Out of scope leads, one line each.
- Recommended verdict: comment, request changes, or approve.

Then stop. I cut, adjust, or approve findings.

## 5. Deliver

Someone else's PR, after my yes:
- Check for an existing pending review of mine first. If one exists, do not
  create a second or touch it. Print the findings in chat instead.
- Stage a pending review: inline comments on anchorable lines, the rest and the
  summary in the body. Omit the event, so it stays a draft. I submit it.
- Follow the repo's comment format where it has one.

My own code: nothing leaves the machine. The findings stay in the file and chat.
No code is changed. I write the fixes, or ask for one explicitly through /bgw-task-flow.

## Re-review

Start from the existing analysis file.
For each earlier finding, check the fix in the committed code, not the author's
claim: `fixed`, `declined-accepted`, `declined-held`, or `still open`, with evidence.
Then run phases 3 to 5 on the new diff only: what changed since the last review.
Recommend approve only when every earlier finding is closed.

## Never

- Edit, stage, or commit the code under review.
- Submit a review, or post anything, without my yes.
- Copy tokens, identity numbers, salary, or bank details into comments, chat, or the file.
