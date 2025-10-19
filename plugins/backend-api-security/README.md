# backend-api-security

> API security hardening, authentication implementation, authorization patterns, rate limiting, and input validation

**Version:** 1.2.0
**Category:** security
**Author:** Seth Hobson

## Overview

### What This Plugin Does

API security hardening, authentication implementation, authorization patterns, rate limiting, and input validation

### Primary Use Cases

- Api Security workflows
- Authentication workflows
- Authorization workflows
- Jwt workflows
- Oauth workflows

### Who Should Use This

- Developers working with security systems
- Teams requiring backend api security capabilities
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
claude agents list | grep backend-api-security
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the backend-architect agent
@backend-architect <your request>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### backend-architect

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC APIs, event-driven architectures, service mesh patterns, and modern backend frameworks. Handles service boundary definition, inter-service communication, resilience patterns, and observability. Use PROACTIVELY when creating new backend services or APIs.

**When to Use Proactively:**
- Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems
- When you need specialized backend architect expertise

**Example Invocation:**
```bash
@backend-architect <specific task or question>
```

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
@backend-architect start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@backend-architect`
2. Implementation: `@backend-security-coder`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `backend-api-security` plugin focuses specifically on api security hardening, authentication implementation, authorization patterns, rate limiting, and input validation, while similar plugins may have broader or different specializations.

### Works Well With

- Plugins in the `quality` category
- Plugins in the `infrastructure` category
- Plugins in the `testing` category

### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@backend-architect` for primary tasks in this domain
- Follow the plugin's specialized patterns for security
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

**Plugin:** backend-api-security v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 0
