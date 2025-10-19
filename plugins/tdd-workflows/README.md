# tdd-workflows

> Test-driven development methodology with red-green-refactor cycles and code review

**Version:** 1.2.1
**Category:** workflows
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Test-driven development methodology with red-green-refactor cycles and code review

### Primary Use Cases

- Tdd workflows
- Test Driven workflows
- Workflow workflows
- Red Green Refactor workflows

### Who Should Use This

- Developers working with workflows systems
- Teams requiring tdd workflows capabilities
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
claude agents list | grep tdd-workflows
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the code-reviewer agent
@code-reviewer <your request>
```

Or use the command interface:
```bash
/tdd-workflows:tdd-red <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

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

### tdd-orchestrator

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven development practices. Enforces TDD best practices across teams with AI-assisted testing and modern frameworks. Use PROACTIVELY for TDD implementation and governance.

**When to Use Proactively:**
- Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven development practices
- When you need specialized tdd orchestrator expertise

**Example Invocation:**
```bash
@tdd-orchestrator <specific task or question>
```

## Commands Reference

This plugin provides **4 slash commands**:

### /tdd-workflows:tdd-red

**Description:** 

**Usage:**
```bash
/tdd-workflows:tdd-red [options]
```

### /tdd-workflows:tdd-refactor

**Description:** 

**Usage:**
```bash
/tdd-workflows:tdd-refactor [options]
```

### /tdd-workflows:tdd-green

**Description:** 

**Usage:**
```bash
/tdd-workflows:tdd-green [options]
```

### /tdd-workflows:tdd-cycle

**Description:** 

**Usage:**
```bash
/tdd-workflows:tdd-cycle [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/tdd-workflows:tdd-red
```

2. Work with agent:
```bash
@code-reviewer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@code-reviewer`
2. Implementation: `@tdd-orchestrator`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `tdd-workflows` plugin focuses specifically on test-driven development methodology with red-green-refactor cycles and code review, while similar plugins may have broader or different specializations.

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

**Plugin:** tdd-workflows v1.2.1
**Last Updated:** 1.2.1
**Agents:** 2 | **Skills:** 0 | **Commands:** 4
