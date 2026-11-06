---
name: bgw-qa-walk
description: Browser walkthrough of a UI change. Use when a change affects rendering, routing, forms, or anything a user sees.
---

# QA walk

## Before starting

State and get confirmation on: URL, route, tenant, user role, and any feature
flag or seed data the paths depend on. Do not start until I confirm.

## Walking

Walk the happy path first, then each edge case named in the plan.
Screenshot the final state of each path, and every failure. Not every click.
Check console and network once per path.

## Reporting

A table: path | expected | observed | pass/fail.
"Observed" describes what is on the screen. If it is empty, you did not look.

Any state you could not reach: name it and say why.
Never infer a pass from code you read.
