---
name: firebase-storage-cdn
description: Firebase Storage for file uploads, Firebase Hosting for CDN delivery, asset optimization, and video/audio distribution strategies. Use when handling media uploads, serving static assets via CDN, or distributing video/audio content at scale.
---

# Firebase Storage & CDN

Comprehensive guide to Firebase Storage for file management and Firebase Hosting for global CDN delivery of static assets, videos, and audio files.

## When to Use This Skill

- Upload and store user-generated content (images, videos, audio)
- Serve static assets via global CDN
- Distribute video/audio content at scale
- Host static websites with custom domains
- Implement file upload/download functionality
- Optimize media delivery performance
- Handle large file uploads with resumable uploads
- Secure file access with authentication
- Deploy static sites automatically via CI/CD

## Firebase Storage

### Setup and Configuration

```bash
# Install Firebase Admin SDK (if not already)
npm install firebase-admin

# Client SDK (for browser uploads)
npm install firebase
```

```typescript
// Initialize Storage
import { initializeApp } from 'firebase-admin/app';
import { getStorage } from 'firebase-admin/storage';

const app = initializeApp();
const storage = getStorage(app);
const bucket = storage.bucket(); // Default bucket
// Or specific bucket:
// const bucket = storage.bucket('my-project.appspot.com');
```

### File Upload Patterns

#### Client-Side Upload (Browser)

```typescript
// Client-side upload with progress
import { getStorage, ref, uploadBytesResumable, getDownloadURL } from 'firebase/storage';

async function uploadFile(file: File, path: string) {
  const storage = getStorage();
  const storageRef = ref(storage, path);

  // Upload with progress tracking
  const uploadTask = uploadBytesResumable(storageRef, file, {
    contentType: file.type,
    customMetadata: {
      uploadedBy: currentUser.uid,
      originalName: file.name
    }
  });

  return new Promise((resolve, reject) => {
    uploadTask.on(
      'state_changed',
      (snapshot) => {
        const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        console.log(`Upload is ${progress}% done`);

        switch (snapshot.state) {
          case 'paused':
            console.log('Upload is paused');
            break;
          case 'running':
            console.log('Upload is running');
            break;
        }
      },
      (error) => {
        // Handle error
        console.error('Upload failed:', error);
        reject(error);
      },
      async () => {
        // Upload complete
        const downloadURL = await getDownloadURL(uploadTask.snapshot.ref);
        console.log('File available at', downloadURL);
        resolve(downloadURL);
      }
    );
  });
}

// Usage
const videoFile = document.querySelector('input[type=file]').files[0];
const downloadURL = await uploadFile(
  videoFile,
  `videos/${userId}/${Date.now()}_${videoFile.name}`
);
```

#### Server-Side Upload

```typescript
// Server-side upload (Admin SDK)
import { getStorage } from 'firebase-admin/storage';

async function uploadFromServer(localFilePath: string, storagePath: string) {
  const bucket = getStorage().bucket();

  await bucket.upload(localFilePath, {
    destination: storagePath,
    metadata: {
      contentType: 'video/mp4',
      cacheControl: 'public, max-age=31536000', // 1 year
      metadata: {
        uploadedAt: new Date().toISOString(),
        processed: 'true'
      }
    }
  });

  // Get public URL
  const file = bucket.file(storagePath);
  await file.makePublic();

  return `https://storage.googleapis.com/${bucket.name}/${storagePath}`;
}

// Usage
const publicURL = await uploadFromServer(
  './episodes/pilot/output/episode.mp4',
  'videos/pilot/episode.mp4'
);
```

### File Download Patterns

```typescript
// Download to local file
async function downloadFile(storagePath: string, localPath: string) {
  const bucket = getStorage().bucket();

  await bucket.file(storagePath).download({
    destination: localPath
  });
}

// Get file as buffer
async function getFileBuffer(storagePath: string): Promise<Buffer> {
  const bucket = getStorage().bucket();
  const [buffer] = await bucket.file(storagePath).download();
  return buffer;
}

