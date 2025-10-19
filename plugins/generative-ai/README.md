# Generative AI Prompt Engineering Plugin

A comprehensive Claude Code plugin providing expert agents, commands, and skills for AI image generation prompt engineering across **Midjourney v7**, **ComfyUI** (SDXL/FLUX), **Google Gemini Imagen 3**, and **Adobe Firefly**.

## Overview

This plugin enables you to:
- Generate production-ready prompts for any of 4 major AI image generation platforms
- Convert prompts between platforms with intent preservation
- Browse and apply 50+ comic art styles
- Access expert guidance on platform-specific optimization
- Plan complex multi-platform production workflows

**Perfect for**: Comic creators, concept artists, game designers, illustrators, animation studios, and anyone generating images with AI.

## Quick Start

### Generate Your First Prompt

```
/prompt-midjourney manga warrior in dynamic fighting stance
/prompt-comfyui manga warrior in dynamic fighting stance
/prompt-gemini manga warrior in dynamic fighting stance
/prompt-firefly manga warrior in dynamic fighting stance
```

Each command returns a production-ready prompt optimized for that platform.

### Convert Between Platforms

```
/convert-prompt midjourney comfyui [your-midjourney-prompt]
/convert-prompt comfyui gemini [your-comfyui-prompt]
/convert-prompt gemini firefly [your-gemini-prompt]
```

### Explore Comic Art Styles

```
/style-library manga
/style-library western comics
/style-library european comics
```

Browse 50+ comic art styles with artist references and platform recommendations.

## Components

### 5 Expert Agents

Each agent specializes in one platform or cross-platform function:

#### 1. **Midjourney Expert** (`midjourney-expert.md`)
Specializes in Midjourney v7 and Niji 7 with deep knowledge of:
- SREF codes for style consistency
- Comic book art styles (50+)
- Parameters: `--ar`, `--s`, `--c`, `--q`, `--niji`, `--style`
- Advanced techniques: multi-prompting, permutations, character references
- When to use: Artistic iterations, speed, anime/manga specialist

#### 2. **ComfyUI Expert** (`comfyui-expert.md`)
Specializes in ComfyUI workflows with expertise in:
- SDXL, FLUX.1, Stable Diffusion models
- LoRAs, InstantID, ControlNet for character consistency
- Prompt weights and emphasis syntax
- Comic art LoRA recommendations
- When to use: Character consistency, local generation, production pipelines

#### 3. **Gemini Expert** (`gemini-expert.md`)
Specializes in Google Gemini Imagen 3 with focus on:
- Natural language prompting (no technical syntax)
- Text-in-image rendering (best-in-class)
- Photorealistic output quality
- Vertex AI integration
- When to use: Photorealism, text-heavy images, natural language workflows

#### 4. **Firefly Expert** (`firefly-expert.md`)
Specializes in Adobe Firefly with expertise in:
- Concise prompting (30-60 words optimal)
- Commercial-safe generation by default
- Adobe ecosystem integration (Photoshop, Express)
- Style filters for rapid stylization
- When to use: Speed, commercial projects, Adobe workflows

#### 5. **Prompt Converter** (`prompt-converter.md`)
Specializes in cross-platform prompt conversion:
- Intelligent concept extraction
- Platform-specific syntax transformation
- Feature mapping and capability analysis
- Quality preservation strategies
- When to use: Multi-platform testing, workflow migration, team collaboration

### 5 Commands

Each command generates production-ready prompts or performs conversions:

#### `/prompt-midjourney [style] [description]`
Generate Midjourney v7 or Niji 7 prompts for any comic art style.

**Returns**:
- `/imagine:` command ready to copy-paste
- Parameter recommendations (`--ar`, `--s`, `--niji`, etc.)
- Style analysis and artist references
- Quality notes and iteration suggestions

**Example**:
```
/prompt-midjourney golden age comic superhero flying over city
```

#### `/prompt-comfyui [style] [description] [options]`
Generate ComfyUI prompts with LoRA recommendations and sampler settings.

**Returns**:
- Positive and negative prompts with weights
- LoRA specifications with recommended weights
- Sampler settings (CFG, steps, method, etc.)
- Model recommendations (SDXL, FLUX, SD1.5)
- InstantID/ControlNet guidance if requested

**Example**:
```
/prompt-comfyui manga warrior in action pose consistency model:sdxl
```

