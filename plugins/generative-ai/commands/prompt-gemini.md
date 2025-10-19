# /prompt-gemini

Generate production-ready Google Gemini Imagen 3 prompts using natural language for photorealistic and illustrated content.

## Syntax

```
/prompt-gemini [style] [description] [options]
```

## Arguments

- **style** (required): Comic art style or photography style
  - Examples: "manga", "western comic", "photorealistic", "digital painting"
  - Accepts style names from 50+ comic art styles library
  - Can include photography/concept art styles

- **description** (required): Scene or subject description
  - Examples: "character with detailed appearance", "scene with lighting details"
  - Should be descriptive and narrative
  - Can include environment, lighting, mood details

- **[options]** (optional):
  - `aspect:1:1` - Square (default)
  - `aspect:9:16` - Vertical (portrait, mobile)
  - `aspect:16:9` - Horizontal (landscape, widescreen)
  - `aspect:2:3` - Comic panel portrait
  - `aspect:3:2` - Comic panel landscape
  - `text:true` - Include text rendering guidance
  - `quality:high` - Emphasize high-quality output
  - `photorealism:true` - Optimize for photorealistic style

## Agent Delegation

Routes to: **gemini-expert** agent

## Output Format

The command returns:

1. **Style Analysis** - Confirms style choice and approach
2. **Optimized Prompt** - Natural language prompt ready for Gemini
3. **Text-in-Image Guidance** (if applicable) - How to render text
4. **Vertex AI Parameters**:
   - Aspect ratio recommendation
   - Model parameters
   - Safety settings

5. **Quality Notes** - Explanation of prompt construction
6. **Gemini Strengths** - What Gemini does best
7. **Iteration Suggestions** - How to refine if needed

## Examples

### Example 1: Manga Illustration with Character Details

```
/prompt-gemini manga teenage warrior in dynamic pose
```

**Returns**:
```
STYLE ANALYSIS
- Style: Manga (Japanese comic illustration)
- Gemini Approach: Use natural descriptive language focusing on manga aesthetics
- Key Elements: Expressive eyes, bold linework, screentone shading, dynamic composition
- Format: Narrative description rather than technical tags

OPTIMIZED PROMPT FOR GEMINI
A professional manga-style illustration of a teenage warrior character
with spiky dark hair and determined expression, wearing traditional combat clothing.
The character is depicted in a dynamic action pose, mid-strike with sword raised,
showing intense focus. The background features an ancient temple setting with
morning sunlight filtering through stone pillars. The artwork demonstrates
professional manga style with clean bold linework, screentone shading for depth,
large expressive eyes characteristic of manga, dynamic action lines, and Japanese
comic aesthetic. The composition is dramatic with low-angle perspective emphasizing
the hero's strength. Highly detailed, sharp focus, professional manga illustration
quality, award-winning artwork.

ASPECT RATIO RECOMMENDATION
- Default: 2:3 (vertical, standard manga panel)
- Alternative: 1:1 (square for character close-up)
- Alternatives: 9:16 (mobile/webtoon), 16:9 (double-page spread)

VERTEX AI PARAMETERS
- Model: imagegeneration@006 (Gemini Imagen 3)
- Aspect Ratio: 2:3
- Output Format: PNG
- Safety Filters: Automatic (content-appropriate)

QUALITY NOTES
- Gemini excels with narrative description
- "Professional manga-style illustration of..." establishes clear intent
- Specific character details ensure consistent appearance
- Environmental details prevent blank backgrounds
- Quality markers ("award-winning", "professional") guide output quality
- Gemini interprets artistic style well from description

GEMINI STRENGTHS FOR THIS PROMPT
- Natural language understanding of manga aesthetics
- Excellent character detail rendering
- Strong linework and clarity
- Good at expressive facial features
- Professional quality consistent
- Maintains coherent composition

ITERATION SUGGESTIONS
1. If character appearance varies: Add more specific details (clothing color, accessories)
2. If background is generic: Describe specific environmental features
3. If action is unclear: Use more action-specific verbs ("mid-punch", "striking", "defending")
4. For different mood: Adjust lighting description ("dramatic shadows", "warm lighting")
5. For style variation: Try different manga substyles ("shoujo manga" vs "seinen manga")

TEXT-IN-IMAGE (Not needed for this example)
If text required, Gemini excels at rendering text. See text examples below.

NEXT STEPS
1. Copy optimized prompt above
2. Go to Google Vertex AI or Gemini API
3. Set aspect ratio to 2:3
4. Paste prompt and generate
5. Review output quality
6. Iterate if needed using suggestions above

RELATED STYLES TO TRY
- Shounen manga: For action-focused warriors
- Seinen manga: For more realistic, mature art
- Shoujo manga: For romantic character focus with sparkles
- Professional anime illustration: For animation-style appearance
```

