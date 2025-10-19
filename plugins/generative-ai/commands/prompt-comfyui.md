# /prompt-comfyui

Generate production-ready ComfyUI prompts (positive + negative) with LoRA recommendations and sampler settings.

## Syntax

```
/prompt-comfyui [style] [description] [options]
```

## Arguments

- **style** (required): Comic art style or technique reference
  - Examples: "manga", "western comic", "digital painting", "cel-shaded"
  - Accepts style names from 50+ comic art styles library
  - Can specify model preference with style: "manga+SDXL", "vintage+flux"

- **description** (required): Scene or subject description
  - Examples: "character in action pose", "superhero flying", "detective scene"
  - Can include technical details (resolution, aspect ratio)
  - Include character details, setting, lighting needs

- **[options]** (optional):
  - `model:sdxl` - Use SDXL (default, balanced)
  - `model:flux` - Use FLUX (best quality, slower)
  - `model:sd15` - Use SD 1.5 (fastest, legacy LoRAs)
  - `consistency` - Include InstantID setup if character reference available
  - `controlnet` - Include ControlNet setup for pose control
  - `style-code:true` - Show SREF-equivalent mappings
  - `steps:N` - Recommend N steps (default: 40)

## Agent Delegation

Routes to: **comfyui-expert** agent

## Output Format

The command returns:

1. **Model Recommendation** - Analysis of best model choice
2. **Positive Prompt** - Detailed tag-based positive prompt with weights
3. **Negative Prompt** - Quality control negative prompt
4. **LoRA Recommendations** - Specific LoRAs with weights
5. **Sampler Settings**:
   - CFG Scale
   - Sampling method
   - Step count
   - Recommended resolution/aspect ratio

6. **Advanced Options**:
   - InstantID setup (if character consistency needed)
   - ControlNet suggestions
   - Refinement options

7. **Quality Notes** - Explanation of choices
8. **Optimization Tips** - How to improve results

## Examples

### Example 1: Manga Action Scene with SDXL

```
/prompt-comfyui manga warrior in dynamic fighting stance
```

**Returns**:
```
MODEL ANALYSIS
- Recommended: SDXL 1.0
- Reasoning: Balanced quality/speed, excellent manga support, large LoRA ecosystem
- Alternatives: FLUX.1 for ultimate quality, SD1.5 for speed

POSITIVE PROMPT
1 male warrior, muscular build, spiky hair, dynamic fighting stance, mid-action,
intense focused expression, speed lines, energy effects glowing, battle atmosphere,
traditional manga inking style, bold black lines, high contrast, screentone shading,
professional manga art, highly detailed character anatomy, sharp focus, masterpiece,
<lora:manga_expressive:0.9>, <lora:shounen_style:0.85>, <lora:speed_lines:0.7>, <lora:perfect_hands:0.6>

NEGATIVE PROMPT
lowres, bad anatomy, bad hands, extra limbs, text, error, missing fingers,
extra digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,
signature, watermark, username, blurry, distortion, ugly, deformed

LORA RECOMMENDATIONS
Primary Style LoRAs:
- manga_expressive (0.9): Core manga aesthetic with emotional expression
- shounen_style (0.85): Shounen-specific action and energy
- speed_lines (0.7): Action lines effect
- perfect_hands (0.6): Hand quality enhancement

Alternative LoRA Combinations:
- For more realistic: Add anatomy_correction (0.5) instead of shounen_style
- For different artist: Try specific_artist_style LoRA if available
- For extreme detail: Add detail_enhancer (0.5)

SAMPLER SETTINGS
- Base Model: SDXL 1.0
- CFG Scale: 8.0 (balanced for manga style adherence)
- Sampler: DPM++ 2M Karras
- Steps: 40 (good balance of quality and speed)
- Scheduler: Karras (smooth progression)

RESOLUTION & ASPECT
- Recommended: 768x1152 (2:3 portrait, standard comic panel)
- Alternatives:
  - 1024x1024 (square, for close-ups)
  - 512x768 (quick preview)
  - 1152x768 (horizontal action scene)

ADVANCED OPTIONS

Character Consistency (if you have reference images):
- Use InstantID + character LoRA for face consistency
- Reference image weight: 0.8-1.0
- Combine with style LoRA for artistic effect

Pose Control (if exact pose needed):
- Use ControlNet lineart or pose
- Provide reference image of desired pose
- Combine with main generation for controlled output

Quality Enhancement:
- For maximum quality: Increase steps to 50+, set CFG 8.5
- For artistic variation: Increase CFG to 9-10
- For prompt-literal: Lower CFG to 6-7

QUALITY NOTES
- SDXL provides excellent manga support with proper LoRAs
- 0.9 weight on manga_expressive brings strong aesthetic
- Combination of speed_lines + shounen_style matches source perfectly
- Negative prompt comprehensive for clean output
- CFG 8.0 balances style adherence with artistic generation

OPTIMIZATION TIPS
1. Test with 30 steps first, increase if needed
2. Adjust LoRA weights up to 1.0 for stronger effect
3. Try different samplers if results seem off (Heun, DPM++SDE)
4. For consistency across multiple images:
   - Save the positive/negative prompts
   - Use --seed for reproducibility
   - Reduce CFG slightly (7.5) for variation
5. If hands look wrong, increase perfect_hands to 0.8
6. For more detailed backgrounds, add background_detail (0.5) LoRA

NEXT STEPS
1. Load SDXL in your ComfyUI workflow
2. Set sampler parameters as above
3. Paste positive/negative prompts
4. Load recommended LoRAs with specified weights
5. Generate and review
6. Adjust CFG/steps if needed for your preference
```

