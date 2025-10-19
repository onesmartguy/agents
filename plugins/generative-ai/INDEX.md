# Generative AI Prompt Engineering Plugin - Complete Index

## Quick Navigation

### Start Here
- **README.md** - Complete plugin overview and user guide
- **QUICK_START.md** - 5-minute quick reference
- **PLUGIN_SUMMARY.md** - Detailed creation summary
- **INDEX.md** - This file

### 5 Expert Agents (agents/)
- **midjourney-expert.md** - Midjourney v7, Niji 7, SREF codes
- **comfyui-expert.md** - ComfyUI, SDXL, FLUX, LoRAs, InstantID
- **gemini-expert.md** - Google Gemini Imagen 3, natural language
- **firefly-expert.md** - Adobe Firefly, concise, commercial-safe
- **prompt-converter.md** - Cross-platform conversion

### 5 Production Commands (commands/)
- **prompt-midjourney.md** - `/prompt-midjourney` command
- **prompt-comfyui.md** - `/prompt-comfyui` command
- **prompt-gemini.md** - `/prompt-gemini` command
- **prompt-firefly.md** - `/prompt-firefly` command
- **convert-prompt.md** - `/convert-prompt` command

### 2 Reusable Skills (skills/)
- **prompt-conversion/SKILL.md** - Cross-platform conversion skill
- **style-library/SKILL.md** - 50+ comic art styles skill

### Plugin Configuration (.claude-plugin/)
- **plugin.json** - Plugin manifest
- **marketplace.json** - Marketplace metadata

## By Task

### "I want to generate a prompt"
1. Choose platform: Midjourney, ComfyUI, Gemini, or Firefly
2. Go to corresponding command file in commands/
3. Follow the syntax and examples
4. Copy the returned prompt
5. Use in your chosen platform

### "I want to convert a prompt"
1. Go to **commands/convert-prompt.md**
2. Specify source and target platform
3. Copy your source prompt
4. Review the converted prompt
5. Use in target platform

### "I want to learn about comic art styles"
1. Read **skills/style-library/SKILL.md**
2. Browse 50+ styles organized by category
3. Find platform-specific guidance
4. Check examples and artist references

### "I want to compare platforms"
1. Read **README.md** Platform Comparison section
2. See statistics table showing strengths/weaknesses
3. Review workflow examples for multi-platform workflows

### "I want to understand a specific platform"
1. Find platform in agents/ directory
2. Read corresponding agent profile
3. Review command documentation
4. Check examples in command files

## By Platform

### Midjourney (v7, Niji 7)
- **Agent**: agents/midjourney-expert.md
- **Command**: commands/prompt-midjourney.md
- **Best for**: Artistic stylization, speed, anime/manga
- **Specialty**: SREF codes, parameters, Niji 7
- **Documentation**: Em & E Comics Midjourney docs

### ComfyUI (SDXL, FLUX)
- **Agent**: agents/comfyui-expert.md
- **Command**: commands/prompt-comfyui.md
- **Best for**: Character consistency, control, local generation
- **Specialty**: LoRAs, InstantID, ControlNet, model selection
- **Documentation**: Em & E Comics ComfyUI docs

### Gemini (Imagen 3)
- **Agent**: agents/gemini-expert.md
- **Command**: commands/prompt-gemini.md
- **Best for**: Photorealism, text-in-image, natural language
- **Specialty**: Descriptive language, Vertex AI, text rendering
- **Documentation**: Em & E Comics Gemini docs

### Firefly
- **Agent**: agents/firefly-expert.md
- **Command**: commands/prompt-firefly.md
- **Best for**: Speed, commercial projects, Adobe workflow
- **Specialty**: Concise prompting, filters, commercial safety
- **Documentation**: Em & E Comics Firefly docs

### Cross-Platform
- **Agent**: agents/prompt-converter.md
- **Command**: commands/convert-prompt.md
- **Skill**: skills/prompt-conversion/SKILL.md
- **Documentation**: Em & E Comics cross-platform guide

## By Comic Art Style Category

### Manga & Anime (8 styles)
Shounen, Seinen, Shoujo, Josei, Kodomo, Mecha, Chibi, Gore

### Western Comics (10+ styles)
Golden Age, Silver Age, Bronze Age, Modern, Marvel, DC, Image, Indie

### European Comics (6 styles)
Ligne Claire, Moebius, Franco-Belgian, Fumetti, Heavy Metal, Editorial

### Alternative & Underground (4 styles)
Underground Comix, Alternative, Zine, Webcomic

### Genre-Specific (10+ styles)
Superhero, Noir, Horror, Sci-Fi, Fantasy, Western, War, Romance, Comedy, Spy

### Digital & Modern (5+ styles)
Webtoon, Manhwa, Manhua, Digital Painting, Cel-Shaded

### Experimental & Hybrid (7+ styles)
Minimalist, Watercolor, Mixed Media, Retro, Street Art, Collage, Abstract

See **skills/style-library/SKILL.md** for complete style reference.

## Command Reference

### /prompt-midjourney
```
/prompt-midjourney [style] [description]
Returns: /imagine command with parameters
See: commands/prompt-midjourney.md
```

