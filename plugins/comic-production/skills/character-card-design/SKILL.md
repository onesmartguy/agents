---
name: character-card-design
description: Character card JSON schemas, visual design specifications, and consistency strategy documentation. Use when creating new characters, documenting character details, or maintaining character databases.
---

# Character Card Design

Complete character card schema and design specifications for maintaining consistent character identity across comic production.

## Character Card Schema

```json
{
  "slug": "em",
  "name": "Em",
  "role": "daughter",

  "base_prompt": "pre-teen girl, 11-13 years old, high ponytail brown hair, expressive brown eyes, friendly smile, sporty dark blue hoodie (#2D6BFF), white hi-top sneakers, athletic build, confident posture",

  "negative_prompt": "adult woman, elderly, child, baby, different hairstyle, long hair, short hair, dress, skirt, formal wear, heels, makeup, jewelry",

  "ref_face_url": "characters/em/refs/head01.png",
  "ref_face_ids": [
    "characters/em/refs/head01.png",
    "characters/em/refs/head02.png",
    "characters/em/refs/head03.png"
  ],

  "lora": {
    "model_path": "characters/em/lora/em_v1.safetensors",
    "trigger_word": "em_character",
    "weight": 0.8,
    "training_images": 120
  },

  "meta": {
    "age_range": "11-13",
    "height": "average",
    "build": "athletic",

    "colorway": {
      "primary": "#2D6BFF",
      "secondary": "#7C4DFF",
      "accent": "#FFFFFF",
      "skin": "#F5D5C0",
      "hair": "#4A3428"
    },

    "outfit_anchors": [
      "sporty hoodie",
      "hi-top sneakers",
      "athletic wear"
    ],

    "personality_traits": [
      "smart",
      "quick-witted",
      "tech-savvy",
      "playful",
      "confident"
    ],

    "speech_style": "smart fast quips, modern slang, playful sass",

    "catchphrases": [
      "W dad... sometimes.",
      "Father... no.",
      "Okay but hear me out—"
    ]
  },

  "variations": {
    "default": {
      "outfit": "dark blue hoodie, jeans, white sneakers",
      "expression": "confident smile",
      "pose": "hands on hips"
    },
    "excited": {
      "expression": "wide smile, eyes bright",
      "pose": "jumping, arms up"
    },
    "thinking": {
      "expression": "focused, slight frown",
      "pose": "hand on chin, looking up"
    }
  },

  "technical": {
    "preferred_model": "sdxl-lightning",
    "checkpoint": "realisticVision_v5",
    "controlnet_presets": ["openpose", "lineart"],
    "resolution": "1024x1536",
    "seed_range": [1000, 5000]
  }
}
```

## Reference Image Requirements

**Primary Reference (head01.png)**:
- Resolution: 1024x1024 minimum
- Face: 30-40% of image
- Angle: Straight-on (front view)
- Expression: Neutral
- Lighting: Clear, well-lit
- Quality: Professional, sharp
- Obstructions: None (no hair over face, glasses, etc.)

**Secondary References (head02-05.png)**:
- 3/4 view
- Profile view
- Different expressions (happy, serious, surprised)
- Different lighting conditions

## Color Palette Design

```javascript
const characterPalettes = {
  em: {
    primary: "#2D6BFF",    // Blue hoodie
    secondary: "#7C4DFF",  // Purple accents
    accent: "#FFFFFF",     // White sneakers
    skin: "#F5D5C0",       // Warm skin tone
    hair: "#4A3428"        // Dark brown
  },
  e: {
    primary: "#4A4A4A",    // Gray hoodie
    secondary: "#2E5C8A",  // Blue jeans
    accent: "#8B6F47",     // Brown shoes
    skin: "#FFD5B5",       // Light skin tone
    hair: "#3D3226"        // Brown hair
  }
}
```

## Outfit Anchors

**Critical Elements** (never change):
- Primary clothing: "sporty dark blue hoodie"
- Distinctive accessories: "white hi-top sneakers"
- Hair style: "high ponytail"
- Color scheme: "blue and white palette"

**Flexible Elements**:
- Pose and position
- Expression
- Background
- Lighting
- Camera angle

## Expression Library

```javascript
const expressions = {
  neutral: {
    eyes: "relaxed, friendly",
    mouth: "slight smile",
    eyebrows: "natural position"
  },
  excited: {
    eyes: "wide, bright, sparkle",
    mouth: "big smile, showing teeth",
    eyebrows: "raised"
  },
  sass: {
    eyes: "half-lidded, knowing look",
    mouth: "smirk, one corner up",
    eyebrows: "one raised"
  },
  thinking: {
    eyes: "looking up, focused",
    mouth: "slight frown, lips pursed",
    eyebrows: "furrowed"
  },
  surprised: {
    eyes: "very wide, eyebrows up",
    mouth: "open in O shape",
    eyebrows: "high raised"
  }
}
```

## Pose Library

```
assets/poses/em/
├── confident_stance.png (hands on hips)
├── sitting_casual.png (cross-legged)
├── running.png (mid-stride)
├── jumping_excited.png (arms up)
├── thinking_pose.png (hand on chin)
└── pointing.png (index finger extended)
```

## Creating New Character

```javascript
async function createCharacter(characterData) {
  // 1. Create directory structure
  await createDirectory(`characters/${characterData.slug}/`)
  await createDirectory(`characters/${characterData.slug}/refs/`)
  await createDirectory(`characters/${characterData.slug}/lora/`)

  // 2. Save character card
  await saveJSON(
    `characters/${characterData.slug}/card.json`,
    characterData
  )

  // 3. Generate reference images
  const refs = await generateReferenceImages(characterData.base_prompt)
  await saveReferences(refs, `characters/${characterData.slug}/refs/`)

  // 4. Prepare LoRA training data
  const trainingData = await prepareTrainingData(characterData)

  // 5. Train LoRA (optional)
  // await trainLoRA(trainingData)

  // 6. Register with MCP
  await mcp__em_e_comics__create_character({
    slug: characterData.slug,
    base_prompt: characterData.base_prompt,
    ref_images: refs.map(r => r.path)
  })
}
```

## Consistency Strategy

1. **InstantID**: Face/identity preservation (0.8 weight)
2. **LoRA**: Character details, outfit, style (0.8 weight)
3. **Prompt Anchors**: Exact same descriptions
4. **ControlNet**: Pose consistency (0.7 weight)
5. **Negative Prompt**: Exclude unwanted variations

## Character Database

```javascript
// characters/index.json
{
  "characters": [
    {
      "slug": "em",
      "name": "Em",
      "card_path": "characters/em/card.json",
      "status": "active",
      "episodes": ["pilot", "episode_02"]
    },
    {
      "slug": "e",
      "name": "E",
      "card_path": "characters/e/card.json",
      "status": "active",
      "episodes": ["pilot", "episode_02"]
    }
  ]
}
```

## Resources

- Character Design Principles
- Color Theory for Comics
- InstantID Documentation
- LoRA Training Guide
