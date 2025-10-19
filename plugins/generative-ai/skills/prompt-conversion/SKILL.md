# Prompt Conversion Skill

## Overview

Converts AI image generation prompts between Midjourney, ComfyUI, Gemini, and Adobe Firefly platforms while preserving intent and optimizing for target platform strengths.

## When to Use This Skill

### Primary Use Cases
1. **Cross-platform testing** - Generate same concept in multiple platforms
2. **Workflow migration** - Switch from one platform to another
3. **Batch conversion** - Convert multiple prompts at once
4. **Optimization exploration** - Try same concept across platforms
5. **Team collaboration** - Share prompts across teams using different platforms
6. **Production workflows** - Concept in Firefly, production in ComfyUI
7. **Quality comparison** - Compare outputs between platforms

### Specific Scenarios
- "I have a Midjourney prompt I want to try in ComfyUI"
- "Convert my ComfyUI setup to Firefly for speed"
- "Create Gemini version for photorealistic comparison"
- "Need this prompt in all 4 platforms"
- "Switch from Midjourney to ComfyUI for consistency"

## How It Works

### Step 1: Concept Extraction
Breaks down source prompt into universal elements:
- Subject (character, scene, object)
- Action/pose
- Environment/background
- Lighting and mood
- Style and aesthetic
- Technical parameters
- Quality requirements

### Step 2: Platform Analysis
Assesses source and target platforms:
- Syntax differences
- Feature capabilities
- Conversion feasibility
- Quality trade-offs
- Optimal settings

### Step 3: Intelligent Transformation
Converts to target platform:
- Restructures syntax
- Maps equivalent features
- Adds platform-specific optimizations
- Preserves creative intent
- Maximizes quality potential

### Step 4: Optimization
Tailors for target platform:
- Recommends parameters/settings
- Suggests LoRAs or filters
- Adjusts prompts for platform strengths
- Provides quality guidance

## Progressive Disclosure

### Level 1: Quick Conversion
**Best for**: Standard concepts, quick exploration

Returns:
- Converted prompt
- Basic parameter recommendations
- Quick quality notes

**Example**:
```
/convert-prompt midjourney comfyui [prompt]
```

### Level 2: Detailed Analysis
**Best for**: Important projects, quality critical

Returns:
- Full source/target analysis
- Concept extraction
- Platform mapping
- Converted prompt with detailed settings
- Trade-off explanation
- Optimization suggestions

**Triggers when**: Complex prompt, special parameters, or user asks for detail

### Level 3: Expert Consultation
**Best for**: Advanced workflows, character consistency, multi-platform strategies

Returns:
- Everything in Level 2, plus:
- Character consistency strategy
- Batch workflow recommendations
- Iteration suggestions
- Comparative analysis
- Production workflow design

**Access**: Ask for "detailed analysis" or ask about specific advanced features

## Platform Conversion Guide

### High-Fidelity Conversions (90%+ quality)
- **Midjourney ↔ Gemini**: Both use natural language
- **ComfyUI ↔ Midjourney**: Similar conceptual structure
- **Any ↔ Any**: For standard concepts without special features

### Moderate-Fidelity (75-90%)
- **Any → Firefly**: Requires condensation but straightforward
- **Advanced features → simpler platform**: Feature loss expected

### Challenging Conversions (60-75%)
- **ComfyUI character consistency → Firefly**: No equivalent features
- **Complex LoRA setup → Midjourney**: Feature gaps
- **Multi-model workflow → single platform**: Architectural differences

## Conversion Matrices

### From Midjourney
```
To ComfyUI:    High fidelity - tags + LoRAs
To Gemini:     High fidelity - expand description
To Firefly:    Moderate - condense significantly
```

### From ComfyUI
```
To Midjourney: High fidelity - prose + parameters
To Gemini:     High fidelity - expand prose
To Firefly:    Moderate - simplify drastically
```

### From Gemini
```
To Midjourney: High fidelity - condense prose
To ComfyUI:    High fidelity - convert to tags
To Firefly:    Moderate - extreme condensation
```

### From Firefly
```
To Midjourney: Moderate - expand to parameters
To ComfyUI:    Moderate - add LoRAs, details
To Gemini:     High fidelity - expand narrative
```

## Common Conversion Patterns

### Pattern 1: Artistic → Technical
**Midjourney/Gemini → ComfyUI**
- Prose → Tags
- Implicit weights → Explicit (word:1.3)
- Style descriptions → LoRA specifications
- Single negative concept → Comprehensive negative prompt

### Pattern 2: Technical → Artistic
**ComfyUI → Midjourney/Gemini**
- Tags → Prose
- LoRAs → Style descriptions
- Weights → Relative emphasis
- Negative → `--no` flags or prose avoidance

### Pattern 3: Detailed → Concise
**Any → Firefly**
- Reduce word count to 30-60
- Remove technical syntax
- Use filters instead of style description
- Keep only essentials

### Pattern 4: Concise → Detailed
**Firefly → Any**
- Expand with more detail
- Add context and environment
- Specify lighting and mood explicitly
- Include quality markers

