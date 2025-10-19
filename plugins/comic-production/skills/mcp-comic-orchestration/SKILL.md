---
name: mcp-comic-orchestration
description: MCP server tools for comic production orchestration, story development, character/environment creation, image generation, and assembly automation. Use when coordinating production workflows, managing characters/environments, or automating generation tasks.
---

# MCP Comic Orchestration

Comprehensive guide to using the AI Comic Strip Studio MCP server (`mcp-comic-strip-studio`) for AI-powered comic production.

## Overview

The MCP server provides **28 specialized tools** across 8 categories for automated comic creation from story to final output. All tools use the naming convention: `mcp__comic_strip_studio__<tool_name>`

## Story Development Tools (5 tools)

### create_beat_sheet

Generate structured beat sheet from a story premise using 3-act structure.

```javascript
await mcp__comic_strip_studio__create_beat_sheet({
  episodeId: "pilot",
  premise: "E teaches Em about debugging after her code mysteriously breaks",
  targetDuration: 60,  // seconds
  genre: "comedy",
  characters: ["em", "e"]
})

// Returns beat sheet with:
// - Act 1 (25%): Setup / Hook / Inciting Incident
// - Act 2 (50%): Rising Action / Complications / Midpoint / Crisis
// - Act 3 (25%): Climax / Resolution / Closing Image
```

### draft_script

Create script with dialogue from beat sheet.

```javascript
await mcp__comic_strip_studio__draft_script({
  episodeId: "pilot",
  beatSheetPath: "episodes/pilot/content/beat_sheet.md",
  characterVoices: {
    "em": "curious, enthusiastic, sometimes frustrated",
    "e": "patient, technical, encouraging"
  }
})

// Generates script.md with:
// - Scene headers
// - Character dialogue
// - Action descriptions
// - Visual directions
```

### build_shotlist

Build shot-by-shot breakdown from script.

```javascript
await mcp__comic_strip_studio__build_shotlist({
  episodeId: "pilot",
  scriptPath: "episodes/pilot/content/script.md",
  targetFormat: "vertical-video",  // or "print" or "both"
  avgShotDuration: 3  // seconds per shot
})

// Generates shotlist.json with shots:
// - shot_id, duration, camera angle
// - characters, environment, action
// - dialogue/speech bubbles
```

### validate_story

Validate story structure for pacing, character arcs, and conflicts.

```javascript
await mcp__comic_strip_studio__validate_story({
  episodeId: "pilot"
})

// Checks:
// - Beat sheet completeness
// - Character consistency
// - Pacing issues
// - Missing story elements
```

### export_story

Export story content in various formats.

```javascript
await mcp__comic_strip_studio__export_story({
  episodeId: "pilot",
  format: "pdf",  // or "docx", "markdown"
  includeNotes: true
})
```

## Character Tools (8 tools)

### create_character_from_photo

Create character appearance from photo analysis using AI vision.

```javascript
await mcp__comic_strip_studio__create_character_from_photo({
  characterName: "em",
  photoPath: ["photos/em_front.jpg", "photos/em_side.jpg"],
  analysisPrompt: "Focus on clothing, hairstyle, and accessories",
  updateExisting: false  // false = replace, true = merge
})

// AI analyzes photos and creates:
// characters/references/em.json:
// {
//   "name": "em",
//   "appearance": {
//     "clothing": "dark blue sporty hoodie, white hi-top sneakers",
//     "accessories": "high ponytail with red scrunchie",
//     "notes": "Pre-teen girl, athletic build, friendly expression"
//   }
// }
```

### list_characters

List all created characters.

```javascript
const characters = await mcp__comic_strip_studio__list_characters()

// Returns array of character names and reference paths
```

### add_character_pose

Add pose variation to character library.

```javascript
await mcp__comic_strip_studio__add_character_pose({
  characterName: "em",
  poseName: "confident",
  poseDescription: "Hands on hips, standing tall, slight smile",
  referenceImage: "poses/em_confident.png"  // optional
})

// Saves to: characters/references/em.json
```

### add_character_expression

Add facial expression variation.

