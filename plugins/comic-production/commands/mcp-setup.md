---
description: Set up and configure MCP server with all 28 comic production tools. Activates episode-manager agent.
---

Set up and configure the AI Comic Strip Studio MCP server (`mcp-comic-strip-studio`) with all 28 production tools.

## Usage

```bash
/comic-production:mcp-setup [options]
```

## Arguments

- `--install`: Install MCP server dependencies
- `--config`: Configure MCP server settings
- `--test`: Test MCP server connection and tools
- `--status`: Check MCP server status

## What It Does

**Install Mode** (`--install`):
1. Checks for Node.js and pnpm
2. Installs MCP server dependencies
3. Builds MCP server
4. Configures Claude Desktop integration

**Test Mode** (`--test`):
1. Tests MCP server connection
2. Verifies all 28 tools are available
3. Tests basic operations

## Example

```bash
# Install MCP server
/comic-production:mcp-setup --install

# Test all 28 tools
/comic-production:mcp-setup --test

# Check status
/comic-production:mcp-setup --status
```

## Available MCP Tools (28 Total)

### Story Development Tools (5)
- `create_beat_sheet` - Generate structured beat sheet from premise
- `draft_script` - Create script with dialogue from beat sheet
- `build_shotlist` - Build shot-by-shot breakdown from script
- `validate_story` - Validate story structure
- `export_story` - Export story content in various formats

### Character Tools (8)
- `create_character_from_photo` - Create character from photo analysis (AI vision)
- `list_characters` - List all created characters
- `add_character_pose` - Add pose variation
- `add_character_expression` - Add facial expression
- `add_character_prop` - Add prop associated with character
- `add_prop_state` - Add state variation to prop
- `add_prop_animation` - Add animation sequence to prop
- `generate_character_overview` - Generate character documentation

### Environment Tools (5)
- `create_environment_from_photo` - Create environment from photo analysis
- `list_environments` - List all created environments
- `add_environment_setting` - Add environment variation (time, weather)
- `add_environment_prop` - Add prop to environment
- `generate_environment_overview` - Generate environment documentation

### Image Generation Tools (3)
- `render_panel` - Render comic panel (multi-provider with auto fallback)
- `list_providers` - List available providers (Gemini, Replicate, FLUX, Local)
- `get_provider_info` - Get detailed provider information

### Production Tools (3)
- `render_segment` - Render comic segment (character-panel, speech-bubble, effect, border)
- `render_speech_bubble` - Render speech bubble with text
- `render_comic_effect` - Render comic visual effect

### Assembly Tools (2)
- `compose_beats` - Compose rendered segments into video (Remotion)
- `assemble_page` - Assemble segments into print pages (Canvas/PDF)

### Orchestration Tools (1)
- `direct_story` - High-level workflow automation (full pipeline)

### Style Tools (1)
- `get_style_presets` - Get available style presets (11 presets)

## Installation Steps

1. **Prerequisites Check**:
   - Node.js 18+ installed
   - pnpm installed
   - Claude Desktop installed

2. **Install Dependencies**:
   ```bash
   cd ~/source/ai-comic-strip/apps/mcp-comic-strip-studio
   pnpm install
   pnpm build
   ```

3. **Configure Claude Desktop**:
   Updates `~/Library/Application Support/Claude/claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "comic-strip-studio": {
         "command": "node",
         "args": [
           "/Users/eddie.flores/source/ai-comic-strip/apps/mcp-comic-strip-studio/dist/server.js"
         ]
       }
     }
   }
   ```

4. **Restart Claude Desktop**

## Testing

```bash
# Test story tools
await mcp__comic_strip_studio__create_beat_sheet({
  episodeId: "test",
  premise: "Test story",
  targetDuration: 60,
  genre: "comedy",
  characters: ["em", "e"]
})

# Test character tools
await mcp__comic_strip_studio__list_characters()

# Test image generation
await mcp__comic_strip_studio__list_providers()
```

## Troubleshooting

**MCP server not responding**:
1. Check Claude Desktop logs
2. Restart Claude Desktop
3. Verify MCP server path in config
4. Rebuild MCP server (`pnpm build`)

**Tools not available**:
1. Verify all 28 tools are listed
2. Check MCP server version
3. Restart Claude Desktop

**Provider errors**:
1. Check API keys (Gemini, Replicate)
2. Verify ComfyUI is running (for local provider)
3. Test with different provider

## Next Steps

1. Verify all 28 tools are available in Claude
2. Test photo-based character creation
3. Test multi-provider panel generation
4. Create first episode with `/comic-production:episode-scaffold`
