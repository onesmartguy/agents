# deployment-strategies

> Deployment patterns, rollback automation, and infrastructure templates

**Version:** 1.2.0
**Category:** infrastructure
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Deployment patterns, rollback automation, and infrastructure templates

### Primary Use Cases

- Deployment workflows
- Rollout workflows
- Rollback workflows
- Canary workflows
- Blue Green workflows

### Who Should Use This

- Developers working with infrastructure systems
- Teams requiring deployment strategies capabilities
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
claude agents list | grep deployment-strategies
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the terraform-specialist agent
@terraform-specialist <your request>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### terraform-specialist

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. Handles complex module design, multi-cloud deployments, GitOps workflows, policy as code, and CI/CD integration. Covers migration strategies, security best practices, and modern IaC ecosystems. Use PROACTIVELY for advanced IaC, state management, or infrastructure automation.

**When to Use Proactively:**
- Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns
- When you need specialized terraform specialist expertise

**Example Invocation:**
```bash
@terraform-specialist <specific task or question>
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

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@terraform-specialist start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@terraform-specialist`
2. Implementation: `@deployment-engineer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `kubernetes-operations` - Related infrastructure plugin
- `cloud-infrastructure` - Related infrastructure plugin
- `cicd-automation` - Related infrastructure plugin

### Differences from Similar Plugins

The `deployment-strategies` plugin focuses specifically on deployment patterns, rollback automation, and infrastructure templates, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@terraform-specialist` for primary tasks in this domain
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

**Plugin:** deployment-strategies v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 0