```javascript
await mcp__comic_strip_studio__add_character_expression({
  characterName: "em",
  expressionName: "frustrated",
  expressionDescription: "Furrowed brow, slight frown, eyes looking up",
  referenceImage: "expressions/em_frustrated.png"  // optional
})
```

### add_character_prop

Add prop (object) associated with character.

```javascript
await mcp__comic_strip_studio__add_character_prop({
  characterName: "em",
  propName: "laptop",
  propDescription: "Modern silver laptop with coding stickers",
  defaultState: "open",
  interactions: ["typing", "closing", "frustrated-stare"]
})
```

### add_prop_state

Add state variation to existing prop.

```javascript
await mcp__comic_strip_studio__add_prop_state({
  characterName: "em",
  propName: "laptop",
  stateName: "error-screen",
  stateDescription: "Red error dialog with stack trace visible"
})
```

### add_prop_animation

Add animation sequence to prop.

```javascript
await mcp__comic_strip_studio__add_prop_animation({
  characterName: "em",
  propName: "laptop",
  animationName: "boot-up",
  frames: ["black-screen", "loading", "desktop"],
  duration: 2  // seconds
})
```

### generate_character_overview

Generate comprehensive character documentation.

```javascript
await mcp__comic_strip_studio__generate_character_overview({
  characterName: "em"
})

// Creates markdown doc with:
// - Base appearance
// - All poses
// - All expressions
// - Props and states
// - Usage examples
```

## Environment Tools (5 tools)

### create_environment_from_photo

Create environment/location from photo analysis.

```javascript
await mcp__comic_strip_studio__create_environment_from_photo({
  environmentName: "ems-bedroom",
  photoPath: ["bedroom_wide.jpg", "bedroom_desk.jpg"],
  analysisPrompt: "Focus on desk setup, wall decorations, lighting",
  updateExisting: false
})

// Creates: environments/references/ems-bedroom.json
// {
//   "name": "ems-bedroom",
//   "description": "Small bedroom with coding desk, RGB lights, posters",
//   "lighting": "warm ambient with blue RGB accents",
//   "settings": ["day", "night", "night-rgb-on"]
// }
```

### list_environments

List all created environments.

```javascript
const environments = await mcp__comic_strip_studio__list_environments()
```

### add_environment_setting

Add environment variation (time of day, weather, etc.).

```javascript
await mcp__comic_strip_studio__add_environment_setting({
  environmentName: "ems-bedroom",
  settingName: "morning-sunlight",
  settingDescription: "Bright sunlight streaming through window, warm golden tones"
})
```

### add_environment_prop

Add prop to environment.

```javascript
await mcp__comic_strip_studio__add_environment_prop({
  environmentName: "ems-bedroom",
  propName: "desk-lamp",
  propDescription: "Modern LED desk lamp with adjustable arm",
  defaultState: "on",
  interactions: ["on", "off", "dimmed"]
})
```

### generate_environment_overview

Generate comprehensive environment documentation.

```javascript
await mcp__comic_strip_studio__generate_environment_overview({
  environmentName: "ems-bedroom"
})
```

## Image Generation Tools (3 tools)

### render_panel

Render comic panel using multi-provider system with automatic fallback.

**Provider Fallback Order:**
1. Gemini 2.5 Flash (fast, character-consistent, $0.002)
2. Replicate Consistent Character (character-consistent, $0.01)
3. Replicate FLUX (high quality, $0.03)
4. Local ComfyUI (full control, free, requires setup)

```javascript
// Option 1: Structured prompt building (recommended)
await mcp__comic_strip_studio__render_panel({
  episodeId: "pilot",
  shotId: "S01",
  characters: ["em", "e"],
  env: "ems-bedroom",
  camera: "medium-wide, rule-of-thirds, eye-level",
  style: "em-e-comics",  // optional override
  characterAppearances: [  // optional overrides for this panel
    {
      character: "em",
      clothing: "pajamas with code patterns",
      notes: "just woke up"
    }
  ],
  width: 768,
  height: 1365,  // 9:16 vertical video
  provider: "auto",  // or "gemini", "consistent", "flux", "local"
  outputPath: "output/pilot/panels/S01.png"  // optional
})

// Option 2: Raw prompt (bypasses prompt builder)
await mcp__comic_strip_studio__render_panel({
  episodeId: "pilot",
  shotId: "S02",
  prompt: "Pre-teen girl with high ponytail, wearing hoodie, frustrated expression, looking at laptop with error screen, comic book style, clean lines",
  negativePrompt: "blurry, realistic, photograph, multiple heads",
  width: 768,
  height: 1365,
  referenceImage: "characters/references/em_front.png",  // for consistency
  provider: "gemini"
})

// Returns:
// ✅ Panel S01 rendered successfully!
// 📁 Output: output/pilot/panels/S01.png
// 🎨 Provider: gemini-2.5-flash
// ⏱️  Duration: 4.2s
// 💰 Cost: $0.002
// 🖼️  Size: 768×1365
```

