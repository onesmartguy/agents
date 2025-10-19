---
description: Generate comic panels using multi-provider image generation (Gemini, Replicate, FLUX, ComfyUI). Activates panel-generator and prompt-engineer-comics agents.
---

Generate all comic panel segments using multi-provider image generation system with automatic fallback.

## Usage

```bash
/comic-production:panels-generate [episode-slug] [options]
```

## Arguments

- `episode-slug`: Episode to generate (uses current directory if not specified)
- `--shots`: Specific shot IDs to generate (comma-separated)
- `--provider`: Image provider - "auto", "gemini", "consistent", "flux", "local" (default: "auto")
- `--quality`: Style preset (default: "em-e-comics")

## What It Does

1. Loads shotlist and character/environment references
2. Renders panels using multi-provider fallback system
3. Applies character consistency techniques
4. Generates segments with proper sizing (768x1365 for 9:16 video)
5. Saves to `episodes/{episode}/output/panels/`

## Example

```bash
# Generate all panels with auto provider fallback
/comic-production:panels-generate episode_02

# Generate specific shots with Gemini (fast, cheap)
/comic-production:panels-generate episode_02 --shots S01,S02,S03 --provider gemini

# High quality with FLUX
/comic-production:panels-generate --provider flux --quality graphic-novel
```

## MCP Tools Used

```javascript
// 1. Render panel with auto provider fallback
await mcp__comic_strip_studio__render_panel({
  episodeId: "episode_02",
  shotId: "S01",
  characters: ["em", "e"],
  env: "ems-bedroom",
  camera: "medium-wide, rule-of-thirds, eye-level",
  style: "em-e-comics",
  width: 768,
  height: 1365,  // 9:16 vertical video
  provider: "auto"  // Fallback: Gemini → Consistent → FLUX → Local
})

// 2. List available providers
const providers = await mcp__comic_strip_studio__list_providers()
// Returns: gemini-2.5-flash ($0.002), replicate-consistent-character ($0.01),
//          replicate-flux ($0.03), comfyui-local (free)

// 3. Get provider details
await mcp__comic_strip_studio__get_provider_info({
  provider: "gemini"
})

// 4. Get style presets
const styles = await mcp__comic_strip_studio__get_style_presets()
// Returns 11 presets: em-e-comics, comic-book-classic, manga-style,
// graphic-novel, newspaper-strip, webcomic-modern, action-dynamic,
// slice-of-life-calm, horror-dark, sci-fi-neon, fantasy-painterly
```

## Provider Selection

**Auto** (recommended):
- Tries providers in order: Gemini → Consistent → FLUX → Local
- Automatic fallback on failure
- Cost-optimized

**Gemini 2.5 Flash**:
- Cost: $0.002/image
- Speed: 4-6s
- Best for: Rapid iteration, testing, wide shots
- Character consistency: Good

**Replicate Consistent Character**:
- Cost: $0.01/image
- Speed: 10-15s
- Best for: Character-critical shots, close-ups
- Character consistency: Excellent

**Replicate FLUX**:
- Cost: $0.03/image
- Speed: 15-20s
- Best for: Hero shots, final renders
- Character consistency: Excellent

**Local ComfyUI**:
- Cost: Free
- Speed: Varies (GPU-dependent)
- Best for: Full control, testing, no API limits
- Requires: ComfyUI setup

## Style Presets

Available via `get_style_presets`:
- `em-e-comics` (default) - Clean modern comic style
- `comic-book-classic` - Traditional American comics
- `manga-style` - Japanese manga influence
- `graphic-novel` - Sophisticated illustration
- `webcomic-modern` - Digital webcomic style
- `action-dynamic` - High-energy action scenes
- `slice-of-life-calm` - Gentle everyday moments

## Progress Monitoring

```bash
# Panels are generated with progress feedback
# ✅ Panel S01 rendered successfully!
# 📁 Output: output/pilot/panels/S01.png
# 🎨 Provider: gemini-2.5-flash
# ⏱️  Duration: 4.2s
# 💰 Cost: $0.002
```

## Next Steps

1. Review generated panels in `output/panels/` directory
2. Regenerate any unsatisfactory panels with different provider
3. Run `/comic-production:video-assemble` or `/comic-production:page-assemble`
