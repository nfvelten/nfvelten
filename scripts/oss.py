#!/usr/bin/env python3
"""Render oss.svg: the upstream projects I have contributed to."""

import json
import subprocess

import theme

OUT = "oss.svg"
README = "README.md"
START = "<!-- OSS:START -->"
END = "<!-- OSS:END -->"

# Repos I own or co-own: the Projects card covers those.
MINE = {"nfvelten", "mateCreations", "arbitusgateway", "harbefas"}
# Link-only entries in awesome-lists say nothing about the code.
SKIP_REPOS = {"bh-rat/awesome-mcp-enterprise", "Puliczek/awesome-mcp-security"}
# Merged elsewhere after the maintainer deleted my PR (search API only finds PRs
# still attributed to me): corosolto/client#490, folded into #500 by the maintainer.
MANUAL_MERGED = {"corosolto/client"}

COLS = 4
CELL_W, CELL_H = 197, 52
PAD_Y = 96
AVATAR = 26


def search(*flags):
    out = subprocess.run(
        ["gh", "search", "prs", "--author", "nfvelten", "--limit", "100",
         "--visibility", "public", "--json", "repository", *flags],
        capture_output=True, text=True, check=True,
    ).stdout
    names = {pr["repository"]["nameWithOwner"] for pr in json.loads(out)} - SKIP_REPOS
    return {r for r in names if r.split("/")[0] not in MINE}


def collect():
    merged = search("--merged") | MANUAL_MERGED
    review = search("--state", "open") - merged
    entries = [(r, "merged") for r in merged] + [(r, "in review") for r in review]
    order = {"merged": 0, "in review": 1}
    return sorted(entries, key=lambda e: (order[e[1]], e[0].lower()))


def render(entries):
    rows = -(-len(entries) // COLS)
    height = PAD_Y + rows * CELL_H + 24
    colors = {"merged": "var(--ac)", "in review": "var(--yl)"}

    defs, cells = [], []
    for i, (repo, status) in enumerate(entries):
        owner, name = repo.split("/")
        x = theme.MARGIN + (i % COLS) * CELL_W
        y = PAD_Y + (i // COLS) * CELL_H
        defs.append(f'<clipPath id="c{i}"><circle cx="{x + AVATAR // 2}" '
                    f'cy="{y + AVATAR // 2}" r="{AVATAR // 2}"/></clipPath>')
        cells.append(f"""<image x="{x}" y="{y}" width="{AVATAR}" height="{AVATAR}"
  clip-path="url(#c{i})" href="{theme.avatar(owner)}"/>
<text x="{x + AVATAR + 10}" y="{y + 12}" font-family="{theme.SERIF}"
  font-size="14"><tspan fill="var(--ui3)">{theme.esc(owner)}/</tspan><tspan
  fill="var(--tx)">{theme.esc(name)}</tspan></text>
<text x="{x + AVATAR + 10}" y="{y + 26}" font-family="{theme.MONO}"
  font-size="9" letter-spacing="1.5" fill="{colors[status]}">{status.upper()}</text>""")

    body = theme.header("Open source", "UPSTREAM CONTRIBUTIONS") + "\n\n" + "\n".join(cells)
    return theme.svg(height, body, "\n".join(defs))


if __name__ == "__main__":
    open(OUT, "w").write(render(collect()))
    theme.embed(OUT, README, START, END, "Open source")
