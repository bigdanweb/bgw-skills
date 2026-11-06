---
name: bgw-task-flow
description: Structured workflow for a non-trivial task - research, plan, implement, verify, summarize. Use when starting a bug fix or feature that spans more than one file.
---

# Task flow

Phases 1 and 2 run once for the whole task.
Phases 3 and 4 loop, once per sub-step from the phase 2 plan.
Phase 5 runs once at the end, over the final diff.
Stop and wait for confirmation between every phase and every loop.

## 1. Research

Run /bgw-analysis-flow. Its rounds and checkpoints are this phase.
The phase ends when its verdict is complete, or I accept what is missing.

## 2. Plan

Start from the analysis file that phase 1 wrote.

Identify happy paths, edge cases, and adjacent areas that will be affected.
Break the work into small steps that can each be verified on their own.
Each step names its tests and its doc impact.

Output, plain English, no code, two sections:
- Technical: what changes, why, and the effect on developer experience.
- Business: what the user or API consumer sees differently.
- Steps: numbered, each one independently verifiable.

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

Concise throughout. No detail unless asked.
