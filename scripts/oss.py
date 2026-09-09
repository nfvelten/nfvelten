#!/usr/bin/env python3
"""Render oss.svg: the upstream projects I have contributed to."""

import json
import re
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
# retransmission/retransmission#295 cherry-picked and merged my
# transmission/transmission#9096, opened by ckerr (search API only finds PRs
# authored by me).
MANUAL_MERGED = {"corosolto/client", "retransmission/retransmission"}
MANUAL_REVIEW = set()

# A repo only ever leaves the card if its PR is deleted, so a shorter answer from
# the search API means the API came back short, not that the work went away.
RENDERED = re.compile(r'--ui3\)">([^<]+)/</tspan><tspan\s+fill="var\(--tx\)">([^<]+)<'
                      r'.*?font-size="9"[^>]*>([A-Z ]+)<', re.S)

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


def rendered():
    """Repo -> status already on the card, so a short search cannot erase it."""
    try:
        svg = open(OUT).read()
    except FileNotFoundError:
        return {}
    return {f"{owner}/{name}": status.lower()
            for owner, name, status in RENDERED.findall(svg)
            if f"{owner}/{name}" not in SKIP_REPOS and owner not in MINE}


def collect():
    merged = search("--merged") | MANUAL_MERGED
    review = (search("--state", "open") | MANUAL_REVIEW) - merged
    status = dict.fromkeys(merged, "merged") | dict.fromkeys(review, "in review")

    was = rendered()
    lost = sorted(r for r in was if r not in status)
    demoted = sorted(r for r, s in was.items()
                     if s == "merged" and status.get(r) == "in review")
    if lost or demoted:
        raise SystemExit(f"search came back short (lost {lost}, demoted {demoted}); "
                         "card left as is")

    order = {"merged": 0, "in review": 1}
    return sorted(status.items(), key=lambda e: (order[e[1]], e[0].lower()))


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
