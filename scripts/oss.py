#!/usr/bin/env python3
"""Render oss.svg: the upstream projects I have contributed to, as a card.

Avatars and the display font are embedded as data URIs because GitHub proxies
the SVG through camo, where external references never load.
"""

import base64
import json
import re
import subprocess
import urllib.request

CARD = "card.svg"       # source of the shared palette and the embedded font
OUT = "oss.svg"
README = "README.md"
START = "<!-- OSS:START -->"
END = "<!-- OSS:END -->"

# Repos I own or co-own: the Projects section covers those.
MINE = {"nfvelten", "mateCreations", "arbitusgateway", "harbefas"}
# Link-only entries in awesome-lists say nothing about the code.
SKIP_REPOS = {"bh-rat/awesome-mcp-enterprise", "Puliczek/awesome-mcp-security"}
COLS = 4
CELL_W, CELL_H = 197, 52
PAD_X, PAD_Y = 56, 96
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
    merged = search("--merged")
    review = search("--state", "open") - merged
    entries = [(r, "merged") for r in merged] + [(r, "in review") for r in review]
    order = {"merged": 0, "in review": 1}
    return sorted(entries, key=lambda e: (order[e[1]], e[0].lower()))


def avatar(owner):
    """Return a data URI. GitHub serves some avatars as JPEG despite the .png path."""
    url = f"https://github.com/{owner}.png?size=64"
    with urllib.request.urlopen(url, timeout=30) as r:
        raw = r.read()
    mime = "image/png" if raw[:8] == b"\x89PNG\r\n\x1a\n" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(raw).decode()}"


def font_face():
    return re.search(r"@font-face \{.*?\}", open(CARD).read(), re.S).group(0)


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(entries):
    rows = -(-len(entries) // COLS)
    height = PAD_Y + rows * CELL_H + 24
    colors = {"merged": "var(--ac)", "in review": "var(--yl)"}

    defs, cells = [], []
    for i, (repo, status) in enumerate(entries):
        owner = repo.split("/")[0]
        x = PAD_X + (i % COLS) * CELL_W
        y = PAD_Y + (i // COLS) * CELL_H
        defs.append(
            f'<clipPath id="c{i}"><circle cx="{x + AVATAR // 2}" cy="{y + AVATAR // 2}" '
            f'r="{AVATAR // 2}"/></clipPath>'
        )
        cells.append(f"""<image x="{x}" y="{y}" width="{AVATAR}" height="{AVATAR}"
  clip-path="url(#c{i})" href="{avatar(owner)}"/>
<text x="{x + AVATAR + 10}" y="{y + 12}" font-family="'EBG', Georgia, serif"
  font-size="14"><tspan fill="var(--ui3)">{esc(owner)}/</tspan><tspan
  fill="var(--tx)">{esc(repo.split("/")[1])}</tspan></text>
<text x="{x + AVATAR + 10}" y="{y + 26}" font-family="'Fira Code', 'Courier New', monospace"
  font-size="9" letter-spacing="1.5" fill="{colors[status]}">{status.upper()}</text>""")

    return f"""<svg width="900" height="{height}" viewBox="0 0 900 {height}"
  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<defs>
<style>
{font_face()}
:root {{ --bg: #282d1c; --ui: #4f5b4a; --ui3: #7a8573; --tx: #dce0d9;
  --ac: #7eb2d1; --yl: #a67c52; }}
@media (prefers-color-scheme: light) {{
  :root {{ --bg: #fbf1c7; --ui: #ddd2a0; --ui3: #928374; --tx: #3c3836;
    --ac: #076678; --yl: #b57614; }}
}}
</style>
{chr(10).join(defs)}
</defs>

<rect width="900" height="{height}" fill="var(--bg)"/>

<text x="56" y="52" font-family="'EBG', Georgia, serif" font-size="26"
  font-weight="700" fill="var(--tx)">Open source</text>
<text x="57" y="70" font-family="'Fira Code', 'Courier New', monospace"
  font-size="10" letter-spacing="3" fill="var(--ui3)">UPSTREAM CONTRIBUTIONS</text>
<line x1="56" y1="80" x2="844" y2="80" stroke="var(--ui)" stroke-width="1"/>

{chr(10).join(cells)}
</svg>
"""


def main():
    open(OUT, "w").write(render(collect()))
    block = (
        f'{START}\n\n## Open source\n\n<img src="{OUT}" alt="Upstream contributions" '
        f'width="900"/>\n\n{END}'
    )
    readme = open(README).read()
    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END), lambda _: block, readme, flags=re.S
    )
    if updated != readme:
        open(README, "w").write(updated)


if __name__ == "__main__":
    main()
