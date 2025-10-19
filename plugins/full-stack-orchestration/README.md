# full-stack-orchestration

> End-to-end feature orchestration with testing, security, performance, and deployment

**Version:** 1.2.1
**Category:** workflows
**Author:** Seth Hobson

## Overview

### What This Plugin Does

End-to-end feature orchestration with testing, security, performance, and deployment

### Primary Use Cases

- Full Stack workflows
- Orchestration workflows
- Deployment workflows
- Security workflows
- Testing workflows

### Who Should Use This

- Developers working with workflows systems
- Teams requiring full stack orchestration capabilities
- Projects leveraging 4 specialized agents for task automation

## Quick Start

### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep full-stack-orchestration
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the test-automator agent
@test-automator <your request>
```

Or use the command interface:
```bash
/full-stack-orchestration:full-stack-feature <arguments>
```

## Agents Reference

This plugin provides **4 specialized agents**:

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

### deployment-engineer

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. Masters GitHub Actions, ArgoCD/Flux, progressive delivery, container security, and platform engineering. Handles zero-downtime deployments, security scanning, and developer experience optimization. Use PROACTIVELY for CI/CD design, GitOps implementation, or deployment automation.

**When to Use Proactively:**
- Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation
- When you need specialized deployment engineer expertise

**Example Invocation:**
```bash
@deployment-engineer <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /full-stack-orchestration:full-stack-feature

**Description:** 

**Usage:**
```bash
/full-stack-orchestration:full-stack-feature [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/full-stack-orchestration:full-stack-feature
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

The `full-stack-orchestration` plugin focuses specifically on end-to-end feature orchestration with testing, security, performance, and deployment, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@test-automator` for primary tasks in this domain
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

**Plugin:** full-stack-orchestration v1.2.1
**Last Updated:** 1.2.1
**Agents:** 4 | **Skills:** 0 | **Commands:** 1
