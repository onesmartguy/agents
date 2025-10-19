# accessibility-compliance

> WCAG accessibility auditing, compliance validation, UI testing for screen readers, keyboard navigation, and inclusive design

**Version:** 1.2.0
**Category:** accessibility
**Author:** Seth Hobson

## Overview

### What This Plugin Does

WCAG accessibility auditing, compliance validation, UI testing for screen readers, keyboard navigation, and inclusive design

### Primary Use Cases

- Accessibility workflows
- Wcag workflows
- A11Y workflows
- Compliance workflows
- Inclusive Design workflows

### Who Should Use This

- Developers working with accessibility systems
- Teams requiring accessibility compliance capabilities
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
claude agents list | grep accessibility-compliance
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the ui-visual-validator agent
@ui-visual-validator <your request>
```

Or use the command interface:
```bash
/accessibility-compliance:accessibility-audit <arguments>
```

## Agents Reference

This plugin provides **1 specialized agents**:

### ui-visual-validator

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. Masters screenshot analysis, visual regression testing, and component validation. Use PROACTIVELY to verify UI modifications have achieved their intended goals through comprehensive visual analysis.

**When to Use Proactively:**
- Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification
- When you need specialized ui visual validator expertise

**Example Invocation:**
```bash
@ui-visual-validator <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /accessibility-compliance:accessibility-audit

**Description:** 

**Usage:**
```bash
/accessibility-compliance:accessibility-audit [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/accessibility-compliance:accessibility-audit
```

2. Work with agent:
```bash
@ui-visual-validator implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow


## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `accessibility-compliance` plugin focuses specifically on wcag accessibility auditing, compliance validation, ui testing for screen readers, keyboard navigation, and inclusive design, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@ui-visual-validator` for primary tasks in this domain
- Follow the plugin's specialized patterns for accessibility
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

**Plugin:** accessibility-compliance v1.2.0
**Last Updated:** 1.2.0
**Agents:** 1 | **Skills:** 0 | **Commands:** 1
