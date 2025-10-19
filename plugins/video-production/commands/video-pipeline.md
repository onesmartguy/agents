---
description: Design and implement an end-to-end video production pipeline with creation, processing, and distribution
---

Design a complete video production pipeline.

## Pipeline Stages

1. **Content Creation** (Remotion or upload)
2. **Processing** (FFmpeg optimization)
3. **Storage** (S3, Cloud Storage)
4. **Distribution** (CDN, social media)

## Architecture Options

**Serverless:**
```
S3 Upload → Lambda → FFmpeg → Output S3 → CDN
```

**Batch Processing:**
```
Cron Job → Database → Generate Videos → Process → Distribute
```

**Real-Time:**
```
API Request → Remotion Render → FFmpeg → Stream to CDN
```

Include:
- Error handling and retries
- Monitoring and logging
- CDN purging automation
- Multi-platform optimization
- Cost optimization strategies