### Example 2: Western Comic with Character Consistency

```
/prompt-comfyui western comic superhero in action pose consistency
```

**Returns**:
```
MODEL ANALYSIS
- Recommended: SDXL 1.0 (with InstantID for character consistency)
- For character-consistent generation: Combine with InstantID + character LoRA
- Speed trade-off: ~90-120s per generation with InstantID

POSITIVE PROMPT
superhero character, muscular build, flowing cape, dynamic action pose,
flying heroically, city background, sunset sky, golden hour lighting,
dramatic low-angle perspective, bold comic book ink lines, vibrant colors,
professional comic art style, Jim Lee influence, highly detailed,
sharp focus, masterpiece quality,
<lora:comic_book_style:0.8>, <lora:superhero_anatomy:0.7>, <lora:ink_lines:0.7>

NEGATIVE PROMPT
lowres, bad anatomy, bad hands, extra limbs, text, error, missing fingers,
extra digits, cropped, worst quality, low quality, jpeg artifacts,
signature, watermark, blurry, distortion, ugly

CHARACTER CONSISTENCY SETUP

IMPORTANT: For character consistency across multiple poses:

Option 1: InstantID (Recommended)
- Requires: Reference image of character face
- Setup:
  1. Load InstantID model in ComfyUI
  2. Provide clear headshot reference (768x768+)
  3. Use InstantID weight: 0.85-0.95
  4. Combine with style LoRA (comic_book_style:0.8)
  5. Add character LoRA if available: (superhero_character:0.7)

InstantID Integration:
- IP-Adapter strength: 0.6-0.8
- Face weight: 0.9
- Body weight: 0.5 (let LoRA handle body)

Option 2: Character LoRA (If available)
- Fine-tune LoRA on character screenshots (20+ images minimum)
- Use weight: 0.8-1.0
- Combine with comic style LoRA
- Most control over appearance

SAMPLER SETTINGS (with InstantID)
- Base Model: SDXL 1.0
- Refiner: SDXL Refiner (recommended for faces)
- CFG Scale: 8.5 (high for character adherence)
- Sampler: DPM++ 2M Karras
- Steps: 45 (extra steps for face quality)
- InstantID Steps: 20-30 (separate)

RESOLUTION
- For character consistency: 768x1152 (2:3 portrait)
- For full-body consistency: 1024x1024 (square)
- Never scale up reference + input simultaneously

QUALITY NOTES
- InstantID maintains character face across different poses/expressions
- Works best with clear, well-lit reference images
- Combine with LoRA for consistent clothing/style
- Requires separate IP-Adapter integration in ComfyUI
- Face consistency ~95%+, body consistency ~70-80% (LoRA dependent)

WORKFLOW RECOMMENDATIONS
1. Generate base character with InstantID
2. Create different pose variations (same LoRA/InstantID)
3. Use consistent negative prompt
4. Vary pose description, keep character description stable
5. For consistency: Lower CFG slightly (8.0) when varying poses

CHARACTER CONSISTENCY EXAMPLES
Same character, different poses:
- Prompt 1: "[character], standing with hands on hips, confident pose"
- Prompt 2: "[character], sitting at desk, thinking pose"
- Prompt 3: "[character], running toward camera, action pose"
- All use same InstantID setup, same character LoRA

NEXT STEPS FOR CHARACTER CONSISTENCY
1. Gather 3-5 clear reference images of character (different angles if possible)
2. Choose best headshot for InstantID reference
3. Follow InstantID setup above
4. Test generation with different poses
5. Fine-tune character LoRA if consistency not perfect (optional)
```

### Example 3: FLUX Model - Highest Quality

```
/prompt-comfyui digital painting sci-fi character model:flux
```

