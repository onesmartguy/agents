---
description: Set up and configure MCP server for comic production. Activates episode-manager agent.
---

Set up and configure the Em & E Comics MCP server for production workflow orchestration.

## Usage

```bash
/comic-production:mcp-setup [options]
```

## Arguments

- `--install`: Install MCP server dependencies
- `--config`: Configure MCP server settings
- `--test`: Test MCP server connection
- `--status`: Check MCP server status

## What It Does

**Install Mode** (`--install`):
1. Checks for Node.js and pnpm
2. Installs MCP server dependencies
3. Builds MCP server
4. Configures Claude Desktop integration

**Config Mode** (`--config`):
1. Configures MCP server settings
2. Sets working directory
3. Configures ComfyUI connection
4. Sets up episode paths

**Test Mode** (`--test`):
1. Tests MCP server connection
2. Verifies all tools available
3. Tests episode creation
4. Tests character management

## Example

```bash
# Install MCP server
/comic-production:mcp-setup --install

# Configure settings
/comic-production:mcp-setup --config

# Test connection
/comic-production:mcp-setup --test

# Check status
/comic-production:mcp-setup --status
```

## Installation Steps

1. **Prerequisites Check**:
   - Node.js 18+ installed
   - pnpm installed
   - ComfyUI running (optional for testing)

2. **Install Dependencies**:
   ```bash
   cd ~/source/ai-comic-strip/apps/mcp-em-e-comics
   pnpm install
   pnpm build
   ```

3. **Configure Claude Desktop**:
   Updates `~/Library/Application Support/Claude/claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "em-e-comics": {
         "command": "node",
         "args": [
           "/Users/eddie.flores/source/ai-comic-strip/apps/mcp-em-e-comics/dist/index.js"
         ]
       }
     }
   }
   ```

4. **Restart Claude Desktop**

## Configuration

**MCP Server Settings** (`config.json`):
```json
{
  "working_directory": "/Users/eddie.flores/source/ai-comic-strip",
  "episodes_path": "episodes",
  "characters_path": "characters",
  "assets_path": "assets",
  "comfyui_url": "http://127.0.0.1:8188"
}
```

## Available MCP Tools

After setup, these tools are available:
- `mcp__em_e_comics__create_episode`
- `mcp__em_e_comics__update_episode`
- `mcp__em_e_comics__create_character`
- `mcp__em_e_comics__create_shotlist`
- `mcp__em_e_comics__generate_panel`
- `mcp__em_e_comics__batch_generate_shots`
- `mcp__em_e_comics__assemble_episode`
- `mcp__em_e_comics__render_video`
- `mcp__em_e_comics__export_pages`

## Testing

```bash
# Test episode creation
await mcp__em_e_comics__create_episode({
  title: "Test Episode",
  logline: "Testing MCP integration",
  target_duration: 60,
  output_format: "both"
})

# Test character management
await mcp__em_e_comics__get_character({
  slug: "em"
})
```

## Troubleshooting

**MCP server not responding**:
1. Check Claude Desktop logs
2. Restart Claude Desktop
3. Verify MCP server path in config
4. Rebuild MCP server (`pnpm build`)

**Tools not available**:
1. Check MCP server is running
2. Verify configuration
3. Restart Claude Desktop

**Connection errors**:
1. Check ComfyUI is running (if needed)
2. Verify working directory path
3. Check file permissions

## Next Steps

1. Verify MCP tools are available in Claude
2. Set WORKING_EPISODE environment variable
3. Create first episode with `/comic-production:episode-scaffold`
