# /prompt-firefly

Generate concise, commercial-safe Adobe Firefly prompts optimized for quick iterations and professional use.

## Syntax

```
/prompt-firefly [style] [description] [options]
```

## Arguments

- **style** (required): Comic art style or filter-compatible style
  - Examples: "comic book", "manga", "illustration", "concept art"
  - Should be filter-compatible (Firefly has built-in filters)
  - Keep concise (Firefly optimized for brevity)

- **description** (required): Concise scene description
  - Examples: "superhero flying over city", "character in action pose"
  - 20-40 words ideal
  - Focus on essential elements only

- **[options]** (optional):
  - `aspect:1:1` - Square (default)
  - `aspect:9:16` - Vertical portrait
  - `aspect:16:9` - Horizontal landscape
  - `aspect:2:3` - Comic panel portrait
  - `batch:5` - Generate 5 variations
  - `photoshop:true` - Optimize for Photoshop integration
  - `speed:true` - Prioritize fast generation over maximum quality
  - `commercial:true` - Emphasize commercial-safe (default)

## Agent Delegation

Routes to: **firefly-expert** agent

## Output Format

The command returns:

1. **Style Analysis** - Confirms style and filter choice
2. **Concise Prompt** - 30-60 word optimized prompt
3. **Firefly Filter Recommendation** - Which built-in filter to use
4. **Content Type** - Illustration/Photo/3D/Animation selection
5. **Aspect Ratio** - Recommendation for intended use
6. **Commercial Safety Note** - Generated content is commercial-use safe
7. **Quality Notes** - Why this approach works
8. **Adobe Integration** - Photoshop/Express integration guidance
9. **Iteration Suggestions** - How to refine results

## Examples

### Example 1: Comic Book Style Superhero

```
/prompt-firefly comic book superhero in red cape flying over city
```

**Returns**:
```
STYLE ANALYSIS
- Style: Comic Book (American superhero comic aesthetic)
- Filter Recommendation: "Comic Book"
- Approach: Concise natural language, let filter handle styling
- Firefly Advantage: Fast generation, commercial-safe

OPTIMIZED PROMPT (45 words, perfect length)
Superhero in vibrant red cape and blue suit flying dynamically over city skyline.
Sunset backdrop with golden lighting, dramatic action pose. Bold comic book style,
vibrant colors, heroic mood.

FIREFLY FILTER RECOMMENDATION
Filter: "Comic Book"
Why: Applies professional comic book aesthetic automatically
Effect: Bold outlines, vibrant colors, heroic proportions
Result: Professional comic book illustration without styling in prompt

CONTENT TYPE
Recommended: "Illustration"
Why: Matches comic book style better than "Photo"
Alternative: "Digital Art" (similar results)

ASPECT RATIO RECOMMENDATION
Default: 2:3 (vertical comic panel)
Alternatives:
- 1:1 (square for social media)
- 16:9 (widescreen double-page spread)
- 9:16 (mobile/story vertical)

COMMERCIAL SAFETY
- Generated content is 100% commercial-use safe
- Can use in publishing, marketing, web, print
- No copyright concerns
- Firefly content is yours to use
- Perfect for professional comic projects

QUALITY NOTES
- Prompt is optimal 45 words (within 30-60 sweet spot)
- Filter handles style, prompt focuses on content
- Concise descriptions work best with Firefly
- Commercial safety built-in
- Generation is fast (~15-30 seconds typical)

PHOTOSHOP INTEGRATION
If using Firefly in Photoshop:
1. Generate with this prompt
2. Use Generative Fill to expand canvas
3. Use Generative Expand for composition
4. Combine with other Firefly outputs
5. Apply traditional filters and effects

WORKFLOW RECOMMENDATIONS
- Generate 1-2 base variations
- Use Photoshop Generative Fill for touch-ups
- Combine best elements from multiple generations
- Apply color grading for final polish
- Export for print or web

NEXT STEPS
1. Go to firefly.adobe.com
2. Use prompt above
3. Apply "Comic Book" filter
4. Set Content Type to "Illustration"
5. Choose aspect ratio 2:3
6. Generate and review

ITERATION SUGGESTIONS
1. Different character: Replace "superhero in red cape" with other character type
2. Different setting: "city skyline" → "space station", "mountain", "desert"
3. Different mood: "sunset backdrop" → "stormy night", "dawn", "neon-lit"
4. Different action: "flying" → "fighting", "standing heroically", "running"
5. Batch variations: Use batch:5 option to generate 5 versions

SPEED OPTIMIZATION
- Current setup generates in ~15-30 seconds
- Use for quick iterations
- Perfect for concept exploration
- Batch option for exploring variations
- Fast feedback loop for creative work

COMMERCIAL USE EXAMPLES
- Comic book panel generation for indie comics
- Marketing/promotional illustration
- Social media content
- Print publications
- Web illustrations
- Game promotional art
- Book cover concepts
```

