# data-validation-suite

> Schema validation, data quality monitoring, streaming validation pipelines, and input validation for backend APIs

**Version:** 1.2.0
**Category:** data
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Schema validation, data quality monitoring, streaming validation pipelines, and input validation for backend APIs

### Primary Use Cases

- Validation workflows
- Schema workflows
- Data Quality workflows
- Pydantic workflows
- Jsonschema workflows

### Who Should Use This

- Developers working with data systems
- Teams requiring data validation suite capabilities
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
claude agents list | grep data-validation-suite
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the backend-security-coder agent
@backend-security-coder <your request>
```

## Agents Reference

This plugin provides **1 specialized agents**:

### backend-security-coder

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert in secure backend coding practices specializing in input validation, authentication, and API security. Use PROACTIVELY for backend security implementations or security code reviews.

**When to Use Proactively:**
- Expert in secure backend coding practices specializing in input validation, authentication, and API security
- When you need specialized backend security coder expertise

**Example Invocation:**
```bash
@backend-security-coder <specific task or question>
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@backend-security-coder start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow


## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `data-validation-suite` plugin focuses specifically on schema validation, data quality monitoring, streaming validation pipelines, and input validation for backend apis, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@backend-security-coder` for primary tasks in this domain
- Follow the plugin's specialized patterns for data
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

**Plugin:** data-validation-suite v1.2.0
**Last Updated:** 1.2.0
**Agents:** 1 | **Skills:** 0 | **Commands:** 0
