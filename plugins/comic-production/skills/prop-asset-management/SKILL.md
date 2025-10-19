---
name: prop-asset-management
description: Organize, version, and reuse props, backgrounds, and visual assets across episodes. Use when managing reusable assets, organizing asset libraries, or optimizing asset workflows.
---

# Prop & Asset Management

Comprehensive asset organization system for efficient comic production and consistent visual elements across episodes.

## Asset Directory Structure

```
assets/
├── characters/
│   ├── em/
│   │   ├── card.json
│   │   ├── refs/
│   │   └── lora/
│   ├── e/
│   └── p/
├── props/
│   ├── tech/
│   │   ├── laptop_01.png
│   │   ├── phone_01.png
│   │   └── arduino_board.png
│   ├── furniture/
│   │   ├── workbench.png
│   │   ├── desk_chair.png
│   │   └── garage_shelves.png
│   └── everyday/
│       ├── coffee_mug.png
│       ├── tools_pegboard.png
│       └── baseball_bat.png
├── backgrounds/
│   ├── garage_day.png
│   ├── garage_night.png
│   ├── living_room.png
│   ├── em_bedroom.png
│   └── backyard.png
├── poses/
│   ├── em/
│   ├── e/
│   └── shared/
└── effects/
    ├── motion_lines.png
    ├── impact_stars.png
    └── sweat_drops.png
```

## Prop Database

### Prop Catalog JSON

```json
{
  "props": [
    {
      "id": "laptop_01",
      "name": "E's Laptop",
      "category": "tech",
      "description": "Silver laptop with stickers, used by E",
      "file_path": "assets/props/tech/laptop_01.png",
      "dimensions": "512x384",
      "transparent": true,
      "tags": ["tech", "work", "garage"],
      "used_in_episodes": ["pilot", "episode_02"],
      "generation_prompt": "silver laptop computer, tech stickers, open lid, screen visible, realistic, high detail",
      "consistency_ref": true
    },
    {
      "id": "coffee_mug_01",
      "name": "Coffee Mug",
      "category": "everyday",
      "description": "White ceramic coffee mug, often knocked over",
      "file_path": "assets/props/everyday/coffee_mug.png",
      "dimensions": "256x256",
      "transparent": true,
      "tags": ["everyday", "kitchen", "garage"],
      "used_in_episodes": ["pilot"],
      "generation_prompt": "white ceramic coffee mug, simple design, side view, realistic",
      "consistency_ref": true
    }
  ]
}
```

## Background Library

### Background Specifications

```json
{
  "backgrounds": [
    {
      "id": "garage_day",
      "name": "Garage Interior - Daytime",
      "file_path": "assets/backgrounds/garage_day.png",
      "resolution": "1024x1536",
      "lighting": "afternoon sunlight through window, warm overhead lights",
      "mood": "cozy, productive workspace",
      "elements": [
        "workbench with tools",
        "pegboard with organized tools",
        "car equipment on shelves",
        "window with afternoon light",
        "concrete floor"
      ],
      "generation_prompt": "suburban garage interior, workbench with organized tools on pegboard, afternoon sunlight streaming through window, warm lighting, car equipment visible, concrete floor, cozy workspace atmosphere, no people, comic book style",
      "variations": {
        "night": "assets/backgrounds/garage_night.png",
        "messy": "assets/backgrounds/garage_messy.png"
      }
    }
  ]
}
```

## Asset Generation Workflow

### Generating Reusable Props

```python
async def generate_prop(prop_spec):
    """Generate prop with transparency"""

    # Generate with transparent background
    workflow = {
        "prompt": f"{prop_spec['generation_prompt']}, transparent background, isolated object, no background",
        "negative": "background, scene, environment",
        "checkpoint": "realisticVision_v5",
        "steps": 25,
        "cfg": 7.5,
        "width": prop_spec['width'],
        "height": prop_spec['height']
    }

    # Generate
    image = await comfyui_generate(workflow)

    # Remove background
    image_no_bg = await remove_background(image)

    # Save
    save_png(image_no_bg, prop_spec['file_path'])

    # Update catalog
    update_prop_catalog(prop_spec)
```

### Background Generation

