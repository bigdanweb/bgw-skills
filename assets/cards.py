"""Generates one SVG card per skill into this folder. Run: python assets/cards.py"""
from pathlib import Path
from xml.sax.saxutils import escape

W, PAD = 800, 48
INNER = W - 2 * PAD
SANS = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
ROW_H = 71

CARDS = [
    {
        "file": "bgw-analysis-flow",
        "kicker": "Claude skill · analysis",
        "title": ["UNDERSTAND", "FIRST."],
        "subtitle": "Seven lenses, in rounds. Every claim carries its evidence.",
        "rows": [
            ("Setup", "once", "git status", " · ~/.claude/analyses/<repo>/<task>.md"),
            ("Round 1 · every lens", "levels 1–2", "code · data · business · process", " · history · tests · failure"),
            ("Labels", "on every claim", "verified  read  told  assumed", ""),
            ("Checkpoint", "stop", "findings · label count · questions", " · open branches"),
            ("Later rounds", "you pick", "one level deeper", " · only the branches you chose"),
            ("Done", "verdict", "decision rests on verified or told", ""),
        ],
        "columns": [
            ("Asks less", ["Answers what it can itself.", "Asks you about intent and", "business rules only."]),
            ("Leaves no trace", ["Temporary changes removed;", "git status matches the", "starting state."]),
            ("Feeds the flows", ["Phase 1 of task-flow and", "debug-flow. Plan starts", "from its file."]),
        ],
        "command": "/bgw-analysis-flow <ticket or question>",
    },
    {
        "file": "bgw-task-flow",
        "kicker": "Claude skill · implementation",
        "title": ["FROM TICKET", "TO DIFF."],
        "subtitle": "Research, plan, implement, verify, summarise.",
        "rows": [
            ("1 · Research", "once", "/bgw-analysis-flow", " → analysis file"),
            ("2 · Plan", "once", "technical · business · steps", " each verifiable"),
            ("3 · Implement", "per step ↻", "smallest diff + tests", " · docs it invalidates"),
            ("4 · Verify", "per step ↻", "run the suite · review the diff", " · what was verified"),
            ("5 · Summarise", "once", "docs/<task-name>.md", " · one Mermaid per section"),
        ],
        "columns": [
            ("Stops often", ["Waits for your yes", "between every phase", "and every step."]),
            ("Small steps", ["Each step names its", "tests and its doc", "impact up front."]),
            ("Hands off to QA", ["User-facing change?", "It tells you to run", "/bgw-qa-walk."]),
        ],
        "command": "/bgw-task-flow <ticket> <what to build>",
    },
    {
        "file": "bgw-debug-flow",
        "kicker": "Claude skill · debugging",
        "title": ["PROVE IT,", "THEN FIX IT."],
        "subtitle": "No fix before the cause switches the bug on and off.",
        "rows": [
            ("1 · Reproduce", "once", "/bgw-analysis-flow", " → a loop that fails on demand"),
            ("2 · Hypothesise", "once", "2–4 ranked causes", " · one check that rules each out"),
            ("3 · Prove", "once", "bug on ↔ bug off", " · root cause, not the call site"),
            ("4 · Fix", "per step ↻", "red test → smallest fix → suite", " · logging removed"),
            ("5 · Summarise", "once", "docs/<bug-name>.md", " · why it was missed"),
        ],
        "columns": [
            ("UI / browser", ["Console and network on", "the failing path; check", "hydration and caches."]),
            ("Server / API", ["Find the request in logs;", "call it directly; ours", "or the upstream's?"]),
            ("CI / tooling", ["First error, not last line;", "compare versions; rerun", "once for flaky."]),
        ],
        "command": "/bgw-debug-flow <symptom>",
    },
    {
        "file": "bgw-review-flow",
        "kicker": "Claude skill · code review",
        "title": ["READ WIDE,", "REPORT NARROW."],
        "subtitle": "Reads around the diff. Reports only what the diff causes.",
        "rows": [
            ("1 · Target", "from the argument", "PR · branch · staged · commit", " · re-review if a file exists"),
            ("2 · Orient", "once", "/bgw-pr-brief · gh pr checks", " · /bgw-analysis-flow"),
            ("3 · Findings", "evidence bar", "blocker=verified  warning=read", "  assumed→question"),
            ("4 · Checkpoint", "stop", "counts · findings · questions", " · recommended verdict"),
            ("5 · Deliver", "after your yes", "pending review on GitHub", " · own code stays local"),
        ],
        "columns": [
            ("Repo rules win", ["Severities, format and", "area skills come from", "the repo when it has them."]),
            ("Never posts alone", ["Draft review only after", "your yes. You submit", "it yourself."]),
            ("Re-review", ["fixed · declined · open,", "checked in the code,", "then the new diff."]),
        ],
        "command": "/bgw-review-flow <PR> | staged | commit",
    },
    {
        "file": "bgw-improve-flow",
        "kicker": "Claude skill · improvement",
        "title": ["GOOD.", "NOW BETTER."],
        "subtitle": "A second look at finished work. Briefs, not edits.",
        "rows": [
            ("1 · Baseline", "once", "HEAD sha · commands · one test run", " · red stays red"),
            ("2 · Look", "8 lenses", "simpler · duplication · consistency", " · sturdy · tests · next"),
            ("Tags", "on every item", "introduced  pre-existing", "  + evidence label"),
            ("3 · Checkpoint", "stop", "table by value · next steps apart", " · rejected"),
            ("4 · Briefs", "you pick", "sha · excerpts · steps · STOP", " → /bgw-task-flow"),
        ],
        "columns": [
            ("Baseline first", ["Tests red before the", "pass are never blamed", "on the change."]),
            ("Old debt counts", ["Pre-existing items in", "the touched code are", "kept, not dropped."]),
            ("Never edits", ["Writes only its own", "file. Fixes go through", "/bgw-task-flow."]),
        ],
        "command": "/bgw-improve-flow [staged | commit | path]",
    },
    {
        "file": "bgw-pr-brief",
        "kicker": "Claude skill · PR briefing",
        "title": ["A BIG PR,", "MADE READABLE."],
        "subtitle": "Five sections, grounded in the diff, not the description.",
        "rows": [
            ("1 · Purpose", "≤ 3 sentences", "why it exists", " · what breaks without it"),
            ("2 · Summary", "non-technical", "what a user or caller notices", " · or 'nothing visible'"),
            ("3 · How to review", "reading order", "files by kind and lines", " · where to stop"),
            ("4 · How to test", "concrete steps", "happy path · edge cases", " · the failure path"),
            ("5 · Questions", "for the author", "only ones the diff can't answer", ""),
        ],
        "columns": [
            ("Read-only", ["No comments, no reviews,", "nothing written to", "GitHub."]),
            ("Diff over claims", ["Where description and", "diff disagree, the diff", "wins: it's a question."]),
            ("No verdict", ["A briefing, not a grade.", "You form the opinion."]),
        ],
        "command": "/bgw-pr-brief <PR>",
    },
    {
        "file": "bgw-qa-walk",
        "kicker": "Claude skill · browser QA",
        "title": ["SEE IT.", "DON'T INFER IT."],
        "subtitle": "A browser walkthrough of a UI change.",
        "rows": [
            ("Before", "you confirm", "URL · route · tenant · role", " · flags · seed data"),
            ("Walk", "per path", "happy path first", " · then each edge case"),
            ("Capture", "per path", "final state + every failure", " · console · network"),
            ("Report", "table", "path | expected | observed | pass/fail", ""),
        ],
        "columns": [
            ("Observed means seen", ["An empty 'observed' cell", "means nobody looked."]),
            ("Names the gaps", ["Any state it couldn't", "reach, and why."]),
            ("No code-reading passes", ["Never infers a pass", "from code it read."]),
        ],
        "command": "/bgw-qa-walk",
    },
    {
        "file": "bgw-explain",
        "kicker": "Claude skill · explanation",
        "title": ["PLAIN WORDS,", "REAL EXAMPLE."],
        "subtitle": "Stops the work and explains, in simple Romanian.",
        "rows": [
            ("Input", "optional", "/bgw-explain", " · /bgw-explain junction · eroarea de mai sus"),
            ("1 · Pe scurt", "one sentence", "ce e, pe scurt", ""),
            ("2 · Cum funcționează", "steps", "mecanismul, pas cu pas", " · exemplu din sesiune"),
            ("3 · De ce contează aici", "consequence", "ce se strică · cine observă", ""),
            ("4 · De reținut", "1–2 lines", "ce iei cu tine", " · + Mermaid when it's a flow"),
        ],
        "columns": [
            ("Romanian", ["The simplest words that", "are still correct."]),
            ("Terms kept", ["English term, Romanian", "gloss the first time."]),
            ("Never false", ["A simplification that", "drops a case says so."]),
        ],
        "command": "/bgw-explain [term | error | file]",
    },
    {
        "file": "bgw-plain",
        "kicker": "Output style · every message",
        "title": ["RESULT FIRST,", "THEN WHY."],
        "subtitle": "Every chat message: short, explained, in Romanian.",
        "rows": [
            ("1 · Result", "first sentence", "what happened, or the answer", ""),
            ("2 · Mechanism", "2–4 sentences", "X se întâmplă, deci Y", " · a real example"),
            ("3 · Consequence", "when it matters", "what breaks · who notices", " · what it costs"),
            ("Language", "split", "chat + analyses: română", " · repo + people: English"),
        ],
        "columns": [
            ("Always on", ["Selected once in", "Settings; applies to", "every new session."]),
            ("Coding intact", ["keep-coding-instructions", "is true, so the coding", "rules stay."]),
            ("Full detail", ["Errors, warnings and", "confirmations keep", "their full content."]),
        ],
        "command": "Settings → Claude Code → Output style",
    },
]


