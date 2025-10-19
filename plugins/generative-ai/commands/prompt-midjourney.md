# /prompt-midjourney

Generate a production-ready Midjourney prompt for any comic art style and description.

## Syntax

```
/prompt-midjourney [style] [description]
```

## Arguments

- **style** (required): Comic art style or artist reference
  - Examples: "shounen manga", "golden age comic", "Jim Lee", "ligne claire", "cyberpunk"
  - Accepts style names from 50+ comic art styles library
  - Or specific artist names and art movements

- **description** (required): Scene or subject description
  - Examples: "warrior in action pose", "superhero flying over city", "detective in noir setting"
  - Can include composition details, mood, setting
  - Should describe what you want to see in the image

## Agent Delegation

Routes to: **midjourney-expert** agent

## Output Format

The command returns:

1. **Analysis** - Confirms style choice and clarifies interpretation
2. **Prompt Generation** - Full `/imagine:` command ready to use
3. **Parameter Recommendations**:
   - `--ar` (aspect ratio)
   - `--s` (stylization level)
   - `--c` (chaos for variation)
   - `--q` (quality)
   - `--v` (version: 7 or 6.1)
   - `--niji` (for anime/manga)
   - Other parameters as relevant

4. **Quality Notes** - Explanation of choices
5. **Variations** - Suggestions for tweaks or alternatives
6. **Style References** - Artist/style information for context

## Examples

### Example 1: Manga Action Scene

```
/prompt-midjourney shounen manga warrior in dynamic fighting stance
```

**Returns**:
```
STYLE ANALYSIS
- Style: Shounen Manga (Young male audience, dynamic action)
- Artist References: Eiichiro Oda (One Piece), Masashi Kishimoto (Naruto)
- Characteristics: Speed lines, energy effects, bold inking, high contrast

GENERATED PROMPT
/imagine: 1male warrior in dynamic fighting stance, intense action pose,
speed lines and motion effects, energy aura glowing, battle atmosphere,
traditional manga inking with bold lines, high contrast black and white,
professional shounen manga style, Masashi Kishimoto influence,
highly detailed, sharp focus, expressive character design
--niji 7 --style expressive --ar 2:3 --s 300 --c 20

PARAMETER RECOMMENDATIONS
- Version: Niji 7 (specialized for manga/anime)
- Style: --style expressive (brings out dramatic manga emotions)
- Aspect Ratio: --ar 2:3 (standard comic panel portrait)
- Stylization: --s 300 (balanced for manga detail)
- Chaos: --c 20 (low for consistency)

QUALITY NOTES
- Niji 7 is optimized for manga aesthetics
- 'expressive' style brings out emotional manga qualities
- 2:3 aspect ideal for vertical comic panels
- Speed lines and energy specified to match shounen conventions

VARIATIONS TO TRY
1. Different pose: "standing with fists raised" instead of "fighting stance"
2. Different setting: "mountain peak" or "urban rooftop"
3. Different mood: More dramatic with "stormy weather" or "night setting"
4. Artist variation: Try different artists (Tite Kubo, Akira Toriyama)

REFERENCE INFORMATION
- Shounen (少年): Manga for young male audience (ages 12-18+)
- Known for: Dynamic action, expressive characters, tournament arcs
- Comparable series: One Piece, Naruto, Bleach, Dragon Ball, My Hero Academia
```

### Example 2: Classic Western Comic

```
/prompt-midjourney golden age comic superhero flying over city
```

**Returns**:
```
STYLE ANALYSIS
- Style: Golden Age Comics (1940s-1950s superhero era)
- Characteristics: Bold outline, saturated colors, heroic poses, dramatic lighting
- Historical Context: Superman, Batman, Wonder Woman era
- Comparable Artists: Jerry Siegel, Bob Kane, Joe Shuster

GENERATED PROMPT
/imagine: superhero character in flowing cape flying over city skyline,
dynamic upward angle, arms positioned heroically, 1940s Golden Age
comic book style, bold black ink outlines, saturated vibrant colors,
dramatic lighting with strong shadows, heroic composition, retro
comic book aesthetic, highly detailed, sharp focus, masterpiece
--ar 2:3 --s 350 --v 7 --q 1

PARAMETER RECOMMENDATIONS
- Version: v7 (main version, best for artistic interpretation)
- Quality: --q 1 (high quality for rendered detail)
- Stylization: --s 350 (bring out comic art aesthetics)
- Aspect Ratio: --ar 2:3 (vertical comic panel)

QUALITY NOTES
- V7 better at understanding Golden Age aesthetic through description
- 'Bold black outlines' triggers ink-line rendering
- 'Saturated vibrant colors' ensures bright, bold palette
- High stylization (350) emphasizes comic art style

VARIATIONS TO TRY
1. Different hero pose: "standing with fists on hips" or "walking determinedly"
2. Different setting: "in battle with villain" or "protecting citizens"
3. Art reference: Add specific artist "in the style of Jerry Siegel"
4. Decade variation: Try Silver Age (1960s), Bronze Age (1970s-80s)

REFERENCE INFORMATION
- Golden Age (1940s-1950s): First era of superhero comics
- Characteristics: Bold, colorful, heroic, dramatic
- Famous Characters: Superman, Batman, Wonder Woman, Flash, Green Lantern
- Visual Style: Thick outlines, saturated colors, dynamic poses
```

