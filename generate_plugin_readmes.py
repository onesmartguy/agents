#!/usr/bin/env python3
"""
Generate comprehensive README.md files for all plugins in the Claude Code marketplace.
"""
import json
import os
from pathlib import Path
from typing import Dict, List, Any

def read_file_safe(filepath: Path) -> str:
    """Read file content safely, return empty string if file doesn't exist."""
    try:
        return filepath.read_text()
    except Exception as e:
        return f"<!-- Error reading file: {e} -->"

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown file."""
    if not content.startswith('---'):
        return {}

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}

    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()
    return frontmatter

def get_plugin_files(plugin_dir: Path) -> Dict[str, List[Path]]:
    """Get all agents, skills, and commands for a plugin."""
    return {
        'agents': list(plugin_dir.glob('agents/*.md')),
        'skills': list(plugin_dir.glob('skills/*/SKILL.md')),
        'commands': list(plugin_dir.glob('commands/*.md'))
    }

def generate_readme_content(plugin: Dict[str, Any], base_path: Path) -> str:
    """Generate comprehensive README content for a plugin."""
    plugin_name = plugin['name']
    plugin_dir = base_path / plugin['source'].lstrip('./')

    # Get all files
    files = get_plugin_files(plugin_dir)

    # Read agent files
    agents_info = []
    for agent_file in files['agents']:
        content = read_file_safe(agent_file)
        frontmatter = parse_frontmatter(content)
        agents_info.append({
            'file': agent_file.name,
            'name': frontmatter.get('name', agent_file.stem),
            'description': frontmatter.get('description', ''),
            'model': frontmatter.get('model', 'unknown'),
            'content': content
        })

    # Read skill files
    skills_info = []
    for skill_file in files['skills']:
        content = read_file_safe(skill_file)
        frontmatter = parse_frontmatter(content)
        skills_info.append({
            'name': frontmatter.get('name', skill_file.parent.name),
            'description': frontmatter.get('description', ''),
            'content': content,
            'path': skill_file.parent.name
        })

    # Read command files
    commands_info = []
    for cmd_file in files['commands']:
        content = read_file_safe(cmd_file)
        frontmatter = parse_frontmatter(content)
        commands_info.append({
            'file': cmd_file.name,
            'name': frontmatter.get('name', cmd_file.stem),
            'description': frontmatter.get('description', ''),
            'content': content
        })

    # Generate README
    readme = f"""# {plugin_name}

> {plugin['description']}

**Version:** {plugin['version']}
**Category:** {plugin['category']}
**Author:** {plugin['author']['name']}

## Overview

### What This Plugin Does

{plugin['description']}

### Primary Use Cases

"""

    # Add use cases based on keywords
    if 'keywords' in plugin:
        for keyword in plugin['keywords'][:5]:
            readme += f"- {keyword.replace('-', ' ').title()} workflows\n"

    readme += f"""
### Who Should Use This

- Developers working with {plugin['category']} systems
- Teams requiring {plugin_name.replace('-', ' ')} capabilities
"""

    if len(agents_info) > 0:
        readme += f"- Projects leveraging {len(agents_info)} specialized agents for task automation\n"

    readme += "\n## Quick Start\n\n"
    readme += f"""### Installation

1. Install the plugin in Claude Code:
```bash
# Add to your .claude-plugin/marketplace.json or install via Claude Code CLI
```

2. Verify installation:
```bash
# List available agents
claude agents list | grep {plugin_name}
```

### Basic Usage

"""

    # Add example based on first agent or command
    if agents_info:
        first_agent = agents_info[0]
        readme += f"""Invoke the primary agent:
```bash
# Using the {first_agent['name']} agent
@{first_agent['name']} <your request>
```

"""

    if commands_info:
        first_cmd = commands_info[0]
        readme += f"""Or use the command interface:
```bash
/{plugin_name}:{first_cmd['name'].replace('.md', '')} <arguments>
```

"""

    # Agents Reference
    if agents_info:
        readme += "## Agents Reference\n\n"
        readme += f"This plugin provides **{len(agents_info)} specialized agents**:\n\n"

        for agent in agents_info:
            model_reason = {
                'sonnet': 'Complex reasoning and architecture decisions',
                'haiku': 'Fast execution and deterministic tasks'
            }.get(agent['model'], 'General purpose')

            readme += f"""### {agent['name']}

