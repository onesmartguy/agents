# comprehensive-review

> Multi-perspective code analysis covering architecture, security, and best practices

**Version:** 1.2.1
**Category:** quality
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Multi-perspective code analysis covering architecture, security, and best practices

### Primary Use Cases

- Code Review workflows
- Quality workflows
- Architecture workflows
- Security workflows
- Best Practices workflows

### Who Should Use This

- Developers working with quality systems
- Teams requiring comprehensive review capabilities
- Projects leveraging 3 specialized agents for task automation

## Quick Start

### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep comprehensive-review
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the code-reviewer agent
@code-reviewer <your request>
```

Or use the command interface:
```bash
/comprehensive-review:pr-enhance <arguments>
```

## Agents Reference

This plugin provides **3 specialized agents**:

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

### architect-review

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD. Reviews system designs and code changes for architectural integrity, scalability, and maintainability. Use PROACTIVELY for architectural decisions.

**When to Use Proactively:**
- Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD
- When you need specialized architect review expertise

**Example Invocation:**
```bash
@architect-review <specific task or question>
```

### security-auditor

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. Masters vulnerability assessment, threat modeling, secure authentication (OAuth2/OIDC), OWASP standards, cloud security, and security automation. Handles DevSecOps integration, compliance (GDPR/HIPAA/SOC2), and incident response. Use PROACTIVELY for security audits, DevSecOps, or compliance implementation.

**When to Use Proactively:**
- Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks
- When you need specialized security auditor expertise

**Example Invocation:**
```bash
@security-auditor <specific task or question>
```

## Commands Reference

This plugin provides **2 slash commands**:

### /comprehensive-review:pr-enhance

**Description:** 

**Usage:**
```bash
/comprehensive-review:pr-enhance [options]
```

### /comprehensive-review:full-review

**Description:** 

**Usage:**
```bash
/comprehensive-review:full-review [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/comprehensive-review:pr-enhance
```

2. Work with agent:
```bash
@code-reviewer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@code-reviewer`
2. Implementation: `@architect-review`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `comprehensive-review` plugin focuses specifically on multi-perspective code analysis covering architecture, security, and best practices, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@code-reviewer` for primary tasks in this domain
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

**Plugin:** comprehensive-review v1.2.1
**Last Updated:** 1.2.1
**Agents:** 3 | **Skills:** 0 | **Commands:** 2
