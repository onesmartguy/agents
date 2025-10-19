# deployment-validation

> Pre-deployment checks, configuration validation, and deployment readiness assessment

**Version:** 1.2.0
**Category:** infrastructure
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Pre-deployment checks, configuration validation, and deployment readiness assessment

### Primary Use Cases

- Validation workflows
- Pre Flight workflows
- Configuration workflows
- Deployment Safety workflows

### Who Should Use This

- Developers working with infrastructure systems
- Teams requiring deployment validation capabilities
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
claude agents list | grep deployment-validation
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the cloud-architect agent
@cloud-architect <your request>
```

Or use the command interface:
```bash
/deployment-validation:config-validate <arguments>
```

## Agents Reference

This plugin provides **1 specialized agents**:

### cloud-architect

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns. Masters serverless, microservices, security, compliance, and disaster recovery. Use PROACTIVELY for cloud architecture, cost optimization, migration planning, or multi-cloud strategies.

**When to Use Proactively:**
- Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns
- When you need specialized cloud architect expertise

**Example Invocation:**
```bash
@cloud-architect <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /deployment-validation:config-validate

**Description:** 

**Usage:**
```bash
/deployment-validation:config-validate [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/deployment-validation:config-validate
```

2. Work with agent:
```bash
@cloud-architect implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow


## Plugin Relationships

### Similar Plugins

- `kubernetes-operations` - Related infrastructure plugin
- `cloud-infrastructure` - Related infrastructure plugin
- `cicd-automation` - Related infrastructure plugin

### Differences from Similar Plugins

The `deployment-validation` plugin focuses specifically on pre-deployment checks, configuration validation, and deployment readiness assessment, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@cloud-architect` for primary tasks in this domain
- Follow the plugin's specialized patterns for infrastructure
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

**Plugin:** deployment-validation v1.2.0
**Last Updated:** 1.2.0
**Agents:** 1 | **Skills:** 0 | **Commands:** 1
