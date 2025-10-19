# quantitative-trading

> Quantitative analysis, algorithmic trading strategies, financial modeling, portfolio risk management, and backtesting

**Version:** 1.2.0
**Category:** finance
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Quantitative analysis, algorithmic trading strategies, financial modeling, portfolio risk management, and backtesting

### Primary Use Cases

- Fintech workflows
- Quant workflows
- Trading workflows
- Algorithmic Trading workflows
- Risk Management workflows

### Who Should Use This

- Developers working with finance systems
- Teams requiring quantitative trading capabilities
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
claude agents list | grep quantitative-trading
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the quant-analyst agent
@quant-analyst <your request>
```

## Agents Reference

This plugin provides **2 specialized agents**:

### quant-analyst

**Model:** sonnet - Complex reasoning and architecture decisions

**Purpose:** Build financial models, backtest trading strategies, and analyze market data. Implements risk metrics, portfolio optimization, and statistical arbitrage. Use PROACTIVELY for quantitative finance, trading algorithms, or risk analysis.

**When to Use Proactively:**
- Build financial models, backtest trading strategies, and analyze market data
- When you need specialized quant analyst expertise

**Example Invocation:**
```bash
@quant-analyst <specific task or question>
```

### risk-manager

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses. Use PROACTIVELY for risk assessment, trade tracking, or portfolio protection.

**When to Use Proactively:**
- Monitor portfolio risk, R-multiples, and position limits
- When you need specialized risk manager expertise

**Example Invocation:**
```bash
@risk-manager <specific task or question>
```

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@quant-analyst start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow

Multi-agent coordination:

1. Architecture planning: `@quant-analyst`
2. Implementation: `@risk-manager`
3. Review and refinement

## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `quantitative-trading` plugin focuses specifically on quantitative analysis, algorithmic trading strategies, financial modeling, portfolio risk management, and backtesting, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@quant-analyst` for primary tasks in this domain
- Follow the plugin's specialized patterns for finance
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

**Plugin:** quantitative-trading v1.2.0
**Last Updated:** 1.2.0
**Agents:** 2 | **Skills:** 0 | **Commands:** 0
