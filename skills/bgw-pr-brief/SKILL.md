---
name: bgw-pr-brief
description: Reviewer's briefing for a pull request - purpose, plain-language summary, reading order, test plan, and questions for the author. Use when invoked with a PR link or number, or when the user asks how to understand or approach reviewing a PR.
---

# PR brief

Read-only. Produces a briefing that makes a large PR reviewable by a human.
It does not review, does not grade findings, and never writes to GitHub.

## Input

A PR URL, `#84`, or a bare number. Resolve the repo from the URL; otherwise
use the current repo's `origin`. If neither resolves, ask - do not guess.

## Ground every section in the diff

Never describe a PR from its title, its description, or the conversation.
Compute the facts first:

```bash
gh pr view <n> --repo <owner/repo> --json title,body,author,baseRefName,additions,deletions,changedFiles,commits
gh pr diff <n> --repo <owner/repo>
gh pr checks <n> --repo <owner/repo>
```

The base branch is whatever `baseRefName` says - often a feature umbrella, not
`master`. Diffing against the wrong base pulls in another ticket's commits.

A PR description is the author's claim, not evidence. Where the diff and the
description disagree, the diff wins and the contradiction becomes a Section 5
question.

Name anything you could not read instead of working around it.

## Output

All five sections in one response. No stopping between them - this is one
document, not a sequence of work. Plain language throughout. Concise: no
detail the reviewer did not ask for.

### 1. Purpose

Why this PR exists. What it fixes or adds, and what goes wrong without it.
Three sentences at most. If the diff does not support the stated purpose, say so.

### 2. Summary

What changed, for a non-technical reader. Business and UI/UX effect: what a
user, an API consumer, or an on-call engineer notices differently. Say "nothing
visible changes" plainly when that is the truth - most hardening PRs are that.

### 3. How to review it

First, split the changed files by weight and kind - production code, tests,
mocks, config - with line counts per file. State the production-code total
separately from the total diff; on a test-heavy PR the two differ by several
times, and that number is what makes the PR feel reviewable.

Then a numbered reading order over the production files only, each with the one
question that file answers. Order by dependency: the file that defines the
rules before the file that applies them, the entry point last. Say where to
stop.

Then: which files to skip entirely, and why. Name any file that looks unrelated
to the PR's stated purpose - that is a Section 5 question too.

Point at tests as documentation where they serve better than the source: a spec
that states input and expected output is faster to read cold than the logic it
covers.

### 4. How to test it

Reproduce the core requirement first, then the edge cases. Concrete steps -
commands to run, values to feed, what to observe - not "verify it works".

Cover:
- The happy path the PR claims to deliver.
- Edge cases the diff's own tests do not cover. Read the specs to find the gap.
- The failure path: what happens when the thing being guarded actually fires.
- Whatever the change protects, driven deliberately once.

Name what can only be checked by reading, and what needs the app running.
Where the repo documents its own gates, run those scripts rather than raw tools.

### 5. Questions for the author

Only genuine ones. Delete any question the diff already answers - a question
you could have resolved by reading is noise that costs the author time.

Look for: missing cases, silent failure modes, a guard that fails open, scope
creep, a claim in the description the code does not support, an odd or clever
choice where a boring one existed, a test asserting the implementation rather
than the behaviour.

One line each. State the concern, then the question. Group by whether an answer
would change the merge decision or not.

## Boundaries

- Read-only. No `gh pr review`, no comments, no pushes, no edits. Staging a
  review is a separate, explicitly-requested step.
- A briefing, not a verdict. No approve or request-changes recommendation, and
  no severity labels - the reviewer forms their own opinion from this.
- Do not run the repo's CI gates. Read their status with `gh pr checks` and
  report it; a red run is worth naming in Section 1.
