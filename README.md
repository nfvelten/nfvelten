<div align="center">

<img src="card.svg" alt="Nicholas Velten" width="900"/>

</div>

<br/>

<div align="center">

[Arbitus](https://github.com/arbitusgateway/arbitus) · [Agent Code Buddy](https://github.com/harbefas/agent-code-buddy) · [Paperboy](https://github.com/harbefas/paperboy)

</div>

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

<img src="https://raw.githubusercontent.com/nfvelten/nfvelten/main/oss.svg?v=63b50358" alt="Open source" width="900"/>

<!-- OSS:END -->

## Writing

Notes on software, tools and the work of building things — [nicholas-velten.xyz](https://nicholas-velten.xyz)

---

[nicholas-velten.xyz](https://nicholas-velten.xyz) · [LinkedIn](https://linkedin.com/in/nicholasvelten) · nicholasfvelten@gmail.com
