---
name: serverless-video-processing
description: Serverless video processing with AWS Lambda, S3 triggers, cloud functions, and event-driven architectures. Use when building scalable cloud video pipelines or implementing automated processing workflows.
---

# Serverless Video Processing

## AWS Lambda Pattern

```javascript
// S3 trigger → Lambda → Process → Upload
exports.handler = async (event) => {
  const { bucket, key } = event.Records[0].s3

  // Download
  const input = await downloadFromS3(bucket, key)

  // Process with FFmpeg (Lambda Layer)
  const output = await processVideo(input)

  // Upload
  await uploadToS3(output, outputBucket)

  // Purge CDN
  await purgeCDN(`https://cdn.example.com/${key}`)
}
```

## Google Cloud Functions

```javascript
exports.processVideo = async (file, context) => {
  const bucket = file.bucket
  const name = file.name

  // Download from Cloud Storage
  await bucket.file(name).download({ destination: '/tmp/input.mp4' })

  // Process
  await ffmpegProcess('/tmp/input.mp4', '/tmp/output.mp4')

  // Upload
  await bucket.upload('/tmp/output.mp4')
}
```

## Error Handling & Retries

```javascript
async function processWithRetry(video, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await processVideo(video)
    } catch (error) {
      if (i === maxRetries - 1) throw error
      await sleep(Math.pow(2, i) * 1000)  // Exponential backoff
    }
  }
}
```

## Cost Optimization

- Use spot instances for batch jobs
- Right-size Lambda memory (1769MB for FFmpeg)
- Cache intermediate results in S3
- Set lifecycle policies (move to Glacier after 90 days)

## Monitoring

```javascript
import { CloudWatch } from 'aws-sdk'

await cloudwatch.putMetricData({
  Namespace: 'VideoPipeline',
  MetricData: [{
    MetricName: 'ProcessingTime',
    Value: duration,
    Unit: 'Seconds'
  }]
})
```

## Best Practices

1. Event-driven triggers (not polling)
2. Timeout handling (Lambda 15min limit)
3. Memory optimization (FFmpeg needs 1-2GB)
4. Parallel processing with Step Functions
5. Dead letter queues for failures

## Resources

- AWS Lambda Layers (FFmpeg)
- Google Cloud Functions
- Azure Functions
