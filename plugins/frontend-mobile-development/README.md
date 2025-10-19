# frontend-mobile-development

> Frontend UI development and mobile application implementation across platforms

**Version:** 1.2.0
**Category:** development
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Frontend UI development and mobile application implementation across platforms

### Primary Use Cases

- Frontend workflows
- Mobile workflows
- React workflows
- Ui workflows
- Cross Platform workflows

### Who Should Use This

- Developers working with development systems
- Teams requiring frontend mobile development capabilities
- Projects leveraging 2 specialized agents for task automation

## Quick Start

### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep frontend-mobile-development
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the mobile-developer agent
@mobile-developer <your request>
```

Or use the command interface:
```bash
/frontend-mobile-development:component-scaffold <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### mobile-developer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrations, offline sync, and app store optimization. Use PROACTIVELY for mobile features, cross-platform code, or app optimization.

**When to Use Proactively:**
- Develop React Native, Flutter, or native mobile apps with modern architecture patterns
- When you need specialized mobile developer expertise

**Example Invocation:**
```bash
@mobile-developer <specific task or question>
```

### frontend-developer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern frontend architecture. Optimizes performance and ensures accessibility. Use PROACTIVELY when creating UI components or fixing frontend issues.

**When to Use Proactively:**
- Build React components, implement responsive layouts, and handle client-side state management
- When you need specialized frontend developer expertise

**Example Invocation:**
```bash
@frontend-developer <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /frontend-mobile-development:component-scaffold

**Description:** 

**Usage:**
```bash
/frontend-mobile-development:component-scaffold [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/frontend-mobile-development:component-scaffold
```

2. Work with agent:
```bash
@mobile-developer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@mobile-developer`
2. Implementation: `@frontend-developer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `backend-development` - Related development plugin
- `full-stack-orchestration` - Related development plugin

### Differences from Similar Plugins

The `frontend-mobile-development` plugin focuses specifically on frontend ui development and mobile application implementation across platforms, while similar plugins may have broader or different specializations.

### Works Well With

- Plugins in the `testing` category
- Plugins in the `documentation` category
- Plugins in the `quality` category

### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@mobile-developer` for primary tasks in this domain
- Follow the plugin's specialized patterns for development
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

**Plugin:** frontend-mobile-development v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 1
