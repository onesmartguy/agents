---
description: Create new episode with directory structure, metadata, and initial files. Activates comic-director and episode-manager agents.
---

Create a new comic episode with complete directory structure and initial setup.

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
4. Sets WORKING_EPISODE environment variable
5. Registers episode with MCP server

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
