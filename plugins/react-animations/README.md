# react-animations

> Framer Motion animation patterns, performance optimization, and React animation architecture

**Version:** 1.2.3
**Category:** development
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Framer Motion animation patterns, performance optimization, and React animation architecture

### Primary Use Cases

- Framer Motion workflows
- Motion workflows
- Animation workflows
- React workflows
- Performance workflows

### Who Should Use This

- Developers working with development systems
- Teams requiring react animations capabilities
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
claude agents list | grep react-animations
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the framer-motion-pro agent
@framer-motion-pro <your request>
```

Or use the command interface:
```bash
/react-animations:animation-scaffold <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### framer-motion-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert in Motion (formerly Framer Motion) animation patterns, variants, AnimatePresence, and hardware-accelerated animations. Use PROACTIVELY when implementing React animations, creating animation systems, or optimizing animation performance.

**When to Use Proactively:**
- Expert in Motion (formerly Framer Motion) animation patterns, variants, AnimatePresence, and hardware-accelerated animations
- When you need specialized framer motion pro expertise

**Example Invocation:**
```bash
@framer-motion-pro <specific task or question>
```

### react-animation-architect

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Designs complex multi-element animation orchestrations, animation systems, and performance-optimized animation architectures for React applications. Use PROACTIVELY when architecting animation systems, designing complex interactions, or establishing animation design patterns.

**When to Use Proactively:**
- Designs complex multi-element animation orchestrations, animation systems, and performance-optimized animation architectures for React applications
- When you need specialized react animation architect expertise

**Example Invocation:**
```bash
@react-animation-architect <specific task or question>
```

## Skills Reference

This plugin includes **4 progressive disclosure skills** for advanced patterns:

### layout-animations

**Description:** Motion layout animations using the layout prop, shared layout transitions, FLIP animations, and automatic position/size transitions. Use when animating layout changes, implementing shared element transitions, or creating responsive animations.

**Activation Triggers:**
Motion layout animations using the layout prop, shared layout transitions, FLIP animations, and automatic position/size transitions. Use when animating layout changes, implementing shared element transitions, or creating responsive animations.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### motion-orchestration

**Description:** Coordinating multiple Motion animations with timing controls, sequencing, staggering, and complex multi-element choreography. Use when implementing complex animation sequences, coordinated transitions, or multi-step interactions.

**Activation Triggers:**
Coordinating multiple Motion animations with timing controls, sequencing, staggering, and complex multi-element choreography. Use when implementing complex animation sequences, coordinated transitions, or multi-step interactions.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### animation-performance-optimization

**Description:** Hardware acceleration, willChange optimization, lazy loading patterns, and performance profiling for Motion animations. Use when optimizing animation performance, achieving 60fps target, or reducing jank in complex animations.

**Activation Triggers:**
Hardware acceleration, willChange optimization, lazy loading patterns, and performance profiling for Motion animations. Use when optimizing animation performance, achieving 60fps target, or reducing jank in complex animations.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### motion-variants-patterns

**Description:** Motion (Framer Motion) variant definitions, propagation, orchestration, and state-based animation patterns. Use when implementing reusable animation states, coordinating multi-element animations, or building animation libraries.

**Activation Triggers:**
Motion (Framer Motion) variant definitions, propagation, orchestration, and state-based animation patterns. Use when implementing reusable animation states, coordinating multi-element animations, or building animation libraries.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **1 slash commands**:

### /react-animations:animation-scaffold

**Description:** Scaffold a new Motion (Framer Motion) animation system with design tokens, variant library, and reusable components

**Usage:**
```bash
/react-animations:animation-scaffold [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/react-animations:animation-scaffold
```

2. Work with agent:
```bash
@framer-motion-pro implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@framer-motion-pro`
2. Implementation: `@react-animation-architect`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `backend-development` - Related development plugin
- `frontend-mobile-development` - Related development plugin
- `full-stack-orchestration` - Related development plugin

### Differences from Similar Plugins

The `react-animations` plugin focuses specifically on framer motion animation patterns, performance optimization, and react animation architecture, while similar plugins may have broader or different specializations.

### Works Well With

- Plugins in the `testing` category
- Plugins in the `documentation` category
- Plugins in the `quality` category

### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@framer-motion-pro` for primary tasks in this domain
- Follow the plugin's specialized patterns for development
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

## Advanced Topics

### Power User Features

- **layout-animations:** Advanced patterns for power users
- **motion-orchestration:** Advanced patterns for power users

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

**Plugin:** react-animations v1.2.3
**Last Updated:** 1.2.3
**Agents:** 2 | **Skills:** 4 | **Commands:** 1
