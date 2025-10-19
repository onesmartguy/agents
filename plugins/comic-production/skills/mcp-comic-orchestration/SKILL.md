---
name: mcp-comic-orchestration
description: MCP server tools for comic production orchestration, episode management, and workflow automation. Use when coordinating production workflows, managing episodes, or automating generation tasks.
---

# MCP Comic Orchestration

Comprehensive guide to using the Em & E Comics MCP server for production workflow orchestration.

## MCP Tool Reference

### Episode Management

```javascript
// Create episode
await mcp__em_e_comics__create_episode({
  title: "The Debugging Dilemma",
  logline: "E teaches Em about debugging",
  target_duration: 300,
  output_format: "both"  // vertical-video | print | both
})

// Update episode
await mcp__em_e_comics__update_episode({
  status: "generation_in_progress",
  characters: ["em", "e", "p"],
  segments_completed: 5
})

// Get episode status
const status = await mcp__em_e_comics__get_episode_status()

// List all episodes
const episodes = await mcp__em_e_comics__list_episodes()
```

### Character Management

```javascript
// Create character
await mcp__em_e_comics__create_character({
  slug: "em",
  base_prompt: "pre-teen girl, high ponytail, sporty hoodie",
  ref_images: ["characters/em/refs/head01.png"]
})

// Update with LoRA
await mcp__em_e_comics__update_character({
  slug: "em",
  lora_path: "characters/em/lora/em_v1.safetensors",
  trigger_word: "em_character"
})

// Get character
const character = await mcp__em_e_comics__get_character({ slug: "em" })
```

### Shotlist & Generation

```javascript
// Create shotlist from beat sheet
await mcp__em_e_comics__create_shotlist({
  beat_sheet_path: "episodes/pilot/content/beat_sheet.md",
  output_format: "both"
})

// Update shot
await mcp__em_e_comics__update_shot({
  shot_id: "S01",
  panel_updates: { /* changes */ }
})

// Generate single panel
await mcp__em_e_comics__generate_panel({
  shot_id: "S01",
  segment_id: "S01_character_panel",
  character_refs: ["em"],
  output_path: "episodes/pilot/segments/"
})

// Batch generate
await mcp__em_e_comics__batch_generate_shots({
  shot_ids: ["S01", "S02", "S03", "S04", "S05"]
})

// Get generation progress
const progress = await mcp__em_e_comics__get_generation_progress()
// { completed: 5, total: 20, percentage: 25 }
```

### Assembly

```javascript
// Assemble episode
await mcp__em_e_comics__assemble_episode({
  output_formats: ["vertical-video", "print-pdf"],
  generate_artifacts_website: true
})

// Render video
await mcp__em_e_comics__render_video({
  output_path: "episodes/pilot/output/episode.mp4",
  quality: 80
})

// Export pages
await mcp__em_e_comics__export_pages({
  format: "pdf",
  output_path: "episodes/pilot/output/pages.pdf"
})
```

## WORKING_EPISODE Environment Variable

```bash
# Set working episode
export WORKING_EPISODE=pilot

# All MCP tools default to this episode
# Reduces errors, maintains context
```

```javascript
// Access in Node.js
const workingEpisode = process.env.WORKING_EPISODE || 'pilot'

// MCP server reads automatically
await mcp__em_e_comics__generate_panel({
  shot_id: "S01"  // Uses WORKING_EPISODE automatically
})
```

## Production Workflow

### Full Episode Pipeline

```javascript
async function produceEpisode(episodeSlug) {
  process.env.WORKING_EPISODE = episodeSlug

  // 1. Create episode
  await mcp__em_e_comics__create_episode({
    title: "Episode Title",
    logline: "Description",
    target_duration: 300,
    output_format: "both"
  })

  // 2. Wait for script (manual step)
  await waitForFile(`episodes/${episodeSlug}/content/script.md`)

  // 3. Create shotlist
  await mcp__em_e_comics__create_shotlist({
    beat_sheet_path: `episodes/${episodeSlug}/content/beat_sheet.md`
  })

  // 4. Generate panels
  const shotlist = loadShotlist(episodeSlug)
  const shotIds = shotlist.map(s => s.shot_id)

  await mcp__em_e_comics__batch_generate_shots({ shot_ids: shotIds })

  // 5. Monitor progress
  let progress = await mcp__em_e_comics__get_generation_progress()
  while (progress.percentage < 100) {
    await sleep(5000)
    progress = await mcp__em_e_comics__get_generation_progress()
  }

  // 6. Assemble
  await mcp__em_e_comics__assemble_episode({
    output_formats: ["vertical-video", "print-pdf"],
    generate_artifacts_website: true
  })

  // 7. Mark complete
  await mcp__em_e_comics__update_episode({
    status: "ready_for_review"
  })
}
```

### Parallel Processing

```javascript
// Generate multiple shots in parallel batches
async function batchParallel(shotIds, batchSize = 5) {
  const batches = chunk(shotIds, batchSize)

  for (const batch of batches) {
    await Promise.all(
      batch.map(shotId =>
        mcp__em_e_comics__generate_panel({ shot_id: shotId })
      )
    )
  }
}
```

## Episode Status States

```javascript
const STATES = {
  "in_development": "Initial creation, content development",
  "script_complete": "Beat sheet and script finished",
  "shotlist_complete": "Shotlist ready for generation",
  "generation_in_progress": "Panels being generated",
  "generation_complete": "All panels generated",
  "assembly_in_progress": "Assembling outputs",
  "assembly_complete": "Video and PDF created",
  "ready_for_review": "Ready for approval",
  "revisions_needed": "Needs changes",
  "approved": "Approved for publication",
  "published": "Published and distributed",
  "archived": "Completed and archived",
  "error": "Production error occurred"
}
```

## Production Metrics

```javascript
const metrics = await mcp__em_e_comics__get_production_metrics()

// {
//   episodes_total: 10,
//   episodes_in_progress: 2,
//   episodes_completed: 8,
//   segments_generated_today: 45,
//   avg_generation_time: 120,  // seconds
//   storage_used: "15.2 GB"
// }
```

## Automation Scripts

### Daily Production

```bash
#!/bin/bash
export WORKING_EPISODE=${1:-pilot}

# Generate panels (max 20/day)
node scripts/batch-generate.js --episode $WORKING_EPISODE --limit 20

# If complete, assemble
TOTAL=$(jq '.length' "episodes/$WORKING_EPISODE/content/shotlist.json")
COMPLETED=$(ls episodes/$WORKING_EPISODE/segments/*_character_panel.png | wc -l)

if [ "$COMPLETED" -eq "$TOTAL" ]; then
  node scripts/assemble-episode.js --episode $WORKING_EPISODE
fi
```

## Resources

- MCP Server Docs: ai-comic-strip/apps/mcp-em-e-comics
- Episode Structure: CLAUDE.md in ai-comic-strip repo
- Workflow Examples: Production scripts
