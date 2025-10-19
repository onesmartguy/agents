# dependency-management

> Dependency auditing, version management, and security vulnerability scanning

**Version:** 1.2.0
**Category:** utilities
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Dependency auditing, version management, and security vulnerability scanning

### Primary Use Cases

- Dependencies workflows
- Npm workflows
- Security workflows
- Auditing workflows
- Upgrades workflows

### Who Should Use This

- Developers working with utilities systems
- Teams requiring dependency management capabilities
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
claude agents list | grep dependency-management
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the legacy-modernizer agent
@legacy-modernizer <your request>
```

Or use the command interface:
```bash
/dependency-management:deps-audit <arguments>
```

## Agents Reference

This plugin provides **1 specialized agents**:

### legacy-modernizer

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and backward compatibility. Use PROACTIVELY for legacy system updates, framework migrations, or technical debt reduction.

**When to Use Proactively:**
- Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization
- When you need specialized legacy modernizer expertise

**Example Invocation:**
```bash
@legacy-modernizer <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /dependency-management:deps-audit

**Description:** 

**Usage:**
```bash
/dependency-management:deps-audit [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/dependency-management:deps-audit
```

2. Work with agent:
```bash
@legacy-modernizer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow


## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `dependency-management` plugin focuses specifically on dependency auditing, version management, and security vulnerability scanning, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@legacy-modernizer` for primary tasks in this domain
- Follow the plugin's specialized patterns for utilities
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

**Plugin:** dependency-management v1.2.0
**Last Updated:** 1.2.0
**Agents:** 1 | **Skills:** 0 | **Commands:** 1
