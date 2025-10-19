# security-scanning

> SAST analysis, dependency vulnerability scanning, OWASP Top 10 compliance, container security scanning, and automated security hardening

**Version:** 1.2.2
**Category:** security
**Author:** Seth Hobson

## Overview

### What This Plugin Does

SAST analysis, dependency vulnerability scanning, OWASP Top 10 compliance, container security scanning, and automated security hardening

### Primary Use Cases

- Security workflows
- Sast workflows
- Vulnerability Scanning workflows
- Owasp workflows
- Devsecops workflows

### Who Should Use This

- Developers working with security systems
- Teams requiring security scanning capabilities
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
claude agents list | grep security-scanning
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the security-auditor agent
@security-auditor <your request>
```

Or use the command interface:
```bash
/security-scanning:security-sast <arguments>
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

## Skills Reference

This plugin includes **1 progressive disclosure skills** for advanced patterns:

### sast-configuration

**Description:** Configure Static Application Security Testing (SAST) tools for automated vulnerability detection in application code. Use when setting up security scanning, implementing DevSecOps practices, or automating code vulnerability detection.

**Activation Triggers:**
Configure Static Application Security Testing (SAST) tools for automated vulnerability detection in application code. Use when setting up security scanning, implementing DevSecOps practices, or automating code vulnerability detection.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **3 slash commands**:

### /security-scanning:security-sast

**Description:** Static Application Security Testing (SAST) for code vulnerability analysis across multiple languages and frameworks

**Usage:**
```bash
/security-scanning:security-sast [options]
```

### /security-scanning:security-hardening

**Description:** 

**Usage:**
```bash
/security-scanning:security-hardening [options]
```

### /security-scanning:security-dependencies

**Description:** 

**Usage:**
```bash
/security-scanning:security-dependencies [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/security-scanning:security-sast
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

The `security-scanning` plugin focuses specifically on sast analysis, dependency vulnerability scanning, owasp top 10 compliance, container security scanning, and automated security hardening, while similar plugins may have broader or different specializations.

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

## Advanced Topics

### Power User Features

- **sast-configuration:** Advanced patterns for power users

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

**Plugin:** security-scanning v1.2.2
**Last Updated:** 1.2.2
**Agents:** 1 | **Skills:** 1 | **Commands:** 3