### Example 2: Western Comic Superhero with Text

```
/prompt-gemini western comic superhero in action text:true
```

**Returns**:
```
STYLE ANALYSIS
- Style: Western Comics (American superhero comic book aesthetic)
- Gemini Approach: Natural description with comic book vocabulary
- Text Rendering: Gemini's strength - excellent text rendering capability
- Key Elements: Bold outlines, vibrant colors, dramatic composition, speech bubbles

OPTIMIZED PROMPT FOR GEMINI
A dynamic comic book illustration of a superhero character in a dramatic action pose,
flying through a cityscape at sunset. The character wears a vibrant blue suit with
red accents and a flowing cape, muscles tensed in heroic stance. The background
shows a downtown city skyline with tall skyscrapers illuminated by golden sunset
light. A speech bubble near the character contains the text "I'll protect them!"
with clear, bold lettering. The artwork features professional comic book style with
thick black ink outlines defining all edges, vibrant saturated colors creating
energy, dramatic low-angle perspective emphasizing heroism, and professional comic
book illustration quality. The style references classic American superhero comics
with bold graphic design and dynamic composition. Highly detailed, sharp focus,
masterpiece-quality comic book art.

TEXT RENDERING SPECIFICATIONS
- Text Content: "I'll protect them!"
- Placement: Speech bubble (positioned near character's mouth area)
- Visibility: Clear, readable text (most important)
- Style: Bold letters, white text on dark bubble background
- Gemini's Text Strength: Gemini renders actual readable text very reliably

TEXT BUBBLE STYLING (Optional Details)
- Shape: Standard rounded speech bubble
- Border: Black outline
- Tail: Points toward character's mouth
- Background: White or light color
- Text Color: Black for strong contrast

ASPECT RATIO RECOMMENDATION
- Default: 2:3 (vertical comic panel)
- Alternative: 16:9 (widescreen dramatic scene)
- Alternative: 1:1 (squared panel composition)

VERTEX AI PARAMETERS
- Model: imagegeneration@006
- Aspect Ratio: 2:3
- Output Format: PNG
- Text Rendering: Included in prompt (Gemini handles naturally)

QUALITY NOTES
- Gemini's text rendering is best-in-class among AI image generators
- Explicit text specifications improve clarity
- "Speech bubble containing the text..." works very well
- Gemini interprets comic book style well
- Bold outline description ensures ink-line appearance
- Character positioning clear for consistent output

GEMINI TEXT RENDERING ADVANTAGES
- Actual readable text (vs other platforms that struggle)
- Accurate character matching
- Proper bubble placement
- Font style interpretation
- Text-heavy compositions possible

COMMON TEXT RENDERING EXAMPLES
- Comic panels with dialogue: "Speech bubble says '[text]'"
- Captions: "Caption box at bottom reads '[text]'"
- Sound effects: "Large bold letters spell 'BOOM!' with motion lines"
- Signs/storefronts: "Store sign reads '[business name]'"
- Thought bubbles: "Thought bubble shows '[character's thoughts]'"

IF TEXT NOT RENDERING PERFECTLY
- Retry with simpler text (shorter phrases)
- Use different text placement description
- Try different bubble style description
- Simplify other scene elements
- Increase focus on text in prompt

NEXT STEPS
1. Copy optimized prompt above
2. Access Google Vertex AI or Gemini API
3. Set aspect ratio to 2:3
4. Paste prompt and generate
5. Verify text is readable
6. If text needs adjustment, iterate with new prompt

ITERATION SUGGESTIONS
1. Different dialogue: Replace "[I'll protect them!]" with other text
2. Different character: Describe different superhero appearance
3. Different setting: Change "downtown city" to "space station", "mountain peak", etc.
4. Different mood: Try "dark stormy weather" instead of "sunset"
5. Additional text: Add second speech bubble or caption box

RELATED STYLES
- DC Comics style
- Marvel Comics style
- Golden Age Comics (1940s aesthetic)
- Modern indie comics
- Manga-western fusion
```

