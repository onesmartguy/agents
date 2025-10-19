# Generative AI Prompt Engineering Plugin - Quick Start

## Installation
Plugin location: `/Users/eddie.flores/source/agents/generative-ai/`

## 5 Commands at Your Fingertips

### 1. Generate Midjourney Prompts
```
/prompt-midjourney [style] [description]

Examples:
/prompt-midjourney manga warrior in dynamic fighting stance
/prompt-midjourney golden age comic superhero flying over city
/prompt-midjourney film noir detective in rain-soaked alley
```
**Returns**: Production-ready `/imagine:` command with all parameters

### 2. Generate ComfyUI Prompts
```
/prompt-comfyui [style] [description] [options]

Examples:
/prompt-comfyui manga warrior in action pose
/prompt-comfyui western comic superhero in action pose consistency
/prompt-comfyui digital painting sci-fi character model:flux
```
**Returns**: Positive/negative prompts + LoRA recommendations + sampler settings

### 3. Generate Gemini Prompts
```
/prompt-gemini [style] [description] [options]

Examples:
/prompt-gemini manga teenage warrior in dynamic pose
/prompt-gemini western comic superhero in action text:true
/prompt-gemini photorealistic character design reference photorealism:true
```
**Returns**: Natural language prompt + Vertex AI settings

### 4. Generate Firefly Prompts
```
/prompt-firefly [style] [description] [options]

Examples:
/prompt-firefly comic book superhero in red cape flying over city
/prompt-firefly manga teenage warrior in action pose batch:5 aspect:2:3
/prompt-firefly concept art sci-fi character design photoshop:true
```
**Returns**: Concise prompt + filter + commercial safety confirmation

### 5. Convert Between Platforms
```
/convert-prompt [from-platform] [to-platform] [prompt]

Examples:
/convert-prompt midjourney comfyui [your-midjourney-prompt]
/convert-prompt comfyui firefly [your-comfyui-prompt]
/convert-prompt gemini firefly [your-gemini-prompt]
```
**Returns**: Converted prompt + platform mapping + settings

## 2 Skills for Deep Knowledge

### Skill 1: Prompt Conversion
Reusable knowledge for converting between platforms.

**Use when**:
- Testing concept across multiple platforms
- Switching platforms for a project
- Optimizing for different platform strengths

**Access**: Referenced in /convert-prompt command

### Skill 2: Style Library
50+ comic art styles with platform guidance.

**Use when**:
- Exploring available comic art styles
- Finding styles for your concept
- Getting platform-specific implementation guidance

**Access**: Reference in commands, or ask about specific styles

## Platform Quick Guide

| Platform | Best For | Speed | Learning Curve |
|----------|----------|-------|---|
| **Midjourney** | Artistic stylization, anime/manga | Medium | Easy |
| **ComfyUI** | Character consistency, control | Slow | Steep |
| **Gemini** | Photorealism, text-in-image | Medium | Easy |
| **Firefly** | Speed, commercial projects | Fast | Easiest |

## 5 Expert Agents

1. **Midjourney Expert**: v7, Niji 7, SREF codes, stylization
2. **ComfyUI Expert**: SDXL, FLUX, LoRAs, InstantID, ControlNet
3. **Gemini Expert**: Natural language, photorealism, text rendering
4. **Firefly Expert**: Concise prompting, filters, commercial safety
5. **Prompt Converter**: Cross-platform conversion, feature mapping

## 50+ Comic Art Styles

- **Manga**: Shounen, Seinen, Shoujo, Josei, Kodomo, Mecha, Chibi, Gore
- **Western**: Golden Age, Silver Age, Bronze Age, Modern, Marvel, DC, Image, Indie
- **European**: Ligne Claire, Moebius, Franco-Belgian, Fumetti, Heavy Metal, Editorial
- **Alternative**: Underground, Alternative, Zine, Webcomic
- **Genre**: Superhero, Noir, Horror, Sci-Fi, Fantasy, Western, War, Romance, Comedy, Spy
- **Digital**: Webtoon, Manhwa, Manhua, Digital Painting, Cel-Shaded
- **Experimental**: Minimalist, Watercolor, Mixed Media, Retro, Street Art, Collage, Abstract

## Common Workflows

