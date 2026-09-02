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

Merged upstream:

| Change | Project |
|--------|---------|
| [Allow hiding the key-binding hint bar](https://github.com/bjarneo/cliamp/pull/404) | <img src="https://github.com/bjarneo.png?size=20" width="20" height="20" align="top"/> [bjarneo/cliamp](https://github.com/bjarneo/cliamp) |
| [Trim a credit list in search_author to the first name](https://github.com/calibrain/shelfmark/pull/1290) | <img src="https://github.com/calibrain.png?size=20" width="20" height="20" align="top"/> [calibrain/shelfmark](https://github.com/calibrain/shelfmark) |
| [Use CURLOPT_PROTOCOLS_STR where available](https://github.com/eafer/rdrview/pull/50) | <img src="https://github.com/eafer.png?size=20" width="20" height="20" align="top"/> [eafer/rdrview](https://github.com/eafer/rdrview) |
| [Complete attached long flag values](https://github.com/jdx/usage/pull/1349) | <img src="https://github.com/jdx.png?size=20" width="20" height="20" align="top"/> [jdx/usage](https://github.com/jdx/usage) |
| [Return a JSON body when /torrents rejects a request](https://github.com/YouROK/TorrServer/pull/848) | <img src="https://github.com/YouROK.png?size=20" width="20" height="20" align="top"/> [YouROK/TorrServer](https://github.com/YouROK/TorrServer) |

In review:

| Change | Project |
|--------|---------|
| [Fix Comment mode help alignment](https://github.com/agavra/tuicr/pull/667) | <img src="https://github.com/agavra.png?size=20" width="20" height="20" align="top"/> [agavra/tuicr](https://github.com/agavra/tuicr) |
| [Show delete shortcut in help](https://github.com/atuinsh/atuin/pull/4039) | <img src="https://github.com/atuinsh.png?size=20" width="20" height="20" align="top"/> [atuin](https://github.com/atuinsh/atuin) |
| [Substitui a action local fantasma do issues-bot pelos passos reais](https://github.com/corosolto/client/pull/490) | <img src="https://github.com/corosolto.png?size=20" width="20" height="20" align="top"/> [corosolto/client](https://github.com/corosolto/client) |
| [Reset reader when changing books](https://github.com/gotson/komga/pull/2416) | <img src="https://github.com/gotson.png?size=20" width="20" height="20" align="top"/> [gotson/komga](https://github.com/gotson/komga) |
| [Don't hang mpv when no session bus is available](https://github.com/hoyon/mpv-mpris/pull/145) | <img src="https://github.com/hoyon.png?size=20" width="20" height="20" align="top"/> [hoyon/mpv-mpris](https://github.com/hoyon/mpv-mpris) |
| [Refresh playlist after rating changes](https://github.com/navidrome/navidrome/pull/6066) | <img src="https://github.com/navidrome.png?size=20" width="20" height="20" align="top"/> [navidrome](https://github.com/navidrome/navidrome) |
| [Point the PKGBUILD at the current repo and release](https://github.com/omacom/ttfx/pull/23) | <img src="https://github.com/omacom.png?size=20" width="20" height="20" align="top"/> [omacom/ttfx](https://github.com/omacom/ttfx) |
| [Add a setting to hide the lyrics button](https://github.com/stappmus/Omarchy-Spotify/pull/46) | <img src="https://github.com/stappmus.png?size=20" width="20" height="20" align="top"/> [stappmus/Omarchy-Spotify](https://github.com/stappmus/Omarchy-Spotify) |
| [Restore the bindings.lua instructions for Super+Shift+M](https://github.com/stappmus/Omarchy-Spotify/pull/44) | <img src="https://github.com/stappmus.png?size=20" width="20" height="20" align="top"/> [stappmus/Omarchy-Spotify](https://github.com/stappmus/Omarchy-Spotify) |
| [Emit a real edit when inserting past the last line](https://github.com/stevearc/conform.nvim/pull/898) | <img src="https://github.com/stevearc.png?size=20" width="20" height="20" align="top"/> [stevearc/conform.nvim](https://github.com/stevearc/conform.nvim) |
| [Scope returned cookies to the requested page](https://github.com/ThePhaseless/Byparr/pull/409) | <img src="https://github.com/ThePhaseless.png?size=20" width="20" height="20" align="top"/> [ThePhaseless/Byparr](https://github.com/ThePhaseless/Byparr) |
| [Collapse is_martian_addr() into is_valid_for_peers()](https://github.com/transmission/transmission/pull/9096) | <img src="https://github.com/transmission.png?size=20" width="20" height="20" align="top"/> [transmission](https://github.com/transmission/transmission) |
| [Support x.pe peer addresses in magnet links](https://github.com/transmission/transmission/pull/9095) | <img src="https://github.com/transmission.png?size=20" width="20" height="20" align="top"/> [transmission](https://github.com/transmission/transmission) |
| [\[listview\] restore scrolling to the top on a second G/End](https://github.com/tstack/lnav/pull/1746) | <img src="https://github.com/tstack.png?size=20" width="20" height="20" align="top"/> [tstack/lnav](https://github.com/tstack/lnav) |
| [Add --initial-events to emit events for existing paths](https://github.com/watchexec/watchexec/pull/1104) | <img src="https://github.com/watchexec.png?size=20" width="20" height="20" align="top"/> [watchexec](https://github.com/watchexec/watchexec) |

<!-- OSS:END -->

## Writing

Notes on software, tools and the work of building things — [nicholas-velten.xyz](https://nicholas-velten.xyz)

---

[nicholas-velten.xyz](https://nicholas-velten.xyz) · [LinkedIn](https://linkedin.com/in/nicholasvelten) · nicholasfvelten@gmail.com
