# cloud-infrastructure

> Cloud architecture design for AWS/Azure/GCP, Kubernetes cluster configuration, Terraform infrastructure-as-code, hybrid cloud networking, and multi-cloud cost optimization

**Version:** 1.2.1
**Category:** infrastructure
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Cloud architecture design for AWS/Azure/GCP, Kubernetes cluster configuration, Terraform infrastructure-as-code, hybrid cloud networking, and multi-cloud cost optimization

### Primary Use Cases

- Cloud workflows
- Aws workflows
- Azure workflows
- Gcp workflows
- Kubernetes workflows

### Who Should Use This

- Developers working with infrastructure systems
- Teams requiring cloud infrastructure capabilities
- Projects leveraging 6 specialized agents for task automation

## Quick Start

### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep cloud-infrastructure
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the terraform-specialist agent
@terraform-specialist <your request>
```

## Agents Reference

This plugin provides **6 specialized agents**:

### terraform-specialist

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. Handles complex module design, multi-cloud deployments, GitOps workflows, policy as code, and CI/CD integration. Covers migration strategies, security best practices, and modern IaC ecosystems. Use PROACTIVELY for advanced IaC, state management, or infrastructure automation.

**When to Use Proactively:**
- Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns
- When you need specialized terraform specialist expertise

**Example Invocation:**
```bash
@terraform-specialist <specific task or question>
```

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

### hybrid-cloud-architect

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware). Masters hybrid connectivity, workload placement optimization, edge computing, and cross-cloud automation. Handles compliance, cost optimization, disaster recovery, and migration strategies. Use PROACTIVELY for hybrid architecture, multi-cloud strategy, or complex infrastructure integration.

**When to Use Proactively:**
- Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware)
- When you need specialized hybrid cloud architect expertise

**Example Invocation:**
```bash
@hybrid-cloud-architect <specific task or question>
```

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

### network-engineer

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. Masters multi-cloud connectivity, service mesh, zero-trust networking, SSL/TLS, global load balancing, and advanced troubleshooting. Handles CDN optimization, network automation, and compliance. Use PROACTIVELY for network design, connectivity issues, or performance optimization.

**When to Use Proactively:**
- Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization
- When you need specialized network engineer expertise

**Example Invocation:**
```bash
@network-engineer <specific task or question>
```

## Skills Reference

This plugin includes **4 progressive disclosure skills** for advanced patterns:

### hybrid-cloud-networking

**Description:** Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and dedicated connections. Use when building hybrid cloud architectures, connecting data centers to cloud, or implementing secure cross-premises networking.

**Activation Triggers:**
Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and dedicated connections. Use when building hybrid cloud architectures, connecting data centers to cloud, or implementing secure cross-premises networking.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### cost-optimization

**Description:** Optimize cloud costs through resource rightsizing, tagging strategies, reserved instances, and spending analysis. Use when reducing cloud expenses, analyzing infrastructure costs, or implementing cost governance policies.

**Activation Triggers:**
Optimize cloud costs through resource rightsizing, tagging strategies, reserved instances, and spending analysis. Use when reducing cloud expenses, analyzing infrastructure costs, or implementing cost governance policies.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### multi-cloud-architecture

**Description:** Design multi-cloud architectures using a decision framework to select and integrate services across AWS, Azure, and GCP. Use when building multi-cloud systems, avoiding vendor lock-in, or leveraging best-of-breed services from multiple providers.

**Activation Triggers:**
Design multi-cloud architectures using a decision framework to select and integrate services across AWS, Azure, and GCP. Use when building multi-cloud systems, avoiding vendor lock-in, or leveraging best-of-breed services from multiple providers.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### terraform-module-library

**Description:** Build reusable Terraform modules for AWS, Azure, and GCP infrastructure following infrastructure-as-code best practices. Use when creating infrastructure modules, standardizing cloud provisioning, or implementing reusable IaC components.

**Activation Triggers:**
Build reusable Terraform modules for AWS, Azure, and GCP infrastructure following infrastructure-as-code best practices. Use when creating infrastructure modules, standardizing cloud provisioning, or implementing reusable IaC components.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

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
2. Implementation: `@kubernetes-architect`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `kubernetes-operations` - Related infrastructure plugin
- `cicd-automation` - Related infrastructure plugin

### Differences from Similar Plugins

The `cloud-infrastructure` plugin focuses specifically on cloud architecture design for aws/azure/gcp, kubernetes cluster configuration, terraform infrastructure-as-code, hybrid cloud networking, and multi-cloud cost optimization, while similar plugins may have broader or different specializations.

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

## Advanced Topics

### Power User Features

- **hybrid-cloud-networking:** Advanced patterns for power users
- **cost-optimization:** Advanced patterns for power users

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

**Plugin:** cloud-infrastructure v1.2.1
**Last Updated:** 1.2.1
**Agents:** 6 | **Skills:** 4 | **Commands:** 0
