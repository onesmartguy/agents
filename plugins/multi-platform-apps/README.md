# multi-platform-apps

> Cross-platform application development coordinating web, iOS, Android, and desktop implementations

**Version:** 1.2.1
**Category:** development
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Cross-platform application development coordinating web, iOS, Android, and desktop implementations

### Primary Use Cases

- Cross Platform workflows
- Mobile workflows
- Web workflows
- Desktop workflows
- React Native workflows

### Who Should Use This

- Developers working with development systems
- Teams requiring multi platform apps capabilities
- Projects leveraging 6 specialized agents for task automation

## Quick Start

### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep multi-platform-apps
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the backend-architect agent
@backend-architect <your request>
```

Or use the command interface:
```bash
/multi-platform-apps:multi-platform <arguments>
```

## Agents Reference

This plugin provides **6 specialized agents**:

### backend-architect

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC APIs, event-driven architectures, service mesh patterns, and modern backend frameworks. Handles service boundary definition, inter-service communication, resilience patterns, and observability. Use PROACTIVELY when creating new backend services or APIs.

**When to Use Proactively:**
- Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems
- When you need specialized backend architect expertise

**Example Invocation:**
```bash
@backend-architect <specific task or question>
```

### ios-developer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Develop native iOS applications with Swift/SwiftUI. Masters iOS 18, SwiftUI, UIKit integration, Core Data, networking, and App Store optimization. Use PROACTIVELY for iOS-specific features, App Store optimization, or native iOS development.

**When to Use Proactively:**
- Develop native iOS applications with Swift/SwiftUI
- When you need specialized ios developer expertise

**Example Invocation:**
```bash
@ios-developer <specific task or question>
```

### flutter-expert

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. Handles state management, animations, testing, and performance optimization for mobile, web, desktop, and embedded platforms. Use PROACTIVELY for Flutter architecture, UI implementation, or cross-platform features.

**When to Use Proactively:**
- Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment
- When you need specialized flutter expert expertise

**Example Invocation:**
```bash
@flutter-expert <specific task or question>
```

### ui-ux-designer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools. Specializes in design tokens, component libraries, and inclusive design. Use PROACTIVELY for design systems, user flows, or interface optimization.

**When to Use Proactively:**
- Create interface designs, wireframes, and design systems
- When you need specialized ui ux designer expertise

**Example Invocation:**
```bash
@ui-ux-designer <specific task or question>
```

### mobile-developer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrations, offline sync, and app store optimization. Use PROACTIVELY for mobile features, cross-platform code, or app optimization.

**When to Use Proactively:**
- Develop React Native, Flutter, or native mobile apps with modern architecture patterns
- When you need specialized mobile developer expertise

**Example Invocation:**
```bash
@mobile-developer <specific task or question>
```

### frontend-developer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern frontend architecture. Optimizes performance and ensures accessibility. Use PROACTIVELY when creating UI components or fixing frontend issues.

**When to Use Proactively:**
- Build React components, implement responsive layouts, and handle client-side state management
- When you need specialized frontend developer expertise

**Example Invocation:**
```bash
@frontend-developer <specific task or question>
```

## Commands Reference

This plugin provides **1 slash commands**:

### /multi-platform-apps:multi-platform

**Description:** 

**Usage:**
```bash
/multi-platform-apps:multi-platform [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/multi-platform-apps:multi-platform
```

2. Work with agent:
```bash
@backend-architect implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@backend-architect`
2. Implementation: `@ios-developer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `backend-development` - Related development plugin
- `frontend-mobile-development` - Related development plugin
- `full-stack-orchestration` - Related development plugin

### Differences from Similar Plugins

The `multi-platform-apps` plugin focuses specifically on cross-platform application development coordinating web, ios, android, and desktop implementations, while similar plugins may have broader or different specializations.

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

- Use `@backend-architect` for primary tasks in this domain
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

**Plugin:** multi-platform-apps v1.2.1
**Last Updated:** 1.2.1
**Agents:** 6 | **Skills:** 0 | **Commands:** 1