// Stream file
async function streamFile(storagePath: string, res: Response) {
  const bucket = getStorage().bucket();
  const file = bucket.file(storagePath);

  const readStream = file.createReadStream();
  readStream.pipe(res);
}
```

### Security Rules

```javascript
// storage.rules
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    // Public read, authenticated write
    match /public/{allPaths=**} {
      allow read;
      allow write: if request.auth != null;
    }

    // User-specific files
    match /users/{userId}/{allPaths=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Episode videos (public read, admin write)
    match /episodes/{episode}/videos/{video} {
      allow read;
      allow write: if request.auth != null && request.auth.token.admin == true;
    }

    // Size limit (50MB)
    match /uploads/{allPaths=**} {
      allow create: if request.resource.size < 50 * 1024 * 1024
                    && request.auth != null;
    }

    // Content type validation
    match /images/{image} {
      allow create: if request.resource.contentType.matches('image/.*')
                    && request.auth != null;
    }

    match /videos/{video} {
      allow create: if request.resource.contentType.matches('video/.*')
                    && request.auth != null;
    }
  }
}
```

### File Management

```typescript
// Delete file
async function deleteFile(storagePath: string) {
  const bucket = getStorage().bucket();
  await bucket.file(storagePath).delete();
}

// List files
async function listFiles(prefix: string) {
  const bucket = getStorage().bucket();
  const [files] = await bucket.getFiles({ prefix });

  return files.map(file => ({
    name: file.name,
    size: file.metadata.size,
    contentType: file.metadata.contentType,
    created: file.metadata.timeCreated,
    updated: file.metadata.updated
  }));
}

// Get file metadata
async function getFileMetadata(storagePath: string) {
  const bucket = getStorage().bucket();
  const file = bucket.file(storagePath);
  const [metadata] = await file.getMetadata();
  return metadata;
}

// Update metadata
async function updateMetadata(storagePath: string, metadata: any) {
  const bucket = getStorage().bucket();
  const file = bucket.file(storagePath);

  await file.setMetadata({
    metadata: {
      ...metadata,
      updatedAt: new Date().toISOString()
    }
  });
}

// Copy file
async function copyFile(sourcePath: string, destPath: string) {
  const bucket = getStorage().bucket();
  const sourceFile = bucket.file(sourcePath);

  await sourceFile.copy(destPath);
}

// Move file (copy + delete)
async function moveFile(sourcePath: string, destPath: string) {
  await copyFile(sourcePath, destPath);
  await deleteFile(sourcePath);
}
```

## Firebase Hosting

### Setup

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login
firebase login

# Initialize hosting
firebase init hosting
```

### firebase.json Configuration

```json
{
  "hosting": {
    "public": "dist",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],

    // Rewrites (SPA routing)
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ],

    // Headers for caching and security
    "headers": [
      {
        "source": "**/*.@(jpg|jpeg|gif|png|webp|svg)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000, immutable"
          }
        ]
      },
      {
        "source": "**/*.@(mp4|webm|ogg)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000, immutable"
          }
        ]
      },
      {
        "source": "**/*.@(js|css)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000, immutable"
          }
        ]
      },
      {
        "source": "**/*.html",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=0, must-revalidate"
          }
        ]
      }
    ],

    // Redirects
    "redirects": [
      {
        "source": "/old-page",
        "destination": "/new-page",
        "type": 301
      }
    ],

    // Clean URLs
    "cleanUrls": true,

    // Trailing slash
    "trailingSlash": false
  }
}
```

### Deployment

```bash
# Deploy to default site
firebase deploy --only hosting

# Deploy to specific site (multi-site)
firebase deploy --only hosting:app

# Deploy with specific version
firebase deploy --only hosting -m "Deployment message"

# Preview before deploy
firebase hosting:channel:deploy preview

# Rollback to previous version
firebase hosting:channel:delete preview
```

### CI/CD Deployment

