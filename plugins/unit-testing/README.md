# unit-testing

> Unit and integration test automation for Python, JavaScript, and .NET with debugging support, xUnit, NUnit, Moq, and FluentAssertions

**Version:** 1.2.1
**Category:** testing
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Unit and integration test automation for Python, JavaScript, and .NET with debugging support, xUnit, NUnit, Moq, and FluentAssertions

### Primary Use Cases

- Testing workflows
- Unit Tests workflows
- Python workflows
- Javascript workflows
- Dotnet workflows

### Who Should Use This

- Developers working with testing systems
- Teams requiring unit testing capabilities
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
claude agents list | grep unit-testing
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the test-automator agent
@test-automator <your request>
```

Or use the command interface:
```bash
/unit-testing:test-generate <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### test-automator

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing strategies with advanced CI/CD integration. Use PROACTIVELY for testing automation or quality assurance.

**When to Use Proactively:**
- Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering
- When you need specialized test automator expertise

**Example Invocation:**
```bash
@test-automator <specific task or question>
```

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

## Skills Reference

This plugin includes **1 progressive disclosure skills** for advanced patterns:

### dotnet-testing-patterns

**Description:** Master .NET testing with xUnit, NUnit, MSTest, Moq, FluentAssertions, integration testing with WebApplicationFactory, CQRS testing patterns, and code coverage tools. Use when implementing unit tests, integration tests, or test-driven development in .NET applications.

**Activation Triggers:**
Master .NET testing with xUnit, NUnit, MSTest, Moq, FluentAssertions, integration testing with WebApplicationFactory, CQRS testing patterns, and code coverage tools. Use when implementing unit tests, integration tests, or test-driven development in .NET applications.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **1 slash commands**:

### /unit-testing:test-generate

**Description:** 

**Usage:**
```bash
/unit-testing:test-generate [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/unit-testing:test-generate
```

2. Work with agent:
```bash
@test-automator implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@test-automator`
2. Implementation: `@debugger`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `unit-testing` plugin focuses specifically on unit and integration test automation for python, javascript, and .net with debugging support, xunit, nunit, moq, and fluentassertions, while similar plugins may have broader or different specializations.

### Works Well With

- Plugins in the `development` category
- Plugins in the `quality` category
- Plugins in the `workflows` category

### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@test-automator` for primary tasks in this domain
- Follow the plugin's specialized patterns for testing
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

- **dotnet-testing-patterns:** Advanced patterns for power users

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

**Plugin:** unit-testing v1.2.1
**Last Updated:** 1.2.1
**Agents:** 2 | **Skills:** 1 | **Commands:** 1
