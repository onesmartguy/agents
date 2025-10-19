# machine-learning-ops

> ML model training pipelines, hyperparameter tuning, model deployment automation, experiment tracking, and MLOps workflows

**Version:** 1.2.1
**Category:** ai-ml
**Author:** Seth Hobson

## Overview

### What This Plugin Does

ML model training pipelines, hyperparameter tuning, model deployment automation, experiment tracking, and MLOps workflows

### Primary Use Cases

- Machine Learning workflows
- Mlops workflows
- Model Training workflows
- Tensorflow workflows
- Pytorch workflows

### Who Should Use This

- Developers working with ai-ml systems
- Teams requiring machine learning ops capabilities
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
claude agents list | grep machine-learning-ops
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the ml-engineer agent
@ml-engineer <your request>
```

Or use the command interface:
```bash
/machine-learning-ops:ml-pipeline <arguments>
```

## Agents Reference

This plugin provides **3 specialized agents**:

### ml-engineer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. Implements model serving, feature engineering, A/B testing, and monitoring. Use PROACTIVELY for ML model deployment, inference optimization, or production ML infrastructure.

**When to Use Proactively:**
- Build production ML systems with PyTorch 2
- When you need specialized ml engineer expertise

**Example Invocation:**
```bash
@ml-engineer <specific task or question>
```

### mlops-engineer

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. Implements automated training, deployment, and monitoring across cloud platforms. Use PROACTIVELY for ML infrastructure, experiment management, or pipeline automation.

**When to Use Proactively:**
- Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools
- When you need specialized mlops engineer expertise

**Example Invocation:**
```bash
@mlops-engineer <specific task or question>
```

### data-scientist

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive modeling, and business intelligence. Use PROACTIVELY for data analysis tasks, ML modeling, statistical analysis, and data-driven insights.

**When to Use Proactively:**
- Expert data scientist for advanced analytics, machine learning, and statistical modeling
- When you need specialized data scientist expertise

**Example Invocation:**
```bash
@data-scientist <specific task or question>
```

## Skills Reference

This plugin includes **1 progressive disclosure skills** for advanced patterns:

### ml-pipeline-workflow

**Description:** Build end-to-end MLOps pipelines from data preparation through model training, validation, and production deployment. Use when creating ML pipelines, implementing MLOps practices, or automating model training and deployment workflows.

**Activation Triggers:**
Build end-to-end MLOps pipelines from data preparation through model training, validation, and production deployment. Use when creating ML pipelines, implementing MLOps practices, or automating model training and deployment workflows.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Commands Reference

This plugin provides **1 slash commands**:

### /machine-learning-ops:ml-pipeline

**Description:** 

**Usage:**
```bash
/machine-learning-ops:ml-pipeline [options]
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Initialize with command:
```bash
/machine-learning-ops:ml-pipeline
```

2. Work with agent:
```bash
@ml-engineer implement the feature
```

3. Review and iterate

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@ml-engineer`
2. Implementation: `@mlops-engineer`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `machine-learning-ops` plugin focuses specifically on ml model training pipelines, hyperparameter tuning, model deployment automation, experiment tracking, and mlops workflows, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@ml-engineer` for primary tasks in this domain
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

- **ml-pipeline-workflow:** Advanced patterns for power users

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

**Plugin:** machine-learning-ops v1.2.1
**Last Updated:** 1.2.1
**Agents:** 3 | **Skills:** 1 | **Commands:** 1
