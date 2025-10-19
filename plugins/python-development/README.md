# python-development

> Modern Python development with Python 3.12+, Django, FastAPI, async patterns, and production best practices

**Version:** 1.2.1
**Category:** languages
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Modern Python development with Python 3.12+, Django, FastAPI, async patterns, and production best practices

### Primary Use Cases

- Python workflows
- Django workflows
- Fastapi workflows
- Async workflows
- Backend workflows

### Who Should Use This

- Developers working with languages systems
- Teams requiring python development capabilities
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
claude agents list | grep python-development
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the fastapi-pro agent
@fastapi-pro <your request>
```

Or use the command interface:
```bash
/python-development:python-scaffold <arguments>
```

## Agents Reference

This plugin provides **3 specialized agents**:

### fastapi-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python async patterns. Use PROACTIVELY for FastAPI development, async optimization, or API architecture.

**When to Use Proactively:**
- Build high-performance async APIs with FastAPI, SQLAlchemy 2
- When you need specialized fastapi pro expertise

**Example Invocation:**
```bash
@fastapi-pro <specific task or question>
```

### django-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, and deployment. Use PROACTIVELY for Django development, ORM optimization, or complex Django patterns.

**When to Use Proactively:**
- Master Django 5
- When you need specialized django pro expertise

**Example Invocation:**
```bash
@django-pro <specific task or question>
```

### python-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the latest Python ecosystem including uv, ruff, pydantic, and FastAPI. Use PROACTIVELY for Python development, optimization, or advanced Python patterns.

**When to Use Proactively:**
- Master Python 3
- When you need specialized python pro expertise

**Example Invocation:**
```bash
@python-pro <specific task or question>
```

## Skills Reference

This plugin includes **5 progressive disclosure skills** for advanced patterns:

### python-testing-patterns

**Description:** Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setting up test suites, or implementing testing best practices.

**Activation Triggers:**
Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setting up test suites, or implementing testing best practices.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### python-packaging

**Description:** Create distributable Python packages with proper project structure, setup.py/pyproject.toml, and publishing to PyPI. Use when packaging Python libraries, creating CLI tools, or distributing Python code.

**Activation Triggers:**
Create distributable Python packages with proper project structure, setup.py/pyproject.toml, and publishing to PyPI. Use when packaging Python libraries, creating CLI tools, or distributing Python code.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### uv-package-manager

**Description:** Master the uv package manager for fast Python dependency management, virtual environments, and modern Python project workflows. Use when setting up Python projects, managing dependencies, or optimizing Python development workflows with uv.

**Activation Triggers:**
Master the uv package manager for fast Python dependency management, virtual environments, and modern Python project workflows. Use when setting up Python projects, managing dependencies, or optimizing Python development workflows with uv.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### async-python-patterns

**Description:** Master Python asyncio, concurrent programming, and async/await patterns for high-performance applications. Use when building async APIs, concurrent systems, or I/O-bound applications requiring non-blocking operations.

**Activation Triggers:**
Master Python asyncio, concurrent programming, and async/await patterns for high-performance applications. Use when building async APIs, concurrent systems, or I/O-bound applications requiring non-blocking operations.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### python-performance-optimization

**Description:** Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, optimizing bottlenecks, or improving application performance.

**Activation Triggers:**
Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, optimizing bottlenecks, or improving application performance.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **1 slash commands**:

### /python-development:python-scaffold

**Description:** 

**Usage:**
```bash
/python-development:python-scaffold [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/python-development:python-scaffold
```

2. Work with agent:
```bash
@fastapi-pro implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@fastapi-pro`
2. Implementation: `@django-pro`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `javascript-typescript` - Related languages plugin
- `dotnet-development` - Related languages plugin

### Differences from Similar Plugins

The `python-development` plugin focuses specifically on modern python development with python 3.12+, django, fastapi, async patterns, and production best practices, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@fastapi-pro` for primary tasks in this domain
- Follow the plugin's specialized patterns for languages
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

- **python-testing-patterns:** Advanced patterns for power users
- **python-packaging:** Advanced patterns for power users

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

**Plugin:** python-development v1.2.1
**Last Updated:** 1.2.1
**Agents:** 3 | **Skills:** 5 | **Commands:** 1
