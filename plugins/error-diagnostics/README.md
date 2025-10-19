# error-diagnostics

> Error tracing, root cause analysis, and smart debugging for production systems

**Version:** 1.2.0
**Category:** operations
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Error tracing, root cause analysis, and smart debugging for production systems

### Primary Use Cases

- Diagnostics workflows
- Error Tracing workflows
- Root Cause workflows
- Debugging workflows

### Who Should Use This

- Developers working with operations systems
- Teams requiring error diagnostics capabilities
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
claude agents list | grep error-diagnostics
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the debugger agent
@debugger <your request>
```

Or use the command interface:
```bash
/error-diagnostics:smart-debug <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### debugger

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.

**When to Use Proactively:**
- Debugging specialist for errors, test failures, and unexpected behavior
- When you need specialized debugger expertise

**Example Invocation:**
```bash
@debugger <specific task or question>
```

### error-detective

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. Use PROACTIVELY when debugging issues, analyzing logs, or investigating production errors.

**When to Use Proactively:**
- Search logs and codebases for error patterns, stack traces, and anomalies
- When you need specialized error detective expertise

**Example Invocation:**
```bash
@error-detective <specific task or question>
```

## Commands Reference

This plugin provides **3 slash commands**:

### /error-diagnostics:smart-debug

**Description:** 

**Usage:**
```bash
/error-diagnostics:smart-debug [options]
```

### /error-diagnostics:error-trace

**Description:** 

**Usage:**
```bash
/error-diagnostics:error-trace [options]
```

### /error-diagnostics:error-analysis

**Description:** 

**Usage:**
```bash
/error-diagnostics:error-analysis [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/error-diagnostics:smart-debug
```

2. Work with agent:
```bash
@debugger implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@debugger`
2. Implementation: `@error-detective`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `error-diagnostics` plugin focuses specifically on error tracing, root cause analysis, and smart debugging for production systems, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@debugger` for primary tasks in this domain
- Follow the plugin's specialized patterns for operations
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

**Plugin:** error-diagnostics v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 3