### Example 3: Photorealistic Character Design Reference

```
/prompt-gemini photorealistic character design reference photorealism:true
```

**Returns**:
```
STYLE ANALYSIS
- Style: Photorealistic (photography-like quality)
- Gemini Approach: Detailed natural language with photographic vocabulary
- Use Case: Character design reference, concept art, photoshoot aesthetic
- Key Elements: Realistic lighting, detailed textures, professional photography quality

OPTIMIZED PROMPT FOR GEMINI
A professional photorealistic character portrait of a skilled assassin character
with intense dark eyes, sharp jawline, and weathered features showing years of
experience. The character has black shoulder-length hair and wears dark tactical
clothing with subtle armor plating visible. The portrait is shot in studio lighting
with professional photography technique, using three-point lighting to create
dramatic shadows emphasizing character features. The background is softly blurred
with dark tones, keeping focus on the character. The photography style is cinematic
and professional, comparable to high-end movie character design reference photography.
The skin has realistic texture with natural imperfections, the eyes have depth and
intensity, and the overall image has film photography quality with warm color grading.
Sharp focus on face, highly detailed, professional photography quality, 8k resolution,
studio portrait lighting, cinematography-grade image quality.

PHOTOREALISM SPECIFICATIONS
- Photography Type: Studio portrait
- Lighting: Three-point professional lighting
- Lens: 85mm (ideal for portraits, flatters features)
- Depth of Field: Shallow (background blurred)
- Color Grading: Warm, cinematic tones
- Resolution: 8k quality (for detail)

ASPECT RATIO RECOMMENDATION
- Default: 1:1 (square portrait, professional standard)
- Alternative: 9:16 (vertical portrait)
- Alternative: 4:5 (Instagram portrait)

VERTEX AI PARAMETERS
- Model: imagegeneration@006
- Aspect Ratio: 1:1
- Output Format: PNG
- Photorealism Focus: Natural language emphasizes photographic quality

QUALITY NOTES
- Gemini excels at photorealistic rendering
- Detailed lighting description improves results
- Photography vocabulary (studio, three-point, 85mm) enhances quality
- Character details ensure consistent appearance
- Professional quality markers guide output
- 8k resolution request ensures detail

GEMINI PHOTOREALISM STRENGTHS
- Realistic lighting and shadows
- Natural skin texture
- Professional photography quality
- Detailed facial features
- Consistent lighting across image
- Film photography aesthetic achievable

LIGHTING TECHNIQUES FOR PHOTOREALISM
- Three-point lighting: Key light, fill light, back light (professional standard)
- Golden hour: Warm sunset lighting (flattering, natural)
- Studio lighting: Controlled, even, professional
- Dramatic lighting: High contrast shadows (for character/mood)
- Soft lighting: Diffused, flattering (for portraits)
- Rim lighting: Backlighting to separate subject from background

PHOTOGRAPHY VOCABULARY FOR PROMPTS
- Studio portrait: Professional controlled environment
- 35mm, 50mm, 85mm: Lens focal lengths (85mm best for portraits)
- Shallow depth of field: Blurred background
- Bokeh: Blurred background circles (aesthetic)
- RAW image quality: Maximum detail capture
- Color grading: Post-processing tone adjustment
- Cinematography: Film-quality appearance
- HDR photography: High detail in shadows and highlights

USING FOR CHARACTER DESIGN
- Generate reference images for character artists
- Create consistent appearance guidelines
- Develop character backstory through appearance
- Professional pitch-worthy quality
- Game dev character reference

NEXT STEPS
1. Copy optimized prompt above
2. Access Google Vertex AI or Gemini API
3. Set aspect ratio to 1:1 (square)
4. Paste prompt and generate
5. Use as character reference for illustration or other platforms
6. Iterate for character design variations

ITERATION SUGGESTIONS
1. Different character type: "warrior" → "diplomat", "scientist", "leader"
2. Different appearance: Modify hair, clothing, accessories
3. Different lighting mood: "dramatic shadows" → "soft warm", "cool blue", "neon"
4. Different settings: "studio" → "outdoor", "industrial", "mansion"
5. Different photography style: "professional portrait" → "paparazzi candid", "action shot"

RELATED USES
- Concept art reference
- Game character design
- Movie casting reference
- Novel character visualization
- Animation character model
- Costume design reference
```

