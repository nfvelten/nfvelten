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

<!-- OSS:START -->

## Open source

Merged:

[cliamp](https://github.com/bjarneo/cliamp) · [shelfmark](https://github.com/calibrain/shelfmark) · [rdrview](https://github.com/eafer/rdrview) · [usage](https://github.com/jdx/usage) · [TorrServer](https://github.com/YouROK/TorrServer)

In review:

[<img src="https://github.com/atuinsh.png?size=40" width="20" height="20" align="top"/> atuin](https://github.com/atuinsh/atuin) · [<img src="https://github.com/corosolto.png?size=40" width="20" height="20" align="top"/> corosolto/client](https://github.com/corosolto/client) · [<img src="https://github.com/navidrome.png?size=40" width="20" height="20" align="top"/> navidrome](https://github.com/navidrome/navidrome) · [<img src="https://github.com/omacom.png?size=40" width="20" height="20" align="top"/> ttfx](https://github.com/omacom/ttfx) · [<img src="https://github.com/transmission.png?size=40" width="20" height="20" align="top"/> transmission](https://github.com/transmission/transmission) · [<img src="https://github.com/watchexec.png?size=40" width="20" height="20" align="top"/> watchexec](https://github.com/watchexec/watchexec) · [tuicr](https://github.com/agavra/tuicr) · [komga](https://github.com/gotson/komga) · [mpv-mpris](https://github.com/hoyon/mpv-mpris) · [Omarchy-Spotify](https://github.com/stappmus/Omarchy-Spotify) · [conform.nvim](https://github.com/stevearc/conform.nvim) · [Byparr](https://github.com/ThePhaseless/Byparr) · [lnav](https://github.com/tstack/lnav)

<!-- OSS:END -->

## Writing

Notes on software, tools and the work of building things — [nicholas-velten.xyz](https://nicholas-velten.xyz)

---

[nicholas-velten.xyz](https://nicholas-velten.xyz) · [LinkedIn](https://linkedin.com/in/nicholasvelten) · nicholasfvelten@gmail.com
