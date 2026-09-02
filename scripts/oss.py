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
SKIP_REPOS = {"bh-rat/awesome-mcp-enterprise", "Puliczek/awesome-mcp-security"}


def repos(*flags):
    out = subprocess.run(
        ["gh", "search", "prs", "--author", "nfvelten", "--limit", "100",
         "--visibility", "public", "--json", "repository", *flags],
        capture_output=True, text=True, check=True,
    ).stdout
    names = {pr["repository"]["nameWithOwner"] for pr in json.loads(out)}
    names -= SKIP_REPOS
    return sorted((r for r in names if r.split("/")[0] not in MINE), key=str.lower)


# Repo names that say nothing on their own: show them as owner/name.
GENERIC = {"client", "server", "core", "app", "cli", "web", "api", "docs", "site"}


def label(repo):
    name = repo.split("/")[1]
    return repo if name.lower() in GENERIC else name


def row(names):
    return " · ".join(f"[{label(r)}](https://github.com/{r})" for r in names)


def main():
    merged = repos("--merged")
    review = [r for r in repos("--state", "open") if r not in merged]

    body = ["## Open source", ""]
    if merged:
        body += ["Merged:", "", row(merged), ""]
    if review:
        body += ["In review:", "", row(review), ""]

    readme = open(README).read()
    block = f"{START}\n\n" + "\n".join(body).rstrip() + f"\n\n{END}"
    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END), lambda _: block, readme, flags=re.S
    )
    if updated != readme:
        open(README, "w").write(updated)


if __name__ == "__main__":
    main()
