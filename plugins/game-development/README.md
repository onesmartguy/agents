# game-development

> Unity game development with C# scripting, Minecraft server plugin development with Bukkit/Spigot APIs

**Version:** 1.2.0
**Category:** gaming
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Unity game development with C# scripting, Minecraft server plugin development with Bukkit/Spigot APIs

### Primary Use Cases

- Gaming workflows
- Unity workflows
- Minecraft workflows
- Game Dev workflows
- Bukkit workflows

### Who Should Use This

- Developers working with gaming systems
- Teams requiring game development capabilities
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
claude agents list | grep game-development
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the minecraft-bukkit-pro agent
@minecraft-bukkit-pro <your request>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### minecraft-bukkit-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. Specializes in event-driven architecture, command systems, world manipulation, player management, and performance optimization. Use PROACTIVELY for plugin architecture, gameplay mechanics, server-side features, or cross-version compatibility.

**When to Use Proactively:**
- Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs
- When you need specialized minecraft bukkit pro expertise

**Example Invocation:**
```bash
@minecraft-bukkit-pro <specific task or question>
```

### unity-developer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. Masters Unity 6 LTS, URP/HDRP pipelines, and cross-platform deployment. Handles gameplay systems, UI implementation, and platform optimization. Use PROACTIVELY for Unity performance issues, game mechanics, or cross-platform builds.

**When to Use Proactively:**
- Build Unity games with optimized C# scripts, efficient rendering, and proper asset management
- When you need specialized unity developer expertise

**Example Invocation:**
```bash
@unity-developer <specific task or question>
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@minecraft-bukkit-pro start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@minecraft-bukkit-pro`
2. Implementation: `@unity-developer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `game-development` plugin focuses specifically on unity game development with c# scripting, minecraft server plugin development with bukkit/spigot apis, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@minecraft-bukkit-pro` for primary tasks in this domain
- Follow the plugin's specialized patterns for gaming
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

**Plugin:** game-development v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 0
