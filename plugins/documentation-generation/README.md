# documentation-generation

> OpenAPI specification generation, Mermaid diagram creation, tutorial writing, API reference documentation

**Version:** 1.2.0
**Category:** documentation
**Author:** Seth Hobson

## Overview

### What This Plugin Does

OpenAPI specification generation, Mermaid diagram creation, tutorial writing, API reference documentation

### Primary Use Cases

- Documentation workflows
- Api Docs workflows
- Diagrams workflows
- Openapi workflows
- Swagger workflows

### Who Should Use This

- Developers working with documentation systems
- Teams requiring documentation generation capabilities
- Projects leveraging 5 specialized agents for task automation

## Quick Start

### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep documentation-generation
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the reference-builder agent
@reference-builder <your request>
```

Or use the command interface:
```bash
/documentation-generation:doc-generate <arguments>
```

## Agents Reference

This plugin provides **5 specialized agents**:

### reference-builder

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and searchable reference materials. Use PROACTIVELY for API docs, configuration references, or complete technical specifications.

**When to Use Proactively:**
- Creates exhaustive technical references and API documentation
- When you need specialized reference builder expertise

**Example Invocation:**
```bash
@reference-builder <specific task or question>
```

### docs-architect

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to produce long-form technical manuals and ebooks. Use PROACTIVELY for system documentation, architecture guides, or technical deep-dives.

**When to Use Proactively:**
- Creates comprehensive technical documentation from existing codebases
- When you need specialized docs architect expertise

**Example Invocation:**
```bash
@docs-architect <specific task or question>
```

### api-documenter

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SDKs, and build comprehensive developer portals. Use PROACTIVELY for API documentation or developer portal creation.

**When to Use Proactively:**
- Master API documentation with OpenAPI 3
- When you need specialized api documenter expertise

**Example Invocation:**
```bash
@api-documenter <specific task or question>
```

### tutorial-engineer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with hands-on examples. Use PROACTIVELY for onboarding guides, feature tutorials, or concept explanations.

**When to Use Proactively:**
- Creates step-by-step tutorials and educational content from code
- When you need specialized tutorial engineer expertise

**Example Invocation:**
```bash
@tutorial-engineer <specific task or question>
```

### mermaid-expert

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. Masters syntax for all diagram types and styling. Use PROACTIVELY for visual documentation, system diagrams, or process flows.

**When to Use Proactively:**
- Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures
- When you need specialized mermaid expert expertise

**Example Invocation:**
```bash
@mermaid-expert <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /documentation-generation:doc-generate

**Description:** 

**Usage:**
```bash
/documentation-generation:doc-generate [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/documentation-generation:doc-generate
```

2. Work with agent:
```bash
@reference-builder implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@reference-builder`
2. Implementation: `@docs-architect`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `documentation-generation` plugin focuses specifically on openapi specification generation, mermaid diagram creation, tutorial writing, api reference documentation, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@reference-builder` for primary tasks in this domain
- Follow the plugin's specialized patterns for documentation
- Leverage progressive disclosure skills for advanced features
- Combine with complementary plugins for full-stack workflows

### Don'ts

- Don't use this plugin for tasks outside its domain
- Avoid mixing incompatible plugin patterns
- Don't skip the recommended workflow steps

### Common Pitfalls

1. **Over-complexity:** Start simple, add features incrementally
2. **Wrong agent:** Use the right agent for the task
3. **Missing context:** Provide sufficient background information

### Optimization Tips

- Use progressive disclosure to load only needed knowledge
- Cache agent responses when appropriate

## Troubleshooting

### Common Issues

**Issue:** Agent not responding as expected

**Solution:**
- Verify plugin installation
- Check agent name spelling
- Provide more context in your request

**Issue:** Skill not activating

**Solution:**
- Ensure trigger criteria match your use case
- Explicitly mention the skill in your request

### Error Messages


| Error | Cause | Solution |
|-------|-------|----------|
| Agent not found | Plugin not installed | Verify installation |
| Skill unavailable | Path mismatch | Check skill directory structure |
| Command failed | Missing dependencies | Review prerequisites |

### Debugging Techniques

1. **Verbose mode:** Request detailed explanations from agents
2. **Step-by-step:** Break complex tasks into smaller steps
3. **Isolation:** Test agents individually before combining


## Contributing

Contributions are welcome! Please see the [main repository](https://github.com/wshobson/agents) for guidelines.

## License

MIT

## Support

- **Issues:** [GitHub Issues](https://github.com/wshobson/agents/issues)
- **Discussions:** [GitHub Discussions](https://github.com/wshobson/agents/discussions)
- **Documentation:** [Full Documentation](https://github.com/wshobson/agents)

---

**Plugin:** documentation-generation v1.2.0
**Last Updated:** 1.2.0
**Agents:** 5 | **Skills:** 0 | **Commands:** 1