```yaml
# .github/workflows/deploy.yml
name: Deploy to Firebase Hosting

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Deploy to Firebase
        uses: FirebaseExtended/action-hosting-deploy@v0
        with:
          repoToken: '${{ secrets.GITHUB_TOKEN }}'
          firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
          channelId: live
          projectId: my-project
```

## Video/Audio Distribution Strategies

### Video Optimization Workflow

```typescript
// 1. Upload original video to Storage
async function uploadVideo(videoPath: string, episodeId: string) {
  const bucket = getStorage().bucket();

  // Upload original
  await bucket.upload(videoPath, {
    destination: `videos/${episodeId}/original.mp4`,
    metadata: {
      contentType: 'video/mp4',
      metadata: {
        episodeId,
        processed: 'false'
      }
    }
  });

  // Trigger Cloud Function for processing
  // (See Cloud Functions for transcoding)
}

// 2. Serve optimized video via CDN
async function getVideoURL(episodeId: string, quality: string = '1080p') {
  const bucket = getStorage().bucket();
  const file = bucket.file(`videos/${episodeId}/${quality}.mp4`);

  // Generate signed URL (expires in 1 hour)
  const [url] = await file.getSignedUrl({
    version: 'v4',
    action: 'read',
    expires: Date.now() + 3600 * 1000
  });

  return url;

  // Or make public and use direct URL:
  // await file.makePublic();
  // return `https://storage.googleapis.com/${bucket.name}/${file.name}`;
}
```

### Adaptive Bitrate Streaming (HLS)

```typescript
// Generate HLS manifest from multiple qualities
async function generateHLSManifest(episodeId: string) {
  const bucket = getStorage().bucket();

  const manifest = `#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=640x360
https://storage.googleapis.com/${bucket.name}/videos/${episodeId}/360p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1400000,RESOLUTION=854x480
https://storage.googleapis.com/${bucket.name}/videos/${episodeId}/480p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=2800000,RESOLUTION=1280x720
https://storage.googleapis.com/${bucket.name}/videos/${episodeId}/720p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080
https://storage.googleapis.com/${bucket.name}/videos/${episodeId}/1080p.m3u8
`;

  // Upload manifest
  const file = bucket.file(`videos/${episodeId}/master.m3u8`);
  await file.save(manifest, {
    contentType: 'application/vnd.apple.mpegurl',
    metadata: {
      cacheControl: 'public, max-age=3600'
    }
  });
}
```

### Audio Podcast Distribution

```typescript
// Upload podcast episode
async function uploadPodcastEpisode(audioPath: string, episodeId: string) {
  const bucket = getStorage().bucket();

  await bucket.upload(audioPath, {
    destination: `podcasts/${episodeId}.mp3`,
    metadata: {
      contentType: 'audio/mpeg',
      cacheControl: 'public, max-age=31536000', // 1 year
      metadata: {
        episodeId,
        title: 'Episode Title',
        duration: '1800' // 30 minutes in seconds
      }
    }
  });

  // Make public
  const file = bucket.file(`podcasts/${episodeId}.mp3`);
  await file.makePublic();

  return `https://storage.googleapis.com/${bucket.name}/${file.name}`;
}

// Generate podcast RSS feed
async function generatePodcastRSS(episodes: any[]) {
  const rss = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>My Podcast</title>
    <description>Podcast description</description>
    ${episodes.map(ep => `
    <item>
      <title>${ep.title}</title>
      <enclosure url="${ep.url}" type="audio/mpeg" length="${ep.size}"/>
      <guid>${ep.id}</guid>
      <pubDate>${ep.publishedAt}</pubDate>
    </item>
    `).join('')}
  </channel>
</rss>`;

  // Upload RSS to Hosting
  const bucket = getStorage().bucket();
  const file = bucket.file('podcast.rss');
  await file.save(rss, {
    contentType: 'application/rss+xml',
    metadata: {
      cacheControl: 'public, max-age=3600' // 1 hour
    }
  });

  await file.makePublic();
  return `https://storage.googleapis.com/${bucket.name}/podcast.rss`;
}
```

## Performance Optimization

### Compression

```typescript
// Upload with gzip compression
import { createReadStream } from 'fs';
import { createGzip } from 'zlib';

