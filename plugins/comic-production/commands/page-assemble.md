---
description: Assemble segments into print pages and export to PDF using Canvas rendering. Activates comic-assembler agent.
---

Assemble generated segments into print-ready comic pages (6.875" x 10.5" @ 300 DPI) and export to PDF.

## Usage

```bash
/comic-production:page-assemble [episode-slug] [options]
```

## Arguments

- `episode-slug`: Episode to assemble (uses current directory if not specified)
- `--layout`: Layout preset - "standard", "action", "conversation" (default: "standard")
- `--format`: Output format - "pdf", "png", "both" (default: "pdf")
- `--output`: Custom output path (default: `output/pages.pdf`)

## What It Does

1. Loads shotlist and panel segments
2. Groups shots into pages (based on page attribute)
3. Calculates panel layouts based on preset
4. Renders pages using Canvas
5. Adds speech bubbles and effects
6. Exports to PDF or PNG sequence

## Example

```bash
# Standard assembly
/comic-production:page-assemble episode_02

# Action layout with dynamic panels
/comic-production:page-assemble episode_02 --layout action

# Export as PNG sequence for print service
/comic-production:page-assemble --format png

# Both PDF and PNG
/comic-production:page-assemble --format both
```

## MCP Tools Used

```javascript
// Assemble print pages
await mcp__comic_strip_studio__assemble_page({
  episodeId: "episode_02",
  pageNumber: 1,
  layout: "standard",  // or "action", "conversation"
  format: "pdf",  // or "png", "both"
  outputPath: "output/episode_02/pages.pdf",
  pageSize: {
    width: 6.875,   // inches
    height: 10.5,   // inches
    dpi: 300
  }
})
```

## Layout Presets

**standard**:
- 6-8 panels per page
- Balanced composition
- Mix of wide and small panels
- Best for: General storytelling

**action**:
- 4-6 panels per page
- Dynamic panel sizes
- Emphasis on movement
- Best for: Action sequences, fight scenes

**conversation**:
- Wide establish shot
- Alternating speakers (reaction shots)
- Dialogue-focused
- Best for: Character interactions, dialogue-heavy scenes

## Output Specifications

**PDF**:
- Size: 6.875" x 10.5" (standard comic book)
- Resolution: 300 DPI
- Color: RGB
- Compression: Optimized for print

**PNG**:
- Resolution: 2550x3300 pixels (8.5" x 11" @ 300 DPI)
- Format: PNG-24 (lossless)
- Naming: `page_001.png`, `page_002.png`, etc.

## Print Guidelines

- **Bleed**: 0.125" (37.5px) beyond trim
- **Safe Zone**: 0.25" (75px) from edges
- **Text**: Keep important text in safe zone
- **Colors**: RGB for digital, convert to CMYK for print

## Next Steps

1. Review pages in PDF viewer
2. Check bleed and safe zones
3. Verify text readability
4. Send to print service or distribute digitally
