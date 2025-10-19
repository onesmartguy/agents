---
description: Assemble segments into vertical video episode using Remotion. Activates comic-assembler agent.
---

Assemble generated segments into final vertical video (1080x1920) using Remotion.

## Usage

```bash
/comic-production:video-assemble [episode-slug] [options]
```

## Arguments

- `episode-slug`: Episode to assemble (uses WORKING_EPISODE if not specified)
- `--quality`: Output quality 0-100 (default: 80)
- `--fps`: Frames per second (default: 30)
- `--output`: Custom output path (default: `output/episode.mp4`)
- `--preview`: Generate preview only (lower quality, faster)

## What It Does

1. Loads shotlist and segments
2. Creates Remotion composition
3. Sequences shots with timing
4. Adds speech bubbles with animations
5. Adds comic effects
6. Renders video with FFmpeg
7. Optimizes for web playback
8. Saves to `episodes/{episode}/output/`

## Example

```bash
# Standard assembly
export WORKING_EPISODE=pilot
/comic-production:video-assemble

# High quality
/comic-production:video-assemble episode_02 --quality 95

# Quick preview
/comic-production:video-assemble --preview

# Custom output
/comic-production:video-assemble --output custom_episode.mp4
```

## Quality Settings

**preview** (--preview flag):
- Quality: 60
- Resolution: 720x1280
- Fast encoding
- Use for: Quick review

**standard** (default):
- Quality: 80
- Resolution: 1080x1920
- Balanced encoding
- Use for: Social media

**high** (--quality 95):
- Quality: 95
- Resolution: 1080x1920
- Slow encoding, best quality
- Use for: Final distribution

## Output Formats

Video is optimized for:
- TikTok (1080x1920, 9:16)
- Instagram Reels
- YouTube Shorts
- Web playback (fast start)

## Next Steps

1. Preview video in `output/episode.mp4`
2. Generate artifacts website for review
3. Distribute to social media platforms
