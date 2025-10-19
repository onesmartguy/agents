# systems-programming

> Systems programming with Rust, Go, C, and C++ for performance-critical and low-level development

**Version:** 1.2.0
**Category:** languages
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Systems programming with Rust, Go, C, and C++ for performance-critical and low-level development

### Primary Use Cases

- Rust workflows
- Golang workflows
- C workflows
- Cpp workflows
- Systems Programming workflows

### Who Should Use This

- Developers working with languages systems
- Teams requiring systems programming capabilities
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
claude agents list | grep systems-programming
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the golang-pro agent
@golang-pro <your request>
```

Or use the command interface:
```bash
/systems-programming:rust-project <arguments>
```

## Agents Reference

This plugin provides **4 specialized agents**:

### golang-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. Expert in the latest Go ecosystem including generics, workspaces, and cutting-edge frameworks. Use PROACTIVELY for Go development, architecture design, or performance optimization.

**When to Use Proactively:**
- Master Go 1
- When you need specialized golang pro expertise

**Example Invocation:**
```bash
@golang-pro <specific task or question>
```

### cpp-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performance optimization. Use PROACTIVELY for C++ refactoring, memory safety, or complex C++ patterns.

**When to Use Proactively:**
- Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms
- When you need specialized cpp pro expertise

**Example Invocation:**
```bash
@cpp-pro <specific task or question>
```

### rust-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. Expert in the latest Rust ecosystem including Tokio, axum, and cutting-edge crates. Use PROACTIVELY for Rust development, performance optimization, or systems programming.

**When to Use Proactively:**
- Master Rust 1
- When you need specialized rust pro expertise

**Example Invocation:**
```bash
@rust-pro <specific task or question>
```

### c-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Write efficient C code with proper memory management, pointer arithmetic, and system calls. Handles embedded systems, kernel modules, and performance-critical code. Use PROACTIVELY for C optimization, memory issues, or system programming.

**When to Use Proactively:**
- Write efficient C code with proper memory management, pointer arithmetic, and system calls
- When you need specialized c pro expertise

**Example Invocation:**
```bash
@c-pro <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /systems-programming:rust-project

**Description:** 

**Usage:**
```bash
/systems-programming:rust-project [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/systems-programming:rust-project
```

2. Work with agent:
```bash
@golang-pro implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@golang-pro`
2. Implementation: `@cpp-pro`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `python-development` - Related languages plugin
- `javascript-typescript` - Related languages plugin
- `dotnet-development` - Related languages plugin

### Differences from Similar Plugins

The `systems-programming` plugin focuses specifically on systems programming with rust, go, c, and c++ for performance-critical and low-level development, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@golang-pro` for primary tasks in this domain
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


## Contributing

Contributions are welcome! Please see the [main repository](https://github.com/wshobson/agents) for guidelines.

## License

MIT

## Support

- **Issues:** [GitHub Issues](https://github.com/wshobson/agents/issues)
- **Discussions:** [GitHub Discussions](https://github.com/wshobson/agents/discussions)
- **Documentation:** [Full Documentation](https://github.com/wshobson/agents)

---

**Plugin:** systems-programming v1.2.0
**Last Updated:** 1.2.0
**Agents:** 4 | **Skills:** 0 | **Commands:** 1
