---
description: Assemble segments into vertical video using Remotion composition. Activates comic-assembler agent.
---

Assemble generated segments into final vertical video (1080x1920) using beat composition.

## Usage

```bash
/comic-production:video-assemble [episode-slug] [options]
```

## Arguments

- `episode-slug`: Episode to assemble (uses current directory if not specified)
- `--quality`: Output quality 0-100 (default: 80)
- `--fps`: Frames per second (default: 30)
- `--output`: Custom output path (default: `output/episode.mp4`)
- `--format`: Video format - "mp4" or "webm" (default: "mp4")

## What It Does

1. Loads shotlist and panel segments
2. Composes beats with timing
3. Adds speech bubbles with animations
4. Adds comic effects
5. Renders video with optimized settings
6. Saves to `episodes/{episode}/output/`

## Example

```bash
# Standard assembly
/comic-production:video-assemble episode_02

# High quality MP4
/comic-production:video-assemble episode_02 --quality 95

# WebM format for web
/comic-production:video-assemble episode_02 --format webm

# Custom output path
/comic-production:video-assemble --output custom_episode.mp4
```

## MCP Tools Used

```javascript
// 1. Compose beats into video
await mcp__comic_strip_studio__compose_beats({
  episodeId: "episode_02",
  outputPath: "output/episode_02/episode.mp4",
  fps: 30,
  quality: 80,
  format: "mp4",  // or "webm"
  includeAudio: true  // if audio tracks exist
})

// 2. Render speech bubbles (called automatically)
await mcp__comic_strip_studio__render_speech_bubble({
  episodeId: "episode_02",
  shotId: "S01",
  character: "em",
  text: "Why isn't this working?!",
  bubbleType: "speech",  // or "thought", "shout", "whisper"
  position: { x: 0.5, y: 0.2 },
  tailDirection: "bottom-left"
})

// 3. Render comic effects (called automatically)
await mcp__comic_strip_studio__render_comic_effect({
  episodeId: "episode_02",
  shotId: "S03",
  effectType: "impact",  // or "speed-lines", "emphasis", "action"
  position: { x: 0.7, y: 0.5 },
  intensity: 0.8
})
```

## Quality Settings

**Standard** (quality: 80):
- Resolution: 1080x1920
- Bitrate: Balanced
- Use for: Social media distribution

**High** (quality: 95):
- Resolution: 1080x1920
- Bitrate: High
- Use for: Final master, archival

**Preview** (quality: 60):
- Resolution: 720x1280
- Bitrate: Low
- Use for: Quick review

## Output Formats

**MP4** (default):
- Best compatibility
- Optimized for: TikTok, Instagram Reels, YouTube Shorts
- Fast start enabled (web streaming)

**WebM**:
- Smaller file size
- Best for: Web embedding
- May have limited platform support

## Next Steps

1. Preview video in `output/episode.mp4`
2. Review timing and transitions
3. Distribute to social media platforms
4. Generate artifacts website for stakeholder review
