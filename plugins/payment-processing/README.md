# payment-processing

> Payment gateway integration with Stripe, PayPal, RainforestPay, checkout flow implementation, subscription billing, and PCI compliance

**Version:** 1.2.2
**Category:** payments
**Author:** Seth Hobson

## Overview

### What This Plugin Does

Payment gateway integration with Stripe, PayPal, RainforestPay, checkout flow implementation, subscription billing, and PCI compliance

### Primary Use Cases

- Payments workflows
- Stripe workflows
- Paypal workflows
- Rainforest workflows
- Checkout workflows

### Who Should Use This

- Developers working with payments systems
- Teams requiring payment processing capabilities
- Projects leveraging 1 specialized agents for task automation

## Quick Start

### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep payment-processing
```

### Basic Usage

Invoke the primary agent:
```bash
# Using the payment-integration agent
@payment-integration <your request>
```

## Agents Reference

This plugin provides **1 specialized agents**:

### payment-integration

**Model:** haiku - Fast execution and deterministic tasks

**Purpose:** Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance. Use PROACTIVELY when implementing payments, billing, or subscription features.

**When to Use Proactively:**
- Integrate Stripe, PayPal, and payment processors
- When you need specialized payment integration expertise

**Example Invocation:**
```bash
@payment-integration <specific task or question>
```

## Skills Reference

This plugin includes **5 progressive disclosure skills** for advanced patterns:

### stripe-integration

**Description:** Implement Stripe payment processing for robust, PCI-compliant payment flows including checkout, subscriptions, and webhooks. Use when integrating Stripe payments, building subscription systems, or implementing secure checkout flows.

**Activation Triggers:**
Implement Stripe payment processing for robust, PCI-compliant payment flows including checkout, subscriptions, and webhooks. Use when integrating Stripe payments, building subscription systems, or implementing secure checkout flows.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### billing-automation

**Description:** Build automated billing systems for recurring payments, invoicing, subscription lifecycle, and dunning management. Use when implementing subscription billing, automating invoicing, or managing recurring payment systems.

**Activation Triggers:**
Build automated billing systems for recurring payments, invoicing, subscription lifecycle, and dunning management. Use when implementing subscription billing, automating invoicing, or managing recurring payment systems.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### paypal-integration

**Description:** Integrate PayPal payment processing with support for express checkout, subscriptions, and refund management. Use when implementing PayPal payments, processing online transactions, or building e-commerce checkout flows.

**Activation Triggers:**
Integrate PayPal payment processing with support for express checkout, subscriptions, and refund management. Use when implementing PayPal payments, processing online transactions, or building e-commerce checkout flows.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### pci-compliance

**Description:** Implement PCI DSS compliance requirements for secure handling of payment card data and payment systems. Use when securing payment processing, achieving PCI compliance, or implementing payment card security measures.

**Activation Triggers:**
Implement PCI DSS compliance requirements for secure handling of payment card data and payment systems. Use when securing payment processing, achieving PCI compliance, or implementing payment card security measures.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

### rainforest-integration

**Description:** Implement RainforestPay embedded payment processing for vertical SaaS platforms with secure components, API integration, and webhook handling. Use when building embedded payments for SaaS platforms, reducing PCI scope, or implementing white-label payment solutions.

**Activation Triggers:**
Implement RainforestPay embedded payment processing for vertical SaaS platforms with secure components, API integration, and webhook handling. Use when building embedded payments for SaaS platforms, reducing PCI scope, or implementing white-label payment solutions.

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

## Complete Workflow Examples

### Example 1: Basic Workflow

1. Engage the agent:
```bash
@payment-integration start new project
```

2. Follow agent guidance for implementation

### Example 2: Advanced Workflow


## Plugin Relationships

### Similar Plugins


### Differences from Similar Plugins

The `payment-processing` plugin focuses specifically on payment gateway integration with stripe, paypal, rainforestpay, checkout flow implementation, subscription billing, and pci compliance, while similar plugins may have broader or different specializations.

### Works Well With


### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

- Use `@payment-integration` for primary tasks in this domain
- Follow the plugin's specialized patterns for payments
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

- **stripe-integration:** Advanced patterns for power users
- **billing-automation:** Advanced patterns for power users

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

**Plugin:** payment-processing v1.2.2
**Last Updated:** 1.2.2
**Agents:** 1 | **Skills:** 5 | **Commands:** 0