#### `/prompt-gemini [style] [description] [options]`
Generate Gemini Imagen 3 prompts using natural language.

**Returns**:
- Natural language prompt optimized for Gemini
- Vertex AI parameter settings
- Text-in-image rendering guidance (if applicable)
- Aspect ratio recommendations
- Quality notes and iteration suggestions

**Example**:
```
/prompt-gemini western comic superhero in noir setting
```

#### `/prompt-firefly [style] [description] [options]`
Generate concise Firefly prompts optimized for speed and commercial use.

**Returns**:
- 30-60 word concise prompt
- Filter recommendations (Comic Book, Manga, Illustration, etc.)
- Content type selection
- Adobe integration guidance
- Batch generation options

**Example**:
```
/prompt-firefly manga teenage character in action pose batch:5
```

#### `/convert-prompt [from-platform] [to-platform] [prompt]`
Convert prompts between all 4 platforms intelligently.

**Supported conversions**:
- Midjourney ↔ ComfyUI (high fidelity)
- Midjourney ↔ Gemini (high fidelity)
- Midjourney ↔ Firefly (moderate)
- ComfyUI ↔ Gemini (high fidelity)
- ComfyUI ↔ Firefly (moderate)
- Gemini ↔ Firefly (moderate)

**Returns**:
- Concept extraction from source
- Platform mapping analysis
- Converted prompt ready to use
- Parameter recommendations
- Trade-off analysis if applicable

**Example**:
```
/convert-prompt midjourney comfyui [your-midjourney-prompt]
```

### 2 Skills

Reusable knowledge systems for common tasks:

#### **Prompt Conversion Skill** (`skills/prompt-conversion/SKILL.md`)
Convert prompts between platforms with preservation of creative intent.

**Progressive disclosure**:
- Level 1: Quick conversion
- Level 2: Detailed analysis
- Level 3: Expert consultation
- Level 4: Advanced strategies

**Use when**:
- Testing same concept across platforms
- Switching between platforms
- Migrating production workflows
- Team collaboration across platforms

#### **Style Library Skill** (`skills/style-library/SKILL.md`)
Browse and reference 50+ comic art styles with platform-specific guidance.

**Includes**:
- 50+ comic art styles organized by category
- Artist references for each style
- Visual characteristics and best uses
- Platform-specific implementation guidance
- Style combination strategies

**Use when**:
- Choosing an appropriate style
- Learning about comic art styles
- Planning character designs
- Building style library for project

## Plugin Structure

```
/Users/eddie.flores/source/agents/generative-ai/
├── .claude-plugin/
│   ├── plugin.json              # Plugin manifest
│   └── marketplace.json         # Marketplace metadata
├── agents/
│   ├── midjourney-expert.md     # Midjourney v7, Niji 7 specialist
│   ├── comfyui-expert.md        # ComfyUI, SDXL, FLUX specialist
│   ├── gemini-expert.md         # Gemini Imagen 3 specialist
│   ├── firefly-expert.md        # Adobe Firefly specialist
│   └── prompt-converter.md      # Cross-platform conversion expert
├── commands/
│   ├── prompt-midjourney.md     # /prompt-midjourney command
│   ├── prompt-comfyui.md        # /prompt-comfyui command
│   ├── prompt-gemini.md         # /prompt-gemini command
│   ├── prompt-firefly.md        # /prompt-firefly command
│   └── convert-prompt.md        # /convert-prompt command
├── skills/
│   ├── prompt-conversion/
│   │   └── SKILL.md             # Prompt conversion skill
│   └── style-library/
│       └── SKILL.md             # Comic art style library skill
└── README.md                    # This file
```

## Documentation Reference

This plugin references comprehensive documentation in the Em & E Comics repository:

### Fundamentals (How each platform works)
- Midjourney: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/midjourney/01-midjourney-fundamentals.md`
- ComfyUI: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/comfyui/01-comfyui-fundamentals.md`
- Gemini: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/gemini/01-gemini-imagen-fundamentals.md`
- Firefly: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/adobe-firefly/01-firefly-fundamentals.md`

### Style Guides (50+ comic art styles per platform)
- Midjourney Styles: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/midjourney/02-comic-art-styles.md`
- ComfyUI Styles: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/comfyui/02-comic-art-styles.md`

