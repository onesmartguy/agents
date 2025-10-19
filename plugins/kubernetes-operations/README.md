# kubernetes-operations

> Kubernetes manifest generation, networking configuration, security policies, observability setup, GitOps workflows, and auto-scaling

**Version:** 1.2.1
**Category:** infrastructure
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Kubernetes manifest generation, networking configuration, security policies, observability setup, GitOps workflows, and auto-scaling

### Primary Use Cases

- Kubernetes workflows
- K8S workflows
- Containers workflows
- Helm workflows
- Argocd workflows

### Who Should Use This

- Developers working with infrastructure systems
- Teams requiring kubernetes operations capabilities
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
claude agents list | grep kubernetes-operations
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the kubernetes-architect agent
@kubernetes-architect <your request>
```

## Agents Reference

This plugin provides **1 specialized agents**:

### kubernetes-architect

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration. Masters EKS/AKS/GKE, service mesh (Istio/Linkerd), progressive delivery, multi-tenancy, and platform engineering. Handles security, observability, cost optimization, and developer experience. Use PROACTIVELY for K8s architecture, GitOps implementation, or cloud-native platform design.

**When to Use Proactively:**
- Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration
- When you need specialized kubernetes architect expertise

**Example Invocation:**
```bash
@kubernetes-architect <specific task or question>
```

## Skills Reference

This plugin includes **4 progressive disclosure skills** for advanced patterns:

### helm-chart-scaffolding

**Description:** Design, organize, and manage Helm charts for templating and packaging Kubernetes applications with reusable configurations. Use when creating Helm charts, packaging Kubernetes applications, or implementing templated deployments.

**Activation Triggers:**
Design, organize, and manage Helm charts for templating and packaging Kubernetes applications with reusable configurations. Use when creating Helm charts, packaging Kubernetes applications, or implementing templated deployments.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### gitops-workflow

**Description:** Implement GitOps workflows with ArgoCD and Flux for automated, declarative Kubernetes deployments with continuous reconciliation. Use when implementing GitOps practices, automating Kubernetes deployments, or setting up declarative infrastructure management.

**Activation Triggers:**
Implement GitOps workflows with ArgoCD and Flux for automated, declarative Kubernetes deployments with continuous reconciliation. Use when implementing GitOps practices, automating Kubernetes deployments, or setting up declarative infrastructure management.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### k8s-security-policies

**Description:** Implement Kubernetes security policies including NetworkPolicy, PodSecurityPolicy, and RBAC for production-grade security. Use when securing Kubernetes clusters, implementing network isolation, or enforcing pod security standards.

**Activation Triggers:**
Implement Kubernetes security policies including NetworkPolicy, PodSecurityPolicy, and RBAC for production-grade security. Use when securing Kubernetes clusters, implementing network isolation, or enforcing pod security standards.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### k8s-manifest-generator

**Description:** Create production-ready Kubernetes manifests for Deployments, Services, ConfigMaps, and Secrets following best practices and security standards. Use when generating Kubernetes YAML manifests, creating K8s resources, or implementing production-grade Kubernetes configurations.

**Activation Triggers:**
Create production-ready Kubernetes manifests for Deployments, Services, ConfigMaps, and Secrets following best practices and security standards. Use when generating Kubernetes YAML manifests, creating K8s resources, or implementing production-grade Kubernetes configurations.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@kubernetes-architect start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow


## Plugin Relationships

### Similar Plugins

- `cloud-infrastructure` - Related infrastructure plugin
- `cicd-automation` - Related infrastructure plugin

### Differences from Similar Plugins

The `kubernetes-operations` plugin focuses specifically on kubernetes manifest generation, networking configuration, security policies, observability setup, gitops workflows, and auto-scaling, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@kubernetes-architect` for primary tasks in this domain
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

## Advanced Topics

### Power User Features

- **helm-chart-scaffolding:** Advanced patterns for power users
- **gitops-workflow:** Advanced patterns for power users

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

**Plugin:** kubernetes-operations v1.2.1
**Last Updated:** 1.2.1
**Agents:** 1 | **Skills:** 4 | **Commands:** 0
