# /convert-prompt

Convert AI image generation prompts between Midjourney, ComfyUI, Gemini, and Adobe Firefly platforms.

## Syntax

```
/convert-prompt [from-platform] [to-platform] [prompt]
```

## Arguments

- **from-platform** (required): Source platform
  - Options: `midjourney`, `comfyui`, `gemini`, `firefly`, or `auto` (auto-detect)
  - Example: `midjourney`, `comfyui`

- **to-platform** (required): Target platform
  - Options: `midjourney`, `comfyui`, `gemini`, `firefly`
  - Example: `midjourney`, `comfyui`

- **prompt** (required): The prompt to convert
  - Full prompt text (can be multiple lines)
  - Can include parameters/flags from source platform
  - Can be simplified or full detailed prompt

## Agent Delegation

Routes to: **prompt-converter** agent

This agent:
1. Auto-detects source platform if "auto" specified
2. Extracts universal concept elements
3. Transforms to target platform syntax
4. Optimizes for target platform strengths
5. Preserves original intent

## Output Format

The command returns:

1. **Source Analysis** - Identifies source platform and structure
2. **Concept Extraction** - Universal elements found in prompt
3. **Platform Mapping** - How features translate between platforms
4. **Converted Prompt** - Ready-to-use target platform prompt
5. **Parameter Recommendations** - Platform-specific settings
6. **Quality Notes** - Explanation of conversion choices
7. **Trade-offs** (if applicable) - What changes due to platform differences
8. **Suggestions** - How to optimize for target platform

## Examples

### Example 1: Midjourney to ComfyUI

```
/convert-prompt midjourney comfyui /imagine: manga warrior in dynamic fighting stance, speed lines, intense energy aura, ancient temple ruins background, sunset lighting, dramatic shadows, professional manga art, Masashi Kishimoto influence, highly detailed, sharp focus --niji 7 --style expressive --ar 2:3 --s 300
```

**Returns**:
```
SOURCE ANALYSIS
- Platform: Midjourney Niji 7 (anime/manga specialist)
- Format: /imagine: command with natural language description + parameters
- Parameters Used: --niji 7, --style expressive, --ar 2:3, --s 300
- Total Word Count: ~50 words + parameters

CONCEPT EXTRACTION
- Subject: Manga warrior
- Action: Dynamic fighting stance
- Effects: Speed lines, intense energy aura
- Environment: Ancient temple ruins
- Lighting: Sunset lighting, dramatic shadows
- Style: Professional manga art, Kishimoto influence
- Quality: Highly detailed, sharp focus

PLATFORM MAPPING
Midjourney Feature          → ComfyUI Equivalent
--niji 7 (anime specialist) → LoRA: manga_expressive
--style expressive          → LoRA: shounen_style
--ar 2:3 (aspect ratio)     → Resolution: 768x1152
--s 300 (stylization)       → CFG: 8.0
Parameters                  → Sampler settings
Quality markers             → Tag emphasis + LoRA weights

CONVERTED PROMPT

Model: SDXL 1.0
Aspect Ratio: 2:3 (768x1152)

Positive Prompt:
1 male warrior, muscular build, spiky dark hair, dynamic fighting stance,
mid-action, intense focused expression, speed lines and motion effects,
energy aura glowing brightly, battle atmosphere, ancient temple ruins background,
sunset sky with dramatic lighting and shadows, professional manga art style,
Masashi Kishimoto influence, bold manga linework, screentone shading,
highly detailed character anatomy, sharp focus, masterpiece quality,
<lora:manga_expressive:0.9>, <lora:shounen_style:0.85>, <lora:speed_lines:0.7>,
<lora:perfect_hands:0.6>

Negative Prompt:
lowres, bad anatomy, bad hands, extra limbs, text, error, missing fingers,
extra digits, cropped, worst quality, low quality, jpeg artifacts,
signature, watermark, blurry, distortion, ugly, deformed

SAMPLER SETTINGS
- Model: SDXL 1.0
- Sampler: DPM++ 2M Karras
- CFG Scale: 8.0 (matches Midjourney stylization)
- Steps: 40 (balanced quality/speed)
- Scheduler: Karras (smooth)

QUALITY NOTES
- Midjourney Niji 7 mapped to manga-specific LoRAs
- --style expressive → LoRA: shounen_style (maintains dramatic manga feel)
- --ar 2:3 → 768x1152 resolution (exact match)
- Stylization 300 → CFG 8.0 (equivalent artistic control)
- Speed lines and energy effects preserved through LoRAs
- Kishimoto influence maintained through specific LoRA
- Added comprehensive negative prompt (Midjourney `--no` limited)

TRADE-OFFS
- None major: High-fidelity conversion
- ComfyUI offers more explicit control (benefit)
- Takes longer to generate than Midjourney
- Larger LoRA ecosystem available for experimentation

OPTIMIZATION FOR COMFYUI
- SDXL is optimal model for this style
- Consider using FLUX for ultimate quality
- Can add refiner step for face quality
- InstantID option if character consistency needed
- ControlNet available for exact pose control

NEXT STEPS
1. Copy converted prompt and settings above
2. Set up ComfyUI with SDXL 1.0 model
3. Load recommended LoRAs with specified weights
4. Configure sampler as above
5. Paste positive and negative prompts
6. Generate and compare with Midjourney original

VERIFICATION
Generated ComfyUI output should:
- Show warrior in dynamic pose (✓)
- Include speed lines effect (✓)
- Display energy aura (✓)
- Feature temple background (✓)
- Have sunset lighting (✓)
- Match manga aesthetic (✓)
- Show professional quality (✓)
```