### Cross-Platform
- Conversion Guide: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/cross-platform/prompt-conversion-guide.md`

## Platform Comparison

| Feature | Midjourney | ComfyUI | Gemini | Firefly |
|---------|-----------|---------|--------|---------|
| **Learning Curve** | Easy | Steep | Easy | Easiest |
| **Prompt Style** | Natural language | Tag-based | Natural prose | Concise prose |
| **Speed** | Medium | Medium-Slow | Medium-Slow | Fast |
| **Quality** | Excellent artistic | Highest with tuning | Excellent realistic | Professional |
| **Character Consistency** | `--cref` reference | InstantID + LoRA | Conversation mode | Limited |
| **Cost** | Subscription | Free (local) | API cost | Subscription |
| **Best For** | Artistic stylization | Character consistency | Photorealism | Speed & commercial |
| **Text-in-Image** | Limited | Limited | Excellent | Good |
| **Local Execution** | No | Yes | No | No |

## Common Workflows

### Workflow 1: Quick Comic Concept
1. Use **Firefly** for rapid 5-concept exploration (`batch:5`)
2. Select best concept
3. Use **Photoshop** Generative Fill for refinement
4. Export for review

**Time**: ~5 minutes

### Workflow 2: Character-Consistent Panels
1. Use **ComfyUI** with InstantID for character reference
2. Generate multiple poses/expressions for same character
3. Assemble panels in Photoshop
4. Polish with Firefly Generative Fill

**Time**: ~30-60 minutes per character

### Workflow 3: Cross-Platform Comparison
1. Create concept in **Midjourney** for artistic interpretation
2. Convert to **ComfyUI** for character consistency
3. Convert to **Gemini** for photorealistic reference
4. Convert to **Firefly** for commercial check
5. Compare all 4 outputs

**Time**: ~15 minutes

### Workflow 4: Production Pipeline
1. **Midjourney**: Concept exploration (fast feedback)
2. **Firefly**: Approve concepts with batch variations (fast)
3. **ComfyUI**: Character consistency with InstantID (production)
4. **Photoshop**: Final compositing and effects
5. Export for publication

**Time**: Varies by scale

## Comic Art Styles Covered

### 50+ Styles Organized by Category

**Manga & Anime** (8 styles):
Shounen, Seinen, Shoujo, Josei, Kodomo, Mecha, Chibi, Gore

**Western Comics** (10+ styles):
Golden Age, Silver Age, Bronze Age, Modern, Marvel, DC, Image, Indie

**European Comics** (6 styles):
Ligne Claire, Moebius, Franco-Belgian, Fumetti, Heavy Metal, Editorial

**Alternative** (4 styles):
Underground Comix, Alternative, Zine, Webcomic

**Genre-Specific** (10+ styles):
Superhero, Noir, Horror, Sci-Fi, Fantasy, Western, War, Romance, Comedy, Spy

**Digital & Modern** (5+ styles):
Webtoon, Manhwa, Manhua, Digital Painting, Cel-Shaded

**Experimental** (7+ styles):
Minimalist, Watercolor, Mixed Media, Retro, Street Art, Collage, Abstract

## Getting Started

### Step 1: Choose Your Platform

Pick the platform that fits your needs:

- **Want speed and quality concepts?** → **Firefly**
- **Need artistic stylization?** → **Midjourney**
- **Need character consistency?** → **ComfyUI**
- **Need photorealism?** → **Gemini**

### Step 2: Choose Your Style

Browse 50+ comic art styles:

```
/style-library manga
/style-library western comics
/style-library experimental
```

### Step 3: Generate Your First Prompt

Pick the command for your platform:

```
/prompt-midjourney [style] [description]
/prompt-comfyui [style] [description]
/prompt-gemini [style] [description]
/prompt-firefly [style] [description]
```

### Step 4: Generate and Refine

Copy the returned prompt and generate in your chosen platform. Refine based on results.

### Step 5: Explore Cross-Platform

Once comfortable, try converting prompts between platforms:

```
/convert-prompt [from-platform] [to-platform] [prompt]
```

## Advanced Features

### Character Consistency
For ComfyUI: Use InstantID + character LoRA
For Midjourney: Use `--cref` reference images
For Gemini: Use conversation mode for variations
For Firefly: Generate once, combine in Photoshop

### Batch Generation
Firefly: `batch:5` for 5 variations
ComfyUI: Batch processing in workflows
Midjourney: `--repeat` flag for multiple
Gemini: Multiple requests in conversation

### Style Combinations
Blend styles strategically:
- Primary style (0.9 weight in ComfyUI)
- Secondary style (0.5-0.6 weight)
- 2-3 styles maximum recommended

### Production Optimization
- Concept → Firefly (fast)
- Refinement → ComfyUI (consistent)
- Final → Gemini (photorealism) or Midjourney (artistic)
- Polish → Photoshop + Firefly Generative Fill

## Agent Capabilities Matrix

| Agent | Platform | Expertise | Best For |
|-------|----------|-----------|----------|
| Midjourney Expert | Midjourney v7, Niji 7 | SREF codes, parameters, stylization | Artistic iterations, speed |
| ComfyUI Expert | ComfyUI, SDXL, FLUX | LoRAs, InstantID, ControlNet | Character consistency, control |
| Gemini Expert | Gemini Imagen 3 | Natural language, text-in-image | Photorealism, text rendering |
| Firefly Expert | Adobe Firefly | Concise prompting, filters | Speed, commercial projects |
| Prompt Converter | All platforms | Cross-platform conversion | Multi-platform workflows |

## Tips for Success

1. **Start with one platform** - Master one before multi-platform workflows
2. **Use descriptions specific to style** - Each style has unique vocabulary
3. **Reference artist names** - Specific artists guide style more than generic descriptors
4. **Test parameters** - Recommended settings are starting points
5. **Save successful prompts** - Build your own prompt library
6. **Batch generate for comparison** - Try multiple variations
7. **Use filters/LoRAs strategically** - Let these handle styling vs. text description
8. **Iterate based on output** - Refine prompts for your desired results

## Common Questions

### "Which platform is best?"
**All four excel at different things:**
- **Fastest**: Firefly (~30s)
- **Best artistic**: Midjourney
- **Most control**: ComfyUI
- **Best photorealistic**: Gemini
- **Character consistency**: ComfyUI with InstantID

### "Can I use the same prompt everywhere?"
**Use the /convert-prompt command:**
Intelligently converts syntax and optimizes for target platform while preserving intent.

### "How do I maintain character consistency?"
**ComfyUI + InstantID** is best option:
- Reference image for face
- Character LoRA for body
- Same setup across multiple generations

### "Should I use Firefly or Midjourney?"
**Firefly for**:
- Quick concepts
- Commercial projects (default safe)
- Adobe workflow integration
- Batch exploration

**Midjourney for**:
- Artistic stylization
- Anime/manga (Niji 7)
- Detailed style control
- SREF code library

### "How do I combine styles?"
**Use the prompt descriptions strategically:**
- Midjourney: "manga-influenced western comic style"
- ComfyUI: Two LoRAs at 0.7 and 0.5 weights
- Gemini: Descriptive narrative with both style elements
- Firefly: Note combined style in 30-60 words

## Support & References

### When to Use Each Agent
- **Need Midjourney help?** → Use midjourney-expert agent
- **ComfyUI workflow question?** → Use comfyui-expert agent
- **Gemini natural language?** → Use gemini-expert agent
- **Firefly commercial project?** → Use firefly-expert agent
- **Convert between platforms?** → Use prompt-converter agent

### When to Use Skills
- **Browse comic styles?** → Use style-library skill
- **Convert prompt to another platform?** → Use prompt-conversion skill

### Additional Resources
- See individual agent files for deep expertise profiles
- See individual command files for detailed usage examples
- See documentation links for comprehensive platform guides
- Reference style library for 50+ comic art styles

## Version & Updates

**Plugin Version**: 1.0.0
**Last Updated**: January 2025
**Platforms Supported**: Midjourney v7, Niji 7, ComfyUI (SDXL/FLUX), Gemini Imagen 3, Adobe Firefly
**Comic Art Styles**: 50+
**Commands**: 5
**Agents**: 5
**Skills**: 2

## Integration with Em & E Comics

This plugin is part of the Em & E Comics production framework and directly references:
- Prompt engineering documentation in `docs/prompts/generative-ai/`
- Character and environment systems in the comic production pipeline
- Multi-platform generation workflows for comic panel production

## License

This plugin is part of the Em & E Comics project.

---

**Generative AI Prompt Engineering Plugin**
Professional prompt generation and cross-platform conversion for comic book and illustration creators.

For detailed information, see individual agent and command files, or reference the comprehensive documentation in the Em & E Comics repository.
