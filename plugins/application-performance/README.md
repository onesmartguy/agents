# application-performance

> Application profiling, performance optimization with BenchmarkDotNet, async/await patterns, and observability for frontend and backend systems

**Version:** 1.2.2
**Category:** performance
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Application profiling, performance optimization with BenchmarkDotNet, async/await patterns, and observability for frontend and backend systems

### Primary Use Cases

- Performance workflows
- Profiling workflows
- Optimization workflows
- Core Web Vitals workflows
- Dotnet workflows

### Who Should Use This

- Developers working with performance systems
- Teams requiring application performance capabilities
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
claude agents list | grep application-performance
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the performance-engineer agent
@performance-engineer <your request>
```

Or use the command interface:
```bash
/application-performance:performance-optimization <arguments>
```

## Agents Reference

This plugin provides **3 specialized agents**:

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

### frontend-developer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern frontend architecture. Optimizes performance and ensures accessibility. Use PROACTIVELY when creating UI components or fixing frontend issues.

**When to Use Proactively:**
- Build React components, implement responsive layouts, and handle client-side state management
- When you need specialized frontend developer expertise

**Example Invocation:**
```bash
@frontend-developer <specific task or question>
```

## Skills Reference

This plugin includes **1 progressive disclosure skills** for advanced patterns:

### dotnet-performance-optimization

**Description:** Optimize .NET application performance with BenchmarkDotNet, async/await patterns, memory optimization, Span<T>/Memory<T>, caching strategies, and profiling tools (dotTrace, PerfView). Use when improving application throughput, reducing latency, or optimizing resource usage.

**Activation Triggers:**
Optimize .NET application performance with BenchmarkDotNet, async/await patterns, memory optimization, Span<T>/Memory<T>, caching strategies, and profiling tools (dotTrace, PerfView). Use when improving application throughput, reducing latency, or optimizing resource usage.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **1 slash commands**:

### /application-performance:performance-optimization

**Description:** 

**Usage:**
```bash
/application-performance:performance-optimization [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/application-performance:performance-optimization
```

2. Work with agent:
```bash
@performance-engineer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@performance-engineer`
2. Implementation: `@observability-engineer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `application-performance` plugin focuses specifically on application profiling, performance optimization with benchmarkdotnet, async/await patterns, and observability for frontend and backend systems, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@performance-engineer` for primary tasks in this domain
- Follow the plugin's specialized patterns for performance
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

- Monitor performance metrics
- Profile before optimizing
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

- **dotnet-performance-optimization:** Advanced patterns for power users

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

**Plugin:** application-performance v1.2.2
**Last Updated:** 1.2.2
**Agents:** 3 | **Skills:** 1 | **Commands:** 1
