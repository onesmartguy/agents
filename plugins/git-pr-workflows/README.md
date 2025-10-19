# git-pr-workflows

> Git workflow automation, pull request enhancement, and team onboarding processes

**Version:** 1.2.1
**Category:** workflows
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Git workflow automation, pull request enhancement, and team onboarding processes

### Primary Use Cases

- Git workflows
- Pull Request workflows
- Workflow workflows
- Onboarding workflows
- Essential workflows

### Who Should Use This

- Developers working with workflows systems
- Teams requiring git pr workflows capabilities
- Projects leveraging 1 specialized agents for task automation

## Quick Start

### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep git-pr-workflows
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the code-reviewer agent
@code-reviewer <your request>
```

Or use the command interface:
```bash
/git-pr-workflows:pr-enhance <arguments>
```

## Agents Reference

This plugin provides **1 specialized agents**:

### code-reviewer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production reliability. Masters static analysis tools, security scanning, and configuration review with 2024/2025 best practices. Use PROACTIVELY for code quality assurance.

**When to Use Proactively:**
- Elite code review expert specializing in modern AI-powered code analysis, security vulnerabilities, performance optimization, and production reliability
- When you need specialized code reviewer expertise

**Example Invocation:**
```bash
@code-reviewer <specific task or question>
```

## Commands Reference

This plugin provides **3 slash commands**:

### /git-pr-workflows:pr-enhance

**Description:** 

**Usage:**
```bash
/git-pr-workflows:pr-enhance [options]
```

### /git-pr-workflows:git-workflow

**Description:** 

**Usage:**
```bash
/git-pr-workflows:git-workflow [options]
```

### /git-pr-workflows:onboard

**Description:** 

**Usage:**
```bash
/git-pr-workflows:onboard [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/git-pr-workflows:pr-enhance
```

2. Work with agent:
```bash
@code-reviewer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow


## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `git-pr-workflows` plugin focuses specifically on git workflow automation, pull request enhancement, and team onboarding processes, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@code-reviewer` for primary tasks in this domain
- Follow the plugin's specialized patterns for workflows
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

**Plugin:** git-pr-workflows v1.2.1
**Last Updated:** 1.2.1
**Agents:** 1 | **Skills:** 0 | **Commands:** 3
