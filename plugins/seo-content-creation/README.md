# seo-content-creation

> SEO content writing, planning, and quality auditing with E-E-A-T optimization

**Version:** 1.2.0
**Category:** marketing
**Author:** Seth Hobson

## Overview

### What This Plugin Does

SEO content writing, planning, and quality auditing with E-E-A-T optimization

### Primary Use Cases

- Seo workflows
- Content Writing workflows
- Content Planning workflows
- Content Audit workflows

### Who Should Use This

- Developers working with marketing systems
- Teams requiring seo content creation capabilities
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
claude agents list | grep seo-content-creation
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the seo-content-planner agent
@seo-content-planner <your request>
```

## Agents Reference

This plugin provides **3 specialized agents**:

### seo-content-planner

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Creates comprehensive content outlines and topic clusters for SEO. Plans content calendars and identifies topic gaps. Use PROACTIVELY for content strategy and planning.

**When to Use Proactively:**
- Creates comprehensive content outlines and topic clusters for SEO
- When you need specialized seo content planner expertise

**Example Invocation:**
```bash
@seo-content-planner <specific task or question>
```

### seo-content-writer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practices. Use PROACTIVELY for content creation tasks.

**When to Use Proactively:**
- Writes SEO-optimized content based on provided keywords and topic briefs
- When you need specialized seo content writer expertise

**Example Invocation:**
```bash
@seo-content-writer <specific task or question>
```

### seo-content-auditor

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations based on established guidelines. Use PROACTIVELY for content review.

**When to Use Proactively:**
- Analyzes provided content for quality, E-E-A-T signals, and SEO best practices
- When you need specialized seo content auditor expertise

**Example Invocation:**
```bash
@seo-content-auditor <specific task or question>
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@seo-content-planner start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@seo-content-planner`
2. Implementation: `@seo-content-writer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `seo-content-creation` plugin focuses specifically on seo content writing, planning, and quality auditing with e-e-a-t optimization, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@seo-content-planner` for primary tasks in this domain
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

**Plugin:** seo-content-creation v1.2.0
**Last Updated:** 1.2.0
**Agents:** 3 | **Skills:** 0 | **Commands:** 0