### Example 2: ComfyUI to Firefly

```
/convert-prompt comfyui firefly Positive: superhero character, muscular build, red cape flowing, flying pose, city background, sunset sky, orange and purple clouds, golden hour lighting, dramatic low-angle perspective, bold comic book ink outlines, vibrant colors, professional comic art, Jim Lee style, highly detailed, sharp focus, <lora:comic_book_style:0.8>, <lora:superhero_action:0.7>

Negative: lowres, bad anatomy, bad hands, extra limbs, text, error, missing fingers, extra digits, cropped, worst quality, low quality, jpeg artifacts, signature, watermark, blurry
```

**Returns**:
```
SOURCE ANALYSIS
- Platform: ComfyUI (tag-based structured prompts)
- Format: Positive/Negative pair with LoRA specifications
- LoRAs Used: comic_book_style (0.8), superhero_action (0.7)
- Quality: Very detailed (technical specification)
- Word Count: ~60 words positive, ~20 words negative

CONCEPT EXTRACTION
- Subject: Superhero character, muscular
- Appearance: Red cape, flying pose
- Environment: City, sunset sky, clouds
- Lighting: Golden hour, dramatic angle
- Style: Comic book, Jim Lee influence, bold ink outlines
- Colors: Vibrant, orange and purple
- Quality: Professional, highly detailed

PLATFORM MAPPING
ComfyUI Feature              → Firefly Equivalent
tag-based structure          → Natural language description
LoRA: comic_book_style      → Filter: "Comic Book"
LoRA: superhero_action      → Described in prompt
Technical tag emphasis       → Concise natural language
Negative prompt              → Omit (Firefly uses content filtering)
"highly detailed"            → Quality descriptor preserved

CONVERTED PROMPT (Concise for Firefly - 48 words)

Superhero in vibrant red cape and muscular build flying dynamically over city.
Sunset sky with orange and purple clouds, golden hour lighting. Dramatic upward
angle, bold comic book style with strong ink outlines, vibrant colors, professional
quality.

FIREFLY SETTINGS
- Filter: "Comic Book" (replaces LoRA styling)
- Content Type: "Illustration"
- Aspect Ratio: 2:3 (vertical comic panel)
- Safety: Commercial-safe (automatic)

QUALITY NOTES
- Drastically condensed (~60 → 48 words, removes 20% verbosity)
- ComfyUI tag structure converted to flowing prose
- LoRAs replaced with Firefly filter selection
- Comic book style moved to filter (lets Firefly optimize)
- Negative prompt omitted (Firefly uses built-in safety filtering)
- Kept essential elements: character, action, environment, lighting, style
- Quality markers preserved ("professional quality")

TRADE-OFFS
- Generation time: MUCH faster (30s vs 90s) - BENEFIT
- Fine detail control: Reduced (ComfyUI has more control) - TRADE-OFF
- Speed: ~3x faster generation - BENEFIT
- Commercial safety: Guaranteed (vs ComfyUI no guarantee) - BENEFIT
- Consistency: Reduced across generations (no character LoRA) - TRADE-OFF

WHY THIS TRADE-OFF
- Firefly optimized for speed and commercial use
- 48 words ideal for Firefly (vs ComfyUI's 80+ tags)
- Filter handles style (vs LoRA in ComfyUI)
- Generation feedback loop much faster
- Perfect for quick exploration, less suitable for detailed control

OPTIMIZATION FOR FIREFLY
- 48 words is optimal length for Firefly
- "Comic Book" filter is perfect match for style
- Prompt simplification is appropriate (not a loss, optimization)
- Consider batch:5 for quick variations
- Fast iteration enables quick exploration

ALTERNATIVE APPROACHES
1. If you need ComfyUI control: Don't convert, keep using ComfyUI
2. If you need Firefly speed: Accept reduced control
3. Compromise: Generate concept in Firefly, refine in ComfyUI

NEXT STEPS
1. Go to firefly.adobe.com
2. Paste prompt above
3. Apply "Comic Book" filter
4. Set to Illustration content type
5. Choose 2:3 aspect ratio
6. Generate and compare with ComfyUI

QUALITY EXPECTATIONS
- Generated image will be similar in content
- Firefly quality is professional (but different aesthetic)
- Execution differences expected (different models)
- Ideal for quick concepts, not character consistency
- Fast turnaround (~30 seconds)

RECOMMENDATION
- Use Firefly for: Quick exploration, concepts, commercialuse
- Use ComfyUI for: Character consistency, detailed control, production
- Use both: Concept in Firefly, production in ComfyUI
```

