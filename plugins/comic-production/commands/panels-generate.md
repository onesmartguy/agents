---
description: Generate comic panels from shotlist using ComfyUI with character consistency. Activates panel-generator and prompt-engineer-comics agents.
---

Generate all comic panel segments from shotlist using ComfyUI workflows with InstantID, LoRA, and ControlNet.

## Usage

```bash
/comic-production:panels-generate [episode-slug] [options]
```

## Arguments

- `episode-slug`: Episode to generate (uses WORKING_EPISODE if not specified)
- `--shots`: Specific shot IDs to generate (comma-separated)
- `--batch-size`: Number of panels to generate in parallel (default: 5)
- `--quality`: Quality preset - "draft", "standard", "high" (default: "standard")

## What It Does

1. Loads shotlist and character cards
2. Groups shots by characters for efficiency
3. Loads character models (LoRA, InstantID references)
4. Generates character panels with consistency stack
5. Creates segment files (panels, effects)
6. Updates generation progress
7. Saves to `episodes/{episode}/segments/`

## Example

```bash
# Generate all panels
export WORKING_EPISODE=pilot
/comic-production:panels-generate

# Generate specific shots
/comic-production:panels-generate episode_02 --shots S01,S02,S03

# High quality generation
/comic-production:panels-generate --quality high

# Larger batch size (requires more VRAM)
/comic-production:panels-generate --batch-size 10
```

## Quality Presets

**draft** (fast):
- Steps: 15
- Resolution: 512x768 (upscaled to 1024x1536)
- Use for: Quick previews, testing

**standard** (balanced):
- Steps: 25
- Resolution: 1024x1536
- Use for: Production

**high** (slow):
- Steps: 35
- Resolution: 1024x1536
- Additional refinement passes
- Use for: Final renders, key panels

## Progress Monitoring

```bash
# Check progress
/comic-production:panels-generate --status

# Output:
# Completed: 15/40 panels (37.5%)
# Current: Generating S16_character_panel
# Estimated time remaining: 45 minutes
```

## Next Steps

1. Review generated panels in `segments/` directory
2. Regenerate any unsatisfactory panels
3. Run `/comic-production:video-assemble` or `/comic-production:page-assemble`
