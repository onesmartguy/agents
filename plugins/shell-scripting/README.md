# shell-scripting

> Production-grade Bash scripting with defensive programming, POSIX compliance, and comprehensive testing

**Version:** 1.2.1
**Category:** languages
**Author:** Ryan Snodgrass

## Overview

### What This Plugin Does

Production-grade Bash scripting with defensive programming, POSIX compliance, and comprehensive testing

### Primary Use Cases

- Bash workflows
- Shell workflows
- Scripting workflows
- Automation workflows
- Posix workflows

### Who Should Use This

- Developers working with languages systems
- Teams requiring shell scripting capabilities
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
claude agents list | grep shell-scripting
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the posix-shell-pro agent
@posix-shell-pro <your request>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### posix-shell-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. Specializes in shell scripts that run on any POSIX-compliant shell (dash, ash, sh, bash --posix).

**When to Use Proactively:**
- Expert in strict POSIX sh scripting for maximum portability across Unix-like systems
- When you need specialized posix shell pro expertise

**Example Invocation:**
```bash
@posix-shell-pro <specific task or question>
```

### bash-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities. Expert in safe, portable, and testable shell scripts.

**When to Use Proactively:**
- Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities
- When you need specialized bash pro expertise

**Example Invocation:**
```bash
@bash-pro <specific task or question>
```

## Skills Reference

This plugin includes **3 progressive disclosure skills** for advanced patterns:

### bats-testing-patterns

**Description:** Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipelines, or requiring test-driven development of shell utilities.

**Activation Triggers:**
Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipelines, or requiring test-driven development of shell utilities.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### bash-defensive-patterns

**Description:** Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring fault tolerance and safety.

**Activation Triggers:**
Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring fault tolerance and safety.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### shellcheck-configuration

**Description:** Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code issues, or ensuring script portability.

**Activation Triggers:**
Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code issues, or ensuring script portability.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@posix-shell-pro start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@posix-shell-pro`
2. Implementation: `@bash-pro`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `python-development` - Related languages plugin
- `javascript-typescript` - Related languages plugin
- `dotnet-development` - Related languages plugin

### Differences from Similar Plugins

The `shell-scripting` plugin focuses specifically on production-grade bash scripting with defensive programming, posix compliance, and comprehensive testing, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@posix-shell-pro` for primary tasks in this domain
- Follow the plugin's specialized patterns for languages
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

## Advanced Topics

### Power User Features

- **bats-testing-patterns:** Advanced patterns for power users
- **bash-defensive-patterns:** Advanced patterns for power users

### Customization Options

- Adapt agent instructions for your workflow
- Extend skills with custom patterns
- Configure progressive disclosure depth

### Performance Tuning

- Use Haiku agents for speed-critical paths
- Batch similar operations
- Optimize context window usage


## Contributing

Contributions are welcome! Please see the [main repository](https://github.com/wshobson/agents) for guidelines.

## License

MIT

## Support

- **Issues:** [GitHub Issues](https://github.com/wshobson/agents/issues)
- **Discussions:** [GitHub Discussions](https://github.com/wshobson/agents/discussions)
- **Documentation:** [Full Documentation](https://github.com/wshobson/agents)

---

**Plugin:** shell-scripting v1.2.1
**Last Updated:** 1.2.1
**Agents:** 2 | **Skills:** 3 | **Commands:** 0