### Example 3: Gemini to Midjourney with Auto-Detect

```
/convert-prompt auto midjourney A professional manga-style illustration of a teenage warrior character with spiky dark hair and determined expression, wearing traditional combat clothing. The character is depicted in a dynamic action pose, mid-strike with sword raised, showing intense focus. The background features an ancient temple setting with morning sunlight filtering through stone pillars. The artwork demonstrates professional manga style with clean bold linework, screentone shading for depth, large expressive eyes characteristic of manga, dynamic action lines, and Japanese comic aesthetic.
```

**Returns**:
```
SOURCE ANALYSIS
- Platform: Auto-detected as Gemini (natural language, descriptive)
- Format: Narrative prose description (no technical syntax)
- Approach: Flowing sentences, descriptive language
- Word Count: ~100 words
- No parameters or flags (Gemini standard)

CONCEPT EXTRACTION
- Subject: Teenage warrior character
- Appearance: Spiky dark hair, determined expression, traditional clothing
- Action: Dynamic action pose, mid-strike, sword raised
- Environment: Ancient temple, morning sunlight through pillars
- Style: Professional manga, bold linework, screentone shading
- Quality: Clean, detailed, expressive
- Mood: Intense, focused, action-oriented

PLATFORM MAPPING
Gemini Feature               → Midjourney Equivalent
Natural language flow        → /imagine: structured + prose
Descriptive style           → Artistic description language
Quality emphasis            → Quality parameters (--q, --s)
No parameters               → Add appropriate flags
Photorealistic focus        → Stylization parameter
Manga vocabulary            → --niji 7 for anime specialist

CONVERTED PROMPT

/imagine: dynamic manga panel of teenage warrior character with spiky dark hair
and determined expression, wearing traditional combat clothing, in action pose
mid-strike with sword raised high, intense focused expression,
ancient temple setting background with morning sunlight filtering through pillars,
professional manga style with bold clean linework, screentone shading,
large expressive manga eyes, dynamic action lines, Japanese comic aesthetic,
highly detailed, sharp focus, masterpiece quality
--niji 7 --style expressive --ar 2:3 --s 300 --q 0.5

PARAMETER RECOMMENDATIONS
- Version: --niji 7 (anime/manga specialist, perfect for this)
- Style: --style expressive (brings out manga emotion and drama)
- Aspect Ratio: --ar 2:3 (vertical comic panel, ideal)
- Stylization: --s 300 (high for artistic manga feel)
- Quality: --q 0.5 (standard, good balance)
- Chaos: --c 0 (low for consistency)

QUALITY NOTES
- Gemini's narrative approach well-suited to Midjourney
- Descriptive language converts directly to /imagine: command
- Added Niji 7 flag (best for manga generation)
- Specificity preserved (teenage warrior, dark hair, etc.)
- Action and emotion emphasized (Midjourney strength)
- Manga vocabulary directly applicable
- Higher stylization (300) brings out artistic feel
- Reduced from ~100 words (Gemini) to ~65 words (Midjourney optimal)

TRADE-OFFS
- None major: High-fidelity conversion
- Midjourney will be faster than Gemini
- Artistic interpretation will differ (different models)
- Niji 7 excellent match for manga style
- Quality comparable to Gemini (perhaps more stylized)

OPTIMIZATION FOR MIDJOURNEY
- Parameters well-optimized for manga generation
- Niji 7 is ideal specialist model for this
- Expressive style flag enhances emotional manga qualities
- 2:3 aspect perfect for comic panel
- High stylization (300) maintains artistic feel

NEXT STEPS
1. Copy prompt and parameters above
2. Go to Midjourney Discord
3. Use /imagine command
4. Paste complete prompt with parameters
5. Generate and compare with Gemini version

EXPECTED RESULTS
- Similar warrior character and pose
- More artistic/stylized than Gemini
- Professional manga aesthetic
- Faster generation than Gemini
- Character consistency better with Niji 7
- Dynamic action conveyed clearly

WHEN TO USE EACH
- Midjourney: Artistic iterations, speed, manga specialty
- Gemini: Photorealistic, text rendering, narrative quality
- Both: Generate in both for comparison, choose best
```

