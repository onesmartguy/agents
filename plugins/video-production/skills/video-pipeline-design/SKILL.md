---
name: video-pipeline-design
description: End-to-end video pipeline architecture from content creation to distribution, including cloud processing, CDN integration, and multi-platform delivery. Use when designing scalable video systems or building automated content workflows.
---

# Video Pipeline Design

## Serverless Pipeline Pattern

```
Upload → S3 → Lambda → FFmpeg → Output S3 → CDN → Purge Cache
```

## Remotion + FFmpeg Hybrid

```
Data API → Remotion Render → FFmpeg Optimize → Multi-Platform Distribution
```

## CI/CD with CDN Auto-Purge

```yaml
# GitHub Actions
- name: Upload to S3
  run: aws s3 sync ./dist s3://video-bucket/

- name: Purge CDN
  run: |
    curl -X POST https://api.cdn.com/purge \
      -H "Authorization: Bearer $TOKEN" \
      -d '{"files": ["https://cdn.example.com/*"]}'
```

## Multi-Platform Distribution

```javascript
async function distribute(video, metadata) {
  const [youtube, instagram, tiktok] = await Promise.all([
    optimizeForPlatform(video, 'youtube'),   // 1920x1080
    optimizeForPlatform(video, 'instagram'), // 1080x1080
    optimizeForPlatform(video, 'tiktok')     // 1080x1920
  ])

  await Promise.all([
    uploadToYouTube(youtube, metadata),
    uploadToInstagram(instagram, metadata),
    uploadToTikTok(tiktok, metadata)
  ])
}
```

## Best Practices

1. Event-driven (S3 triggers, not polling)
2. Idempotent operations (safe retries)
3. Parallel processing when possible
4. CDN integration with auto-purge
5. Monitoring and error handling
6. Cost optimization (spot instances, caching)

## Resources

- AWS Media Services
- Remotion Lambda
- CloudFlare Stream
