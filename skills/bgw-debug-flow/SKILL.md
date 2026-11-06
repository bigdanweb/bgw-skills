---
name: bgw-debug-flow
description: Structured debugging workflow - reproduce, hypothesise, prove the cause, fix with a regression test, summarize. Use when something is broken, throwing, red in CI, or behaves differently than expected and the cause is not yet known.
---

# Debug flow

Phases 1 to 3 run once, until the cause is proven.
Phase 4 loops, once per step from the phase 3 fix plan.
Phase 5 runs once at the end, over the final diff.
Stop and wait for confirmation between every phase and every loop.
No fix before the cause is proven in phase 3.

## 1. Reproduce

Run /bgw-analysis-flow first. Its rounds and checkpoints come before the loop below.
Phases 2 and 3 start from the analysis file it wrote.

Collect the exact symptom: error text, stack, URL or command, environment, time.
Build a loop that shows the bug on demand: a failing test, a script, a command,
or a browser path. Make it as small and fast as you can.
Find what differs between where it breaks and where it works:
environment, versions, data, user, feature flags.
Cannot reproduce: say so, list what you tried, and stop. Do not guess a fix.
Name anything you could not access instead of guessing around it.

Output, plain English, no code:
- Symptom: what is observed, quoted exactly.
- Repro: numbered steps, and how long one run takes.
- Works vs breaks: the differences found.

## 2. Hypothesise

List two to four candidate causes, ranked.
For each: the evidence for it, the evidence against, and one check that rules it out.
Run the cheapest checks first.
Change one thing at a time. Revert anything that did not help.
Temporary logging only where a check needs it. Track it for removal in phase 4.

Output: the ranked list, which checks ran, and what each showed.

## 3. Prove the cause

The cause is proven when you can switch the bug on and off through it.
"This line looks wrong" is not proof.
Look for the root cause, not only the place where it surfaced.

Output, plain English, no code:
- Cause: what is actually wrong, and why it produces the symptom.
- Evidence: the check that proved it.
- Blast radius: what else shares the cause.
- Fix plan: numbered steps, each with its regression test and doc impact.

## 4. Fix (per step)

Write the regression test first. Run it. It must fail, for the reason from phase 3.
Smallest diff that fixes the cause. Match the patterns already in those files.
Run the test again: it passes. Run the suite.
Unrelated failures: report and stop.
Remove the temporary logging from phase 2.
End with an explicit line on what you verified and what you could not.

If the bug is user-facing, tell me to run /bgw-qa-walk. Don't skip it silently.

## 5. Summarize (once)

Write docs/<bug-name>.md, aimed at both a future developer and a future
Claude session with no context:

- Symptom: what users or callers saw.
- Cause: what was wrong, and how it was found.
- Fix: what changed, and the test that now guards it.
- Why it was not caught earlier, and what would catch it next time.
- One Mermaid diagram of the failing path, before and after the fix.
- Adjacent items, one line each, grouped: good-to-know / should-change /
  must-change. Things you noticed but correctly did not fix.

Concise throughout. No detail unless asked.

## By kind of bug

Apply the section that matches, on top of the phases above.

### UI / browser

- Reproduce in the browser. Read console and network on the failing path.
- Hydration errors: compare the server-rendered HTML with what the client renders.
- Rule out the client state: clean profile, no cache, cookies, or extensions.
- Screenshot the broken state and the fixed state.

### Server / BFF / API

- Find the failing request in the logs by time or correlation id.
- Call the endpoint directly and compare with what the client actually sent.
- Check the upstream response on its own: is the bug ours or theirs?
- Auth or session: check token expiry, cookie flags, clock skew, environment config.
- Never copy tokens, identity numbers, salary, or bank details into chat, logs, or docs.

### CI / build / tooling

- Read the failing step's log from its first error, not from its last line.
- Compare versions between CI and local: runtime, package manager, lockfile.
- Rerun once to tell flaky from broken. Flaky is still a bug.
- Reproduce locally with the exact CI command, not a similar one.