**Model:** {agent['model']} - {model_reason}

**Purpose:** {agent['description']}

**When to Use Proactively:**
- {agent['description'].split('.')[0]}
- When you need specialized {agent['name'].replace('-', ' ')} expertise

**Example Invocation:**
```bash
@{agent['name']} <specific task or question>
```

"""

    # Skills Reference
    if skills_info:
        readme += "## Skills Reference\n\n"
        readme += f"This plugin includes **{len(skills_info)} progressive disclosure skills** for advanced patterns:\n\n"

        for skill in skills_info:
            readme += f"""### {skill['name']}

**Description:** {skill['description']}

**Activation Triggers:**
{skill['description']}

**Key Techniques:**
- Progressive disclosure of knowledge
- On-demand pattern loading
- Context-aware skill activation

"""

    # Commands Reference
    if commands_info:
        readme += "## Commands Reference\n\n"
        readme += f"This plugin provides **{len(commands_info)} slash commands**:\n\n"

        for cmd in commands_info:
            readme += f"""### /{plugin_name}:{cmd['name'].replace('.md', '')}

**Description:** {cmd['description']}

**Usage:**
```bash
/{plugin_name}:{cmd['name'].replace('.md', '')} [options]
```

"""

    # Workflow Examples
    readme += """## Complete Workflow Examples

### Example 1: Basic Workflow

"""

    if agents_info and commands_info:
        readme += f"""1. Initialize with command:
```bash
/{plugin_name}:{commands_info[0]['name'].replace('.md', '')}
```

2. Work with agent:
```bash
@{agents_info[0]['name']} implement the feature
```

3. Review and iterate
"""
    elif agents_info:
        readme += f"""1. Engage the agent:
```bash
@{agents_info[0]['name']} start new project
```

2. Follow agent guidance for implementation
"""

    readme += "\n### Example 2: Advanced Workflow\n\n"

    if len(agents_info) > 1:
        readme += f"""Multi-agent coordination:

1. Architecture planning: `@{agents_info[0]['name']}`
2. Implementation: `@{agents_info[1]['name']}`
3. Review and refinement
"""

    # Plugin Relationships
    readme += """
## Plugin Relationships

### Similar Plugins

"""

    # Add similar plugins based on category
    category_plugins = {
        'development': ['backend-development', 'frontend-mobile-development', 'full-stack-orchestration'],
        'languages': ['python-development', 'javascript-typescript', 'dotnet-development'],
        'infrastructure': ['kubernetes-operations', 'cloud-infrastructure', 'cicd-automation'],
    }

    similar = category_plugins.get(plugin['category'], [])
    for sim in similar[:3]:
        if sim != plugin_name:
            readme += f"- `{sim}` - Related {plugin['category']} plugin\n"

    readme += """
### Differences from Similar Plugins

"""

    readme += f"The `{plugin_name}` plugin focuses specifically on {plugin['description'].lower()}, "
    readme += "while similar plugins may have broader or different specializations.\n\n"

    readme += "### Works Well With\n\n"

    # Add complementary plugins
    complements = {
        'development': ['testing', 'documentation', 'quality'],
        'testing': ['development', 'quality', 'workflows'],
        'security': ['quality', 'infrastructure', 'testing'],
    }

    comp = complements.get(plugin['category'], [])
    for c in comp:
        readme += f"- Plugins in the `{c}` category\n"

    readme += """
### Integration Patterns

- **Sequential workflows:** Chain multiple agents for complex tasks
- **Parallel execution:** Run independent agents simultaneously
- **Context sharing:** Maintain state across agent interactions

## Best Practices

### Do's

"""

    if agents_info:
        readme += f"- Use `@{agents_info[0]['name']}` for primary tasks in this domain\n"

    readme += f"""- Follow the plugin's specialized patterns for {plugin['category']}
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

"""

    if 'performance' in plugin['keywords'] if 'keywords' in plugin else []:
        readme += "- Monitor performance metrics\n"
        readme += "- Profile before optimizing\n"

    readme += "- Use progressive disclosure to load only needed knowledge\n"
    readme += "- Cache agent responses when appropriate\n"

    readme += """
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

"""

    readme += """
