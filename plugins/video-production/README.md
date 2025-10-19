# video-production

> Programmatic video creation with Remotion, FFmpeg automation, and cloud video pipelines

**Version:** 1.2.3
**Category:** media
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Programmatic video creation with Remotion, FFmpeg automation, and cloud video pipelines

### Primary Use Cases

- Remotion workflows
- Ffmpeg workflows
- Video workflows
- Automation workflows
- Media Processing workflows

### Who Should Use This

- Developers working with media systems
- Teams requiring video production capabilities
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
claude agents list | grep video-production
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the remotion-pro agent
@remotion-pro <your request>
```

Or use the command interface:
```bash
/video-production:video-pipeline <arguments>
```

## Agents Reference

This plugin provides **3 specialized agents**:

### remotion-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert in Remotion programmatic video creation with React, Player optimization, dynamic content generation, and API integration. Use PROACTIVELY when implementing video generation, creating data-driven videos, or building video automation systems.

**When to Use Proactively:**
- Expert in Remotion programmatic video creation with React, Player optimization, dynamic content generation, and API integration
- When you need specialized remotion pro expertise

**Example Invocation:**
```bash
@remotion-pro <specific task or question>
```

### video-pipeline-architect

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Designs end-to-end video production pipelines from creation to distribution, including Remotion, FFmpeg, cloud processing, and CDN delivery. Use PROACTIVELY when architecting video automation systems, building content distribution workflows, or designing scalable video infrastructure.

**When to Use Proactively:**
- Designs end-to-end video production pipelines from creation to distribution, including Remotion, FFmpeg, cloud processing, and CDN delivery
- When you need specialized video pipeline architect expertise

**Example Invocation:**
```bash
@video-pipeline-architect <specific task or question>
```

### ffmpeg-automator

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** FFmpeg command generation, video processing automation, format conversion, and batch operations. Use PROACTIVELY when processing videos, converting formats, trimming/editing, or building automated video pipelines.

**When to Use Proactively:**
- FFmpeg command generation, video processing automation, format conversion, and batch operations
- When you need specialized ffmpeg automator expertise

**Example Invocation:**
```bash
@ffmpeg-automator <specific task or question>
```

## Skills Reference

This plugin includes **4 progressive disclosure skills** for advanced patterns:

### remotion-patterns

**Description:** Remotion component patterns, Player optimization, composition structure, and React best practices for programmatic video creation. Use when building Remotion videos, optimizing Player performance, or structuring video components.

**Activation Triggers:**
Remotion component patterns, Player optimization, composition structure, and React best practices for programmatic video creation. Use when building Remotion videos, optimizing Player performance, or structuring video components.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### serverless-video-processing

**Description:** Serverless video processing with AWS Lambda, S3 triggers, cloud functions, and event-driven architectures. Use when building scalable cloud video pipelines or implementing automated processing workflows.

**Activation Triggers:**
Serverless video processing with AWS Lambda, S3 triggers, cloud functions, and event-driven architectures. Use when building scalable cloud video pipelines or implementing automated processing workflows.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### ffmpeg-automation

**Description:** FFmpeg command patterns, batch processing, web optimization, and automation scripts for video processing pipelines. Use when processing videos at scale, optimizing for web delivery, or building automated workflows.

**Activation Triggers:**
FFmpeg command patterns, batch processing, web optimization, and automation scripts for video processing pipelines. Use when processing videos at scale, optimizing for web delivery, or building automated workflows.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### video-pipeline-design

**Description:** End-to-end video pipeline architecture from content creation to distribution, including cloud processing, CDN integration, and multi-platform delivery. Use when designing scalable video systems or building automated content workflows.

**Activation Triggers:**
End-to-end video pipeline architecture from content creation to distribution, including cloud processing, CDN integration, and multi-platform delivery. Use when designing scalable video systems or building automated content workflows.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **2 slash commands**:

### /video-production:video-pipeline

**Description:** Design and implement an end-to-end video production pipeline with creation, processing, and distribution

**Usage:**
```bash
/video-production:video-pipeline [options]
```

### /video-production:video-scaffold

**Description:** Scaffold a new Remotion video project with compositions, components, and rendering configuration

**Usage:**
```bash
/video-production:video-scaffold [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/video-production:video-pipeline
```

2. Work with agent:
```bash
@remotion-pro implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@remotion-pro`
2. Implementation: `@video-pipeline-architect`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `video-production` plugin focuses specifically on programmatic video creation with remotion, ffmpeg automation, and cloud video pipelines, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@remotion-pro` for primary tasks in this domain
- Follow the plugin's specialized patterns for media
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

- **remotion-patterns:** Advanced patterns for power users
- **serverless-video-processing:** Advanced patterns for power users

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

**Plugin:** video-production v1.2.3
**Last Updated:** 1.2.3
**Agents:** 3 | **Skills:** 4 | **Commands:** 2
