# web-scripting

> Web scripting with PHP and Ruby for web applications, CMS development, and backend services

**Version:** 1.2.0
**Category:** languages
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Web scripting with PHP and Ruby for web applications, CMS development, and backend services

### Primary Use Cases

- Php workflows
- Ruby workflows
- Rails workflows
- Wordpress workflows
- Web Scripting workflows

### Who Should Use This

- Developers working with languages systems
- Teams requiring web scripting capabilities
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
claude agents list | grep web-scripting
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the ruby-pro agent
@ruby-pro <your request>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### ruby-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. Specializes in Ruby on Rails, gem development, and testing frameworks. Use PROACTIVELY for Ruby refactoring, optimization, or complex Ruby features.

**When to Use Proactively:**
- Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization
- When you need specialized ruby pro expertise

**Example Invocation:**
```bash
@ruby-pro <specific task or question>
```

### php-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. Use PROACTIVELY for high-performance PHP applications.

**When to Use Proactively:**
- Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features
- When you need specialized php pro expertise

**Example Invocation:**
```bash
@php-pro <specific task or question>
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@ruby-pro start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@ruby-pro`
2. Implementation: `@php-pro`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `python-development` - Related languages plugin
- `javascript-typescript` - Related languages plugin
- `dotnet-development` - Related languages plugin

### Differences from Similar Plugins

The `web-scripting` plugin focuses specifically on web scripting with php and ruby for web applications, cms development, and backend services, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@ruby-pro` for primary tasks in this domain
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

**Plugin:** web-scripting v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 0