### Example 3: Atmospheric Noir Detective

```
/prompt-midjourney film noir detective in rain-soaked alley with neon signs
```

**Returns**:
```
STYLE ANALYSIS
- Style: Film Noir / Crime Comics (Dark Age aesthetic)
- Mood: Mysterious, dangerous, atmospheric
- Lighting: Low-key, high contrast, dramatic shadows
- Comparable Works: Blade Runner, Sin City, Batman noir

GENERATED PROMPT
/imagine: hardened detective in trench coat and fedora standing in
rain-soaked urban alley, neon signs glowing in the distance,
harsh streetlight casting dramatic shadows, film noir atmosphere,
moody dark blues and reds, wet pavement reflecting light,
cinematic composition, low-angle perspective, professional noir comic art,
sharp focus, masterpiece quality, heavily detailed
--ar 16:9 --s 400 --v 7 --q 1

PARAMETER RECOMMENDATIONS
- Aspect Ratio: --ar 16:9 (wider composition for atmospheric scene)
- Stylization: --s 400 (higher for dramatic noir aesthetic)
- Quality: --q 1 (for detailed rendering)
- Version: v7 (best for complex mood)

QUALITY NOTES
- Wider aspect ratio (16:9) allows atmospheric composition
- Specific lighting details trigger noir aesthetic
- "Moody dark blues and reds" ensures color palette
- "Cinematic composition" brings film quality
- Neon elements create tension and atmosphere

VARIATIONS TO TRY
1. Different pose: "sitting at desk" or "walking through rain"
2. Character variation: "femme fatale woman" instead of detective
3. Time shift: "late night" vs "dawn" vs "midnight"
4. Location: "rooftop overlooking city" or "crowded nightclub"
5. Story element: "holding gun" or "with mysterious briefcase"

REFERENCE INFORMATION
- Noir Style: Dark, mysterious, atmospheric
- Origins: 1940s-1950s detective comics and film
- Modern adaptations: Sin City, Batman series, Cyberpunk genre
- Visual Elements: Shadows, neon, rain, fedoras, guns, danger
```

## Tips for Best Results

### 1. Be Specific with Style
- Use exact style name when possible
- Combine styles if desired: "manga meets western comic"
- Reference specific artists or eras
- Examples: "Moebius sci-fi", "1960s Silver Age", "CLAMP shoujo"

### 2. Provide Clear Description
- Include character appearance if important
- Specify action or pose
- Mention setting/environment
- Describe mood and lighting

### 3. Leverage Aspect Ratio
- Comic panels: `--ar 2:3` (vertical portrait)
- Horizontal action: `--ar 16:9` (widescreen)
- Character close-up: `--ar 1:1` (square)
- Vertical video/webtoon: `--ar 9:16`

### 4. Stylization Control
- `--s 150`: Minimal stylization (prompt-literal)
- `--s 250`: Moderate stylization (balanced)
- `--s 400+`: High stylization (very artistic)
- Choose based on how stylized you want output

### 5. Character Consistency
If you have a character reference image:
- Get the URL of your reference image
- Ask for character consistency prompt instead
- Returns prompt with `--cref` flag
- Maintains character appearance across variations

## Related Commands

- `/convert-prompt [source] midjourney [prompt]` - Convert from other platforms to Midjourney
- `/prompt-comfyui` - Generate ComfyUI prompts
- `/prompt-gemini` - Generate Gemini prompts
- `/prompt-firefly` - Generate Firefly prompts

## See Also

- **Agent**: `midjourney-expert.md` - Full expert profile
- **Documentation**: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/midjourney/01-midjourney-fundamentals.md`
- **Styles**: `/Users/eddie.flores/source/ai-comic-strip/docs/prompts/generative-ai/midjourney/02-comic-art-styles.md`
- **Style Library Skill**: `/style-library/SKILL.md` - Browse all 50+ styles

## Quick Reference: Comic Styles

**Manga**: shounen, seinen, shoujo, josei, mecha, chibi, gore
**Western**: golden age, silver age, bronze age, marvel, dc, image, indie
**European**: ligne claire, moebius, franco-belgian, fumetti
**Modern**: webtoon, manhwa, manhua, digital painting, cel-shaded
**Experimental**: minimalist, watercolor, mixed media, collage, abstract

---

**Command Version**: 1.0.0
**Agent**: midjourney-expert
**Last Updated**: January 2025
