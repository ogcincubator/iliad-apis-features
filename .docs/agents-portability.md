# Agent & Skill Portability: Claude Code, GitHub Copilot, OpenAI Codex

Summary of how portable the agents, skills, prompts, and repo-context files in this repository are between the three mainstream agentic coding platforms, and what to do about it.

## Summary

The *body* of an agent or prompt (the Markdown prose, code blocks, examples) is portable. The *frontmatter*, directory layout, tool names, invocation semantics, and templating syntax are not. There is no universal spec today. `AGENTS.md` is an emerging shared convention for repo-level guidance, but it does not cover subagents or on-demand skills.

## How the three platforms differ

| Concern | Claude Code | GitHub Copilot | OpenAI Codex |
|---|---|---|---|
| Repo-level context file | `CLAUDE.md` (also reads `AGENTS.md`) | `.github/copilot-instructions.md` | `AGENTS.md` (primary) |
| Subagent / chat-mode files | `.claude/agents/*.md` with `name`, `description`, `tools`, `model` | `.github/chatmodes/*.chatmode.md` with `mode`, `description`, `tools`, `model` | No first-class subagent concept; nested `AGENTS.md` files scope behaviour per directory |
| Reusable skills | `.claude/skills/<name>/SKILL.md` with `name`, `description` | No equivalent (there are "instructions" with an `applyTo` glob, but they auto-attach, they don't load on demand) | No equivalent |
| Slash commands / prompts | `.claude/commands/*.md`; templating via `$ARGUMENTS` | `.github/prompts/*.prompt.md`; templating via `{{selection}}` / `${input:...}` | No first-class concept; prompts are just prose inside `AGENTS.md` |
| Tool allowlist syntax | Comma-separated tool names: `tools: Read, Write, Bash` | Array of tool groups: `tools: ['read', 'edit', 'terminal']` | Inferred from sandbox policy; not declared per-agent |
| Model field | `sonnet`, `opus`, `haiku` | Model names like `GPT-4o`, `Claude Sonnet 4` | Set at CLI launch, not per-agent |
| Auto-selection of an agent | Orchestrator reads `description:` and matches against user request | User manually selects the chat mode from a picker | Single agent scoped by `AGENTS.md`; no selection step |

## What actually ports cleanly

- **Repo-wide guidance.** `AGENTS.md` is the closest thing to common ground. Claude Code, Codex, Cursor, Aider, and several other tools all read it on session start. It is fine for describing what the repo is, the build process, conventions, and pointers to the agent ecosystem.
- **Markdown bodies.** Everything below the frontmatter — prose, JSON examples, schema snippets, Python helpers — is platform-agnostic. A Claude agent body can be pasted into a Copilot chatmode and do roughly the same job once triggered.
- **Prompt intent and examples.** The "when to use this" and "example outputs" sections are portable content; only the trigger metadata and templating placeholders change.

## What does not port cleanly

- **Skills are Claude-only.** There is no Copilot or Codex analogue to Claude's on-demand skill loader. The eight `SKILL.md` files in this repo will remain Claude-specific. The underlying capability (CSV → metadata, NetCDF → STAC, etc.) can still be described in prose for Codex and Copilot to do inline, but the load-on-keyword behaviour does not exist there.
- **Invocation semantics.** Copilot chatmodes are user-selected from a picker. Claude Code subagents are auto-selected by the parent Claude based on `description:` matching the user's request. Codex has neither — it runs as one agent scoped by `AGENTS.md`. The `@agent-name ...` syntax used in this repo's current prose is not a real command on any of the three; it is documentation convention only.
- **Templating.** `{{selection}}` (Copilot), `$ARGUMENTS` (Claude commands), and plain prose (Codex) are mutually incompatible. Any prompt that uses one must be rewritten for the others.
- **Tool allowlists.** Different naming, different granularity, different execution model. Not mechanically convertible.

## Practical strategies for portability

1. **Single source + generator script.** Author one canonical YAML/Markdown file per agent and generate `.claude/agents/`, `.github/chatmodes/`, and per-directory `AGENTS.md` stubs from it with a small build script. Cleanest long-term, but homegrown.
2. **Ruler** (`github.com/intellectronica/ruler`). Open-source tool built for this problem. You author agent rules once; it writes out Claude Code, Cursor, Copilot, Aider, and Codex configs. Covers repo-level instructions and agent definitions reasonably well. Does not handle Claude's skill system.
3. **Symlinks for repo-level context.** `.github/copilot-instructions.md` → `AGENTS.md` → `CLAUDE.md`, all pointing at the same file. Crude but works. Breaks down for per-agent files because each platform's frontmatter diverges.
4. **Shared bodies, per-platform frontmatter shims.** Keep the canonical body as the Claude agent file. Generate minimal Copilot chatmode files that either `include` the body or paraphrase it. Accept some drift or keep it in sync via CI.

## Concrete recommendation for `iliad-apis-features`

Assuming the repo stays primarily Claude Code–focused but wants to stay friendly to Copilot and Codex users:

1. **Consolidate repo-level context into `AGENTS.md` at the root.** Symlink `CLAUDE.md` → `AGENTS.md` and `.github/copilot-instructions.md` → `AGENTS.md`. This gives Codex full fidelity and gives Claude Code / Copilot a shared baseline.
2. **Keep subagents canonical in `.claude/agents/`.** Claude Code is the only one of the three with a real multi-agent model, so this is where the agents are most useful. For Copilot parity, generate thin `.github/chatmodes/*.chatmode.md` stubs via a script so they don't drift.
3. **Accept that skills are Claude-only.** Don't port `.skills/` to Copilot or Codex. In `AGENTS.md`, describe each skill's underlying capability in prose so Codex and Copilot can do the equivalent work inline without the loader.
4. **For prompts / slash commands:** keep them in `.claude/commands/` for Claude and rewrite as `.github/prompts/*.prompt.md` for Copilot if needed. Codex does not need them — users just describe the task.
5. **Consider Ruler** if the cost of running a homegrown sync script is higher than the cost of adopting a tool. Good fit for teams that already use Cursor or Aider alongside these three.

100% portability is not realistic today. Aim for ~80%: shared repo context, shared agent bodies, per-platform frontmatter shims, and a documented acceptance that skills are Claude-only.

## References

- `AGENTS.md` convention — https://agents.md
- Claude Code subagent format — https://docs.claude.com/en/docs/claude-code/sub-agents
- Claude Code skills — https://docs.claude.com/en/docs/claude-code/skills
- GitHub Copilot custom chat modes — https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-custom-chat-modes
- OpenAI Codex CLI — https://github.com/openai/codex
- Ruler (cross-platform rule sync) — https://github.com/intellectronica/ruler
