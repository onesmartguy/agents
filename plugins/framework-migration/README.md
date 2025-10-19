# framework-migration

> Framework updates, migration planning, and architectural transformation workflows

**Version:** 1.2.2
**Category:** modernization
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Framework updates, migration planning, and architectural transformation workflows

### Primary Use Cases

- Migration workflows
- Framework Upgrade workflows
- Modernization workflows
- Angular workflows
- React workflows

### Who Should Use This

- Developers working with modernization systems
- Teams requiring framework migration capabilities
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
claude agents list | grep framework-migration
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the legacy-modernizer agent
@legacy-modernizer <your request>
```

Or use the command interface:
```bash
/framework-migration:deps-upgrade <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

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

### architect-review

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD. Reviews system designs and code changes for architectural integrity, scalability, and maintainability. Use PROACTIVELY for architectural decisions.

**When to Use Proactively:**
- Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD
- When you need specialized architect review expertise

**Example Invocation:**
```bash
@architect-review <specific task or question>
```

## Skills Reference

This plugin includes **4 progressive disclosure skills** for advanced patterns:

### angular-migration

**Description:** Migrate from AngularJS to Angular using hybrid mode, incremental component rewriting, and dependency injection updates. Use when upgrading AngularJS applications, planning framework migrations, or modernizing legacy Angular code.

**Activation Triggers:**
Migrate from AngularJS to Angular using hybrid mode, incremental component rewriting, and dependency injection updates. Use when upgrading AngularJS applications, planning framework migrations, or modernizing legacy Angular code.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### react-modernization

**Description:** Upgrade React applications to latest versions, migrate from class components to hooks, and adopt concurrent features. Use when modernizing React codebases, migrating to React Hooks, or upgrading to latest React versions.

**Activation Triggers:**
Upgrade React applications to latest versions, migrate from class components to hooks, and adopt concurrent features. Use when modernizing React codebases, migrating to React Hooks, or upgrading to latest React versions.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### dependency-upgrade

**Description:** Manage major dependency version upgrades with compatibility analysis, staged rollout, and comprehensive testing. Use when upgrading framework versions, updating major dependencies, or managing breaking changes in libraries.

**Activation Triggers:**
Manage major dependency version upgrades with compatibility analysis, staged rollout, and comprehensive testing. Use when upgrading framework versions, updating major dependencies, or managing breaking changes in libraries.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### database-migration

**Description:** Execute database migrations across ORMs and platforms with zero-downtime strategies, data transformation, and rollback procedures. Use when migrating databases, changing schemas, performing data transformations, or implementing zero-downtime deployment strategies.

**Activation Triggers:**
Execute database migrations across ORMs and platforms with zero-downtime strategies, data transformation, and rollback procedures. Use when migrating databases, changing schemas, performing data transformations, or implementing zero-downtime deployment strategies.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **3 slash commands**:

### /framework-migration:deps-upgrade

**Description:** 

**Usage:**
```bash
/framework-migration:deps-upgrade [options]
```

### /framework-migration:code-migrate

**Description:** 

**Usage:**
```bash
/framework-migration:code-migrate [options]
```

### /framework-migration:legacy-modernize

**Description:** 

**Usage:**
```bash
/framework-migration:legacy-modernize [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/framework-migration:deps-upgrade
```

2. Work with agent:
```bash
@legacy-modernizer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@legacy-modernizer`
2. Implementation: `@architect-review`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `framework-migration` plugin focuses specifically on framework updates, migration planning, and architectural transformation workflows, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@legacy-modernizer` for primary tasks in this domain
- Follow the plugin's specialized patterns for modernization
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

- **angular-migration:** Advanced patterns for power users
- **react-modernization:** Advanced patterns for power users

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

**Plugin:** framework-migration v1.2.2
**Last Updated:** 1.2.2
**Agents:** 2 | **Skills:** 4 | **Commands:** 3
