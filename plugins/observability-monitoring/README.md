# observability-monitoring

> Metrics collection, logging infrastructure, distributed tracing, SLO implementation, and monitoring dashboards

**Version:** 1.2.1
**Category:** operations
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Metrics collection, logging infrastructure, distributed tracing, SLO implementation, and monitoring dashboards

### Primary Use Cases

- Observability workflows
- Monitoring workflows
- Metrics workflows
- Logging workflows
- Tracing workflows

### Who Should Use This

- Developers working with operations systems
- Teams requiring observability monitoring capabilities
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
claude agents list | grep observability-monitoring
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the performance-engineer agent
@performance-engineer <your request>
```

Or use the command interface:
```bash
/observability-monitoring:monitor-setup <arguments>
```

## Agents Reference

This plugin provides **4 specialized agents**:

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

### database-optimizer

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. Masters advanced indexing, N+1 resolution, multi-tier caching, partitioning strategies, and cloud database optimization. Handles complex query analysis, migration strategies, and performance monitoring. Use PROACTIVELY for database optimization, performance issues, or scalability challenges.

**When to Use Proactively:**
- Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures
- When you need specialized database optimizer expertise

**Example Invocation:**
```bash
@database-optimizer <specific task or question>
```

### observability-engineer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and incident response workflows. Use PROACTIVELY for monitoring infrastructure, performance optimization, or production reliability.

**When to Use Proactively:**
- Build production-ready monitoring, logging, and tracing systems
- When you need specialized observability engineer expertise

**Example Invocation:**
```bash
@observability-engineer <specific task or question>
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

### grafana-dashboards

**Description:** Create and manage production Grafana dashboards for real-time visualization of system and application metrics. Use when building monitoring dashboards, visualizing metrics, or creating operational observability interfaces.

**Activation Triggers:**
Create and manage production Grafana dashboards for real-time visualization of system and application metrics. Use when building monitoring dashboards, visualizing metrics, or creating operational observability interfaces.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### prometheus-configuration

**Description:** Set up Prometheus for comprehensive metric collection, storage, and monitoring of infrastructure and applications. Use when implementing metrics collection, setting up monitoring infrastructure, or configuring alerting systems.

**Activation Triggers:**
Set up Prometheus for comprehensive metric collection, storage, and monitoring of infrastructure and applications. Use when implementing metrics collection, setting up monitoring infrastructure, or configuring alerting systems.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### slo-implementation

**Description:** Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error budgets and alerting. Use when establishing reliability targets, implementing SRE practices, or measuring service performance.

**Activation Triggers:**
Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error budgets and alerting. Use when establishing reliability targets, implementing SRE practices, or measuring service performance.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### distributed-tracing

**Description:** Implement distributed tracing with Jaeger and Tempo to track requests across microservices and identify performance bottlenecks. Use when debugging microservices, analyzing request flows, or implementing observability for distributed systems.

**Activation Triggers:**
Implement distributed tracing with Jaeger and Tempo to track requests across microservices and identify performance bottlenecks. Use when debugging microservices, analyzing request flows, or implementing observability for distributed systems.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **2 slash commands**:

### /observability-monitoring:monitor-setup

**Description:** 

**Usage:**
```bash
/observability-monitoring:monitor-setup [options]
```

### /observability-monitoring:slo-implement

**Description:** 

**Usage:**
```bash
/observability-monitoring:slo-implement [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/observability-monitoring:monitor-setup
```

2. Work with agent:
```bash
@performance-engineer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@performance-engineer`
2. Implementation: `@database-optimizer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `observability-monitoring` plugin focuses specifically on metrics collection, logging infrastructure, distributed tracing, slo implementation, and monitoring dashboards, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@performance-engineer` for primary tasks in this domain
- Follow the plugin's specialized patterns for operations
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

- **grafana-dashboards:** Advanced patterns for power users
- **prometheus-configuration:** Advanced patterns for power users

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

**Plugin:** observability-monitoring v1.2.1
**Last Updated:** 1.2.1
**Agents:** 4 | **Skills:** 4 | **Commands:** 2