## Tips for Best Results

### 1. Use Natural, Narrative Language
- Write like describing to an artist
- Use complete sentences when possible
- Avoid technical syntax (tags, weights, flags)
- Descriptive adjectives work better than single tags

### 2. Make Implicit Details Explicit
- Specify lighting direction and quality
- Describe camera angle and perspective
- Include environmental context
- Mention mood and atmosphere

### 3. Art Style Description
- Use specific style names: "manga-style", "photorealistic", "watercolor"
- Reference artists: "in the style of [artist name]"
- Mention art movements: "Art Deco", "Surrealism"
- Describe aesthetic: "professional quality", "masterpiece", "highly detailed"

### 4. Character Descriptions
- Include appearance details (hair, clothing, build)
- Describe expression and mood
- Specify pose or action
- Include distinctive features

### 5. Lighting Specifications
- Quality: "soft lighting", "harsh shadows", "dramatic"
- Direction: "backlighting", "rim lighting", "side lighting"
- Time of day: "golden hour", "sunset", "twilight", "midday"
- Color: "warm golden tones", "cool blue", "neon glow"

### 6. Text-in-Image Success
- Be explicit: "speech bubble containing [exact text]"
- Specify placement: "near character's mouth", "bottom of image"
- Keep text short: Longer text is harder to render accurately
- Consider alternatives: Captions, thought bubbles, signs

## Text-in-Image Examples

```
Example 1 - Speech Bubble:
"A comic panel with character speaking, speech bubble saying 'Watch out!'"

Example 2 - Caption Box:
"An illustration with caption box at bottom reading 'Five years later...'"

Example 3 - Sound Effects:
"An action scene with large bold letters spelling 'CRASH!' with impact lines"

Example 4 - Store Sign:
"A street scene with storefront sign reading 'Joe's Coffee Shop'"

Example 5 - Thought Bubble:
"Character with thought bubble showing 'I must find the truth'"
```

## Aspect Ratios for Different Uses

- **1:1** (Square) - Social media, profile pictures, character portraits
- **9:16** (Vertical) - Mobile, stories, webtoons
- **16:9** (Horizontal) - Widescreen, landscape scenes, cover art
- **2:3** (Portrait) - Comic panels, character art, traditional portrait
- **3:2** (Landscape) - Horizontal panels, wide scenes, panoramic

## Related Commands

- `/convert-prompt [source] gemini [prompt]` - Convert from other platforms to Gemini
- `/prompt-midjourney` - Generate Midjourney prompts
- `/prompt-comfyui` - Generate ComfyUI prompts
- `/prompt-firefly` - Generate Firefly prompts

## See Also

- **Agent**: `gemini-expert.md` - Full expert profile
- **Documentation**: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/gemini/01-gemini-imagen-fundamentals.md`
- **Style Library Skill**: `/style-library/SKILL.md` - Browse all 50+ styles

## Gemini Strengths Summary

- Excellent natural language understanding
- Best-in-class text rendering in images
- Photorealistic output quality
- Good at detailed environments
- Reliable character consistency
- Professional quality consistent
- Great for concept art and references

## Gemini Limitations

- No character consistency across multiple images (use conversation mode)
- No style reference codes (describe style instead)
- Limited extreme art style control (vs ComfyUI)
- No emphasis/weight notation
- No negative prompts (safety built-in)

---

**Command Version**: 1.0.0
**Agent**: gemini-expert
**Last Updated**: January 2025
