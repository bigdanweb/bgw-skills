---
name: bgw-improve-flow
description: Second look at finished work to find what could be better - simpler, more consistent, sturdier, better tested - in the changed code and the code it builds on, then turn the picked items into briefs for /bgw-task-flow. Use when something is built and working and I want an improvement pass, not a correctness review.
---

# Improve flow

Review asks "is this change correct?". Improve asks "what would make it better?".
Runs in phases. Stop and wait for confirmation between every phase.
Never touches the code. The only writes are the improve file and scratchpad scripts.

## 1. Target and baseline

Pick the target from the argument, same as /bgw-review-flow:
- No argument: the current branch against its base (nearest parent branch, ask if unclear).
- `staged`, `commit`: the staged diff, or the last commit.
- A path or folder: that area as it is now, no diff.

Scope: the target files plus their direct callers and consumers. Nothing wider
unless I ask.

Before judging anything, record:
- `git rev-parse --short HEAD`. Every brief stamps it.
- The repo's build, typecheck, lint, and test commands, read from its scripts and CI.
- One run of the test suite. Write down what is already red. Those failures are the
  baseline, never a finding, and no brief may require them to pass.

Improve file: ~/.claude/analyses/<repo>/<target>-improve.md, target being the
branch name, `commit-<sha>`, or a slug of the path. If it already exists, go to "Re-run".

If /bgw-review-flow or /bgw-analysis-flow already wrote ~/.claude/analyses/<repo>/<target>.md,
read it first and do not redo what it settled.

## 2. Look

Code written in this session: run this phase in a fresh sub-agent,
so the author does not grade its own work.

Lenses, each answered or marked "n/a" with the reason:
1. Simpler: run `ponytail:ponytail-review` on the scope. What can be deleted or flattened.
2. Duplication: logic repeated in the scope, or re-implemented next to an existing helper.
3. Consistency: patterns that differ from neighbouring files. Name the exemplar file.
4. Sturdiness: error paths, empty and null cases, retries left thin.
5. Tests: do they fail if the logic breaks? Gaps on the paths that matter.
6. Performance: only on hot paths, with evidence.
7. UI, when the scope renders something: run `web-design-guidelines` as a lens.
8. Next step: what the code itself points at - TODO clusters, half-built pieces,
   one-way pairs (export without import). Never generic ideas.

Tag every item:
- `introduced`: the target added it. `pre-existing`: it was already there in the scope.
- Evidence label from /bgw-analysis-flow: `verified`, `read`, `told`, `assumed`.
  `assumed` is never an item. It becomes a question.
- Effort S / M / L, including tests. Risk of the change LOW / MED / HIGH, one line why.

Vet before showing anything: open every cited file:line yourself.
Sub-agent line numbers are leads, not facts. Drop by-design behaviour, fix wrong
attributions, merge duplicates. Record each rejection with one line of reason.

## 3. Checkpoint

In chat, short:
- One table, ordered by value for effort: #, item, tag, lens, effort, risk, label, file:line.
- Next-step ideas apart from the table, 2 to 4 at most, each with its evidence.
- Rejected, one line each.
- Baseline: what was red before we started.
- Recommend which items to brief. "Not worth doing" is a valid verdict.

Then stop. I pick the items.

## 4. Briefs

One brief per picked item, written into the improve file. Excerpts come from your
own reads in this phase, never from a sub-agent.

Each brief is written for a session with no context:
- Why: the problem, its cost, what improves. Two to four sentences.
- Planned at: the SHA from phase 1. Drift check: `git diff --stat <sha>..HEAD -- <in-scope paths>`.
- Current state: each file with its role, and short excerpts with file:line.
- Pattern to match: one exemplar file and the lines to copy the shape from.
- Scope: files in scope. Files out of scope that look related, and why not.
- Steps: small, ordered, each with a command and its expected result.
- Done: commands and expected results only. Baseline failures excluded by name.
- STOP conditions specific to this item: the excerpt no longer matches,
  the change needs an out-of-scope file, the key assumption turns out false.

Then end with the order to run them in and which depends on which.

To act on a brief: /bgw-task-flow with the brief. Its research phase starts from
the brief and only checks what the drift check says moved.

## Re-run

Start from the existing improve file. For each brief, run its drift check:
- `done`: its done criteria hold on HEAD. Show the evidence.
- `stale`: in-scope files moved. Re-read, refresh the excerpts and SHA, or drop it
  if the problem is gone.
- `open`: untouched and still true.
Then phases 2 and 3 on what changed since the last run only.

## Never

- Edit, stage, or commit code. Post anything anywhere.
- Count a baseline failure as caused by the target.
- Copy tokens, identity numbers, salary, or bank details into chat or the file.
