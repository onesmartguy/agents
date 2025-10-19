# debugging-toolkit

> Interactive debugging, developer experience optimization, and smart debugging workflows

**Version:** 1.2.0
**Category:** development
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Interactive debugging, developer experience optimization, and smart debugging workflows

### Primary Use Cases

- Debugging workflows
- Developer Experience workflows
- Troubleshooting workflows
- Essential workflows

### Who Should Use This

- Developers working with development systems
- Teams requiring debugging toolkit capabilities
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
claude agents list | grep debugging-toolkit
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the debugger agent
@debugger <your request>
```

Or use the command interface:
```bash
/debugging-toolkit:smart-debug <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### debugger

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.

**When to Use Proactively:**
- Debugging specialist for errors, test failures, and unexpected behavior
- When you need specialized debugger expertise

**Example Invocation:**
```bash
@debugger <specific task or question>
```

### dx-optimizer

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Developer Experience specialist. Improves tooling, setup, and workflows. Use PROACTIVELY when setting up new projects, after team feedback, or when development friction is noticed.

**When to Use Proactively:**
- Developer Experience specialist
- When you need specialized dx optimizer expertise

**Example Invocation:**
```bash
@dx-optimizer <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /debugging-toolkit:smart-debug

**Description:** 

**Usage:**
```bash
/debugging-toolkit:smart-debug [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/debugging-toolkit:smart-debug
```

2. Work with agent:
```bash
@debugger implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@debugger`
2. Implementation: `@dx-optimizer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `backend-development` - Related development plugin
- `frontend-mobile-development` - Related development plugin
- `full-stack-orchestration` - Related development plugin

### Differences from Similar Plugins

The `debugging-toolkit` plugin focuses specifically on interactive debugging, developer experience optimization, and smart debugging workflows, while similar plugins may have broader or different specializations.

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

- Use `@debugger` for primary tasks in this domain
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

**Plugin:** debugging-toolkit v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 1
