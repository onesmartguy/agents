# jvm-languages

> JVM language development including Java, Scala, and C# with enterprise patterns and frameworks

**Version:** 1.2.0
**Category:** languages
**Author:** Seth Hobson

## Overview

### What This Plugin Does

JVM language development including Java, Scala, and C# with enterprise patterns and frameworks

### Primary Use Cases

- Java workflows
- Scala workflows
- Csharp workflows
- Jvm workflows
- Enterprise workflows

### Who Should Use This

- Developers working with languages systems
- Teams requiring jvm languages capabilities
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
claude agents list | grep jvm-languages
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the java-pro agent
@java-pro <your request>
```

## Agents Reference

This plugin provides **3 specialized agents**:

### java-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. Expert in the latest Java ecosystem including GraalVM, Project Loom, and cloud-native patterns. Use PROACTIVELY for Java development, microservices architecture, or performance optimization.

**When to Use Proactively:**
- Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3
- When you need specialized java pro expertise

**Example Invocation:**
```bash
@java-pro <specific task or question>
```

### scala-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. Expert in Apache Pekko, Akka, Spark, ZIO/Cats Effect, and reactive architectures. Use PROACTIVELY for Scala system design, performance optimization, or enterprise integration.

**When to Use Proactively:**
- Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing
- When you need specialized scala pro expertise

**Example Invocation:**
```bash
@scala-pro <specific task or question>
```

### csharp-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Write modern C# code with advanced features like records, pattern matching, and async/await. Optimizes .NET applications, implements enterprise patterns, and ensures comprehensive testing. Use PROACTIVELY for C# refactoring, performance optimization, or complex .NET solutions.

**When to Use Proactively:**
- Write modern C# code with advanced features like records, pattern matching, and async/await
- When you need specialized csharp pro expertise

**Example Invocation:**
```bash
@csharp-pro <specific task or question>
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@java-pro start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@java-pro`
2. Implementation: `@scala-pro`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `python-development` - Related languages plugin
- `javascript-typescript` - Related languages plugin
- `dotnet-development` - Related languages plugin

### Differences from Similar Plugins

The `jvm-languages` plugin focuses specifically on jvm language development including java, scala, and c# with enterprise patterns and frameworks, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@java-pro` for primary tasks in this domain
- Follow the plugin's specialized patterns for languages
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

**Plugin:** jvm-languages v1.2.0
**Last Updated:** 1.2.0
**Agents:** 3 | **Skills:** 0 | **Commands:** 0