### Example 4: Midjourney to Gemini - Expanding for Natural Language

```
/convert-prompt midjourney gemini /imagine: cyberpunk detective in trench coat, rain-soaked alley, neon signs, film noir atmosphere, low-angle shot, sharp shadows, professional illustration --ar 16:9 --s 400 --v 7
```

**Returns**:
```
SOURCE ANALYSIS
- Platform: Midjourney v7 (natural language + parameters)
- Format: /imagine: prose description with flags
- Parameters: --ar 16:9 (widescreen), --s 400 (high stylization), --v 7 (latest)
- Implicit Details: Lighting, mood, composition are condensed
- Word Count: ~30 words (Midjourney efficient)

CONCEPT EXTRACTION
- Subject: Cyberpunk detective
- Appearance: Trench coat
- Environment: Rain-soaked alley
- Visual Elements: Neon signs
- Mood/Lighting: Film noir, sharp shadows
- Camera: Low-angle shot
- Quality: Professional illustration

PLATFORM MAPPING
Midjourney Feature          → Gemini Equivalent
/imagine: command           → Natural language description
Implicit lighting           → Explicit lighting description
Mood phrase "film noir"     → Detailed mood language
Low-angle shot             → Camera description
Professional illustration   → Quality language
Parameters                  → Aspect ratio preservation

CONVERTED PROMPT (Expanded Natural Language)

A professional film noir cyberpunk illustration of a hardened detective character
wearing a dark trench coat, standing in a rain-soaked urban alley. Neon signs
glow in the background with blues and reds reflecting off wet pavement. The
detective is captured from a dramatic low-angle perspective looking upward,
creating an imposing heroic stance. Sharp shadows fall across the face, creating
high-contrast dramatic lighting characteristic of film noir cinematography. The
atmosphere is moody, mysterious, and dangerous with wet streets and urban decay.
Professional illustration quality, sharp focus, highly detailed, masterpiece.

ASPECT RATIO RECOMMENDATION
Recommended: 16:9 (horizontal widescreen)
Why: Matches Midjourney --ar 16:9
Perfect for: Wide cinematic composition, alley environment

GEMINI SPECIFIC OPTIMIZATIONS
- Expanded from ~30 words → ~95 words (Gemini's strength)
- Made lighting explicit (Gemini responds to description)
- Added camera angle description (Gemini interprets well)
- Emphasized noir mood through narrative
- Added environmental context (wet pavement, neon reflection)
- Quality markers appropriate for Gemini

QUALITY NOTES
- Expansion is appropriate for Gemini (loves description)
- Film noir atmosphere conveyed through mood language
- Low-angle perspective clearly described
- Lighting details explicit vs Midjourney's implicit
- Professional quality maintained through markers
- Cyberpunk aesthetic preserved

TRADE-OFFS
- Gemini may render more realistically than Midjourney
- Artistic stylization may be different
- Gemini excellent at atmospheric mood
- Different interpretation of "professional illustration"
- Speed: Midjourney faster, Gemini slower

OPTIMIZATION FOR GEMINI
- Natural language expanded (good for Gemini)
- Narrative flow added (Gemini's strength)
- Lighting explicit (Gemini responds well)
- Mood emphasized (Gemini excellent at atmosphere)
- Ideal length for Gemini (~95 words)

NEXT STEPS
1. Copy expanded prompt above
2. Go to Google Vertex AI or Gemini API
3. Set aspect ratio to 16:9
4. Paste prompt
5. Generate and compare with Midjourney

EXPECTED DIFFERENCES
- Gemini rendering more photorealistic
- Possibly less "illustration" appearance than Midjourney
- Atmospheric mood excellent
- Text rendering better than Midjourney (if any text included)
- Cinematic quality strong
- Lighting and shadows beautifully rendered

WHEN TO USE EACH
- Midjourney: Stylized art direction, speed
- Gemini: Atmospheric mood, lighting detail, photorealism
- Both: Different aesthetic approaches to same concept
```