| Error | Cause | Solution |
|-------|-------|----------|
| Agent not found | Plugin not installed | Verify installation |
| Skill unavailable | Path mismatch | Check skill directory structure |
| Command failed | Missing dependencies | Review prerequisites |

### Debugging Techniques

1. **Verbose mode:** Request detailed explanations from agents
2. **Step-by-step:** Break complex tasks into smaller steps
3. **Isolation:** Test agents individually before combining

"""

    # Advanced Topics (if skills exist)
    if skills_info:
        readme += """## Advanced Topics

### Power User Features

"""
        for skill in skills_info[:2]:
            readme += f"- **{skill['name']}:** Advanced patterns for power users\n"

        readme += """
### Customization Options

- Adapt agent instructions for your workflow
- Extend skills with custom patterns
- Configure progressive disclosure depth

### Performance Tuning

- Use Haiku agents for speed-critical paths
- Batch similar operations
- Optimize context window usage

"""

    # Footer
    readme += f"""
## Contributing

Contributions are welcome! Please see the [main repository](https://github.com/wshobson/agents) for guidelines.

## License

{plugin['license']}

## Support

- **Issues:** [GitHub Issues](https://github.com/wshobson/agents/issues)
- **Discussions:** [GitHub Discussions](https://github.com/wshobson/agents/discussions)
- **Documentation:** [Full Documentation](https://github.com/wshobson/agents)

---

**Plugin:** {plugin_name} v{plugin['version']}
**Last Updated:** {plugin['version']}
**Agents:** {len(agents_info)} | **Skills:** {len(skills_info)} | **Commands:** {len(commands_info)}
"""

    return readme


def main():
    """Main function to generate all READMEs."""
    base_path = Path(__file__).parent
    marketplace_file = base_path / '.claude-plugin' / 'marketplace.json'

    # Load marketplace
    with open(marketplace_file) as f:
        marketplace = json.load(f)

    plugins = marketplace['plugins']
    stats = {
        'total': len(plugins),
        'created': 0,
        'updated': 0,
        'errors': [],
        'agents_count': 0,
        'skills_count': 0,
        'commands_count': 0
    }

    print(f"Generating README files for {stats['total']} plugins...\n")

    for plugin in plugins:
        plugin_name = plugin['name']
        plugin_dir = base_path / plugin['source'].lstrip('./')
        readme_path = plugin_dir / 'README.md'

        try:
            # Check if directory exists
            if not plugin_dir.exists():
                stats['errors'].append(f"{plugin_name}: Directory not found")
                print(f"⚠️  {plugin_name}: Directory not found")
                continue

            # Generate README content
            content = generate_readme_content(plugin, base_path)

            # Count components
            files = get_plugin_files(plugin_dir)
            stats['agents_count'] += len(files['agents'])
            stats['skills_count'] += len(files['skills'])
            stats['commands_count'] += len(files['commands'])

            # Check if README exists
            if readme_path.exists():
                # Check if it's the comic-production plugin
                if plugin_name == 'comic-production':
                    print(f"📝 {plugin_name}: Skipping (existing comprehensive README)")
                    continue
                stats['updated'] += 1
                action = "Updated"
            else:
                stats['created'] += 1
                action = "Created"

            # Write README
            readme_path.write_text(content)

            print(f"✅ {plugin_name}: {action} ({len(files['agents'])} agents, {len(files['skills'])} skills, {len(files['commands'])} commands)")

        except Exception as e:
            stats['errors'].append(f"{plugin_name}: {str(e)}")
            print(f"❌ {plugin_name}: Error - {str(e)}")

    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total plugins: {stats['total']}")
    print(f"READMEs created: {stats['created']}")
    print(f"READMEs updated: {stats['updated']}")
    print(f"Errors: {len(stats['errors'])}")
    print(f"\nTotal agents documented: {stats['agents_count']}")
    print(f"Total skills documented: {stats['skills_count']}")
    print(f"Total commands documented: {stats['commands_count']}")

    if stats['errors']:
        print("\nErrors:")
        for error in stats['errors']:
            print(f"  - {error}")

    print("\nDocumentation coverage: {:.1f}%".format(
        ((stats['created'] + stats['updated']) / stats['total']) * 100
    ))


if __name__ == '__main__':
    main()
