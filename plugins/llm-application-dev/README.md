# llm-application-dev

> LLM application development, prompt engineering, and AI assistant optimization

**Version:** 1.2.1
**Category:** ai-ml
**Author:** Seth Hobson

## Overview

### What This Plugin Does

LLM application development, prompt engineering, and AI assistant optimization

### Primary Use Cases

- Llm workflows
- Ai workflows
- Prompt Engineering workflows
- Langchain workflows
- Gpt workflows

### Who Should Use This

- Developers working with ai-ml systems
- Teams requiring llm application dev capabilities
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
claude agents list | grep llm-application-dev
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the prompt-engineer agent
@prompt-engineer <your request>
```

Or use the command interface:
```bash
/llm-application-dev:prompt-optimize <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### prompt-engineer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert prompt engineer specializing in advanced prompting techniques, LLM optimization, and AI system design. Masters chain-of-thought, constitutional AI, and production prompt strategies. Use when building AI features, improving agent performance, or crafting system prompts.

**When to Use Proactively:**
- Expert prompt engineer specializing in advanced prompting techniques, LLM optimization, and AI system design
- When you need specialized prompt engineer expertise

**Example Invocation:**
```bash
@prompt-engineer <specific task or question>
```

### ai-engineer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orchestration, and enterprise AI integrations. Use PROACTIVELY for LLM features, chatbots, AI agents, or AI-powered applications.

**When to Use Proactively:**
- Build production-ready LLM applications, advanced RAG systems, and intelligent agents
- When you need specialized ai engineer expertise

**Example Invocation:**
```bash
@ai-engineer <specific task or question>
```

## Skills Reference

This plugin includes **4 progressive disclosure skills** for advanced patterns:

### rag-implementation

**Description:** Build Retrieval-Augmented Generation (RAG) systems for LLM applications with vector databases and semantic search. Use when implementing knowledge-grounded AI, building document Q&A systems, or integrating LLMs with external knowledge bases.

**Activation Triggers:**
Build Retrieval-Augmented Generation (RAG) systems for LLM applications with vector databases and semantic search. Use when implementing knowledge-grounded AI, building document Q&A systems, or integrating LLMs with external knowledge bases.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### llm-evaluation

**Description:** Implement comprehensive evaluation strategies for LLM applications using automated metrics, human feedback, and benchmarking. Use when testing LLM performance, measuring AI application quality, or establishing evaluation frameworks.

**Activation Triggers:**
Implement comprehensive evaluation strategies for LLM applications using automated metrics, human feedback, and benchmarking. Use when testing LLM performance, measuring AI application quality, or establishing evaluation frameworks.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### prompt-engineering-patterns

**Description:** Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability in production. Use when optimizing prompts, improving LLM outputs, or designing production prompt templates.

**Activation Triggers:**
Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability in production. Use when optimizing prompts, improving LLM outputs, or designing production prompt templates.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### langchain-architecture

**Description:** Design LLM applications using the LangChain framework with agents, memory, and tool integration patterns. Use when building LangChain applications, implementing AI agents, or creating complex LLM workflows.

**Activation Triggers:**
Design LLM applications using the LangChain framework with agents, memory, and tool integration patterns. Use when building LangChain applications, implementing AI agents, or creating complex LLM workflows.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **3 slash commands**:

### /llm-application-dev:prompt-optimize

**Description:** 

**Usage:**
```bash
/llm-application-dev:prompt-optimize [options]
```

### /llm-application-dev:langchain-agent

**Description:** 

**Usage:**
```bash
/llm-application-dev:langchain-agent [options]
```

### /llm-application-dev:ai-assistant

**Description:** 

**Usage:**
```bash
/llm-application-dev:ai-assistant [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/llm-application-dev:prompt-optimize
```

2. Work with agent:
```bash
@prompt-engineer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@prompt-engineer`
2. Implementation: `@ai-engineer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `llm-application-dev` plugin focuses specifically on llm application development, prompt engineering, and ai assistant optimization, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@prompt-engineer` for primary tasks in this domain
- Follow the plugin's specialized patterns for ai-ml
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

- **rag-implementation:** Advanced patterns for power users
- **llm-evaluation:** Advanced patterns for power users

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

**Plugin:** llm-application-dev v1.2.1
**Last Updated:** 1.2.1
**Agents:** 2 | **Skills:** 4 | **Commands:** 3