### list_providers

List available image generation providers and their status.

```javascript
const providers = await mcp__comic_strip_studio__list_providers()

// Returns:
// [
//   {
//     "name": "gemini-2.5-flash",
//     "available": true,
//     "cost": "$0.002/image",
//     "speed": "4-6s",
//     "characterConsistency": true
//   },
//   {
//     "name": "replicate-consistent-character",
//     "available": true,
//     "cost": "$0.01/image",
//     "speed": "10-15s",
//     "characterConsistency": true
//   },
//   ...
// ]
```

### get_provider_info

Get detailed information about a specific provider.

```javascript
await mcp__comic_strip_studio__get_provider_info({
  provider: "gemini"
})

// Returns capabilities, cost, speed, best use cases
```

## Production Tools (3 tools)

### render_segment

Render comic segment (character-panel, speech-bubble, comic-effect, border).

```javascript
await mcp__comic_strip_studio__render_segment({
  episodeId: "pilot",
  shotId: "S01",
  segmentType: "character-panel",  // or speech-bubble, comic-effect, border
  segmentData: { /* type-specific data */ }
})
```

### render_speech_bubble

Render speech bubble with text.

```javascript
await mcp__comic_strip_studio__render_speech_bubble({
  episodeId: "pilot",
  shotId: "S01",
  character: "em",
  text: "Why isn't this working?!",
  bubbleType: "speech",  // or "thought", "shout", "whisper"
  position: { x: 0.5, y: 0.2 },  // normalized 0-1
  tailDirection: "bottom-left"
})
```

### render_comic_effect

Render comic visual effect (speed lines, impact, etc.).

```javascript
await mcp__comic_strip_studio__render_comic_effect({
  episodeId: "pilot",
  shotId: "S03",
  effectType: "impact",  // or "speed-lines", "emphasis", "action"
  position: { x: 0.7, y: 0.5 },
  intensity: 0.8
})
```

## Assembly Tools (2 tools)

### compose_beats

Compose rendered segments into video beats (Remotion).

```javascript
await mcp__comic_strip_studio__compose_beats({
  episodeId: "pilot",
  outputPath: "output/pilot/episode.mp4",
  fps: 30,
  quality: 80,
  format: "mp4",  // or "webm"
  includeAudio: true  // if audio tracks exist
})

// Assembles all segments into final video
// Uses Remotion for programmatic video composition
```

### assemble_page

Assemble segments into print comic pages (Canvas).

```javascript
await mcp__comic_strip_studio__assemble_page({
  episodeId: "pilot",
  pageNumber: 1,
  layout: "standard",  // or "action", "conversation"
  format: "pdf",  // or "png", "both"
  outputPath: "output/pilot/pages.pdf",
  pageSize: {
    width: 6.875,   // inches
    height: 10.5,   // inches
    dpi: 300
  }
})

// Page layouts:
// - standard: 6-8 panels, balanced composition
// - action: 4-6 panels, dynamic sizes
// - conversation: wide establish, alternating speakers
```

## Orchestration Tools (1 tool)

### direct_story

High-level workflow orchestration - automates entire pipeline.

```javascript
await mcp__comic_strip_studio__direct_story({
  episodeId: "pilot",
  premise: "E teaches Em about debugging",
  characters: ["em", "e"],
  targetDuration: 60,
  outputFormat: "both",  // "vertical-video", "print", "both"
  autoGenerate: true,  // auto-generate panels
  maxPanelsPerDay: 20  // rate limiting
})

// Orchestrates:
// 1. create_beat_sheet
// 2. draft_script
// 3. build_shotlist
// 4. render_panel (for all shots)
// 5. compose_beats OR assemble_page
// 6. Final assembly and export
```

