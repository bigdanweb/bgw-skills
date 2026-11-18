---
name: bgw-task-flow
description: Structured workflow for a non-trivial task - research, plan, implement, verify, summarize. Use when starting a bug fix or feature that spans more than one file.
---

# Task flow

Phases 1, 2 and 2b run once for the whole task.
Phases 3 and 4 loop, once per sub-step from the phase 2 plan.
Phase 5 runs once at the end, over the final diff.
Stop and wait for confirmation between every phase and every loop.

## 1. Research

Run /bgw-analysis-flow. Its rounds and checkpoints are this phase.
The phase ends when its verdict is complete, or I accept what is missing.

## 2. Plan

Start from the analysis file that phase 1 wrote.
Write the plan into that same file as `## Plan`. The chat is not the plan.

Identify happy paths, edge cases, and adjacent areas that will be affected.
Break the work into small steps that can each be verified on their own.
Each step names its tests and its doc impact.

Output, plain language, no code, four parts:
- Technical: what changes, why, and the effect on developer experience.
- Business: what the user or API consumer sees differently.
- Dependencies and failure: a table. One row per external thing the design
  relies on (API, database, config, env, clock, another job) and per case:
  normal, missing or empty, error (403, timeout), malformed.
  Columns: what the code does, what the user sees, loud or silent.
  A silent row needs a stated reason, or it is a design bug.
- Steps: numbered, each one independently verifiable.

Example row: `/v2/teams` `billing` | missing | falls back to Hobby |
credit meter gone, no alert | silent.

## 2b. Challenge

The author does not grade its own plan. A fresh sub-agent attacks it.

Its brief is its only context:
- The analysis file, with `## Plan`.
- `~/.claude/bgw/lessons.md`: lessons tagged `general` and this repo's name.
- The repo's rules: CLAUDE.md, docs, comments that state a rule.
- The code.
Not the chat, so it does not inherit the reasoning it should test.

It may do what /bgw-analysis-flow may do without asking, with the same
temporary-change rules. It never edits code or the plan. It only reports.

It looks for:
- Contradictions: plan vs a repo rule, plan vs a `verified` fact in the
  analysis, plan vs itself, and two claims in the analysis that disagree.
- Failure paths missing from the dependencies table.
- Each lesson, asked against this plan.
- Steps that cannot be verified on their own.

Evidence bar. No new code exists yet, so nothing new can be run:
- `blocker`: a contradiction with both sides cited (file:line, plan row,
  or analysis claim), or a probe on the existing system that disproves
  an assumption the plan rests on.
- `warning`: a failure path missing from the table, with the source that
  shows the path exists.
- `assumed`: never a finding. It becomes a question for me.

It writes its findings to the analysis file as `## Challenge`.
Checkpoint: I cut, adjust, or accept. The main session then revises `## Plan`
and notes, per change, which finding caused it.

Round 2 only if the revision changed the design: a new decision, not wording
or docs. A new fresh sub-agent gets only what changed in the plan. No round 3.

When I said to run phases without stopping: apply every `blocker` to the plan
and log it. Warnings and questions stay in `## Challenge` and go into the
final summary. Do not wait.

## 3. Implement (per step)

Smallest diff that does the job. Match the patterns already in those files.
Write tests alongside the change, not after.
Update docs the change invalidates.

## 4. Verify (per step)

Run the test suite.
Review your own diff for structure, security, scalability, dead code.
Confirm the step matches what phase 2 said it would do.
Unrelated failures: report and stop.
End with an explicit line on what you verified and what you could not.

If the change is user-facing, tell me to run /bgw-qa-walk. Don't skip it silently.

## 5. Summarize (once)

Write docs/<task-name>.md, aimed at both a future developer and a future
Claude session with no context:

- Technical: what changed, why, and the impact.
- Business: what behaviour changed for the user or consumer.
- One Mermaid diagram per section. Same story as the prose, for visual reading.
- Adjacent items, one line each, grouped: good-to-know / should-change /
  must-change. Things you noticed but correctly did not fix.
- Open challenge items: warnings and questions from `## Challenge` still open.

Concise throughout. No detail unless asked.
