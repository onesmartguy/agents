# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a Claude Code plugin marketplace repository containing 76 focused, single-purpose plugins that provide 167 specialized AI agents, 89 agent skills, and 87 development tools for intelligent automation and multi-agent orchestration.

## Architecture

### Plugin Structure

Each plugin is isolated in `plugins/{plugin-name}/` with three optional subdirectories:

- `agents/` - Specialized agents (`.md` files with frontmatter)
- `commands/` - Slash commands and tools (`.md` files)
- `skills/` - Progressive disclosure knowledge packages (`SKILL.md` in subdirectories)

**Example plugin structure:**
```
plugins/python-development/
├── agents/
│   ├── python-pro.md
│   ├── django-pro.md
│   └── fastapi-pro.md
├── commands/
│   └── python-scaffold.md
└── skills/
    ├── async-python-patterns/SKILL.md
    ├── python-testing-patterns/SKILL.md
    └── uv-package-manager/SKILL.md
```

### Marketplace Catalog

The `.claude-plugin/marketplace.json` file is the central registry containing all plugin definitions. Each plugin entry includes:

- Metadata (name, description, version, author, license)
- Paths to agents, commands, and skills
- Keywords and category for discoverability
- `strict: false` setting

### Agent Specifications

Agents use YAML frontmatter with:
- `name`: Hyphen-case identifier
- `description`: Agent purpose and when to use PROACTIVELY
- `model`: Either `sonnet` (complex reasoning) or `haiku` (fast execution)

### Skill Specifications

Skills follow the [Agent Skills Specification](https://github.com/anthropics/skills/blob/main/agent_skills_spec.md):
- Located in `plugins/{plugin}/skills/{skill-name}/SKILL.md`
- YAML frontmatter with `name` and `description` (must include "Use when" trigger criteria)
- Progressive disclosure architecture (metadata → instructions → resources)
- Optional `assets/` and `references/` subdirectories for examples

## Common Development Tasks

### Testing Plugin Structure

To verify plugin structure integrity:
```bash
# Check marketplace.json is valid JSON
cat .claude-plugin/marketplace.json | python3 -m json.tool > /dev/null

# List all plugins
cat .claude-plugin/marketplace.json | python3 -c "import json, sys; plugins = json.load(sys.stdin)['plugins']; [print(p['name']) for p in plugins]"
```

### Adding a New Plugin

1. Create plugin directory: `plugins/{plugin-name}/`
2. Create agents in `plugins/{plugin-name}/agents/*.md` with proper frontmatter
3. Create commands in `plugins/{plugin-name}/commands/*.md`
4. Optionally add skills in `plugins/{plugin-name}/skills/{skill-name}/SKILL.md`
5. Update `.claude-plugin/marketplace.json` with plugin definition following existing patterns
6. Set version to current marketplace version (check existing plugins)

### Adding Skills to a Plugin

Skills use progressive disclosure for token efficiency:

1. Create directory: `plugins/{plugin}/skills/{skill-name}/`
2. Create `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: What it does. Use when [trigger criteria].
   ---
   ```
3. Add skill content using progressive disclosure (core instructions first, examples later)
4. Optional: Add `assets/` or `references/` subdirectories for supplementary content
5. Add skill path to plugin's `skills` array in marketplace.json

### Modifying Agents

When updating agent files:
- Maintain YAML frontmatter structure
- Keep description focused on "what" and "when to use PROACTIVELY"
- Use `model: sonnet` for complex reasoning/architecture
- Use `model: haiku` for fast execution/deterministic tasks
- Follow existing agent patterns in the same category

### Updating Marketplace

When modifying `.claude-plugin/marketplace.json`:
- Maintain alphabetical or categorical ordering
- Increment version numbers consistently
- Ensure all paths are relative to plugin source directory
- Keep plugin descriptions concise (5-10 words for focused purpose)

## Design Principles

### Single Responsibility
- Each plugin does ONE thing well
- Average 3.4 components per plugin (follows Anthropic's 2-8 pattern)
- Composable through multi-plugin workflows

### Minimal Token Usage
- Install only needed plugins
- Skills use progressive disclosure (load knowledge on demand)
- No bloated multi-purpose plugins

### Hybrid Model Orchestration
- Haiku agents (52): Fast execution, deterministic tasks (generation, tests, docs, deployments)
- Sonnet agents (110): Complex reasoning, architecture (design, reviews, security, AI/ML)
- Unspecified (5): Agents without explicit model assignments

### Granular Plugin Categories
- 25 categories (Development, Security, Operations, Languages, Infrastructure, AI-ML, etc.)
- 1-8 plugins per category for easy discovery
- Most plugins include agents, commands, or skills for complete workflows

## Key Files

- `.claude-plugin/marketplace.json` - Central plugin registry (all 76 plugin definitions)
- `docs/plugins.md` - Complete plugin catalog and reference
- `docs/agents.md` - All 167 agents organized by category with model assignments
- `docs/agent-skills.md` - 89 skills documentation and usage guide
- `docs/usage.md` - Command reference and workflow examples
- `docs/architecture.md` - Design principles and patterns
- `README.md` - Quick start and overview

## Workflow Examples

### Full-Stack Feature Development
Slash command: `/full-stack-orchestration:full-stack-feature`

Coordinates: backend-architect → database-architect → frontend-developer → test-automator → security-auditor → deployment-engineer → observability-engineer

### Security Hardening
Slash command: `/security-scanning:security-hardening --level comprehensive`

Multi-agent security with SAST, dependency scanning, code review

### Python Project Scaffolding
Slash command: `/python-development:python-scaffold fastapi-microservice`

Creates production-ready FastAPI project, activating async-python-patterns, python-testing-patterns, and uv-package-manager skills

## Important Notes

- Skills must include "Use when" criteria in description for proper activation
- All file paths in marketplace.json are relative to plugin source directory (e.g., `./agents/agent-name.md`)
- Agent names should use hyphen-case, be descriptive, and match filename
- Keep plugins focused - create new plugins rather than expanding existing ones
- Skills count: 89 across 28 plugins (Comic Production: 10, Backend: 5, LLM: 5, CI/CD: 5, Python: 5, Payment Processing: 5, K8s: 4, Cloud: 4, Blockchain: 4, JS/TS: 4, etc.)