```python
async def generate_background(bg_spec):
    """Generate consistent background"""

    workflow = {
        "prompt": f"{bg_spec['generation_prompt']}, no people, empty room",
        "negative": "people, characters, humans, animals",
        "checkpoint": "realisticVision_v5",
        "width": 1024,
        "height": 1536,
        "lineart_controlnet": {
            "strength": 0.4,  # Maintain layout consistency
            "reference": bg_spec.get('layout_ref')
        }
    }

    background = await comfyui_generate(workflow)
    save_png(background, bg_spec['file_path'])

    update_background_catalog(bg_spec)
```

## Asset Reuse & Compositing

### Compositing Props into Panels

```javascript
async function compositePanelWithProps(shot) {
  // 1. Generate character panel
  const characterPanel = await generateCharacterPanel(shot)

  // 2. Load props for this shot
  const props = shot.props.map(p => loadProp(p.id))

  // 3. Composite
  const canvas = createCanvas(1024, 1536)
  const ctx = canvas.getContext('2d')

  // Background
  ctx.drawImage(characterPanel, 0, 0)

  // Props
  for (const prop of props) {
    ctx.drawImage(
      prop.image,
      prop.position.x,
      prop.position.y,
      prop.scale.width,
      prop.scale.height
    )
  }

  return canvas
}
```

## Asset Versioning

### Version Control

```json
{
  "asset_id": "laptop_01",
  "versions": [
    {
      "version": "1.0",
      "file": "laptop_01_v1.png",
      "created": "2024-03-01",
      "notes": "Initial generation"
    },
    {
      "version": "1.1",
      "file": "laptop_01_v1.1.png",
      "created": "2024-03-15",
      "notes": "Added more stickers, brighter screen"
    }
  ],
  "current_version": "1.1"
}
```

## Pose Library Organization

```
assets/poses/
├── em/
│   ├── confident_stance.png
│   ├── sitting_casual.png
│   ├── running.png
│   ├── excited_jump.png
│   └── thinking.png
├── e/
│   ├── typing_laptop.png
│   ├── standing_casual.png
│   ├── explaining_gesture.png
│   └── sitting_relaxed.png
└── shared/
    ├── conversation_facing.png
    ├── walking_together.png
    └── high_five.png
```

### Pose Metadata

```json
{
  "pose_id": "em_confident_stance",
  "character": "em",
  "file_path": "assets/poses/em/confident_stance.png",
  "description": "Hands on hips, athletic stance, confident posture",
  "preprocessor": "openpose",
  "used_count": 15,
  "episodes": ["pilot", "episode_02", "episode_03"]
}
```

## Asset Search & Discovery

```javascript
// Search assets
function searchAssets(query, filters = {}) {
  const catalog = loadAssetCatalog()

  return catalog.filter(asset => {
    // Text search
    const matchesQuery = asset.tags.some(tag => tag.includes(query)) ||
                        asset.name.toLowerCase().includes(query.toLowerCase()) ||
                        asset.description.toLowerCase().includes(query.toLowerCase())

    // Category filter
    const matchesCategory = !filters.category ||
                           asset.category === filters.category

    // Episode filter
    const matchesEpisode = !filters.episode ||
                          asset.used_in_episodes.includes(filters.episode)

    return matchesQuery && matchesCategory && matchesEpisode
  })
}

// Example
const techProps = searchAssets("tech", { category: "props" })
const garageAssets = searchAssets("garage")
```

## Asset Cleanup

```bash
#!/bin/bash
# Clean unused assets

# Find assets not referenced in any episode
for asset in assets/props/*/*.png; do
  asset_name=$(basename "$asset" .png)

  # Search for references
  refs=$(grep -r "$asset_name" episodes/ | wc -l)

  if [ "$refs" -eq 0 ]; then
    echo "Unused: $asset"
    # mv "$asset" "assets/_archive/"
  fi
done
```

## Best Practices

1. **Consistent Naming**: Use descriptive, consistent names
2. **Transparent PNGs**: Generate props with transparency
3. **Version Control**: Track asset versions
4. **Metadata**: Document generation prompts for consistency
5. **Reuse**: Check existing assets before generating new ones
6. **Organization**: Keep assets categorized and searchable
7. **Archive**: Move unused assets to archive, don't delete
8. **Documentation**: Update catalog when adding assets

## Resources

- Asset Management Best Practices
- PNG Transparency Techniques
- Background Removal Tools (rembg, remove.bg)
- Asset Organization Systems