## Conversion Quality Levels

The command assesses conversion quality:

### High-Fidelity Conversions
- Midjourney ↔ Gemini (both natural language)
- ComfyUI ↔ Midjourney (similar structure)
- Between platforms for standard concepts
- **Quality**: 90%+ intent preserved

### Moderate-Fidelity Conversions
- Any → Firefly (simplification necessary)
- Advanced features → basic platform
- Complex LoRAs → simpler approach
- **Quality**: 75-90% intent preserved

### Lossy Conversions
- ComfyUI → Firefly (high control → simplicity)
- Advanced consistency → platforms without support
- **Quality**: 60-75% intent preserved
- **Warning**: Command notes major differences

## Supported Conversion Paths

All bidirectional conversions supported:
- Midjourney ↔ ComfyUI
- Midjourney ↔ Gemini
- Midjourney ↔ Firefly
- ComfyUI ↔ Gemini
- ComfyUI ↔ Firefly
- Gemini ↔ Firefly

## Auto-Detection Syntax

```
/convert-prompt auto [to-platform] [prompt]
```

Auto-detection identifies:
- Midjourney: `/imagine:` command, `--flags`, parameters
- ComfyUI: Tags with commas, `(word:1.3)` weights, LoRAs
- Gemini: Natural narrative prose, no syntax
- Firefly: Concise natural language (30-60 words)

## Tips for Best Conversions

1. **Provide complete prompt** - More context = better conversion
2. **Include parameters** - Flags and settings help mapping
3. **Specify unusual requirements** - Character consistency, specific styles
4. **Review trade-offs** - Command explains quality changes
5. **Test recommendations** - Generated settings are starting points
6. **Iterate if needed** - Conversions can be refined through follow-up commands

## Related Commands

- `/prompt-midjourney` - Generate Midjourney prompts
- `/prompt-comfyui` - Generate ComfyUI prompts
- `/prompt-gemini` - Generate Gemini prompts
- `/prompt-firefly` - Generate Firefly prompts

## See Also

- **Agent**: `prompt-converter.md` - Full conversion expert profile
- **Documentation**: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/cross-platform/prompt-conversion-guide.md`
- **Fundamentals**: Individual platform documentation files

---

**Command Version**: 1.0.0
**Agent**: prompt-converter
**Last Updated**: January 2025
