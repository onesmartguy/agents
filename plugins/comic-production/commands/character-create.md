---
description: Create character from photo analysis with AI vision, poses, expressions, and props. Activates character-designer agent.
---

Create a new character using photo analysis with AI vision for automatic appearance extraction.

## Usage

```bash
/comic-production:character-create <character-slug> [options]
```

## Arguments

- `character-slug`: Character identifier (e.g., "em", "e", "p")
- `--photos`: Comma-separated list of photo paths
- `--name`: Character display name (optional)
- `--prompt`: Analysis prompt for AI vision (optional)
- `--role`: Character role (e.g., "daughter", "dad", "dog")

## What It Does

1. Analyzes photos using AI vision
2. Extracts appearance details (clothing, hairstyle, accessories)
3. Creates character reference JSON
4. Sets up pose and expression library
5. Initializes props system

## Example

```bash
# Create from photos
/comic-production:character-create em \
  --photos "photos/em_front.jpg,photos/em_side.jpg,photos/em_3quarter.jpg" \
  --name "Em" \
  --prompt "Focus on athletic build, ponytail, sporty clothing" \
  --role "daughter"
```

## MCP Tools Used

```javascript
// 1. Create character from photo analysis
await mcp__comic_strip_studio__create_character_from_photo({
  characterName: "em",
  photoPath: [
    "photos/em_front.jpg",
    "photos/em_side.jpg",
    "photos/em_3quarter.jpg"
  ],
  analysisPrompt: "Focus on clothing, hairstyle, and accessories. Note athletic build and confident stance.",
  updateExisting: false  // false = replace, true = merge
})

// 2. Add pose variations
await mcp__comic_strip_studio__add_character_pose({
  characterName: "em",
  poseName: "confident",
  poseDescription: "Hands on hips, standing tall, slight smile"
})

// 3. Add expressions
await mcp__comic_strip_studio__add_character_expression({
  characterName: "em",
  expressionName: "frustrated",
  expressionDescription: "Furrowed brow, slight frown, eyes looking up"
})

// 4. Add props
await mcp__comic_strip_studio__add_character_prop({
  characterName: "em",
  propName: "laptop",
  propDescription: "Modern silver laptop with coding stickers",
  defaultState: "open",
  interactions: ["typing", "closing", "frustrated-stare"]
})

// 5. List all characters
const characters = await mcp__comic_strip_studio__list_characters()
```

## Firestore Path

```
characters/[character-slug]
```

## Next Steps

1. Review generated character appearance in `characters/em/references/em.json`
2. Add additional poses and expressions as needed
3. Use character in episode shotlists
4. Test panel generation with character
