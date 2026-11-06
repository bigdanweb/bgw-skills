---
name: bgw-explain
description: Explain, in simple Romanian, what is happening right now in the session, or a specific thing - a term, an error, a file, a command, a decision. Use when invoked as /bgw-explain, or when I say I don't understand something.
---

# Explain

Stop the work and explain. Resume only when I say so.

## Input

- No argument: explain where we are now - what we are doing, why, and how it works.
- An argument: explain that thing, in the context of this session. A term
  (`junction`), an error (`eroarea de mai sus`), a file, a command, a decision.

If the argument is ambiguous, say which reading you chose in one line and go on.

## Language

Romanian, the simplest words that are still correct.
Technical terms stay in English, in italics, with a Romanian explanation the first
time they appear: "un *hook* (un script care rulează automat înainte de commit)".
Identifiers, commands, files, and settings stay exactly as written, in backticks.
Where a plain Romanian word means the same, use it: "fișier", not "file".

## Shape

Always these four parts, in this order:

1. **Pe scurt**: one sentence.
2. **Cum funcționează**: the mechanism as numbered steps. Use a real example
   from this session - our code, our command, our numbers - not a generic one.
3. **De ce contează aici**: what breaks without it, who notices, what it costs.
4. **De reținut**: one or two lines.

Add a small Mermaid diagram only when the explanation is a flow or an order of
steps between systems.

## Rules

- Mechanism first, then the conclusion: "X se întâmplă, deci Y".
- Never simplify into something false. If the simple version leaves out a case
  that matters, say so in one line.
- Say what you verified and what you only read or assume.
- No questions to test me. I ask if I want them.