### Example 2: Manga Style with Batch Generation

```
/prompt-firefly manga teenage warrior in action pose batch:5 aspect:2:3
```

**Returns**:
```
STYLE ANALYSIS
- Style: Manga (Japanese illustration aesthetic)
- Filter Recommendation: "Manga" or "Anime"
- Batch Generation: 5 variations for exploration
- Aspect Ratio: 2:3 (vertical, perfect for comic panels)

OPTIMIZED PROMPT (38 words)
Teenage warrior with spiky hair in dynamic fighting stance, intense expression.
Traditional manga art style, speed lines around character. Ancient temple background,
professional manga illustration.

FIREFLY FILTER RECOMMENDATION
Primary Filter: "Manga"
Alternative Filters: "Anime", "Illustration"
Why Manga Filter:
- Emphasizes clean linework
- Brings expressive character design
- Matches manga aesthetic perfectly
- Faster than manual description

CONTENT TYPE
Recommended: "Illustration"
Why: Best for comic/manga style
Alternative: "Animation" (more stylized appearance)

BATCH GENERATION SETUP
Number of Variations: 5
Why Batch Mode:
- Explore multiple character poses
- Test different expression variations
- Quick iteration without regenerating
- Compare results side-by-side
- Choose best for final use

ASPECT RATIO
Selected: 2:3 (vertical portrait)
Perfect For: Comic panels, webtoons, character illustration
Generation: 5 images at 2:3 ratio

COMMERCIAL SAFETY (Batch Mode)
- All 5 variations commercial-safe
- Choose best version for publication
- No licensing concerns
- Perfect for indie manga projects
- Professional quality consistent

GENERATION TIME (Batch)
- Typical: ~30-60 seconds for 5 images
- Fast feedback loop
- Explore variations quickly
- Commercial-grade output

RESULTS EVALUATION
After batch generation, compare:
1. Facial expression: Which conveys intended emotion?
2. Pose: Which action is clearest and most dynamic?
3. Background: Which environmental detail works best?
4. Overall style: Which matches manga aesthetic best?
5. Quality: Which has fewest artifacts?

SELECTION STRATEGY
- Generate batch of 5
- Select 2-3 best results
- Combine in Photoshop if needed
- Use strongest for final output
- Can regenerate similar variations with slight prompt tweaks

PHOTOSHOP INTEGRATION (Batch)
1. Generate 5 variations
2. Open best version in Photoshop
3. Use Generative Fill for touch-ups
4. Use Generative Expand for composition
5. Combine elements from other batch images

NEXT STEPS
1. Go to firefly.adobe.com
2. Use prompt above
3. Select "Manga" filter
4. Set to batch mode (5 variations)
5. Choose 2:3 aspect ratio
6. Generate and compare
7. Select best result
8. Optional: Refine in Photoshop

ITERATION SUGGESTIONS FOR BATCH
1. Different pose variations:
   - Batch 1: "fighting stance"
   - Batch 2: "standing heroically"
   - Batch 3: "running toward camera"
   - Compare all variations

2. Different character:
   - Keep same pose, vary character description
   - Explore different character archetypes
   - Build character development options

3. Different settings:
   - Same character, different backgrounds
   - Ancient temple → modern city → fantasy castle
   - Test background effectiveness

4. Different moods:
   - Same pose, vary emotional descriptor
   - "intense" → "confident", "uncertain", "determined"
   - Explore character personality

SPEED ADVANTAGE
- 5 variations in ~45 seconds
- Much faster than generating individually
- Perfect for rapid exploration
- Ideal for creative brainstorming
- Commercial-safe all variations

COMMERCIAL USE FOR BATCH
- Select best from 5 for publication
- Use others as backup alternatives
- Can publish multiple variations as character sheets
- Perfect for game character development
- Manga/comic panel production acceleration

NEXT BATCH VARIATIONS
After reviewing first batch:
- Regenerate with slight prompt tweaks
- Explore different character types
- Test different environmental details
- Build up asset library
- Combine best results in Photoshop
```

