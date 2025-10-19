---
description: Create new episode with directory structure using photo-based character/environment creation. Activates comic-director and episode-manager agents.
---

Create a new comic episode with complete directory structure and photo-based asset initialization.

## Usage

```bash
/comic-production:episode-scaffold <episode-slug> [options]
```

## Arguments

- `episode-slug`: Episode identifier (e.g., "pilot", "episode_02")
- `--title`: Episode title (optional)
- `--duration`: Target duration in seconds (default: 300)
- `--format`: Output format - "video", "print", or "both" (default: "both")

## What It Does

1. Creates episode directory structure
2. Initializes metadata.json
3. Creates placeholder beat sheet and script templates
4. Sets up character and environment references (photo-based)
5. Creates initial shotlist template

## Example

```bash
# Basic usage
/comic-production:episode-scaffold episode_02

# With options
/comic-production:episode-scaffold episode_02 \
  --title "The Debugging Dilemma" \
  --duration 300 \
  --format both
```

## MCP Tools Used

```javascript
// 1. Create characters from photos
await mcp__em_e_comics__create_character_from_photo({
  characterName: "em",
  photoPath: ["photos/em_front.jpg", "photos/em_side.jpg"],
  analysisPrompt: "Focus on clothing, hairstyle, accessories"
})

// 2. Create environment from photos
await mcp__em_e_comics__create_environment_from_photo({
  environmentName: "ems-bedroom",
  photoPath: ["bedroom_wide.jpg", "bedroom_desk.jpg"],
  analysisPrompt: "Focus on desk setup, wall decorations, lighting"
})

// 3. Create beat sheet
await mcp__em_e_comics__create_beat_sheet({
  episodeId: "episode_02",
  premise: "Story premise here",
  targetDuration: 300,
  genre: "comedy",
  characters: ["em", "e"]
})
```

## Created Structure

```
episodes/episode_02/
├── content/
│   ├── beat_sheet.md (template)
│   ├── script.md (template)
│   └── shotlist.json (empty)
├── segments/
├── output/
└── metadata.json
```

## Next Steps

After scaffolding:
1. Edit `content/beat_sheet.md` to develop story
2. Edit `content/script.md` to write dialogue
3. Run `/comic-production:story-develop` to create shotlist
4. Run `/comic-production:panels-generate` to generate visuals