## Style Tools (1 tool)

### get_style_presets

Get available style presets for panel generation.

```javascript
const styles = await mcp__comic_strip_studio__get_style_presets()

// Returns 11 presets:
// - em-e-comics (default)
// - comic-book-classic
// - manga-style
// - graphic-novel
// - newspaper-strip
// - webcomic-modern
// - action-dynamic
// - slice-of-life-calm
// - horror-dark
// - sci-fi-neon
// - fantasy-painterly

// Use in render_panel:
await mcp__comic_strip_studio__render_panel({
  episodeId: "pilot",
  shotId: "S01",
  style: "manga-style",
  ...
})
```

## Complete Production Workflow

### Full Episode Pipeline

```javascript
async function produceEpisode() {
  // 1. Create characters from photos
  await mcp__comic_strip_studio__create_character_from_photo({
    characterName: "em",
    photoPath: ["photos/em_front.jpg", "photos/em_side.jpg"]
  })

  await mcp__comic_strip_studio__create_character_from_photo({
    characterName: "e",
    photoPath: ["photos/e_portrait.jpg"]
  })

  // 2. Create environment
  await mcp__comic_strip_studio__create_environment_from_photo({
    environmentName: "ems-bedroom",
    photoPath: ["bedroom.jpg"]
  })

  // 3. Story development
  const beatSheet = await mcp__comic_strip_studio__create_beat_sheet({
    episodeId: "pilot",
    premise: "E teaches Em about debugging",
    targetDuration: 60,
    genre: "comedy",
    characters: ["em", "e"]
  })

  // 4. Script drafting (review/edit manually)
  await mcp__comic_strip_studio__draft_script({
    episodeId: "pilot",
    beatSheetPath: "episodes/pilot/content/beat_sheet.md"
  })

  // 5. Shotlist creation
  const shotlist = await mcp__comic_strip_studio__build_shotlist({
    episodeId: "pilot",
    scriptPath: "episodes/pilot/content/script.md",
    targetFormat: "vertical-video"
  })

  // 6. Panel generation (batch)
  const shots = JSON.parse(shotlist).shots
  for (const shot of shots) {
    await mcp__comic_strip_studio__render_panel({
      episodeId: "pilot",
      shotId: shot.shot_id,
      characters: shot.characters,
      env: shot.environment,
      camera: shot.camera,
      provider: "auto"
    })

    // Rate limit: wait between panels
    await sleep(2000)
  }

  // 7. Assembly
  await mcp__comic_strip_studio__compose_beats({
    episodeId: "pilot",
    outputPath: "output/pilot/episode.mp4",
    fps: 30
  })

  console.log("✅ Episode complete!")
}
```

### Character-Focused Workflow

```javascript
// Create character with variations
async function setupCharacter(name, photos) {
  // 1. Base character from photos
  await mcp__comic_strip_studio__create_character_from_photo({
    characterName: name,
    photoPath: photos
  })

  // 2. Add poses
  await mcp__comic_strip_studio__add_character_pose({
    characterName: name,
    poseName: "confident",
    poseDescription: "Hands on hips, standing tall"
  })

  await mcp__comic_strip_studio__add_character_pose({
    characterName: name,
    poseName: "thinking",
    poseDescription: "Hand on chin, looking up"
  })

  // 3. Add expressions
  await mcp__comic_strip_studio__add_character_expression({
    characterName: name,
    expressionName: "happy",
    expressionDescription: "Wide smile, bright eyes"
  })

  await mcp__comic_strip_studio__add_character_expression({
    characterName: name,
    expressionName: "frustrated",
    expressionDescription: "Furrowed brow, slight frown"
  })

  // 4. Add props
  await mcp__comic_strip_studio__add_character_prop({
    characterName: name,
    propName: "laptop",
    propDescription: "Modern silver laptop with stickers",
    defaultState: "open"
  })

  // 5. Generate documentation
  await mcp__comic_strip_studio__generate_character_overview({
    characterName: name
  })
}

await setupCharacter("em", [
  "photos/em_front.jpg",
  "photos/em_side.jpg",
  "photos/em_back.jpg"
])
```