## Quality Preservation Strategies

### Strategy 1: Feature Mapping
Maps equivalent features across platforms:
- Midjourney SREF codes → ComfyUI LoRAs
- ComfyUI CFG → Midjourney stylization
- Negative prompts → `--no` flags or avoidance language

### Strategy 2: Mood & Atmosphere Transfer
Preserves emotional intent:
- Lighting descriptions travel directly
- Mood vocabulary kept consistent
- Composition descriptions maintained
- Color palettes referenced across platforms

### Strategy 3: Detail Level Adjustment
Accounts for platform verbosity:
- Midjourney: 50-100 words (efficient)
- ComfyUI: 80-200+ tags (detailed)
- Gemini: 50-150 words (narrative)
- Firefly: 30-60 words (concise)

### Strategy 4: Parameter Equivalence
Maps settings across platforms:
- Stylization/CFG Scale equivalence
- Step count recommendations
- Sampler choice guidance
- Resolution/aspect ratio matching

## Troubleshooting Conversions

### Issue: Lost detail or quality
**Solution**: Increase prompt length if converting to verbose platform
**Or**: Ask for "detailed analysis" for platform optimization

### Issue: Feature not available in target
**Solution**: Skill identifies feature gaps and suggests workarounds
**Example**: "ComfyUI character consistency → alternative LoRA approach"

### Issue: Result quality lower than expected
**Solution**: Optimize parameters for target platform
**Or**: Use alternate platform better suited to requirements

### Issue: Conversion seems off
**Solution**: Provide original concept in simpler terms
**Or**: Use "level 2" or "level 3" for expert analysis

## Advanced Use Cases

### Use Case 1: Multi-Platform Comparison
Convert same concept to all 4 platforms:
```
Generate in Midjourney for artistic stylization
Convert to ComfyUI for character consistency
Convert to Gemini for photorealistic comparison
Convert to Firefly for quick exploration
Compare all 4 outputs to understand platform differences
```

### Use Case 2: Production Pipeline
Combine platforms for optimal workflow:
```
Concept: Quick iterations in Firefly (fast)
Refinement: Copy to ComfyUI with InstantID (consistent)
Final: Best result from batch of ComfyUI generations
Polish: Use Photoshop with Firefly Generative Fill
```

### Use Case 3: Character Development
Generate character across platforms:
```
Initial: Firefly for quick concept (batch:5)
Reference: Gemini for photorealistic reference
Production: ComfyUI for consistency across panels
Variations: Midjourney for artistic explorations
```

### Use Case 4: Team Collaboration
Share concepts across teams:
```
Designer uses Midjourney
Programmer needs ComfyUI local setup
Artist prefers Gemini
Marketing needs Firefly commercial safety
Convert between all platforms for team alignment
```

## Integration Points

This skill works with:
- `/prompt-midjourney` - Generate new Midjourney prompts
- `/prompt-comfyui` - Generate new ComfyUI prompts
- `/prompt-gemini` - Generate new Gemini prompts
- `/prompt-firefly` - Generate new Firefly prompts
- `/convert-prompt` - Direct command (primary usage)

## Related Documentation

**Full Conversion Guide**:
`/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/cross-platform/prompt-conversion-guide.md`

**Platform Fundamentals**:
- `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/midjourney/01-midjourney-fundamentals.md`
- `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/comfyui/01-comfyui-fundamentals.md`
- `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/gemini/01-gemini-imagen-fundamentals.md`
- `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/adobe-firefly/01-firefly-fundamentals.md`

**Agent Reference**:
`agents/prompt-converter.md` - Expert conversion agent

## Tips for Best Conversions

1. **Provide complete source prompt** - More context = better conversion
2. **Include source parameters** - Flags and settings enable better mapping
3. **Specify conversion priorities** - Quality vs speed vs cost
4. **Request detailed analysis** for important projects
5. **Test recommendations** - Converted settings are suggestions
6. **Iterate if needed** - Conversions can be refined through feedback
7. **Consider platform strengths** - Choose target for what it does best

## Skill Limitations

This skill:
- Preserves intent, not pixel-perfect reproduction
- Cannot create platform features that don't exist
- May simplify advanced workflows
- Requires source prompt to be provided
- Works best with complete, detailed source prompts

This skill cannot:
- Generate images directly (use individual platform commands)
- Guarantee identical output across platforms (different models)
- Support platforms beyond the 4 supported
- Convert batch workflows automatically (requires analysis)

## Next Steps After Conversion

1. **Review converted prompt** - Ensure it matches your intent
2. **Check parameter recommendations** - Adjust if desired
3. **Generate in target platform** - Try the converted prompt
4. **Compare with original** - Understand platform differences
5. **Iterate** - Refine prompt for target platform if needed
6. **Save successful conversions** - Build your own conversion library

---

**Skill Version**: 1.0.0
**Platforms Supported**: Midjourney, ComfyUI, Gemini, Firefly
**Conversion Paths**: 12 bidirectional (all combinations supported)
**Quality Levels**: Auto-detection + 3 disclosure levels
**Last Updated**: January 2025
