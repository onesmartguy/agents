---
name: character-consistency-comfyui
description: InstantID + LoRA + ControlNet techniques for maintaining character consistency across panels in ComfyUI. Use when ensuring visual character consistency, troubleshooting generation issues, or optimizing workflows.
---

# Character Consistency in ComfyUI

Complete guide to maintaining consistent character appearance across all comic panels using InstantID, LoRA models, and ControlNet.

## The Consistency Stack

### Layered Approach

```
Layer 1: InstantID (Face/Identity) ← Most Critical
Layer 2: LoRA (Character Details)
Layer 3: ControlNet (Pose/Composition)
Layer 4: Prompt Anchors (Descriptive Consistency)
```

**Use ALL together** for maximum consistency.

## InstantID Setup

### What is InstantID?

AI technique for preserving facial identity across generations using reference images.

**Strengths**:
- Excellent face consistency
- Works with single reference image
- Fast and efficient
- Compatible with LoRA and ControlNet

**Weaknesses**:
- Face-focused (doesn't guarantee outfit consistency)
- Requires good reference images
- Can struggle with extreme angles

### Reference Image Requirements

**Primary Reference** (head01.png):
```
✓ High resolution (1024x1024 minimum)
✓ Clear, well-lit face
✓ Neutral expression
✓ Straight-on angle (front view)
✓ Face is 30-40% of image
✓ No obstructions (hair over face, glasses, etc.)
✓ Professional quality
✗ Avoid: Blurry, dark, extreme angles, covered face
```

**Secondary References** (head02-05.png):
```
- 3/4 view (side angle)
- Profile view
- Different expression (happy, serious)
- Different lighting
All should match primary reference character
```

### InstantID Node Configuration

```python
{
  "instantid": {
    "reference_image": "characters/em/refs/head01.png",
    "weight": 0.8,  # 0.6-0.9 range, higher = stronger identity
    "controlnet_strength": 0.6,  # How much to influence generation
    "start_percent": 0.0,  # Start at beginning
    "end_percent": 0.9   # Stop before final details
  }
}
```

**Weight Guidelines**:
- **0.6-0.7**: Subtle influence, more variation
- **0.7-0.8**: Balanced (recommended)
- **0.8-0.9**: Strong consistency, less variation
- **0.9-1.0**: Very strict (can look repetitive)

## LoRA Training for Characters

### Why LoRA?

**LoRA (Low-Rank Adaptation)** teaches model character-specific details:
- Outfit consistency
- Hair style
- Body proportions
- Color palette
- Style quirks

**InstantID** preserves face, **LoRA** preserves everything else.

### Training Data Preparation

**Dataset Size**:
- Minimum: 50 high-quality images
- Recommended: 100-150 images
- Optimal: 200+ images

**Quality > Quantity**: 50 well-tagged images beat 150 poor ones.

**Dataset Composition** (100 images example):
```
Expressions (30 images):
├─ Neutral: 10 images
├─ Happy/Excited: 10 images
├─ Sad/Concerned: 5 images
└─ Other emotions: 5 images

Poses (30 images):
├─ Standing: 10 images
├─ Sitting: 10 images
└─ Action poses: 10 images

Angles (20 images):
├─ Front view: 8 images
├─ 3/4 view: 8 images
└─ Profile: 4 images

Contexts (20 images):
├─ Indoor settings: 10 images
└─ Outdoor settings: 10 images
```

### Tagging Strategy

**Tag Template**:
```
[trigger_word], [character_description], [expression], [pose], [background], [style]
```

**Example for Em**:
```
em_character, pre-teen girl, high ponytail, sporty dark blue hoodie, white hi-top sneakers,
confident expression, hands on hips,
suburban garage background,
comic book style, clean lines, vibrant colors
```

**Tagging Rules**:
1. **Always start with trigger word** (e.g., "em_character")
2. **Use consistent character anchors** (same description across all images)
3. **Add specific details** (expression, pose, background)
4. **Include style tags** (comic book style, clean lines, etc.)
5. **Be precise but not verbose** (25-40 tags per image)

### Training Parameters (Kohya_ss)

```yaml
# Recommended settings for character LoRA
model: "sdxl-1.0"  # or your base model

network:
  dim: 32  # Rank (16-128, 32 is balanced)
  alpha: 16  # Usually half of dim

training:
  resolution: 1024  # Match your target resolution
  batch_size: 2
  epochs: 10-15
  learning_rate: 3e-5  # Conservative for characters
  text_encoder_lr: 1e-5

optimizer:
  type: "AdamW8bit"
  scheduler: "cosine_with_restarts"

settings:
  mixed_precision: "fp16"
  gradient_accumulation: 2
  save_every_n_epochs: 2
  keep_n_checkpoints: 5
  caption_extension: ".txt"
  shuffle_caption: true
  cache_latents: true
  cache_latents_to_disk: true
```

**Training Tips**:
- Start with 10 epochs, test output
- If undertrained (not enough detail): Increase epochs or learning rate
- If overtrained (artifacts, overfitting): Decrease epochs or learning rate
- Monitor loss graphs: Should decrease steadily
- Test at different checkpoint epochs (epoch 8, 10, 12)

### LoRA Integration in ComfyUI

```python
{
  "lora_loader": {
    "lora_name": "characters/em/lora/em_v1.safetensors",
    "strength_model": 0.8,  # 0.6-1.0
    "strength_clip": 0.8   # Usually same as model strength
  },
  "prompt": "em_character, pre-teen girl, high ponytail, sporty hoodie, ..."
}
```

**Trigger Word**: Must include in prompt (e.g., "em_character")

## ControlNet for Pose Consistency

### Types of ControlNet

**1. OpenPose**: Body pose and skeleton
```python
{
  "controlnet_openpose": {
    "image": "assets/poses/em_confident_stance.png",
    "strength": 0.7,  # 0.5-0.8 recommended
    "preprocessor": "OpenposePreprocessor"
  }
}
```
*Use for*: Matching specific poses, body positions

**2. Lineart**: Line art and edges
```python
{
  "controlnet_lineart": {
    "image": "reference_lineart.png",
    "strength": 0.5,  # 0.3-0.6 for subtle influence
    "preprocessor": "LineartPreprocessor"
  }
}
```
*Use for*: Style consistency, comic book line work

**3. Canny**: Edge detection
```python
{
  "controlnet_canny": {
    "image": "composition_reference.png",
    "strength": 0.4,  # Lower for composition guide
    "preprocessor": "CannyEdgePreprocessor"
  }
}
```
*Use for*: Composition, layout guidance

**4. Depth**: Depth map
```python
{
  "controlnet_depth": {
    "image": "depth_reference.png",
    "strength": 0.5,
    "preprocessor": "DepthPreprocessor"
  }
}
```
*Use for*: 3D composition, foreground/background

### Creating Pose References

**Method 1: Generate & Extract**
```python
# 1. Generate character in desired pose
# 2. Run through OpenPose preprocessor
# 3. Save skeleton as reference
# 4. Reuse across episodes
```

**Method 2: Manual Pose Libraries**
```
Download OpenPose datasets:
- https://github.com/CMU-Perceptual-Computing-Lab/openpose
- Mixamo characters
- 3D pose software (Blender + Rigify)
```

**Organize Pose Library**:
```
assets/poses/
├── em/
│   ├── confident_stance.png
│   ├── sitting_casual.png
│   ├── running.png
│   └── thinking_pose.png
├── e/
│   ├── typing_laptop.png
│   ├── standing_casual.png
│   └── explaining_gesture.png
└── shared/
    ├── conversation_facing.png
    └── walking_together.png
```

## Complete Workflow

### Single Character Panel

```python
workflow = {
  # 1. Load base model
  "checkpoint": "realisticVision_v5.safetensors",

  # 2. Load character LoRA
  "lora": {
    "name": "em_v1.safetensors",
    "strength": 0.8
  },

  # 3. InstantID for face
  "instantid": {
    "reference": "characters/em/refs/head01.png",
    "weight": 0.8
  },

  # 4. ControlNet OpenPose for pose
  "controlnet_pose": {
    "image": "assets/poses/em/confident_stance.png",
    "strength": 0.7
  },

  # 5. ControlNet Lineart for style
  "controlnet_lineart": {
    "strength": 0.4
  },

  # 6. Prompt with trigger word
  "prompt": """em_character, pre-teen girl, high ponytail,
    sporty dark blue hoodie, white hi-top sneakers,
    confident stance, hands on hips,
    suburban garage background, afternoon lighting,
    comic book style, clean lines, vibrant colors""",

  # 7. Negative prompt
  "negative": """adult, elderly, different outfit, low quality,
    blurry, bad anatomy"""
}
```

### Multi-Character Panel

**Challenge**: Maintaining consistency with 2+ characters.

**Solution 1: Regional Prompting**
```python
{
  "regional_prompting": {
    "regions": [
      {
        "mask": "left_half",
        "instantid": "characters/em/refs/head01.png",
        "lora": "em_v1.safetensors",
        "prompt": "em_character, pre-teen girl, sporty hoodie"
      },
      {
        "mask": "right_half",
        "instantid": "characters/e/refs/head01.png",
        "lora": "e_v1.safetensors",
        "prompt": "e_character, 30s dad, casual hoodie"
      }
    ]
  }
}
```

**Solution 2: Sequential Generation + Compositing**
```python
# 1. Generate Em with full consistency stack
em_panel = generate_with_consistency("em", transparency=True)

# 2. Generate E with full consistency stack
e_panel = generate_with_consistency("e", transparency=True)

# 3. Generate background separately
background = generate_background("suburban garage")

# 4. Composite layers
final_panel = composite([background, e_panel, em_panel])
```

## Troubleshooting

### Issue: Face Changes Between Panels

**Symptoms**: Character looks different in each panel

**Diagnosis**:
- InstantID weight too low
- Poor reference image quality
- Reference doesn't match target character

**Solutions**:
1. Increase InstantID weight (0.8 → 0.9)
2. Use higher quality reference images
3. Add multiple reference images
4. Train LoRA with more face variations

### Issue: Wrong Outfit

**Symptoms**: Character wearing different clothes than intended

**Diagnosis**:
- LoRA not loaded or weight too low
- Prompt anchor inconsistent
- Negative prompt missing

**Solutions**:
1. Verify LoRA loaded with trigger word in prompt
2. Increase LoRA strength (0.8 → 1.0)
3. Use exact same outfit description in all prompts
4. Add unwanted outfits to negative prompt
5. Retrain LoRA with more outfit examples

### Issue: Inconsistent Age

**Symptoms**: Character looks older/younger in different panels

**Diagnosis**:
- Prompt includes conflicting age descriptors
- Reference images show different ages
- LoRA trained on varied ages

**Solutions**:
1. Add specific age range to prompt ("11-13 years old")
2. Use age-consistent reference images
3. Add wrong ages to negative prompt ("adult, elderly, child, baby")
4. Retrain LoRA with age-appropriate dataset

### Issue: Style Varies

**Symptoms**: Art style changes between panels

**Diagnosis**:
- Different checkpoints used
- Lineart ControlNet not applied
- Inconsistent style tags

**Solutions**:
1. Use same checkpoint for all panels
2. Apply ControlNet lineart with consistent strength
3. Use exact same style anchors in all prompts
4. Add unwanted styles to negative prompt

## Quality Checklist

**Per Panel Generation**:
- [ ] InstantID loaded with correct reference
- [ ] LoRA loaded with trigger word in prompt
- [ ] ControlNet (pose/lineart) applied if needed
- [ ] Prompt uses exact character anchors
- [ ] Negative prompt includes unwanted variations
- [ ] Same checkpoint model as other panels
- [ ] Resolution matches target (1024x1536)

**Consistency Check** (Compare panels):
- [ ] Face recognizable as same character
- [ ] Outfit matches character card
- [ ] Hair style consistent
- [ ] Color palette matches
- [ ] Age appears consistent
- [ ] Style matches (line work, shading)

## Advanced Techniques

### Multi-Reference InstantID

```python
{
  "instantid": {
    "references": [
      {"image": "head01.png", "weight": 0.8},  # Primary
      {"image": "head02.png", "weight": 0.5},  # 3/4 view
      {"image": "head03.png", "weight": 0.3}   # Expression variety
    ]
  }
}
```

### LoRA Weight Scheduling

```python
# Vary LoRA strength by generation phase
{
  "lora_schedule": {
    "start_percent": 0.0,
    "end_percent": 0.8,
    "weight": 0.9  # Strong during composition
  },
  "lora_schedule_2": {
    "start_percent": 0.8,
    "end_percent": 1.0,
    "weight": 0.6  # Lighter during details
  }
}
```

### IP-Adapter (Alternative to InstantID)

```python
{
  "ip_adapter": {
    "image": "characters/em/refs/full_body_01.png",
    "weight": 0.7,
    "mode": "style"  # or "composition"
  }
}
```

## Resources

- InstantID GitHub: https://github.com/InstantID/InstantID
- Kohya_ss LoRA Training: https://github.com/kohya-ss/sd-scripts
- ControlNet Models: https://github.com/lllyasviel/ControlNet
- ComfyUI Custom Nodes: https://github.com/ltdrdata/ComfyUI-Manager

## Examples

### Em Full Consistency Stack

```json
{
  "checkpoint": "realisticVision_v5.safetensors",
  "lora": {
    "model": "characters/em/lora/em_v1.safetensors",
    "trigger": "em_character",
    "strength": 0.8
  },
  "instantid": {
    "reference": "characters/em/refs/head01.png",
    "weight": 0.85,
    "controlnet_strength": 0.6
  },
  "controlnet_pose": {
    "image": "assets/poses/em_confident.png",
    "strength": 0.7
  },
  "prompt": "em_character, pre-teen girl, 11-13 years old, high ponytail brown hair, sporty dark blue hoodie (#2D6BFF), white hi-top sneakers, confident stance hands on hips, suburban garage, comic book style, clean lines, vibrant colors, masterpiece",
  "negative": "adult woman, elderly, child, baby, different outfit, dress, long hair, short hair, low quality, blurry, bad anatomy"
}
```

**Result**: Highly consistent Em across all panels
