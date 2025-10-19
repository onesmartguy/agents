# seo-analysis-monitoring

> Content freshness analysis, cannibalization detection, and authority building for SEO

**Version:** 1.2.0
**Category:** marketing
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Content freshness analysis, cannibalization detection, and authority building for SEO

### Primary Use Cases

- Seo workflows
- Content Analysis workflows
- E E A T workflows
- Authority workflows
- Monitoring workflows

### Who Should Use This

- Developers working with marketing systems
- Teams requiring seo analysis monitoring capabilities
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
claude agents list | grep seo-analysis-monitoring
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the seo-authority-builder agent
@seo-authority-builder <your request>
```

## Agents Reference

This plugin provides **3 specialized agents**:

### seo-authority-builder

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust. Identifies missing credibility elements. Use PROACTIVELY for YMYL topics.

**When to Use Proactively:**
- Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust
- When you need specialized seo authority builder expertise

**Example Invocation:**
```bash
@seo-authority-builder <specific task or question>
```

### seo-cannibalization-detector

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies. Use PROACTIVELY when reviewing similar content.

**When to Use Proactively:**
- Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues
- When you need specialized seo cannibalization detector expertise

**Example Invocation:**
```bash
@seo-cannibalization-detector <specific task or question>
```

### seo-content-refresher

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that need updating. Use PROACTIVELY for older content.

**When to Use Proactively:**
- Identifies outdated elements in provided content and suggests updates to maintain freshness
- When you need specialized seo content refresher expertise

**Example Invocation:**
```bash
@seo-content-refresher <specific task or question>
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@seo-authority-builder start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@seo-authority-builder`
2. Implementation: `@seo-cannibalization-detector`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `seo-analysis-monitoring` plugin focuses specifically on content freshness analysis, cannibalization detection, and authority building for seo, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@seo-authority-builder` for primary tasks in this domain
- Follow the plugin's specialized patterns for marketing
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

**Plugin:** seo-analysis-monitoring v1.2.0
**Last Updated:** 1.2.0
**Agents:** 3 | **Skills:** 0 | **Commands:** 0