### /prompt-comfyui
```
/prompt-comfyui [style] [description] [options]
Returns: Positive/negative prompts + LoRAs + settings
See: commands/prompt-comfyui.md
```

### /prompt-gemini
```
/prompt-gemini [style] [description] [options]
Returns: Natural language prompt + settings
See: commands/prompt-gemini.md
```

### /prompt-firefly
```
/prompt-firefly [style] [description] [options]
Returns: Concise prompt + filter + settings
See: commands/prompt-firefly.md
```

### /convert-prompt
```
/convert-prompt [from-platform] [to-platform] [prompt]
Returns: Converted prompt + analysis + settings
See: commands/convert-prompt.md
```

## Documentation Structure

### Plugin Files (root)
- README.md - Complete guide
- QUICK_START.md - Quick reference
- PLUGIN_SUMMARY.md - Creation details
- INDEX.md - This file

### Agent Files (agents/)
- Each agent has comprehensive profile
- Specializations and expertise documented
- User interaction patterns explained
- Integration points specified

### Command Files (commands/)
- Syntax and usage documented
- Multiple detailed examples provided
- Parameter recommendations
- Quality notes and tips

### Skill Files (skills/)
- Progressive disclosure (4 levels)
- Use cases and scenarios
- Troubleshooting guidance
- Integration points

### Configuration Files (.claude-plugin/)
- plugin.json - Manifest with metadata
- marketplace.json - Marketplace information

## Key Features

### Production-Ready
- All prompts are copy-paste ready
- Parameter recommendations optimized
- Real-world examples throughout
- Quality guidance included

### Comprehensive Coverage
- 50+ comic art styles documented
- 4 major platforms covered
- 12 conversion paths supported
- Advanced features guided

### Well-Documented
- 6,000+ lines of documentation
- 20+ detailed examples
- Cross-platform workflows
- Troubleshooting guides

### Integration Ready
- References Em & E Comics docs
- Links to platform fundamentals
- Cross-references throughout
- Complete knowledge base

## Common Workflows

### Quick Concept (5 min)
1. `/prompt-firefly` with batch:5
2. Select best concept
3. Refine in Photoshop
4. Export

### Character Consistency (1 hour)
1. `/prompt-comfyui` with consistency
2. Generate multiple poses
3. Assemble in Photoshop
4. Polish with Firefly

### Cross-Platform (15 min)
1. `/prompt-midjourney` - artistic
2. `/convert-prompt` to ComfyUI - consistent
3. `/convert-prompt` to Gemini - photorealistic
4. Compare all versions

### Production Pipeline (variable)
1. Concept in Midjourney
2. Approve in Firefly
3. Production in ComfyUI
4. Polish in Photoshop
5. Export

## Getting Started

### For Complete Beginners
1. Read **QUICK_START.md**
2. Try `/prompt-firefly` (easiest)
3. Generate in Firefly
4. Explore other commands
5. Read README.md for advanced

### For Existing Platform Users
1. Read **README.md** Platform Comparison
2. Find your platform in agents/
3. Read corresponding command file
4. Try generating a prompt
5. Use `/convert-prompt` for other platforms

### For Advanced Users
1. Review all agent profiles
2. Study conversion strategies in prompt-converter.md
3. Read skills for progressive disclosure
4. Plan production workflows
5. Reference Em & E Comics docs for depth

## File Locations

**Main Directory**: `/Users/eddie.flores/source/agents/generative-ai/`

**Subdirectories**:
- `.claude-plugin/` - Configuration
- `agents/` - Expert agents
- `commands/` - Command documentation
- `skills/` - Reusable skills

**Documentation References**:
- `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/`

## Statistics

| Metric | Count |
|--------|-------|
| Total Files | 16 |
| Total Lines | 6,073 |
| Expert Agents | 5 |
| Commands | 5 |
| Skills | 2 |
| Comic Styles | 50+ |
| Platforms | 4 |
| Conversion Paths | 12 |
| Code Examples | 20+ |
| Documentation Pages | 4 |

## Support & References

### Documentation
- See individual files for detailed information
- README.md for comprehensive guide
- QUICK_START.md for immediate reference

### Referenced Em & E Comics Documentation
- Midjourney: `docs/prompts/generative-ai/midjourney/`
- ComfyUI: `docs/prompts/generative-ai/comfyui/`
- Gemini: `docs/prompts/generative-ai/gemini/`
- Firefly: `docs/prompts/generative-ai/adobe-firefly/`
- Cross-Platform: `docs/prompts/generative-ai/cross-platform/`

## Plugin Information

- **Name**: generative-ai-prompt-engineering
- **Version**: 1.0.0
- **Author**: Em & E Comics
- **License**: MIT
- **Status**: Production-Ready
- **Created**: January 2025

---

## Navigation Tips

### Find by Task
Use "By Task" section above to find what you need.

### Find by Platform
Use "By Platform" section to get platform-specific guidance.

### Find by Style
Use "By Comic Art Style Category" to explore styles.

### Find by Command
Use "Command Reference" for quick command lookup.

### Deep Dive
Start with README.md for comprehensive understanding.

---

**Last Updated**: January 2025
**Status**: Production-Ready
**Location**: `/Users/eddie.flores/source/agents/generative-ai/`