### Quick Concept (5 minutes)
1. `/prompt-firefly` - Generate 5 concepts with batch:5
2. Select best concept
3. Use Photoshop Generative Fill for refinement
4. Export for review

### Character Consistency (1 hour)
1. `/prompt-comfyui` with `consistency` option
2. Generate multiple poses/expressions
3. Assemble panels in Photoshop
4. Polish with Firefly Generative Fill

### Cross-Platform Comparison (15 minutes)
1. `/prompt-midjourney` - Artistic version
2. `/convert-prompt` to ComfyUI - For character consistency
3. `/convert-prompt` to Gemini - For photorealism
4. `/convert-prompt` to Firefly - For commercial check
5. Compare all 4 outputs

### Production Pipeline (Varies)
1. Concept in Midjourney
2. Approve with Firefly batch variations
3. Production in ComfyUI with character consistency
4. Final compositing in Photoshop
5. Export for publication

## Tips

1. **Start simple** - Begin with one platform, add complexity later
2. **Use specific artists** - "Jim Lee style" > "comic book style"
3. **Apply filters/LoRAs** - Let these handle styling, describe content
4. **Test parameters** - Recommendations are starting points
5. **Save successful prompts** - Build your prompt library
6. **Batch generate** - Try 5 variations to compare
7. **Iterate based on output** - Refine based on results
8. **Reference documentation** - Each platform has comprehensive docs

## File Locations

**Plugin Root**: `/Users/eddie.flores/source/agents/generative-ai/`

**Key Files**:
- `/README.md` - Full plugin documentation
- `/.claude-plugin/plugin.json` - Plugin manifest
- `/agents/` - Expert agents
- `/commands/` - Command documentation
- `/skills/` - Reusable skills
- `/PLUGIN_SUMMARY.md` - Complete creation summary

**Documentation References**:
- `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/`

## Examples

### Example 1: Quick Manga Character
```
/prompt-midjourney shounen manga teenage warrior in action pose
```
Gets: Midjourney `/imagine` command optimized for action manga

### Example 2: ComfyUI Character Consistency
```
/prompt-comfyui manga character in different pose consistency
```
Gets: ComfyUI setup with InstantID + LoRAs for face consistency

### Example 3: Cross-Platform Comparison
```
/convert-prompt midjourney gemini [your-midjourney-prompt]
```
Gets: Natural language Gemini prompt from your Midjourney prompt

### Example 4: Firefly Batch Concepts
```
/prompt-firefly comic book superhero batch:5
```
Gets: 5 firefly prompts for batch generation

## What Each Command Returns

### /prompt-midjourney
- `/imagine:` command (copy-paste ready)
- Parameter recommendations
- Style analysis
- Quality notes
- Iteration suggestions

### /prompt-comfyui
- Positive prompt with weights
- Negative prompt
- LoRA recommendations with weights
- Sampler settings (CFG, steps, method)
- Resolution/aspect ratio
- Optional: InstantID/ControlNet setup

### /prompt-gemini
- Natural language prompt
- Vertex AI parameters
- Text-in-image guidance (if applicable)
- Aspect ratio recommendation
- Quality notes

### /prompt-firefly
- Concise 30-60 word prompt
- Filter recommendation
- Content type selection
- Aspect ratio
- Commercial safety confirmation

### /convert-prompt
- Source platform analysis
- Concept extraction
- Platform mapping
- Converted prompt (ready to use)
- Parameter recommendations
- Quality trade-offs (if applicable)

## Next Steps

1. **Try one command**: Start with `/prompt-midjourney` or `/prompt-firefly`
2. **Generate in target platform**: Copy prompt and generate
3. **Try another command**: Explore different platforms
4. **Convert between platforms**: Use `/convert-prompt`
5. **Build your library**: Save successful prompts
6. **Explore styles**: Ask about specific comic art styles
7. **Read full docs**: Check README.md for advanced features

## Support

For detailed information:
- See `/README.md` - Complete plugin documentation
- See individual agent files - Deep expertise profiles
- See individual command files - Detailed usage and examples
- See documentation links - Reference Em & E Comics docs

---

**Ready to generate AI prompts? Start with `/prompt-midjourney`, `/prompt-comfyui`, `/prompt-gemini`, or `/prompt-firefly`!**
