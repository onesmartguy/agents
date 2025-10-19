# incident-response

> Production incident management, triage workflows, and automated incident resolution

**Version:** 1.2.1
**Category:** operations
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Production incident management, triage workflows, and automated incident resolution

### Primary Use Cases

- Incident Response workflows
- Production workflows
- Sre workflows
- Troubleshooting workflows

### Who Should Use This

- Developers working with operations systems
- Teams requiring incident response capabilities
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
claude agents list | grep incident-response
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the incident-responder agent
@incident-responder <your request>
```

Or use the command interface:
```bash
/incident-response:incident-response <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### incident-responder

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. Masters incident command, blameless post-mortems, error budget management, and system reliability patterns. Handles critical outages, communication strategies, and continuous improvement. Use IMMEDIATELY for production incidents or SRE practices.

**When to Use Proactively:**
- Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management
- When you need specialized incident responder expertise

**Example Invocation:**
```bash
@incident-responder <specific task or question>
```

### devops-troubleshooter

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. Masters log analysis, distributed tracing, Kubernetes debugging, performance optimization, and root cause analysis. Handles production outages, system reliability, and preventive monitoring. Use PROACTIVELY for debugging, incident response, or system troubleshooting.

**When to Use Proactively:**
- Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability
- When you need specialized devops troubleshooter expertise

**Example Invocation:**
```bash
@devops-troubleshooter <specific task or question>
```

## Commands Reference

This plugin provides **2 slash commands**:

### /incident-response:incident-response

**Description:** 

**Usage:**
```bash
/incident-response:incident-response [options]
```

### /incident-response:smart-fix

**Description:** 

**Usage:**
```bash
/incident-response:smart-fix [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/incident-response:incident-response
```

2. Work with agent:
```bash
@incident-responder implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@incident-responder`
2. Implementation: `@devops-troubleshooter`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `incident-response` plugin focuses specifically on production incident management, triage workflows, and automated incident resolution, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@incident-responder` for primary tasks in this domain
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


## Contributing

Contributions are welcome! Please see the [main repository](https://github.com/wshobson/agents) for guidelines.

## License

MIT

## Support

- **Issues:** [GitHub Issues](https://github.com/wshobson/agents/issues)
- **Discussions:** [GitHub Discussions](https://github.com/wshobson/agents/discussions)
- **Documentation:** [Full Documentation](https://github.com/wshobson/agents)

---

**Plugin:** incident-response v1.2.1
**Last Updated:** 1.2.1
**Agents:** 2 | **Skills:** 0 | **Commands:** 2
