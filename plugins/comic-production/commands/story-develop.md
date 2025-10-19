---
description: Transform beat sheet and script into production-ready shotlist. Activates comic-director and storyboard-artist agents.
---

Convert beat sheet and script into detailed shotlist with camera angles, timing, and segment specifications.

## Usage

```bash
/comic-production:story-develop [episode-slug] [options]
```

## Arguments

- `episode-slug`: Episode to develop (uses current directory if not specified)
- `--beat-sheet`: Path to beat sheet (default: `content/beat_sheet.md`)
- `--script`: Path to script (default: `content/script.md`)
- `--format`: Output format - "video", "print", or "both" (default: "both")

## What It Does

1. Loads beat sheet and creates structured story outline
2. Drafts script with character-appropriate dialogue
3. Converts script into shot-by-shot breakdown
4. Assigns camera angles and compositions
5. Creates segment specifications
6. Validates story structure

## Example

```bash
# Full story development workflow
/comic-production:story-develop episode_02
```

## MCP Tools Used

```javascript
// 1. Create beat sheet from premise
await mcp__comic_strip_studio__create_beat_sheet({
  episodeId: "episode_02",
  premise: "E teaches Em about debugging after her code mysteriously breaks",
  targetDuration: 300,  // 5 minutes
  genre: "comedy",
  characters: ["em", "e"]
})

// 2. Draft script from beat sheet
await mcp__comic_strip_studio__draft_script({
  episodeId: "episode_02",
  beatSheetPath: "episodes/episode_02/content/beat_sheet.md",
  characterVoices: {
    "em": "curious, enthusiastic, sometimes frustrated",
    "e": "patient, technical, encouraging"
  }
})

// 3. Build shotlist from script
await mcp__comic_strip_studio__build_shotlist({
  episodeId: "episode_02",
  scriptPath: "episodes/episode_02/content/script.md",
  targetFormat: "both",  // "vertical-video", "print", or "both"
  avgShotDuration: 3  // seconds per shot for video
})

// 4. Validate story structure
await mcp__comic_strip_studio__validate_story({
  episodeId: "episode_02"
})

// 5. Export for review
await mcp__comic_strip_studio__export_story({
  episodeId: "episode_02",
  format: "pdf",
  includeNotes: true
})
```

## Output

Creates in `episodes/{episode}/content/`:
- `beat_sheet.md` - 3-act structure with 10 beats
- `script.md` - Full dialogue and action descriptions
- `shotlist.json` - Shot-by-shot breakdown with camera specs

## Next Steps

1. Review generated content in `content/` directory
2. Make any manual adjustments to shotlist.json
3. Run `/comic-production:panels-generate` to create visuals