**Returns**:
```
MODEL ANALYSIS
- Selected: FLUX.1-dev (highest quality, ~4x slower than SDXL)
- Why FLUX: Superior text rendering, perfect hands, pose accuracy
- Trade-off: ~240-360s per generation vs ~60-90s for SDXL
- Alternatives: FLUX.1-schnell (faster, lower quality), SDXL (faster)

FLUX SPECIAL NOTES
- FLUX uses natural language (no tags needed)
- No negative prompts supported (safety built-in)
- No emphasis notation (weight via description)
- LoRAs work but limited ecosystem currently
- Best for photorealism and text-in-image

POSITIVE PROMPT (Natural Language for FLUX)
A professional digital painting of a sci-fi character with sleek futuristic armor,
cybernetic enhancements, confident dynamic pose, advanced technology aesthetic,
vibrant neon colors, detailed intricate design, sharp focus, masterpiece quality,
8k resolution, award-winning illustration.

ALTERNATIVE STRUCTURED PROMPT (if using adapters)
sci-fi character, advanced armor, cybernetic enhancements, dynamic pose,
futuristic aesthetic, vibrant neon colors, detailed design, sharp focus,
highly detailed, masterpiece, 8k quality

SAMPLER SETTINGS (FLUX)
- Model: FLUX.1-dev
- CFG Scale: 7.0-8.0 (FLUX is less literal, lower CFG acceptable)
- Sampler: FlowEuler (FLUX-specific)
- Steps: 50+ (FLUX benefits from more steps)
- Scheduler: Simple

ALTERNATIVE SAMPLERS
- FlowMatch: Standard for FLUX
- Euler: Compatible but not optimized
- Manual guidance: If available

RESOLUTION & ASPECT
- Recommended: 1024x1024 (square, most stable)
- Alternatives:
  - 768x1024 (portrait)
  - 1024x768 (landscape)
  - 512x512 (test generation)
- FLUX handles various ratios well

QUALITY NOTES
- FLUX excels at complex details and photorealism
- Hands are nearly perfect (FLUX strength)
- Text rendering in image excellent
- Pose accuracy superior to SDXL
- Generation time ~4x longer than SDXL
- Memory usage higher (requires good GPU)

WHEN TO USE FLUX
- Final showcase images
- Detailed technical designs
- Text-heavy imagery
- Maximum quality requirement
- When generation time is not critical

WHEN TO USE SDXL INSTEAD
- Quick iterations (faster feedback)
- Batch generation (many images)
- Limited GPU resources
- Style LoRA critical (larger ecosystem)
- Budget-conscious generation

OPTIMIZATION TIPS
1. Use FLUX for final output, SDXL for iteration
2. Test concept in SDXL (fast), finalize in FLUX (quality)
3. FLUX handles minimal prompting well - don't over-describe
4. For variations: Change minor details, keep core description
5. Combine multiple FLUX outputs in Photoshop for best results

NEXT STEPS
1. Ensure FLUX model loaded in ComfyUI (requires ~20GB VRAM)
2. Use natural language prompt (simpler is better)
3. Set CFG 7.5, steps 50-60
4. Generate and review quality
5. For production, upscale output with quality enhancer

COMPARATIVE GENERATION TIMES
- SDXL (40 steps): ~60-90 seconds
- FLUX (50 steps): ~240-360 seconds
- FLUX Schnell: ~90-120 seconds (lower quality)
```

## Tips for Best Results

### 1. Choose the Right Model
- **SDXL**: Best balance of speed/quality, largest LoRA ecosystem
- **FLUX**: Best quality, great hands/text, but 4x slower
- **SD1.5**: Fastest, good for quick tests, most LoRAs available

### 2. LoRA Weight Combinations
- Total weight recommended: 1.5-2.5 maximum
- Primary style: 0.8-0.9 weight
- Supporting: 0.6-0.7 weight
- Enhancement: 0.5-0.6 weight
- Don't exceed 1.0+ on multiple LoRAs (saturation)

### 3. CFG Scale Strategy
- 6.0-7.0: Creative, less prompt-literal
- 7.5-8.5: Balanced (recommended)
- 9.0-11.0: Very prompt-literal
- 12.0+: Can cause artifacts, less creative

### 4. Sampler Selection
- **DPM++**: Best all-around quality
- **Euler**: Fast, clean results
- **Heun**: Highest quality, slower
- **LCM**: Ultra-fast, lower quality
- Test different samplers for style optimization

### 5. Step Count Impact
- 20-30 steps: Preview/quick iteration
- 30-50 steps: Standard (recommended)
- 50-70 steps: High quality
- 70+: Diminishing returns, same quality

## Advanced Features

### Character Consistency
- Use InstantID for face consistency
- Combine with character LoRA
- Provide clear reference images
- Returns setup guide with IP-Adapter weights

### Pose Control via ControlNet
- Use when exact pose/composition critical
- Requires reference pose image
- Multiple ControlNets can stack
- Adds ~30-60s to generation time

### Batch Generation
- Use same prompts/seeds for consistency
- Vary CFG slightly for exploration
- Use `--seed` for reproducible results
- Perfect for iterative refinement

## Related Commands

- `/convert-prompt [source] comfyui [prompt]` - Convert from other platforms to ComfyUI
- `/prompt-midjourney` - Generate Midjourney prompts
- `/prompt-gemini` - Generate Gemini prompts
- `/prompt-firefly` - Generate Firefly prompts

## See Also

- **Agent**: `comfyui-expert.md` - Full expert profile
- **Documentation**: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/comfyui/01-comfyui-fundamentals.md`
- **Styles**: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/comfyui/02-comic-art-styles.md`
- **Style Library Skill**: `/style-library/SKILL.md` - Browse all 50+ styles

---

**Command Version**: 1.0.0
**Agent**: comfyui-expert
**Last Updated**: January 2025
