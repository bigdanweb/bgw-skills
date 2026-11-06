---
name: bgw-analysis-flow
description: Deep analysis of a problem before implementing or debugging - code, data, business logic, processes, history, tests, failure modes - in rounds, with every claim labelled by its evidence. Use when a task or bug must be understood before planning, or on its own to understand a PR, ticket, flow, or process.
---

# Analysis flow

Understand the problem completely before anything is planned or changed.
Runs in rounds. Stop and wait for confirmation after every round.
No plan, no fix, no implementation here. Those belong to the flow that called this.

## Setup

- Restate the problem in one or two plain sentences.
- Record `git status` as the starting state.
- Create the analysis file: ~/.claude/analyses/<repo>/<task>.md.
  Task name: the ticket key if there is one, else a short kebab-case slug.
  Update it after every round. It is the source of truth, not the chat.
- A question that blocks the whole analysis (which of two flows is the real one,
  which environment): ask it immediately, alone. Everything else waits for the checkpoint.

## Evidence labels

Every claim carries exactly one:
- `verified`: ran something and saw the result. Name what was run.
- `read`: read code, docs, or a sub-agent's summary. Not executed.
- `told`: from me, or written in the ticket.
- `assumed`: a guess. Say why it seems likely.

Reading code is not verification. Sub-agent findings are always `read`.

## Round 1: every lens

For each lens, write the questions it raises, then answer them or mark them open.
A lens that does not apply: "n/a" with the reason. Never skip one silently.

1. Code: callers, callees, data flow, state, caching.
2. Data and contracts: types, schemas, APIs, database, what goes in and out.
3. Business logic: rules, edge cases, who is affected and what they see.
4. Processes: CI, deploy, feature flags, translations, approvals, other teams.
5. History: git log and blame, earlier PRs and tickets. Why is it like this?
6. Tests: what the current tests cover, and what they miss.
7. Failure modes: errors, concurrency, security, personal data.

Round 1 covers level 1 (the code touched directly) and level 2 (its direct
callers, callees, and consumers). Deeper levels wait for later rounds.

Before asking me anything, try to answer it yourself: code, history, tests,
running it. Ask me only what the system cannot tell you: intent, business
rules, priorities, access.

## Later rounds

Only the branches I pick at the checkpoint. One level deeper per branch.
Same labels, same file. Do not repeat the lenses that were settled.

## What it may do

Without asking:
- Read anything in the repo. Run tests, typecheck, lint.
- Read-only git and gh. Read-only database queries on dev and test.
- Open local or dev pages in the browser. Read logs.
- Write scripts in the scratchpad.
- Temporary changes in the repo, such as debug logging or a probe. List each one
  in the analysis file. Remove all of them before the checkpoint, and confirm
  `git status` matches the starting state.

Ask first: anything on staging or production, sending a message, writing to Jira,
GitHub, Slack or any external system, staging or committing.

Never copy tokens, identity numbers, salary, or bank details into chat or the file.

Sub-agents: the main session drives and connects the lenses. Use a sub-agent only
for a broad search (every caller of X, a module's history), with a narrow brief.
It returns conclusions, not file contents.

## Checkpoint (end of every round)

In chat, short:
- What this round found, with labels.
- Label count: n verified / n read / n told / n assumed.
- Questions for me, in one batch, each with your recommended answer.
- Open branches: the level each needs and what it would settle. Recommend which to take.
- Temporary changes: all removed, `git status` matches the start.

Then stop.

## Done

Complete when every claim the decision rests on is `verified` or `told`, and every
open question is answered or written down with the reason it cannot be.
If it is not complete, say so plainly and name what is missing.

The analysis file ends with this shape:
- Problem: in plain words.
- What we know: every claim, labelled.
- Adjacent impact: what else is touched, and how.
- Open questions: for me, and for yourself.
- Risks.
- Verdict: complete, or what is missing.

The calling flow starts its plan phase from this file.
