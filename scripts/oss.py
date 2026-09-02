#!/usr/bin/env python3
"""Regenerate the Open source section of README.md from my upstream pull requests."""

import json
import re
import subprocess

README = "README.md"
START = "<!-- OSS:START -->"
END = "<!-- OSS:END -->"

# Repos I own or co-own: covered by the Projects section instead.
MINE = {"nfvelten", "mateCreations", "arbitusgateway", "harbefas"}
# Link-only contributions to awesome-lists add no signal here.
SKIP_REPOS = {"bh-rat/awesome-mcp-enterprise", "Puliczek/awesome-mcp-security"}


def search(*flags):
    out = subprocess.run(
        ["gh", "search", "prs", "--author", "nfvelten", "--limit", "100",
         "--visibility", "public",
         "--json", "repository,title,number,url", *flags],
        capture_output=True, text=True, check=True,
    ).stdout
    prs = []
    for pr in json.loads(out):
        repo = pr["repository"]["nameWithOwner"]
        if repo.split("/")[0] in MINE or repo in SKIP_REPOS:
            continue
        prs.append(pr)
    return sorted(prs, key=lambda p: p["repository"]["nameWithOwner"].lower())


def title(raw):
    """Drop the conventional-commit prefix and escape brackets so links stay valid."""
    text = re.sub(r"^\w+(\([^)]*\))?!?:\s*", "", raw)
    text = text[:1].upper() + text[1:]
    return text.replace("[", "\\[").replace("]", "\\]")


def table(prs):
    rows = ["| Change | Project |", "|--------|---------|"]
    for pr in prs:
        repo = pr["repository"]["nameWithOwner"]
        owner, name = repo.split("/")
        avatar = f'<img src="https://github.com/{owner}.png?size=20" width="20" height="20" align="top"/>'
        label = name if owner.lower() in (name.lower(), name.lower() + "sh") else repo
        rows.append(
            f'| [{title(pr["title"])}]({pr["url"]}) '
            f'| {avatar} [{label}](https://github.com/{repo}) |'
        )
    return "\n".join(rows)


def main():
    merged = search("--merged")
    review = search("--state", "open")

    body = ["## Open source", ""]
    if merged:
        body += ["Merged upstream:", "", table(merged), ""]
    if review:
        body += ["In review:", "", table(review), ""]

    readme = open(README).read()
    block = f"{START}\n\n" + "\n".join(body).rstrip() + f"\n\n{END}"
    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END), lambda _: block, readme, flags=re.S
    )
    if updated != readme:
        open(README, "w").write(updated)


if __name__ == "__main__":
    main()
