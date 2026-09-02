<div align="center">

<img src="card.svg" alt="Nicholas Velten" width="900"/>

</div>

<br/>

## Projects

| Project | Stack |
|---------|-------|
| [**Arbitus**](https://github.com/arbitusgateway/arbitus) — Security proxy for MCP servers. Per-agent auth, tool allowlists, audit logging. | `Rust` |
| [**Agent Code Buddy**](https://github.com/harbefas/agent-code-buddy) — Human-in-the-loop approvals for AI agent tool calls via Android. | `Java · Android · Python` |
| [**Paperboy**](https://github.com/harbefas/paperboy) — Keyboard-first local-first RSS reader and podcast player for new tab. | `JavaScript` |
| **agent-memory** *(Rust rewrite in progress)* — Semantic memory layer for AI agents. | `Rust` |

## Agent interface

My portfolio exposes a small read-only MCP service for agents that need to inspect my engineering background, project evidence or role direction.

```text
https://www.nicholas-velten.xyz/mcp
```

Available operations:

- `get_resume` — structured professional history, skills and evidence
- `get_projects` — public software projects and AI systems
- `get_availability` — the kinds of engineering work I am pursuing
- `prepare_intro` — a grounded introduction for a target role or company

Claude Code:

```bash
claude mcp add --transport http nicholas-velten https://www.nicholas-velten.xyz/mcp
```

Generic MCP configuration:

```json
{
  "mcpServers": {
    "nicholas-velten": {
      "url": "https://www.nicholas-velten.xyz/mcp"
    }
  }
}
```

Other machine-readable entry points:

- [Structured resume](https://www.nicholas-velten.xyz/api/resume.json)
- [Plain-text resume](https://www.nicholas-velten.xyz/api/resume.txt)
- [Agent guidance](https://www.nicholas-velten.xyz/AGENTS.md)
- [Portfolio MCP skill](https://www.nicholas-velten.xyz/.well-known/agent-skills/portfolio-mcp/SKILL.md)

Useful prompts include: *Which production problems has Nicholas solved? What evidence supports his fit for full-stack, backend, platform or AI agent infrastructure roles?*

## Open source

Merged upstream:

| Change | Project |
|--------|---------|
| [Complete attached long flag values](https://github.com/jdx/usage/pull/1349) | [jdx/usage](https://github.com/jdx/usage) |
| [Use `CURLOPT_PROTOCOLS_STR` where available](https://github.com/eafer/rdrview/pull/50) | [eafer/rdrview](https://github.com/eafer/rdrview) |
| [Return a JSON body when `/torrents` rejects a request](https://github.com/YouROK/TorrServer/pull/848) | [YouROK/TorrServer](https://github.com/YouROK/TorrServer) |
| [Allow hiding the key-binding hint bar](https://github.com/bjarneo/cliamp/pull/404) | [bjarneo/cliamp](https://github.com/bjarneo/cliamp) |
| [Trim a credit list to the first name in `search_author`](https://github.com/calibrain/shelfmark/pull/1290) | [calibrain/shelfmark](https://github.com/calibrain/shelfmark) |

In review:

| Change | Project |
|--------|---------|
| [Support `x.pe` peer addresses in magnet links](https://github.com/transmission/transmission/pull/9095) | [transmission](https://github.com/transmission/transmission) |
| [Collapse `is_martian_addr()` into `is_valid_for_peers()`](https://github.com/transmission/transmission/pull/9096) | [transmission](https://github.com/transmission/transmission) |
| [Refresh a playlist after rating changes](https://github.com/navidrome/navidrome/pull/6066) | [navidrome](https://github.com/navidrome/navidrome) |
| [Add `--initial-events` to emit events for existing paths](https://github.com/watchexec/watchexec/pull/1104) | [watchexec](https://github.com/watchexec/watchexec) |
| [Show the delete shortcut in search help](https://github.com/atuinsh/atuin/pull/4039) | [atuin](https://github.com/atuinsh/atuin) |
| [Restore scrolling to the top on a second `G`/`End`](https://github.com/tstack/lnav/pull/1746) | [lnav](https://github.com/tstack/lnav) |
| [Emit a real edit when inserting past the last line](https://github.com/stevearc/conform.nvim/pull/898) | [conform.nvim](https://github.com/stevearc/conform.nvim) |
| [Reset the reader when changing books](https://github.com/gotson/komga/pull/2416) | [komga](https://github.com/gotson/komga) |
| [Scope returned cookies to the requested page](https://github.com/ThePhaseless/Byparr/pull/409) | [Byparr](https://github.com/ThePhaseless/Byparr) |
| [Do not hang mpv when no session bus is available](https://github.com/hoyon/mpv-mpris/pull/145) | [mpv-mpris](https://github.com/hoyon/mpv-mpris) |

## Writing

Notes on software, tools and the work of building things — [nicholas-velten.xyz](https://nicholas-velten.xyz)

---

[nicholas-velten.xyz](https://nicholas-velten.xyz) · [LinkedIn](https://linkedin.com/in/nicholasvelten) · nicholasfvelten@gmail.com
