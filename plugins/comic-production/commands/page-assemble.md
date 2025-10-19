---
description: Assemble segments into print pages and export to PDF. Activates comic-assembler agent.
---

Assemble generated segments into print-ready comic pages (6.875" x 10.5" @ 300 DPI) and export to PDF.

## Usage

```bash
/comic-production:page-assemble [episode-slug] [options]
```

## Arguments

- `episode-slug`: Episode to assemble (uses WORKING_EPISODE if not specified)
- `--layout`: Layout preset - "standard", "action", "conversation" (default: "standard")
- `--format`: Output format - "pdf", "png", "both" (default: "pdf")
- `--output`: Custom output path (default: `output/pages.pdf`)

## What It Does

1. Loads shotlist and segments
2. Groups shots into pages (based on page attribute)
3. Calculates panel layouts
4. Renders pages using Canvas
5. Adds speech bubbles and effects
6. Exports to PDF or PNG sequence
7. Saves to `episodes/{episode}/output/`

## Example

```bash
# Standard assembly
export WORKING_EPISODE=pilot
/comic-production:page-assemble

# Action layout
/comic-production:page-assemble episode_02 --layout action

# Export as PNG sequence
/comic-production:page-assemble --format png

# Both PDF and PNG
/comic-production:page-assemble --format both
```

## Layout Presets

**standard**:
- 6-8 panels per page
- Balanced composition
- Mix of wide and small panels

**action**:
- 4-6 panels per page
- Dynamic panel sizes
- Emphasis on movement

**conversation**:
- Wide establish shot
- Alternating speakers
- Reaction shots

## Output Specifications

**PDF**:
- Size: 6.875" x 10.5"
- Resolution: 300 DPI
- Color: RGB
- Compression: Optimized

**PNG**:
- Resolution: 2550x3300 pixels
- Format: PNG-24
- Naming: `page_001.png`, `page_002.png`, etc.

## Print Guidelines

- **Bleed**: 0.125" (37.5px) beyond trim
- **Safe Zone**: 0.25" (75px) from edges
- **Text**: Keep important text in safe zone
- **Colors**: Check for print compatibility

## Next Steps

1. Review pages in PDF viewer
2. Check bleed and safe zones
3. Send to print service or distribute digitally
