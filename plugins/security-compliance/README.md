# security-compliance

> SOC2, HIPAA, and GDPR compliance validation, secrets scanning, compliance checklists, and regulatory documentation

**Version:** 1.2.0
**Category:** security
**Author:** Seth Hobson

## Overview

### What This Plugin Does

SOC2, HIPAA, and GDPR compliance validation, secrets scanning, compliance checklists, and regulatory documentation

### Primary Use Cases

- Compliance workflows
- Soc2 workflows
- Hipaa workflows
- Gdpr workflows
- Secrets workflows

### Who Should Use This

- Developers working with security systems
- Teams requiring security compliance capabilities
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
claude agents list | grep security-compliance
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the security-auditor agent
@security-auditor <your request>
```

Or use the command interface:
```bash
/security-compliance:compliance-check <arguments>
```

## Agents Reference

This plugin provides **1 specialized agents**:

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

This plugin provides **1 slash commands**:

### /security-compliance:compliance-check

**Description:** 

**Usage:**
```bash
/security-compliance:compliance-check [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/security-compliance:compliance-check
```

2. Work with agent:
```bash
@security-auditor implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow


## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `security-compliance` plugin focuses specifically on soc2, hipaa, and gdpr compliance validation, secrets scanning, compliance checklists, and regulatory documentation, while similar plugins may have broader or different specializations.

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

- Use `@security-auditor` for primary tasks in this domain
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

**Plugin:** security-compliance v1.2.0
**Last Updated:** 1.2.0
**Agents:** 1 | **Skills:** 0 | **Commands:** 1
