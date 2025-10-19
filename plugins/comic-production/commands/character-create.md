---
description: Create new character with card, reference images, and LoRA training setup. Activates character-designer agent.
---

Create a new character with complete character card, reference images, and optional LoRA training.

## Usage

```bash
/comic-production:character-create <character-slug> [options]
```

## Arguments

- `character-slug`: Character identifier (e.g., "em", "e", "p")
- `--name`: Character display name (optional)
- `--description`: Base prompt description
- `--age`: Age or age range
- `--role`: Character role (e.g., "daughter", "dad", "dog")

## What It Does

1. Creates character directory structure
2. Generates character card JSON
3. Creates reference image templates
4. Sets up LoRA training directory
5. Registers character with MCP server

## Example

```bash
/comic-production:character-create em \
  --name "Em" \
  --description "pre-teen girl, high ponytail, sporty hoodie" \
  --age "11-13" \
  --role "daughter"
```

## Created Structure

```
characters/em/
├── card.json
├── refs/
│   └── (place reference images here)
└── lora/
    └── (LoRA models will be saved here)
```

## Next Steps

1. Add reference images to `characters/em/refs/`
2. Optionally train LoRA model
3. Update character card with LoRA path and trigger word
4. Use character in episode shotlists