### Example 3: Concept Art for Game Design

```
/prompt-firefly concept art sci-fi character design photoshop:true
```

**Returns**:
```
STYLE ANALYSIS
- Style: Concept Art (Professional game/film development illustration)
- Filter Recommendation: "Concept Art" or "Illustration"
- Photoshop Integration: Optimized for Adobe workflow
- Firefly Advantage: Fast concept iteration, commercial-safe

OPTIMIZED PROMPT (42 words)
Sci-fi character with advanced armor, cybernetic enhancements, and tactical gear.
Blue and silver color scheme, confident stance. Professional concept art illustration,
polished design, high-resolution quality.

FIREFLY FILTER RECOMMENDATION
Filter: "Concept Art"
Alternative: "Illustration" or "Digital Art"
Why Concept Art Filter:
- Professional game development style
- Polished appearance for presentations
- Appropriate for concept documentation
- Technical accuracy emphasized
- Commercial client-ready quality

CONTENT TYPE
Recommended: "Illustration"
Why: Matches concept art aesthetic
Alternative: "Digital Art" (similar professional quality)

ASPECT RATIO
Default: 1:1 (square, professional standard)
Alternative: 4:5 (vertical for character portfolio)

COMMERCIAL SAFETY
- Concept art is 100% commercial-safe
- Use directly in game development presentations
- No licensing concerns
- Perfect for professional portfolio
- Client-ready quality

PHOTOSHOP INTEGRATION WORKFLOW
Step 1: Generate with Firefly
- Use prompt above
- Generate concept art illustration

Step 2: Generative Fill (Refinement)
- Open in Photoshop
- Use Generative Fill to fix areas
- Touch up armor details if needed
- Refine weapon design
- Adjust proportions if desired

Step 3: Generative Expand (Composition)
- Expand canvas for final composition
- Add context around character
- Show full environment integration
- Create more dramatic framing

Step 4: Traditional Editing
- Apply color grading for mood
- Add lighting effects
- Composite multiple Firefly outputs
- Create final presentation piece

Step 5: Export
- Save at high resolution
- Export for presentation
- Include in design documentation
- Use as development reference

GAME DEVELOPMENT WORKFLOW
1. Concept brainstorm: Generate 3-5 character concepts with Firefly
2. Iteration: Refine in Photoshop with Generative Fill
3. Expansion: Add environment context with Generative Expand
4. Polishing: Color grading and effects
5. Documentation: Create final concept art package

NEXT STEPS
1. Go to firefly.adobe.com
2. Use prompt above
3. Apply "Concept Art" filter
4. Set Content Type to "Illustration"
5. Generate concept design
6. Open in Photoshop
7. Refine with Generative Fill/Expand
8. Export for game development use

ITERATION SUGGESTIONS
1. Different character class: "warrior", "mage", "rogue"
2. Different faction: "corporate", "military", "rebellion"
3. Different era: "near-future", "far-future", "post-apocalyptic"
4. Different aesthetic: "sleek and clean" vs "worn and combat-damaged"
5. Different stance: "ready for combat" vs "relaxed" vs "dramatic"

SPEED FOR GAME DEVELOPMENT
- Concept generation: ~20 seconds
- Batch variations: ~45 seconds
- Photoshop refinement: ~5-10 minutes
- Total workflow: <1 hour for polished concept
- Fast iteration for design decisions

COMMERCIAL PRODUCTION WORKFLOW
Perfect For:
- Game character design
- Film/TV concept art
- Animation character development
- Comic character concepts
- Illustration client work
- Marketing illustrations

Professional Quality:
- Client-presentation ready
- Portfolio quality
- Professional aesthetic
- Commercial-safe by default
- No licensing concerns

BATCH GENERATION FOR CONCEPTS
Use batch:5 to generate 5 character concepts:
- Explore different designs
- Compare aesthetic approaches
- Build out character lineup
- Present options to team/client
- Select best for development

COMMERCIAL USE CONFIRMATION
- All generated concepts are yours
- Can use in professional projects
- No copyright restrictions
- Firefly ownership: You own all outputs
- Perfect for commercial game/film production
```

