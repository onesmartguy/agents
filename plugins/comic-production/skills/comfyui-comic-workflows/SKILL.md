---
name: comfyui-comic-workflows
description: Optimized ComfyUI workflows for comic panel generation, custom nodes, GPU optimization, and batch processing. Use when setting up ComfyUI workflows, optimizing generation performance, or troubleshooting issues.
---

# ComfyUI Comic Workflows

Production-optimized ComfyUI workflows for consistent, high-quality comic panel generation.

## Essential Custom Nodes

```bash
# Install via ComfyUI Manager
cd ComfyUI/custom_nodes

# 1. InstantID
git clone https://github.com/cubiq/ComfyUI_InstantID.git

# 2. ControlNet Preprocessors
git clone https://github.com/Fannovel16/comfyui_controlnet_aux.git

# 3. IP-Adapter
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

# 4. Essentials
git clone https://github.com/cubiq/ComfyUI_essentials.git
```

## Standard Comic Panel Workflow

```python
workflow = {
  # 1. Base Model
  "checkpoint_loader": {
    "ckpt_name": "realisticVision_v5.safetensors"
  },

  # 2. LoRA
  "lora_loader": {
    "lora_name": "em_v1.safetensors",
    "strength_model": 0.8,
    "strength_clip": 0.8
  },

  # 3. InstantID
  "instantid": {
    "reference_image": "characters/em/refs/head01.png",
    "weight": 0.8,
    "controlnet_strength": 0.6
  },

  # 4. ControlNet OpenPose
  "controlnet_pose": {
    "image": "poses/em_confident.png",
    "strength": 0.7,
    "preprocessor": "OpenposePreprocessor"
  },

  # 5. Prompts
  "prompt_positive": """em_character, pre-teen girl, high ponytail,
    sporty dark blue hoodie, white sneakers,
    confident stance, suburban garage,
    comic book style, clean lines, vibrant colors,
    masterpiece, best quality""",

  "prompt_negative": """adult, elderly, different outfit,
    low quality, blurry, bad anatomy, deformed,
    watermark, signature, text""",

  # 6. Sampler
  "sampler": {
    "steps": 25,
    "cfg": 7.5,
    "sampler_name": "dpmpp_2m_sde",
    "scheduler": "karras",
    "seed": 42,
    "denoise": 1.0
  },

  # 7. Resolution
  "latent": {
    "width": 1024,
    "height": 1536,
    "batch_size": 1
  }
}
```

## GPU Optimization

### Metal (M1/M2/M3 Mac)

```bash
# Startup
python main.py --force-fp16 --preview-method auto

# Environment
export PYTORCH_ENABLE_MPS_FALLBACK=1
export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0
```

### NVIDIA GPU

```bash
# Startup
python main.py --preview-method auto --use-pytorch-cross-attention

# CUDA
export CUDA_VISIBLE_DEVICES=0
```

### Memory Settings

```json
{
  "vram_mode": "auto",
  "preview_method": "auto",
  "disable_smart_memory": false
}
```

## Batch Processing

```python
def batch_generate_episode(episode_slug):
    shotlist = load_shotlist(episode_slug)

    # Group by character for model efficiency
    by_character = group_by_characters(shotlist)

    for chars, shots in by_character.items():
        # Load character models once
        load_character_models(chars)

        # Generate all shots
        for shot in shots:
            generate_panel(shot)

        # Unload to free VRAM
        unload_character_models(chars)
```

## Workflow Optimization

### Resolution Strategy

```python
# Generate at 512x768, upscale to 1024x1536
def generate_with_upscale(shot):
    # Low-res generation (faster, less VRAM)
    low_res = generate(width=512, height=768)

    # Upscale
    high_res = upscale(low_res, scale=2.0, denoise=0.4)

    return high_res
```

### Model Caching

```python
# Load models once, reuse
loaded_models = {}

def get_model(model_name):
    if model_name not in loaded_models:
        loaded_models[model_name] = load_model(model_name)
    return loaded_models[model_name]
```

## Troubleshooting

**Out of VRAM**:
- Lower resolution
- Unload unused models
- Reduce batch size
- Use `--lowvram` flag

**Slow Generation**:
- Reduce steps (25 → 20)
- Lower resolution temporarily
- Disable preview
- Use faster sampler (euler_a)

**Inconsistent Results**:
- Check same checkpoint across runs
- Verify LoRA loaded
- Ensure InstantID weight consistent
- Use fixed seeds for testing

## Resources

- ComfyUI GitHub: https://github.com/comfyanonymous/ComfyUI
- Custom Nodes Manager: https://github.com/ltdrdata/ComfyUI-Manager
- Workflow Examples: ComfyUI Community
