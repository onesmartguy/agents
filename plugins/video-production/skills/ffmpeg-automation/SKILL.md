---
name: ffmpeg-automation
description: FFmpeg command patterns, batch processing, web optimization, and automation scripts for video processing pipelines. Use when processing videos at scale, optimizing for web delivery, or building automated workflows.
---

# FFmpeg Automation

## Web Optimization (Critical)

```bash
# faststart flag - enables streaming before full download
ffmpeg -i input.mp4 -c copy -movflags +faststart output.mp4

# Complete web optimization
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k -movflags +faststart output.mp4
```

## Always Specify Codec

```bash
# GOOD: Explicit codec
ffmpeg -i input.mov -c:v libx264 -c:a aac output.mp4

# AVOID: Implicit codec
ffmpeg -i input.mov output.mp4
```

## Trimming (No Quality Loss)

```bash
# Fast, no re-encoding
ffmpeg -ss 00:00:10 -i input.mp4 -t 00:00:30 -c copy output.mp4
```

## Batch Processing

```python
import subprocess
from pathlib import Path

for video in Path('/input').glob('*.mp4'):
    subprocess.run([
        'ffmpeg', '-i', str(video),
        '-c:v', 'libx264', '-crf', '23',
        '-movflags', '+faststart',
        f'/output/{video.stem}_processed.mp4'
    ])
```

## Quality Presets

```bash
# High (archival): CRF 18
# Balanced (default): CRF 23
# Fast/smaller: CRF 28
# CRF scale: 0 (lossless) to 51 (worst)
```

## Resources

- https://ffmpeg.org/documentation.html
- https://github.com/rendi-api/ffmpeg-cheatsheet