## Tips for Best Results

### 1. Keep Prompts Concise
- **Target**: 30-60 words
- **Too short** (<20 words): Vague results
- **Too long** (>80 words): Firefly less effective
- **Sweet spot**: 40-50 words optimal

### 2. Focus on Essentials Only
- Main subject
- Key action or pose
- Primary setting
- One style/mood descriptor
- Don't describe style in text if using filter

### 3. Use Filters Instead of Description
- Say "comic book style" in filter, not prompt
- Let filter handle "manga look"
- Describe content, let filter handle aesthetics
- This is Firefly's unique strength

### 4. Plain Language Works Best
- No technical syntax (no parentheses, no weights)
- Natural English phrasing
- Descriptive adjectives fine
- Simple is better than complex

### 5. Content Type Strategy
- **Illustration**: For comic, art, graphic styles (default)
- **Photo**: For realistic, photography styles
- **3D**: For computer-generated appearance
- **Animation**: For animated, cartoon styles

### 6. Batch Generation for Exploration
- Use `batch:5` to generate 5 variations
- Compare and select best
- Fast exploration of concepts
- 5 times faster than individual generations

## Firefly Filters Reference

- **Comic Book** - Bold outlines, vibrant colors
- **Manga** - Clean linework, expressive style
- **Anime** - Animation aesthetic
- **Illustration** - Painted, artistic appearance (default)
- **Digital Art** - Modern digital painting
- **Concept Art** - Professional game/film concept
- **3D Render** - Computer-generated appearance
- **Watercolor** - Watercolor painting style
- **Oil Painting** - Traditional oil painting
- **Sketch** - Drawing, sketch appearance
- **Photograph** - Photography aesthetic
- **Cel-Shading** - Animated appearance
- **Pixel Art** - Retro pixel style
- **Abstract** - Non-representational art

## Adobe Integration Advantages

- **Photoshop**: Generative Fill, Expand, direct access
- **Express**: Quick web-based generation
- **Firefly API**: Custom integrations for workflows
- **Creative Cloud**: Seamless workflow with other tools
- **Batch Processing**: Generate multiple at once

## Related Commands

- `/convert-prompt [source] firefly [prompt]` - Convert from other platforms to Firefly
- `/prompt-midjourney` - Generate Midjourney prompts
- `/prompt-comfyui` - Generate ComfyUI prompts
- `/prompt-gemini` - Generate Gemini prompts

## See Also

- **Agent**: `firefly-expert.md` - Full expert profile
- **Documentation**: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/adobe-firefly/01-firefly-fundamentals.md`
- **Style Library Skill**: `/style-library/SKILL.md` - Browse all 50+ styles

## Firefly Advantages Summary

- **Speed**: Fastest generation (15-30 seconds typical)
- **Commercial Safety**: 100% commercial-safe by default
- **Simplicity**: Easiest learning curve
- **Adobe Integration**: Works in Photoshop, Creative Suite
- **Batch Generation**: Generate 5 at once for quick exploration
- **Cost**: No copyright concerns, licensed for commercial use

## When to Use Firefly

1. **Commercial projects** - Need license-free usage
2. **Quick iterations** - Fast feedback loop needed
3. **Adobe workflow** - Already using Creative Suite
4. **Batch exploration** - Testing multiple concepts
5. **Client work** - Professional, safe content
6. **Social media** - Quick content generation
7. **Photoshop integration** - Inpainting/expansion needed

## When to Use Other Platforms

- **Ultimate quality**: Use Gemini or FLUX
- **Maximum control**: Use ComfyUI
- **Artistic stylization**: Use Midjourney
- **Character consistency**: Use ComfyUI with InstantID

---

**Command Version**: 1.0.0
**Agent**: firefly-expert
**Last Updated**: January 2025