def t(x, y, s, size, fill, family=SANS, weight=400, anchor="start", spacing=0):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'letter-spacing="{spacing}">{escape(s)}</text>')


def card(c):
    longest = max(len(line) for line in c["title"])
    # Arial, the fallback on most machines, runs wider than Inter at heavy weights.
    size = min(104, int(INNER / (longest * 0.74)))
    lh = size * 0.95
    title_top = 150
    parts = [
        t(PAD, 58, "Bogdan Dimoiu", 20, "#ffffff", weight=600),
        t(W - PAD, 58, c["kicker"], 13, "#d6d6d6", family=MONO, anchor="end"),
    ]
    for i, line in enumerate(c["title"]):
        parts.append(t(PAD - 3, title_top + size * 0.8 + i * lh, line, size, "#ffffff",
                       weight=800, spacing=-size * 0.02))
    sub_y = title_top + size * 0.8 + (len(c["title"]) - 1) * lh + 58
    parts.append(t(PAD, sub_y, c["subtitle"], 21, "#9b9b9b"))
    body_y = sub_y + 52

    card_y = body_y + 36
    card_h = len(c["rows"]) * ROW_H
    rows = [f'<rect x="{PAD}" y="{card_y}" width="{INNER}" height="{card_h}" rx="14" fill="#0d0d0d"/>']
    for i, (label, tag, main, dim) in enumerate(c["rows"]):
        y = card_y + i * ROW_H
        if i:
            rows.append(f'<line x1="{PAD}" x2="{W - PAD}" y1="{y}" y2="{y}" stroke="#262626"/>')
        rows.append(t(PAD + 20, y + 26, label, 11.5, "#9a9a9a", family=MONO))
        rows.append(t(W - PAD - 20, y + 26, tag, 11.5, "#9a9a9a", family=MONO, anchor="end"))
        rows.append(f'<text x="{PAD + 20}" y="{y + 52}" font-family="{MONO}" font-size="15">'
                    f'<tspan fill="#ededed">{escape(main)}</tspan>'
                    f'<tspan fill="#6f6f6f">{escape(dim)}</tspan></text>')

    col_y = card_y + card_h + 46
    col_w = (INNER - 2 * 24) / 3
    cols = []
    for i, (head, lines) in enumerate(c["columns"]):
        x = PAD + i * (col_w + 24)
        cols.append(t(x, col_y, f"0{i + 1}", 11.5, "#6f6f6f", family=MONO))
        cols.append(t(x, col_y + 32, head, 19, "#111111", weight=600))
        for j, line in enumerate(lines):
            cols.append(t(x, col_y + 60 + j * 21, line, 14.5, "#5c5c5c"))

    foot_y = col_y + 60 + 3 * 21 + 34
    H = foot_y + 58
    foot = [
        f'<line x1="{PAD}" x2="{W - PAD}" y1="{foot_y}" y2="{foot_y}" stroke="#cfcfcf"/>',
        t(PAD, foot_y + 32, c["command"], 13, "#111111", family=MONO),
        t(W - PAD, foot_y + 32, "bgw-skills", 13, "#111111", family=MONO, anchor="end"),
    ]
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}">',
        f'<title>{escape(c["file"])}</title>',
        f'<rect width="{W}" height="{H:.0f}" fill="#0b0b0b"/>',
        f'<path d="M0 {body_y + 32} Q0 {body_y} 32 {body_y} H{W - 32} Q{W} {body_y} {W} {body_y + 32} V{H:.0f} H0 Z" fill="#ebebeb"/>',
        *parts, *rows, *cols, *foot,
        "</svg>",
    ])


if __name__ == "__main__":
    out = Path(__file__).parent
    for c in CARDS:
        (out / f'{c["file"]}.svg').write_text(card(c), encoding="utf-8")
        print("wrote", c["file"])
