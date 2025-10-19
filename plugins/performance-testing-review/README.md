# performance-testing-review

> Performance analysis, test coverage review, and AI-powered code quality assessment

**Version:** 1.2.0
**Category:** quality
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Performance analysis, test coverage review, and AI-powered code quality assessment

### Primary Use Cases

- Performance Review workflows
- Test Coverage workflows
- Quality Analysis workflows

### Who Should Use This

- Developers working with quality systems
- Teams requiring performance testing review capabilities
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
claude agents list | grep performance-testing-review
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the test-automator agent
@test-automator <your request>
```

Or use the command interface:
```bash
/performance-testing-review:ai-review <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### test-automator

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing strategies with advanced CI/CD integration. Use PROACTIVELY for testing automation or quality assurance.

**When to Use Proactively:**
- Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering
- When you need specialized test automator expertise

**Example Invocation:**
```bash
@test-automator <specific task or question>
```

### performance-engineer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert performance engineer specializing in modern observability, application optimization, and scalable system performance. Masters OpenTelemetry, distributed tracing, load testing, multi-tier caching, Core Web Vitals, and performance monitoring. Handles end-to-end optimization, real user monitoring, and scalability patterns. Use PROACTIVELY for performance optimization, observability, or scalability challenges.

**When to Use Proactively:**
- Expert performance engineer specializing in modern observability, application optimization, and scalable system performance
- When you need specialized performance engineer expertise

**Example Invocation:**
```bash
@performance-engineer <specific task or question>
```

## Commands Reference

This plugin provides **2 slash commands**:

### /performance-testing-review:ai-review

**Description:** 

**Usage:**
```bash
/performance-testing-review:ai-review [options]
```

### /performance-testing-review:multi-agent-review

**Description:** 

**Usage:**
```bash
/performance-testing-review:multi-agent-review [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/performance-testing-review:ai-review
```

2. Work with agent:
```bash
@test-automator implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@test-automator`
2. Implementation: `@performance-engineer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `performance-testing-review` plugin focuses specifically on performance analysis, test coverage review, and ai-powered code quality assessment, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@test-automator` for primary tasks in this domain
- Follow the plugin's specialized patterns for quality
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

**Plugin:** performance-testing-review v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 2
