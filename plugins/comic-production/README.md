# Comic Production Plugin

> End-to-end AI-generated comic episode production with story development, character consistency, ComfyUI generation, Remotion assembly, and MCP orchestration.

Production-ready plugin for creating comic episodes (vertical video + print) using AI image generation (ComfyUI + InstantID + LoRA), Remotion video assembly, and comprehensive story development workflows.

## Overview

The Comic Production plugin provides a complete pipeline for AI-generated comic creation, from initial story concept to final distribution. Built specifically for the [Em & E Comics](https://github.com/yourusername/ai-comic-strip) project, but adaptable to any comic production workflow.

### What It Does

- **Story Development**: Beat sheets, scripts, and visual storytelling principles
- **Character Design**: Character cards, reference management, LoRA training coordination
- **Visual Planning**: Transform scripts into production-ready shotlists with camera angles
- **Panel Generation**: ComfyUI workflows with InstantID + LoRA + ControlNet for consistency
- **Assembly**: Remotion (vertical video) + Canvas (print pages/PDF)
- **Orchestration**: MCP server integration for automated workflows
- **Voice Integration**: Character-matched AI voices via ElevenLabs
- **Asset Management**: Props, backgrounds, poses library organization

### Output Formats

- **Vertical Video** (1080x1920): TikTok, Instagram Reels, YouTube Shorts
- **Print Pages** (6.875" x 10.5" @ 300 DPI): PDF for print or digital distribution
- **Artifacts Website**: Static HTML for review and approval

## Quick Start

### Prerequisites

**Required:**
- Node.js 18+ and pnpm
- ComfyUI running locally (http://127.0.0.1:8188)
- Claude Desktop with plugin support

**Recommended:**
- Em & E Comics MCP Server (for orchestration)
- NVIDIA GPU or M1/M2/M3 Mac (for ComfyUI)
- Firebase project (for asset distribution)

### Installation

1. **Install the plugin** (if using Claude Desktop):
   ```bash
   # The plugin is already in your agents repo
   # Just ensure you have the latest version
   ```

2. **Set up MCP server** (optional but recommended):
   ```bash
   /comic-production:mcp-setup --install
   ```

3. **Install ComfyUI dependencies**:
   ```bash
   cd ComfyUI/custom_nodes

   # InstantID
   git clone https://github.com/cubiq/ComfyUI_InstantID.git

   # ControlNet preprocessors
   git clone https://github.com/Fannovel16/comfyui_controlnet_aux.git

   # IP-Adapter
   git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus.git
   ```

4. **Create your first episode**:
   ```bash
   /comic-production:episode-scaffold pilot --title "First Episode"
   ```

## Complete Workflows

### Workflow 1: Full Episode Production

**End-to-End Production** (5-minute episode, ~12 pages)

```bash
# 1. Initialize episode
export WORKING_EPISODE=pilot
/comic-production:episode-scaffold pilot \
  --title "The Git Commit-ment" \
  --duration 300 \
  --format both

# 2. Develop story (activates comic-director agent)
# Edit: episodes/pilot/content/beat_sheet.md
# Edit: episodes/pilot/content/script.md

# 3. Create shotlist (activates storyboard-artist agent)
/comic-production:story-develop

# 4. Generate panels (activates panel-generator agent)
/comic-production:panels-generate

# 5. Assemble video (activates comic-assembler agent)
/comic-production:video-assemble

# 6. Assemble print pages
/comic-production:page-assemble

# 7. Review
open episodes/pilot/artifacts-website/index.html
open episodes/pilot/output/episode.mp4
open episodes/pilot/output/pages.pdf
```

**Timeline**: ~2-4 hours total
- Story development: 30-60 min
- Shotlist creation: 15-30 min
- Panel generation: 1-2 hours (depends on GPU)
- Assembly: 10-20 min

### Workflow 2: Character Creation

**Create Consistent Character with LoRA**

```bash
# 1. Create character card
/comic-production:character-create em \
  --name "Em" \
  --description "pre-teen girl, high ponytail, sporty hoodie" \
  --age "11-13" \
  --role "daughter"

# 2. Generate reference images
# Use ComfyUI or other tools to create:
# - characters/em/refs/head01.png (primary reference)
# - characters/em/refs/head02.png (3/4 view)
# - characters/em/refs/head03.png (profile)

# 3. Train LoRA (optional but recommended)
# Use Kohya_ss or similar:
# - Collect 100-150 training images
# - Tag with "em_character" trigger word
# - Train with recommended settings
# - Save to characters/em/lora/em_v1.safetensors

# 4. Update character card
# Edit characters/em/card.json to add LoRA info

# 5. Test consistency
# Generate test panels to verify character looks consistent
```

**Timeline**: 4-8 hours
- Reference generation: 1-2 hours
- Training data collection: 2-3 hours
- LoRA training: 1-2 hours
- Testing: 30-60 min

### Workflow 3: Iterative Development

**Rapid Iteration on Specific Scenes**

```bash
export WORKING_EPISODE=pilot

# 1. Regenerate specific shots
/comic-production:panels-generate --shots S05,S06,S07

# 2. Preview changes
/comic-production:video-assemble --preview

# 3. Update shotlist if needed
# Edit: episodes/pilot/content/shotlist.json

# 4. Regenerate and reassemble
/comic-production:panels-generate --shots S05,S06,S07
/comic-production:video-assemble
```

**Timeline**: 30-60 min per iteration

### Workflow 4: Multi-Episode Series

**Efficient Series Production**

```bash
# Create multiple episodes
for ep in episode_01 episode_02 episode_03; do
  /comic-production:episode-scaffold $ep --format both
done

# Daily production routine
export WORKING_EPISODE=episode_02

# Generate 20 panels per day (manage GPU load)
/comic-production:panels-generate --batch-size 5 --limit 20

# Check progress
# Episodes automatically track completion status

# When complete, assemble
/comic-production:video-assemble
/comic-production:page-assemble
```

**Timeline**: 2-3 days per episode (with daily batching)

## Agents Reference

### comic-director (Sonnet)
**When activated**: Episode story development, beat sheet creation, dialogue writing

**Specializes in**:
- Three-act structure for comics
- 10-beat episode templates
- Character arcs and development
- Visual storytelling techniques
- Em & E character voices

**Use for**:
- Creating beat sheets
- Writing scripts
- Planning story arcs
- Developing character moments

**Example**:
```
You: "Help me develop a story about E teaching Em about git commits"
comic-director: [Creates 10-beat structure, writes script with character-appropriate dialogue]
```

### character-designer (Sonnet)
**When activated**: Character creation, visual consistency strategy, LoRA coordination

**Specializes in**:
- Character card JSON schemas
- InstantID reference requirements
- LoRA training data preparation
- Prompt anchoring strategies
- Expression and pose libraries

**Use for**:
- Designing new characters
- Setting up consistency stack
- Planning LoRA training
- Creating reference images

**Example**:
```
You: "Create a character card for a new character: tech-savvy mom"
character-designer: [Generates character card, reference specs, prompt anchors]
```

### storyboard-artist (Sonnet)
**When activated**: Converting beat sheets to shotlists, visual planning

**Specializes in**:
- Camera shot types and angles
- Panel composition rules
- Segment architecture
- Timing and pacing
- Page layout planning

**Use for**:
- Creating shotlists from scripts
- Planning camera angles
- Designing page layouts
- Optimizing visual flow

**Example**:
```
You: "Convert this beat sheet into a shotlist"
storyboard-artist: [Creates detailed shotlist.json with 40 shots, camera specs, segments]
```

### panel-generator (Haiku)
**When activated**: ComfyUI execution, panel generation, batch processing

**Specializes in**:
- ComfyUI workflow execution
- GPU memory optimization
- Batch processing strategies
- InstantID + LoRA + ControlNet integration
- Error handling and retries

**Use for**:
- Generating character panels
- Troubleshooting generation issues
- Optimizing ComfyUI workflows
- Managing GPU resources

**Example**:
```
You: "Generate panels for shots S01-S05"
panel-generator: [Executes ComfyUI workflows, saves segments, reports progress]
```

### comic-assembler (Haiku)
**When activated**: Remotion video assembly, Canvas page rendering, PDF export

**Specializes in**:
- Remotion composition patterns
- Canvas rendering pipelines
- Speech bubble placement
- Multi-format export
- Artifact website generation

**Use for**:
- Assembling videos
- Creating print pages
- Generating review websites
- Exporting final outputs

**Example**:
```
You: "Assemble the episode into vertical video"
comic-assembler: [Creates Remotion composition, renders MP4, optimizes for web]
```

### prompt-engineer-comics (Sonnet)
**When activated**: Prompt optimization, consistency troubleshooting, A/B testing

**Specializes in**:
- Comic-specific prompting
- Prompt anchoring techniques
- Multi-character scene prompting
- Style consistency
- Negative prompt strategies

**Use for**:
- Optimizing character prompts
- Troubleshooting consistency
- Creating prompt libraries
- Testing variations

**Example**:
```
You: "Why does Em's outfit keep changing between panels?"
prompt-engineer-comics: [Analyzes prompts, suggests exact anchor phrases, updates negative prompts]
```

### episode-manager (Haiku)
**When activated**: Episode lifecycle, file organization, workflow orchestration

**Specializes in**:
- WORKING_EPISODE management
- Production status tracking
- File organization
- MCP tool coordination
- Progress monitoring

**Use for**:
- Managing episode metadata
- Tracking production progress
- Organizing assets
- Automating workflows

**Example**:
```
You: "What's the status of pilot episode?"
episode-manager: [Reports: 15/40 panels complete, 37.5% done, estimated 2 hours remaining]
```

## Skills Reference

### comic-story-structure
**Progressive disclosure skill for story development**

**Covers**:
- Three-act structure (25% / 50% / 25%)
- 10-beat template
- Panel-to-panel transitions
- Pacing techniques
- Character arcs

**Activated when**: Planning episode structure, writing beat sheets

**Key concepts**:
- Hook → Establish → Inciting Incident
- Rising action → Midpoint → Crisis
- Climax → Resolution → Tag

### character-consistency-comfyui
**Technical guide for maintaining visual consistency**

**Covers**:
- InstantID setup and configuration
- LoRA training (Kohya_ss)
- ControlNet integration
- Prompt anchoring
- Multi-character scenes

**Activated when**: Setting up character generation, troubleshooting consistency

**Consistency Stack**:
1. InstantID (face/identity) - 0.8 weight
2. LoRA (character details) - 0.8 weight
3. ControlNet (pose) - 0.7 weight
4. Prompt anchors (descriptive consistency)

### shotlist-design
**Transform scripts into production specifications**

**Covers**:
- Shot types (EWS, WS, MS, CU, ECU)
- Camera angles (eye-level, high, low, dutch)
- Composition rules (rule of thirds, leading lines)
- Segment architecture
- Timing guidelines

**Activated when**: Creating shotlists, planning visuals

**Shot Ratio**: 1 beat = 2-4 shots

### comfyui-comic-workflows
**ComfyUI optimization and batch processing**

**Covers**:
- Custom nodes installation
- GPU optimization (Metal/NVIDIA)
- Workflow templates
- Memory management
- Batch processing patterns

**Activated when**: Setting up ComfyUI, optimizing generation

**Memory Optimization**:
- Load models per character batch
- Unload between character switches
- Generate at 512x768, upscale to 1024x1536

### remotion-comic-assembly
**Video composition with Remotion**

**Covers**:
- Remotion composition patterns
- Player performance optimization
- Speech bubble animations
- Rendering optimization
- Export settings

**Activated when**: Creating video episodes

**Critical Pattern**: Player controls as sibling, not child

### comic-page-layout
**Print page design and Canvas rendering**

**Covers**:
- Page specifications (6.875" x 10.5")
- Panel grid layouts
- Canvas rendering
- PDF export
- Print guidelines (bleed, safe zones)

**Activated when**: Creating print pages

**Standard Layout**: 6-8 panels per page, varied sizes

### mcp-comic-orchestration
**MCP server integration and automation**

**Covers**:
- MCP tool reference
- WORKING_EPISODE workflow
- Production pipeline automation
- Status tracking
- Batch processing

**Activated when**: Orchestrating production workflows

**28 MCP Tools** organized by category:
- Story (5): create_beat_sheet, draft_script, build_shotlist, validate_story, export_story
- Character (8): create_character_from_photo, list_characters, add_character_pose/expression/prop, add_prop_state/animation, generate_character_overview
- Environment (5): create_environment_from_photo, list_environments, add_environment_setting/prop, generate_environment_overview
- Image Generation (3): render_panel, list_providers, get_provider_info
- Production (3): render_segment, render_speech_bubble, render_comic_effect
- Assembly (2): compose_beats, assemble_page
- Orchestration (1): direct_story
- Style (1): get_style_presets

### character-card-design
**Character database and specifications**

**Covers**:
- Character card JSON schema
- Reference image requirements
- Color palette design
- Expression/pose libraries
- Consistency strategy

**Activated when**: Creating characters, documenting specs

**Card Sections**:
- Identity (slug, name, role)
- Visual (base_prompt, refs, LoRA)
- Meta (colors, traits, speech style)
- Technical (model, resolution, seeds)

### voice-character-matching
**AI voice design for characters**

**Covers**:
- Voice characteristics (pitch, pace, energy)
- ElevenLabs integration
- Voice cloning workflow
- Dialogue delivery
- Audio comic production

**Activated when**: Creating character voices, producing audio

**Voice Profile**:
- Em: Medium-high pitch, fast pace, energetic
- E: Medium-low pitch, measured pace, warm

### prop-asset-management
**Asset library organization**

**Covers**:
- Asset directory structure
- Prop catalog database
- Background library
- Pose organization
- Version control

**Activated when**: Managing reusable assets

**Asset Types**:
- Props (tech, furniture, everyday)
- Backgrounds (garage, living room, bedroom)
- Poses (character-specific, shared)
- Effects (motion lines, impact stars)

## Commands Reference

### /comic-production:episode-scaffold
**Create new episode with directory structure**

```bash
/comic-production:episode-scaffold <episode-slug> [options]

Options:
  --title <string>      Episode title
  --duration <number>   Target duration in seconds (default: 300)
  --format <string>     Output format: video|print|both (default: both)
```

**Creates**:
```
episodes/<episode-slug>/
├── content/
│   ├── beat_sheet.md (template)
│   ├── script.md (template)
│   └── shotlist.json (empty)
├── segments/
├── output/
└── metadata.json
```

**Next steps**: Edit beat_sheet.md and script.md

### /comic-production:character-create
**Create character from photo analysis using AI vision**

```bash
/comic-production:character-create <character-slug> [options]

Options:
  --photos <string>       Comma-separated photo paths
  --name <string>         Character display name
  --prompt <string>       Analysis prompt for AI vision
  --role <string>         Character role
```

**Uses MCP tool**: `create_character_from_photo` - Analyzes photos with AI vision to extract appearance details

**Creates**:
```
characters/<character-slug>/
├── references/
│   └── <character>.json (AI-generated from photos)
└── (photos stored for reference)
```

**Next steps**: Review generated appearance, add poses/expressions with `add_character_pose/expression`

### /comic-production:story-develop
**Transform beat sheet and script into production-ready shotlist**

```bash
/comic-production:story-develop [episode-slug] [options]

Options:
  --beat-sheet <path>   Path to beat sheet (default: content/beat_sheet.md)
  --script <path>       Path to script (default: content/script.md)
  --format <string>     Output format (default: from metadata)
```

**Uses MCP tools**:
- `create_beat_sheet` - Generate structured beat sheet from premise
- `draft_script` - Create script with character-appropriate dialogue
- `build_shotlist` - Build shot-by-shot breakdown with camera specs
- `validate_story` - Validate story structure and pacing
- `export_story` - Export for review (PDF/Markdown)

**Outputs**: beat_sheet.md, script.md, shotlist.json with camera angles, segments, timing

**Next steps**: Review shotlist, run panels-generate

### /comic-production:panels-generate
**Generate panels using multi-provider image generation (Gemini, Replicate FLUX, ComfyUI)**

```bash
/comic-production:panels-generate [episode-slug] [options]

Options:
  --shots <string>    Specific shot IDs (comma-separated)
  --provider <string> auto|gemini|consistent|flux|local (default: auto)
  --quality <string>  Style preset (default: em-e-comics)
```

**Uses MCP tools**:
- `render_panel` - Multi-provider panel generation with auto fallback
- `list_providers` - Check available providers and costs
- `get_provider_info` - Get provider details
- `get_style_presets` - 11 available style presets

**Provider costs**:
- **Gemini 2.5 Flash**: $0.002/image (4-6s) - Best for rapid iteration
- **Replicate Consistent Character**: $0.01/image (10-15s) - Best for character shots
- **Replicate FLUX**: $0.03/image (15-20s) - Best for hero shots
- **Local ComfyUI**: Free (GPU-dependent) - Full control

**Next steps**: Review segments, assemble video/pages

### /comic-production:video-assemble
**Assemble vertical video using Remotion beat composition**

```bash
/comic-production:video-assemble [episode-slug] [options]

Options:
  --quality <number>    Output quality 0-100 (default: 80)
  --fps <number>        Frames per second (default: 30)
  --output <path>       Custom output path
  --format <string>     mp4|webm (default: mp4)
```

**Uses MCP tools**:
- `compose_beats` - Compose rendered segments into video (Remotion)
- `render_speech_bubble` - Add speech bubbles with animations
- `render_comic_effect` - Add comic visual effects

**Output**: 1080x1920 MP4/WebM optimized for TikTok, Instagram Reels, YouTube Shorts

**Next steps**: Review video, distribute to platforms

### /comic-production:page-assemble
**Assemble print pages using Canvas rendering**

```bash
/comic-production:page-assemble [episode-slug] [options]

Options:
  --layout <string>     standard|action|conversation (default: standard)
  --format <string>     pdf|png|both (default: pdf)
  --output <path>       Custom output path
```

**Uses MCP tool**: `assemble_page` - Assemble segments into print pages (Canvas/PDF)

**Output**: 6.875" x 10.5" @ 300 DPI PDF/PNG with proper bleed and safe zones

**Next steps**: Review pages, send to print or distribute

### /comic-production:mcp-setup
**Configure MCP server with all 28 comic production tools**

```bash
/comic-production:mcp-setup [options]

Options:
  --install   Install MCP server dependencies
  --config    Configure MCP server settings
  --test      Test all 28 MCP tools
  --status    Check MCP server status
```

**Sets up**: Em & E Comics MCP server with 28 tools for complete workflow automation

**All 28 Tools**: Story development (5), Character tools (8), Environment tools (5), Image generation (3), Production tools (3), Assembly (2), Orchestration (1), Style (1)

## MCP Tools Complete Reference

All 28 actual tools from the mcp-em-e-comics server, organized by category.

### Story Development Tools (5)

**create_beat_sheet**
```javascript
await mcp__em_e_comics__create_beat_sheet({
  episodeId: string,
  premise: string,
  targetDuration: number,  // seconds
  genre: string,
  characters: string[]
})
```
Generates structured 3-act beat sheet from premise with 10 beats.

**draft_script**
```javascript
await mcp__em_e_comics__draft_script({
  episodeId: string,
  beatSheetPath: string,
  characterVoices: object  // { "em": "curious, enthusiastic", "e": "patient, technical" }
})
```
Creates script with character-appropriate dialogue from beat sheet.

**build_shotlist**
```javascript
await mcp__em_e_comics__build_shotlist({
  episodeId: string,
  scriptPath: string,
  targetFormat: "vertical-video" | "print" | "both",
  avgShotDuration: number  // seconds per shot for video
})
```
Builds shot-by-shot breakdown with camera angles and compositions.

**validate_story**
```javascript
await mcp__em_e_comics__validate_story({
  episodeId: string
})
```
Validates story structure, pacing, and character arcs.

**export_story**
```javascript
await mcp__em_e_comics__export_story({
  episodeId: string,
  format: "pdf" | "docx" | "markdown",
  includeNotes: boolean
})
```
Exports story content for review or distribution.

### Character Tools (8)

**create_character_from_photo**
```javascript
await mcp__em_e_comics__create_character_from_photo({
  characterName: string,
  photoPath: string[],  // Multiple angles recommended
  analysisPrompt: string,  // Focus areas for AI vision
  updateExisting: boolean  // false = replace, true = merge
})
```
Analyzes photos using AI vision to extract appearance details automatically. This is the primary way to create characters in the system.

**list_characters**
```javascript
const characters = await mcp__em_e_comics__list_characters()
```
Returns list of all created characters with their metadata.

**add_character_pose**
```javascript
await mcp__em_e_comics__add_character_pose({
  characterName: string,
  poseName: string,
  poseDescription: string,
  referenceImage: string  // optional
})
```
Adds pose variation to character (e.g., "confident", "thinking", "running").

**add_character_expression**
```javascript
await mcp__em_e_comics__add_character_expression({
  characterName: string,
  expressionName: string,
  expressionDescription: string,
  referenceImage: string  // optional
})
```
Adds facial expression (e.g., "happy", "frustrated", "surprised").

**add_character_prop**
```javascript
await mcp__em_e_comics__add_character_prop({
  characterName: string,
  propName: string,
  propDescription: string,
  defaultState: string,
  interactions: string[]
})
```
Adds prop associated with character (e.g., laptop, skateboard, coffee mug).

**add_prop_state**
```javascript
await mcp__em_e_comics__add_prop_state({
  characterName: string,
  propName: string,
  stateName: string,
  stateDescription: string
})
```
Adds state variation to prop (e.g., laptop "open", "closed", "broken").

**add_prop_animation**
```javascript
await mcp__em_e_comics__add_prop_animation({
  characterName: string,
  propName: string,
  animationName: string,
  frames: string[],
  duration: number
})
```
Adds animation sequence to prop for video format.

**generate_character_overview**
```javascript
await mcp__em_e_comics__generate_character_overview({
  characterName: string
})
```
Generates comprehensive character documentation (appearance, poses, expressions, props).

### Environment Tools (5)

**create_environment_from_photo**
```javascript
await mcp__em_e_comics__create_environment_from_photo({
  environmentName: string,
  photoPath: string[],
  analysisPrompt: string,
  updateExisting: boolean
})
```
Creates environment from photo analysis (AI vision extracts details).

**list_environments**
```javascript
const environments = await mcp__em_e_comics__list_environments()
```
Returns list of all created environments.

**add_environment_setting**
```javascript
await mcp__em_e_comics__add_environment_setting({
  environmentName: string,
  settingName: string,
  settingDescription: string
})
```
Adds environment variation (e.g., time of day, weather, lighting).

**add_environment_prop**
```javascript
await mcp__em_e_comics__add_environment_prop({
  environmentName: string,
  propName: string,
  propDescription: string,
  defaultState: string,
  interactions: string[]
})
```
Adds prop to environment (furniture, decorations, interactive objects).

**generate_environment_overview**
```javascript
await mcp__em_e_comics__generate_environment_overview({
  environmentName: string
})
```
Generates comprehensive environment documentation.

### Image Generation Tools (3)

**render_panel**
```javascript
await mcp__em_e_comics__render_panel({
  episodeId: string,
  shotId: string,
  // Structured approach (recommended):
  characters: string[],
  env: string,
  camera: string,
  style: string,  // Style preset name
  characterAppearances: object[],  // Optional overrides
  // OR raw prompt approach:
  prompt: string,
  negativePrompt: string,
  referenceImage: string,
  // Common:
  width: number,
  height: number,
  provider: "auto" | "gemini" | "consistent" | "flux" | "local",
  outputPath: string
})
```
Renders comic panel using multi-provider system with automatic fallback. Auto provider tries: Gemini → Consistent → FLUX → Local ComfyUI.

**list_providers**
```javascript
const providers = await mcp__em_e_comics__list_providers()
// Returns: [
//   { name: "gemini-2.5-flash", available: true, cost: "$0.002/image", speed: "4-6s" },
//   { name: "replicate-consistent-character", available: true, cost: "$0.01/image" },
//   { name: "replicate-flux", available: true, cost: "$0.03/image" },
//   { name: "comfyui-local", available: false }
// ]
```
Lists available image generation providers with costs and status.

**get_provider_info**
```javascript
await mcp__em_e_comics__get_provider_info({
  provider: "gemini" | "consistent" | "flux" | "local"
})
```
Gets detailed information about specific provider.

### Production Tools (3)

**render_segment**
```javascript
await mcp__em_e_comics__render_segment({
  episodeId: string,
  shotId: string,
  segmentType: "character-panel" | "speech-bubble" | "comic-effect" | "border",
  segmentData: object  // Type-specific data
})
```
Renders production segment (panels, bubbles, effects, borders).

**render_speech_bubble**
```javascript
await mcp__em_e_comics__render_speech_bubble({
  episodeId: string,
  shotId: string,
  character: string,
  text: string,
  bubbleType: "speech" | "thought" | "shout" | "whisper",
  position: { x: number, y: number },  // Normalized 0-1
  tailDirection: string  // "bottom-left", "top-right", etc.
})
```
Renders speech bubble with text and animations.

**render_comic_effect**
```javascript
await mcp__em_e_comics__render_comic_effect({
  episodeId: string,
  shotId: string,
  effectType: "impact" | "speed-lines" | "emphasis" | "action",
  position: { x: number, y: number },
  intensity: number  // 0-1
})
```
Renders comic visual effect (impact stars, motion lines, etc.).

### Assembly Tools (2)

**compose_beats**
```javascript
await mcp__em_e_comics__compose_beats({
  episodeId: string,
  outputPath: string,
  fps: number,
  quality: number,
  format: "mp4" | "webm",
  includeAudio: boolean
})
```
Composes rendered segments into video using Remotion. Creates 1080x1920 vertical video optimized for social media.

**assemble_page**
```javascript
await mcp__em_e_comics__assemble_page({
  episodeId: string,
  pageNumber: number,
  layout: "standard" | "action" | "conversation",
  format: "pdf" | "png" | "both",
  outputPath: string,
  pageSize: { width: number, height: number, dpi: number }
})
```
Assembles segments into print pages using Canvas. Default: 6.875" x 10.5" @ 300 DPI.

### Orchestration Tools (1)

**direct_story**
```javascript
await mcp__em_e_comics__direct_story({
  episodeId: string,
  premise: string,
  characters: string[],
  targetDuration: number,
  outputFormat: "vertical-video" | "print" | "both",
  autoGenerate: boolean,
  maxPanelsPerDay: number
})
```
High-level workflow automation. Orchestrates complete pipeline: beat sheet → script → shotlist → generation → assembly.

### Style Tools (1)

**get_style_presets**
```javascript
const styles = await mcp__em_e_comics__get_style_presets()
// Returns 11 presets:
// - em-e-comics (default, clean modern)
// - comic-book-classic (traditional American)
// - manga-style (Japanese influence)
// - graphic-novel (sophisticated illustration)
// - newspaper-strip (daily strip style)
// - webcomic-modern (digital webcomic)
// - action-dynamic (high-energy action)
// - slice-of-life-calm (gentle everyday)
// - horror-dark (atmospheric horror)
// - sci-fi-neon (cyberpunk/futuristic)
// - fantasy-painterly (painterly fantasy)
```
Gets available visual style presets for panel generation.

## Best Practices

### Story Development

1. **Start with Character**: What does each character want this episode?
2. **Visual First**: Think in images, not just dialogue
3. **Economy**: Every beat must move story or develop character
4. **Show, Don't Tell**: Use visuals and expressions over dialogue
5. **Pacing**: Vary panel size and count for rhythm

**Example Beat Sheet**:
```markdown
BEAT 1: HOOK - Em can't decide on weekend plans (P1)
BEAT 2: ESTABLISH - E notices pattern, gets idea (P2)
BEAT 3: INCITING - E decides to teach git through planning (P3)
BEAT 4-7: CONFRONTATION - Teaching attempts, complications
BEAT 8: CLIMAX - Breakthrough moment (P10-11)
BEAT 9: RESOLUTION - Understanding achieved (P11-12)
BEAT 10: TAG - P commits to chaos (comedy button) (P12)
```

### Character Consistency

1. **Use ALL Layers**: InstantID + LoRA + ControlNet + Prompts
2. **Exact Anchors**: Same character description every time
3. **Quality References**: High-res, clear, well-lit faces
4. **Train LoRA**: 100-150 images for best results
5. **Test Early**: Generate test panels before full episode

**Consistency Checklist**:
- [ ] InstantID reference loaded (0.8 weight)
- [ ] LoRA loaded with trigger word (0.8 weight)
- [ ] ControlNet pose reference (0.7 weight)
- [ ] Exact same prompt anchors
- [ ] Negative prompt includes unwanted variations

### Production Workflow

1. **Set WORKING_EPISODE**: `export WORKING_EPISODE=pilot`
2. **Batch Processing**: Generate 20 panels/day to manage GPU
3. **Review Frequently**: Check artifacts website after each batch
4. **Iterate**: Regenerate unsatisfactory panels immediately
5. **Document**: Keep notes on what works

**Daily Routine**:
```bash
export WORKING_EPISODE=episode_02

# Morning: Generate panels
/comic-production:panels-generate --batch-size 5 --limit 20

# Afternoon: Review and iterate
open episodes/episode_02/artifacts-website/index.html

# Evening: Regenerate if needed
/comic-production:panels-generate --shots S15,S16,S17
```

### GPU Optimization

1. **Group by Character**: Generate all shots with Em before switching to E
2. **Unload Models**: Free VRAM between character switches
3. **Lower Resolution First**: 512x768 then upscale to 1024x1536
4. **Batch Size**: Start with 5, adjust based on VRAM
5. **Monitor Memory**: Watch GPU usage, restart if needed

**Memory-Efficient Workflow**:
```python
# Generate Em panels (load Em models once)
for shot in em_shots:
    generate_panel(shot)  # Em LoRA + InstantID loaded

# Unload Em models
unload_models()

# Generate E panels (load E models once)
for shot in e_shots:
    generate_panel(shot)  # E LoRA + InstantID loaded
```

### Quality Control

1. **Face Consistency**: Compare faces across panels
2. **Outfit Matching**: Verify clothing matches character card
3. **Style Consistency**: Same art style, line work, colors
4. **Composition**: Camera angles support emotion
5. **Pacing**: Timing feels natural for video/pages

**QC Checklist**:
- [ ] Character faces match references
- [ ] Outfits consistent with character cards
- [ ] Colors match defined palettes
- [ ] No artifacts (extra limbs, distortions)
- [ ] Style matches across all panels
- [ ] Composition follows rules (rule of thirds, etc.)
- [ ] Pacing feels natural
- [ ] Speech bubbles positioned correctly

## Troubleshooting

### Issue: Character looks different in each panel

**Symptoms**: Face changes, different age, inconsistent features

**Solutions**:
1. Increase InstantID weight (0.8 → 0.9)
2. Use higher quality reference images
3. Add multiple reference images (head01, head02, head03)
4. Train LoRA with more varied face images
5. Add specific age to negative prompt

**Check**:
```typescript
// Verify InstantID is loaded
instantid: {
  reference: "characters/em/refs/head01.png",
  weight: 0.85,  // Increase if needed
  controlnet_strength: 0.6
}
```

### Issue: Wrong outfit or colors

**Symptoms**: Character wearing different clothes, wrong colors

**Solutions**:
1. Verify LoRA loaded with trigger word in prompt
2. Increase LoRA strength (0.8 → 1.0)
3. Use exact same outfit description (prompt anchors)
4. Add unwanted outfits to negative prompt
5. Retrain LoRA with more outfit examples

**Fix**:
```typescript
// Add to negative prompt
negative: "adult, elderly, different outfit, dress, skirt,
          long hair, short hair, low quality"

// Strengthen LoRA
lora: {
  strength_model: 0.9,  // Increase from 0.8
  trigger_word: "em_character"  // Must be in prompt
}
```

### Issue: ComfyUI out of memory

**Symptoms**: Generation fails, GPU memory error

**Solutions**:
1. Reduce batch size (5 → 3 or 1)
2. Lower resolution temporarily (1024 → 512)
3. Unload unused models
4. Restart ComfyUI
5. Use `--lowvram` flag

**Commands**:
```bash
# Reduce batch size
/comic-production:panels-generate --batch-size 3

# Use draft quality (lower resolution)
/comic-production:panels-generate --quality draft
```

### Issue: Panels generating too slowly

**Symptoms**: 5+ minutes per panel, very slow progress

**Solutions**:
1. Reduce steps (25 → 20)
2. Use faster sampler (euler_a instead of dpmpp_2m_sde)
3. Disable preview in ComfyUI
4. Check GPU utilization
5. Generate at lower resolution, upscale later

**Optimize**:
```python
sampler: {
  steps: 20,  # Reduce from 25
  sampler_name: "euler_a"  # Faster sampler
}
```

### Issue: Remotion render fails

**Symptoms**: Video assembly errors, rendering issues

**Solutions**:
1. Verify all segments exist in `segments/` directory
2. Check shotlist.json matches segment IDs
3. Ensure Remotion dependencies installed
4. Check Node.js version (18+ required)
5. Review error logs

**Debug**:
```bash
# Check segments
ls episodes/pilot/segments/*_character_panel.png

# Verify shotlist
cat episodes/pilot/content/shotlist.json | python3 -m json.tool

# Test Remotion
cd episodes/pilot && npm run build
```

### Issue: MCP server not responding

**Symptoms**: MCP tools unavailable, connection errors

**Solutions**:
1. Restart Claude Desktop
2. Verify MCP server path in config
3. Rebuild MCP server (`pnpm build`)
4. Check Claude Desktop logs
5. Test server connection

**Fix**:
```bash
# Rebuild MCP server
cd ~/source/ai-comic-strip/apps/mcp-em-e-comics
pnpm install
pnpm build

# Test
/comic-production:mcp-setup --test
```

## Examples

### Example 1: Simple 3-Page Comic

**Concept**: "E teaches Em about git commits using her weekend planning"

```bash
# 1. Create episode
export WORKING_EPISODE=git_commit
/comic-production:episode-scaffold git_commit \
  --title "The Commit-ment Issue" \
  --duration 180 \
  --format both

# 2. Write beat sheet (in episodes/git_commit/content/beat_sheet.md)
```
```markdown
BEAT 1: HOOK - Em can't decide: movie or game night?
BEAT 2: ESTABLISH - E notices her indecision pattern
BEAT 3: INCITING - E: "This is like git commits!"
BEAT 4-5: TEACHING - E explains commits = commitments
BEAT 6: MIDPOINT - Em realizes small decisions matter
BEAT 7: CRISIS - Too many choices, overwhelmed
BEAT 8: CLIMAX - Em makes first "commit" to game night
BEAT 9: RESOLUTION - Understanding achieved
BEAT 10: TAG - P "commits" to stealing the controller
```

```bash
# 3. Create shotlist
/comic-production:story-develop

# 4. Generate panels (12 shots for 3 pages)
/comic-production:panels-generate

# 5. Assemble print pages
/comic-production:page-assemble --layout conversation

# Output: 3-page comic at episodes/git_commit/output/pages.pdf
```

### Example 2: Vertical Video Series

**Concept**: 5-episode series about debugging

```bash
# Create all episodes
for i in {1..5}; do
  /comic-production:episode-scaffold debug_ep0$i \
    --title "Debug Adventures #$i" \
    --duration 300 \
    --format video
done

# Episode 1: Daily production
export WORKING_EPISODE=debug_ep01

# Edit beat sheet and script
# ... (write story)

# Generate shotlist
/comic-production:story-develop

# Generate panels in batches (20/day)
/comic-production:panels-generate --batch-size 5 --limit 20

# Next day: Continue
/comic-production:panels-generate --batch-size 5 --limit 20

# When complete: Assemble
/comic-production:video-assemble

# Output: 1080x1920 MP4 at episodes/debug_ep01/output/episode.mp4
```

### Example 3: Character Development

**Create recurring character: "Code Cat" (Em's coding mentor)**

```bash
# 1. Create character
/comic-production:character-create code_cat \
  --name "Code Cat" \
  --description "wise orange tabby cat, glasses, professor vibe" \
  --age "adult cat" \
  --role "mentor"

# 2. Generate reference images
# Use ComfyUI to create 3 references:
# - characters/code_cat/refs/head01.png (front, glasses)
# - characters/code_cat/refs/head02.png (3/4 view)
# - characters/code_cat/refs/head03.png (profile)

# 3. Collect training images (100-150)
# Generate varied images:
# - Different expressions (wise, amused, thinking)
# - Different poses (sitting, standing, paw raised)
# - Different contexts (library, coding, teaching)

# 4. Train LoRA
# Use Kohya_ss:
# - Trigger: "code_cat_character"
# - 100 images, 10 epochs
# - Learning rate: 3e-5
# - Save to: characters/code_cat/lora/code_cat_v1.safetensors

# 5. Update character card
# Edit characters/code_cat/card.json to add LoRA path

# 6. Use in episodes
# In shotlist: Add "code_cat" to characters array
# InstantID + LoRA will ensure consistency
```

## Integration with Other Plugins

### ai-voice-audio Plugin
**Character Voice Matching**

```bash
# Create voice for Em
# (Uses mcp__elevenlabs__text_to_voice)
# "Young energetic female, pre-teen, bright confident tone"

# Generate dialogue for all speech bubbles
# Save as audio segments

# Mix into video during assembly
# (Remotion can layer audio with video)
```

### video-production Plugin
**Post-Processing**

```bash
# After assembly, optimize video
# FFmpeg automation for web delivery
# Add watermark, optimize codec
# Generate multiple resolutions
```

### backend-development (firebase-storage-cdn)
**Distribution**

```typescript
// Upload episode to Firebase Storage
await uploadVideo(
  'episodes/pilot/output/episode.mp4',
  'videos/pilot/episode.mp4'
);

// Make public via CDN
await file.makePublic();

// Distribute URL
const url = `https://storage.googleapis.com/my-project/videos/pilot/episode.mp4`;
```

## Advanced Topics

### Custom Character Styles

**Manga Style**:
- Train LoRA on manga-style images
- Use lineart ControlNet heavily (0.7 strength)
- Adjust prompt: "manga style, screentone, bold lines"

**Realistic Style**:
- Use realisticVision checkpoint
- Lower ControlNet lineart (0.3 strength)
- Prompt: "photorealistic, detailed, high quality"

### Multi-Character Scenes

**Regional Prompting**:
```python
regions = {
  "left_half": {
    "character": "em",
    "instantid": "characters/em/refs/head01.png",
    "lora": "em_v1.safetensors",
    "prompt": "em_character, pre-teen girl, sporty hoodie"
  },
  "right_half": {
    "character": "e",
    "instantid": "characters/e/refs/head01.png",
    "lora": "e_v1.safetensors",
    "prompt": "e_character, 30s dad, casual hoodie"
  }
}
```

### Batch Episode Production

**Automation Script**:
```bash
#!/bin/bash
# scripts/batch-produce.sh

EPISODES=(pilot episode_02 episode_03)

for ep in "${EPISODES[@]}"; do
  export WORKING_EPISODE=$ep

  # Check if shotlist exists
  if [ -f "episodes/$ep/content/shotlist.json" ]; then
    # Generate panels (20/day limit)
    /comic-production:panels-generate --limit 20

    # Check if complete
    TOTAL=$(jq '.length' "episodes/$ep/content/shotlist.json")
    DONE=$(ls episodes/$ep/segments/*_character_panel.png 2>/dev/null | wc -l)

    if [ "$DONE" -eq "$TOTAL" ]; then
      # Assemble
      /comic-production:video-assemble
      /comic-production:page-assemble
    fi
  fi
done
```

## Contributing

See the main [agents repository](https://github.com/wshobson/agents) for contribution guidelines.

## License

MIT License - see LICENSE file

## Support

- **Documentation**: See individual skill files in `skills/` directory
- **Issues**: Report at https://github.com/wshobson/agents/issues
- **MCP Server**: https://github.com/yourusername/ai-comic-strip

---

**Version**: 1.2.3
**Author**: Seth Hobson
**Category**: Content Creation
**Keywords**: comic, storytelling, comfyui, remotion, instant-id, lora, mcp
