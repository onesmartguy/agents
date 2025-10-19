# javascript-typescript

> JavaScript and TypeScript development with ES6+, Node.js, React, and modern web frameworks

**Version:** 1.2.1
**Category:** languages
**Author:** Seth Hobson

## Overview

### What This Plugin Does

JavaScript and TypeScript development with ES6+, Node.js, React, and modern web frameworks

### Primary Use Cases

- Javascript workflows
- Typescript workflows
- Es6 workflows
- Nodejs workflows
- React workflows

### Who Should Use This

- Developers working with languages systems
- Teams requiring javascript typescript capabilities
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
claude agents list | grep javascript-typescript
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the javascript-pro agent
@javascript-pro <your request>
```

Or use the command interface:
```bash
/javascript-typescript:typescript-scaffold <arguments>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### javascript-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility. Use PROACTIVELY for JavaScript optimization, async debugging, or complex JS patterns.

**When to Use Proactively:**
- Master modern JavaScript with ES6+, async patterns, and Node
- When you need specialized javascript pro expertise

**Example Invocation:**
```bash
@javascript-pro <specific task or question>
```

### typescript-pro

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade patterns. Use PROACTIVELY for TypeScript architecture, type inference optimization, or advanced typing patterns.

**When to Use Proactively:**
- Master TypeScript with advanced types, generics, and strict type safety
- When you need specialized typescript pro expertise

**Example Invocation:**
```bash
@typescript-pro <specific task or question>
```

## Skills Reference

This plugin includes **4 progressive disclosure skills** for advanced patterns:

### javascript-testing-patterns

**Description:** Implement comprehensive testing strategies using Jest, Vitest, and Testing Library for unit tests, integration tests, and end-to-end testing with mocking, fixtures, and test-driven development. Use when writing JavaScript/TypeScript tests, setting up test infrastructure, or implementing TDD/BDD workflows.

**Activation Triggers:**
Implement comprehensive testing strategies using Jest, Vitest, and Testing Library for unit tests, integration tests, and end-to-end testing with mocking, fixtures, and test-driven development. Use when writing JavaScript/TypeScript tests, setting up test infrastructure, or implementing TDD/BDD workflows.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### typescript-advanced-types

**Description:** Master TypeScript's advanced type system including generics, conditional types, mapped types, template literals, and utility types for building type-safe applications. Use when implementing complex type logic, creating reusable type utilities, or ensuring compile-time type safety in TypeScript projects.

**Activation Triggers:**
Master TypeScript's advanced type system including generics, conditional types, mapped types, template literals, and utility types for building type-safe applications. Use when implementing complex type logic, creating reusable type utilities, or ensuring compile-time type safety in TypeScript projects.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### modern-javascript-patterns

**Description:** Master ES6+ features including async/await, destructuring, spread operators, arrow functions, promises, modules, iterators, generators, and functional programming patterns for writing clean, efficient JavaScript code. Use when refactoring legacy code, implementing modern patterns, or optimizing JavaScript applications.

**Activation Triggers:**
Master ES6+ features including async/await, destructuring, spread operators, arrow functions, promises, modules, iterators, generators, and functional programming patterns for writing clean, efficient JavaScript code. Use when refactoring legacy code, implementing modern patterns, or optimizing JavaScript applications.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### nodejs-backend-patterns

**Description:** Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handling, authentication, database integration, and API design best practices. Use when creating Node.js servers, REST APIs, GraphQL backends, or microservices architectures.

**Activation Triggers:**
Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handling, authentication, database integration, and API design best practices. Use when creating Node.js servers, REST APIs, GraphQL backends, or microservices architectures.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **1 slash commands**:

### /javascript-typescript:typescript-scaffold

**Description:** 

**Usage:**
```bash
/javascript-typescript:typescript-scaffold [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/javascript-typescript:typescript-scaffold
```

2. Work with agent:
```bash
@javascript-pro implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@javascript-pro`
2. Implementation: `@typescript-pro`
3. Review and refinement

## Plugin Relationships

### Similar Plugins

- `python-development` - Related languages plugin
- `dotnet-development` - Related languages plugin

### Differences from Similar Plugins

The `javascript-typescript` plugin focuses specifically on javascript and typescript development with es6+, node.js, react, and modern web frameworks, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@javascript-pro` for primary tasks in this domain
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

- **javascript-testing-patterns:** Advanced patterns for power users
- **typescript-advanced-types:** Advanced patterns for power users

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

**Plugin:** javascript-typescript v1.2.1
**Last Updated:** 1.2.1
**Agents:** 2 | **Skills:** 4 | **Commands:** 1
