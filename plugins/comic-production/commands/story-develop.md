---
description: Transform beat sheet and script into production-ready shotlist. Activates comic-director and storyboard-artist agents.
---

Convert beat sheet and script into detailed shotlist with camera angles, timing, and segment specifications.

## Usage

```bash
/comic-production:story-develop [episode-slug] [options]
```

## Arguments

- `episode-slug`: Episode to develop (uses WORKING_EPISODE if not specified)
- `--beat-sheet`: Path to beat sheet (default: `content/beat_sheet.md`)
- `--script`: Path to script (default: `content/script.md`)
- `--format`: Output format - "video", "print", or "both" (default: from metadata)

## What It Does

1. Loads beat sheet and script
2. Analyzes story structure
3. Converts beats into individual shots
4. Assigns camera angles and compositions
5. Creates segment specifications
6. Generates shotlist.json
7. Updates episode metadata

## Example

```bash
# Use WORKING_EPISODE
export WORKING_EPISODE=pilot
/comic-production:story-develop

# Specify episode
/comic-production:story-develop episode_02

# Custom paths
/comic-production:story-develop episode_02 \
  --beat-sheet custom_beat_sheet.md \
  --script custom_script.md
```

## Output

Creates `episodes/{episode}/content/shotlist.json` with:
- Shot IDs and sequence
- Camera specifications
- Character assignments
- Segment breakdowns
- Timing information
- Panel layouts

## Next Steps

1. Review shotlist in artifacts website
2. Make any manual adjustments to shotlist.json
3. Run `/comic-production:panels-generate` to create visuals