async function uploadCompressed(localPath: string, storagePath: string) {
  const bucket = getStorage().bucket();

  await new Promise((resolve, reject) => {
    createReadStream(localPath)
      .pipe(createGzip())
      .pipe(bucket.file(storagePath).createWriteStream({
        metadata: {
          contentEncoding: 'gzip',
          contentType: 'application/json'
        }
      }))
      .on('finish', resolve)
      .on('error', reject);
  });
}
```

### CDN Caching Strategy

```typescript
// Set cache headers strategically
const cacheStrategies = {
  immutable: 'public, max-age=31536000, immutable', // Static assets
  shortTerm: 'public, max-age=3600', // 1 hour
  noCache: 'public, max-age=0, must-revalidate', // HTML
  private: 'private, max-age=0' // User-specific
};

async function uploadWithCaching(
  file: Buffer,
  path: string,
  strategy: keyof typeof cacheStrategies
) {
  const bucket = getStorage().bucket();

  await bucket.file(path).save(file, {
    metadata: {
      cacheControl: cacheStrategies[strategy]
    }
  });
}
```

### Image Optimization

```typescript
// Resize and optimize images on upload
import sharp from 'sharp';

async function uploadOptimizedImage(buffer: Buffer, storagePath: string) {
  const bucket = getStorage().bucket();

  // Create multiple sizes
  const sizes = [
    { name: 'thumbnail', width: 200 },
    { name: 'medium', width: 800 },
    { name: 'large', width: 1600 }
  ];

  await Promise.all(
    sizes.map(async (size) => {
      const resized = await sharp(buffer)
        .resize(size.width)
        .webp({ quality: 80 })
        .toBuffer();

      const path = storagePath.replace(/\.[^.]+$/, `-${size.name}.webp`);

      await bucket.file(path).save(resized, {
        metadata: {
          contentType: 'image/webp',
          cacheControl: 'public, max-age=31536000'
        }
      });
    })
  );
}
```

## Multi-Region Distribution

```typescript
// Set up multi-region buckets
async function setupMultiRegion() {
  const storage = getStorage();

  // Create regional buckets
  const usEast = await storage.bucket('my-project-us-east');
  const euWest = await storage.bucket('my-project-eu-west');
  const asiaEast = await storage.bucket('my-project-asia-east');

  // Upload to nearest region based on user location
}

// Serve from nearest region
function getRegionalURL(userRegion: string, filePath: string) {
  const buckets = {
    'us': 'my-project-us-east',
    'eu': 'my-project-eu-west',
    'asia': 'my-project-asia-east'
  };

  const bucket = buckets[userRegion] || buckets['us'];
  return `https://storage.googleapis.com/${bucket}/${filePath}`;
}
```

## Best Practices

1. **Use Signed URLs for Private Content**
2. **Enable CDN Caching** with appropriate cache headers
3. **Compress Large Files** before upload
4. **Optimize Images** (WebP, multiple sizes)
5. **Use Resumable Uploads** for large files
6. **Implement Security Rules** to prevent unauthorized access
7. **Monitor Storage Usage** and set quotas
8. **Use Cloud Functions** for server-side processing
9. **Implement Retry Logic** for failed uploads
10. **Set up Lifecycle Policies** to auto-delete old files

## Cost Optimization

```typescript
// Lifecycle policy to delete old files
const lifecycleConfig = {
  rule: [
    {
      action: { type: 'Delete' },
      condition: {
        age: 90, // days
        matchesPrefix: ['temp/']
      }
    },
    {
      action: { type: 'SetStorageClass', storageClass: 'NEARLINE' },
      condition: {
        age: 30,
        matchesPrefix: ['archive/']
      }
    }
  ]
};

// Apply lifecycle rules
await bucket.setMetadata({ lifecycle: lifecycleConfig });
```

## Resources

- Firebase Storage Documentation
- Firebase Hosting Documentation
- Cloud Storage Best Practices
- CDN Performance Optimization
- Video Streaming Guide