### Rapid Prototyping Workflow

```javascript
// Quick story testing without full production
async function rapidPrototype() {
  // 1. Beat sheet only
  await mcp__comic_strip_studio__create_beat_sheet({
    episodeId: "test-01",
    premise: "Em discovers a bug in production",
    targetDuration: 30,
    genre: "comedy"
  })

  // 2. Validate story
  const validation = await mcp__comic_strip_studio__validate_story({
    episodeId: "test-01"
  })

  if (validation.issues.length > 0) {
    console.log("Story issues:", validation.issues)
    return
  }

  // 3. Generate just 2-3 key panels
  await mcp__comic_strip_studio__render_panel({
    episodeId: "test-01",
    shotId: "S01-opener",
    prompt: "Girl at computer, shocked expression, error dialog on screen",
    provider: "gemini"  // Fast and cheap
  })

  console.log("✅ Prototype complete - review before full production")
}
```

## Best Practices

### Provider Selection Strategy

```javascript
// Low-cost rapid iteration
provider: "gemini"  // $0.002, 4-6s, good consistency

// Character-critical shots
provider: "consistent"  // $0.01, better face consistency

// Hero shots / high quality
provider: "flux"  // $0.03, best quality

// Full control / testing
provider: "local"  // Free, requires ComfyUI setup
```

### Character Consistency Tips

1. **Create from multiple photo angles** - front, side, 3/4 view
2. **Use reference images** in `render_panel` for critical shots
3. **Test provider** with character before full episode
4. **Document appearance** variations in character library
5. **Use same provider** for all shots in a sequence

### Rate Limiting

```javascript
// Respect API limits
const BATCH_SIZE = 5
const DELAY_MS = 2000

for (let i = 0; i < shots.length; i += BATCH_SIZE) {
  const batch = shots.slice(i, i + BATCH_SIZE)
  await Promise.all(batch.map(shot => renderShot(shot)))
  await sleep(DELAY_MS)
}
```

### Cost Management

```javascript
// Use cheaper providers for:
// - Wide shots (less detail needed)
// - Background panels
// - Rapid iteration/testing

// Use expensive providers for:
// - Close-ups (faces visible)
// - Hero shots
// - Final production renders
```

## Troubleshooting

### Character Consistency Issues

```javascript
// Problem: Characters look different between panels
// Solution 1: Use referenceImage
await mcp__comic_strip_studio__render_panel({
  ...
  referenceImage: "characters/references/em_front.png"
})

// Solution 2: Use consistent-character provider
provider: "consistent"

// Solution 3: Add more detail to character appearance
await mcp__comic_strip_studio__add_character_expression({
  characterName: "em",
  expressionName: "neutral",
  expressionDescription: "Relaxed face, slight smile, looking forward, dark brown eyes, freckles on nose"
})
```

### Generation Failures

```javascript
// Provider fallback should handle most issues
// But if all providers fail:
const providers = await mcp__comic_strip_studio__list_providers()
// Check which providers are available

// Try specific provider
await mcp__comic_strip_studio__render_panel({
  ...
  provider: "local"  // Fallback to local ComfyUI
})
```

### Performance Optimization

```javascript
// Generate in parallel batches
async function batchGenerate(shots, batchSize = 3) {
  const batches = chunk(shots, batchSize)

  for (const batch of batches) {
    await Promise.all(
      batch.map(shot =>
        mcp__comic_strip_studio__render_panel({
          episodeId: "pilot",
          shotId: shot.id,
          characters: shot.characters,
          env: shot.env,
          camera: shot.camera,
          provider: "gemini"  // Fast provider
        })
      )
    )
  }
}
```

## Resources

- **MCP Server Source**: `/Users/eddie.flores/source/ai-comic-strip/apps/mcp-comic-strip-studio`
- **Tool Definitions**: `apps/mcp-comic-strip-studio/src/tools/*/`
- **Character References**: `characters/references/*.json`
- **Environment References**: `environments/references/*.json`
- **Episode Content**: `episodes/{episode-id}/`
- **Generated Output**: `output/{episode-id}/`
