---
name: firebase-backend-integration
description: Integrate Firebase Admin SDK into Node.js/Python backends with authentication, Firestore operations, deployment via CLI/Docker/hosted platforms, and production best practices. Use when building backends that interact with Firebase services or migrating from Firebase client to server-side operations.
---

# Firebase Backend Integration

Master Firebase Admin SDK integration for backend services with authentication verification, Firestore operations, deployment strategies (CLI, Docker, hosted), and production-ready patterns for Node.js and Python.

## When to Use This Skill

- Building backend services that interact with Firebase
- Implementing server-side Firebase authentication verification
- Performing privileged Firestore/Storage operations
- Creating admin panels or internal tools
- Building microservices with Firebase as database
- Migrating from client-side Firebase to backend operations
- Implementing custom authentication flows
- Running Firebase services in containers or cloud platforms

## Core Concepts

### 1. Firebase Admin SDK vs Client SDK

**Admin SDK (Backend):**
- Bypasses security rules
- Full database access
- Server-to-server communication
- Token verification and creation
- User management
- No real-time listeners (use with caution)

**Client SDK (Frontend):**
- Enforces security rules
- User-based access control
- Real-time listeners
- Client-side authentication
- Browser/mobile optimized

### 2. Running Firebase Backends

**Firebase CLI (Development & Deployment)**
- Local emulators for development
- Deploy Cloud Functions
- Manage Firestore indexes
- Configure security rules

**Docker (Containerized)**
- Custom backend services
- Microservices architecture
- Kubernetes deployment
- Development parity with production

**Hosted Platforms**
- Cloud Run (Google Cloud)
- Cloud Functions (serverless)
- App Engine (Google Cloud)
- Kubernetes Engine (GKE)
- Any Node.js/Python hosting (Heroku, AWS, etc.)

## Installation and Setup

### Node.js Installation

```bash
# Install Firebase Admin SDK
npm install firebase-admin

# Optional: Express for API
npm install express cors helmet

# TypeScript support
npm install --save-dev @types/node typescript
```

### Python Installation

```bash
# Install Firebase Admin SDK
pip install firebase-admin

# Optional: Flask for API
pip install flask flask-cors

# Or FastAPI
pip install fastapi uvicorn
```

### Service Account Setup

1. Go to Firebase Console → Project Settings → Service Accounts
2. Click "Generate New Private Key"
3. Save JSON file securely

```bash
# Set environment variable
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/serviceAccountKey.json"

# Or in .env file
FIREBASE_SERVICE_ACCOUNT_KEY=/path/to/serviceAccountKey.json
```

## Running with Firebase CLI

### Install Firebase Tools

```bash
# Install globally
npm install -g firebase-tools

# Login to Firebase
firebase login

# Initialize project
firebase init
```

### Local Development with Emulators

```bash
# Start all emulators
firebase emulators:start

# Start specific emulators
firebase emulators:start --only auth,firestore

# Export emulator data
firebase emulators:export ./emulator-data

# Import emulator data
firebase emulators:start --import=./emulator-data
```

```typescript
// Connect to emulators in code
// src/config/firebase.ts
import * as admin from 'firebase-admin';

if (process.env.NODE_ENV === 'development') {
  // Use emulators
  process.env.FIRESTORE_EMULATOR_HOST = 'localhost:8080';
  process.env.FIREBASE_AUTH_EMULATOR_HOST = 'localhost:9099';
}

admin.initializeApp({
  projectId: 'demo-project', // Use this for emulators
});

export const db = admin.firestore();
export const auth = admin.auth();
```

### firebase.json Configuration

```json
{
  "emulators": {
    "auth": {
      "port": 9099
    },
    "firestore": {
      "port": 8080
    },
    "storage": {
      "port": 9199
    },
    "pubsub": {
      "port": 8085
    },
    "ui": {
      "enabled": true,
      "port": 4000
    }
  },
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  }
}
```

## Running with Docker

### Dockerfile for Node.js Backend

```dockerfile
# Dockerfile
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Build TypeScript (if applicable)
RUN npm run build

# Expose port
EXPOSE 8080

# Set environment to production
ENV NODE_ENV=production

# Start application
CMD ["node", "dist/index.js"]
```

### Docker Compose with Firebase Emulators

```yaml
# docker-compose.yml
version: '3.8'

services:
  # Your backend service
  backend:
    build: .
    ports:
      - "8080:8080"
    environment:
      - FIRESTORE_EMULATOR_HOST=firebase-emulator:8080
      - FIREBASE_AUTH_EMULATOR_HOST=firebase-emulator:9099
      - GOOGLE_CLOUD_PROJECT=demo-project
    depends_on:
      - firebase-emulator
    volumes:
      - ./serviceAccountKey.json:/app/serviceAccountKey.json:ro
    env_file:
      - .env

  # Firebase emulators
  firebase-emulator:
    image: spine3/firebase-emulator
    ports:
      - "4000:4000"   # Emulator UI
      - "8080:8080"   # Firestore
      - "9099:9099"   # Auth
      - "9199:9199"   # Storage
    volumes:
      - ./firebase.json:/firebase.json
      - ./firestore.rules:/firestore.rules
      - ./emulator-data:/data
    environment:
      - GOOGLE_CLOUD_PROJECT=demo-project
```

### Running with Docker

```bash
# Build image
docker build -t my-firebase-backend .

# Run container
docker run -p 8080:8080 \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/serviceAccountKey.json \
  -v $(pwd)/serviceAccountKey.json:/app/serviceAccountKey.json:ro \
  my-firebase-backend

# With Docker Compose
docker-compose up

# In production (with secrets)
docker run -p 8080:8080 \
  -e FIREBASE_PROJECT_ID=my-project \
  -e FIREBASE_CLIENT_EMAIL=service@my-project.iam.gserviceaccount.com \
  -e FIREBASE_PRIVATE_KEY="$(cat serviceAccountKey.json | jq -r .private_key)" \
  my-firebase-backend
```

## Hosted Deployment

### Google Cloud Run

```bash
# Build and deploy
gcloud run deploy my-service \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars FIREBASE_PROJECT_ID=my-project

# With secrets
gcloud run deploy my-service \
  --source . \
  --set-secrets FIREBASE_SERVICE_ACCOUNT=firebase-sa-key:latest
```

### Google Cloud Functions (Already covered in api-scaffolding skill)

```bash
# Deploy function
gcloud functions deploy myFunction \
  --runtime nodejs20 \
  --trigger-http \
  --allow-unauthenticated
```

### Kubernetes (GKE)

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: firebase-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: firebase-backend
  template:
    metadata:
      labels:
        app: firebase-backend
    spec:
      containers:
      - name: backend
        image: gcr.io/my-project/firebase-backend:latest
        ports:
        - containerPort: 8080
        env:
        - name: FIREBASE_PROJECT_ID
          value: "my-project"
        - name: GOOGLE_APPLICATION_CREDENTIALS
          value: /var/secrets/google/key.json
        volumeMounts:
        - name: google-cloud-key
          mountPath: /var/secrets/google
          readOnly: true
      volumes:
      - name: google-cloud-key
        secret:
          secretName: firebase-service-account
---
apiVersion: v1
kind: Service
metadata:
  name: firebase-backend-service
spec:
  selector:
    app: firebase-backend
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
```

```bash
# Create secret
kubectl create secret generic firebase-service-account \
  --from-file=key.json=./serviceAccountKey.json

# Deploy
kubectl apply -f deployment.yaml
```

### Heroku Deployment

```bash
# Create Heroku app
heroku create my-firebase-backend

# Set environment variables
heroku config:set FIREBASE_PROJECT_ID=my-project
heroku config:set FIREBASE_CLIENT_EMAIL=service@my-project.iam.gserviceaccount.com
heroku config:set FIREBASE_PRIVATE_KEY="$(cat serviceAccountKey.json | jq -r .private_key)"

# Deploy
git push heroku main
```

### AWS Elastic Beanstalk

```yaml
# .ebextensions/environment.config
option_settings:
  aws:elasticbeanstalk:application:environment:
    FIREBASE_PROJECT_ID: my-project
    NODE_ENV: production
```

```bash
# Initialize EB
eb init

# Create environment
eb create production

# Deploy
eb deploy
```

## Backend Implementation Patterns

### Pattern 1: Firebase Admin Initialization

```typescript
// src/config/firebase.ts
import * as admin from 'firebase-admin';

let app: admin.app.App;

export function initializeFirebase() {
  if (admin.apps.length > 0) {
    return admin.apps[0];
  }

  // Production: Use service account file
  if (process.env.GOOGLE_APPLICATION_CREDENTIALS) {
    app = admin.initializeApp({
      credential: admin.credential.applicationDefault(),
    });
  }
  // Or use environment variables
  else if (process.env.FIREBASE_PRIVATE_KEY) {
    app = admin.initializeApp({
      credential: admin.credential.cert({
        projectId: process.env.FIREBASE_PROJECT_ID,
        clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
        privateKey: process.env.FIREBASE_PRIVATE_KEY.replace(/\\n/g, '\n'),
      }),
    });
  }
  // Development: Use emulators
  else {
    app = admin.initializeApp({
      projectId: 'demo-project',
    });
  }

  return app;
}

initializeFirebase();

export const db = admin.firestore();
export const auth = admin.auth();
export const storage = admin.storage();
```

### Pattern 2: Authentication Verification Middleware

```typescript
// src/middleware/auth.ts
import { Request, Response, NextFunction } from 'express';
import { auth } from '../config/firebase';

export interface AuthRequest extends Request {
  user?: admin.auth.DecodedIdToken;
}

export async function verifyFirebaseToken(
  req: AuthRequest,
  res: Response,
  next: NextFunction
) {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader?.startsWith('Bearer ')) {
      return res.status(401).json({ error: 'Unauthorized - No token provided' });
    }

    const token = authHeader.split('Bearer ')[1];

    // Verify ID token
    const decodedToken = await auth.verifyIdToken(token, true); // checkRevoked = true
    req.user = decodedToken;

    next();
  } catch (error: any) {
    console.error('Token verification error:', error);

    if (error.code === 'auth/id-token-expired') {
      return res.status(401).json({ error: 'Token expired' });
    }

    return res.status(401).json({ error: 'Invalid token' });
  }
}

// Check specific claims
export function requireClaim(claim: string, value: any) {
  return (req: AuthRequest, res: Response, next: NextFunction) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    if (req.user[claim] !== value) {
      return res.status(403).json({ error: 'Forbidden - Insufficient permissions' });
    }

    next();
  };
}

// Check admin role
export const requireAdmin = requireClaim('admin', true);
```

### Pattern 3: User Management

```typescript
// src/services/userManagement.ts
import { auth, db } from '../config/firebase';

export const userManagement = {
  // Create user
  async createUser(email: string, password: string, displayName?: string) {
    const userRecord = await auth.createUser({
      email,
      password,
      displayName,
      emailVerified: false,
    });

    // Create Firestore user document
    await db.collection('users').doc(userRecord.uid).set({
      email,
      displayName,
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      role: 'user',
    });

    return userRecord;
  },

  // Get user
  async getUser(uid: string) {
    const [authUser, firestoreUser] = await Promise.all([
      auth.getUser(uid),
      db.collection('users').doc(uid).get(),
    ]);

    return {
      ...authUser,
      customData: firestoreUser.data(),
    };
  },

  // Update user
  async updateUser(uid: string, updates: { displayName?: string; photoURL?: string }) {
    await Promise.all([
      auth.updateUser(uid, updates),
      db.collection('users').doc(uid).update({
        ...updates,
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
      }),
    ]);
  },

  // Delete user
  async deleteUser(uid: string) {
    // Delete auth user
    await auth.deleteUser(uid);

    // Delete Firestore data
    await db.collection('users').doc(uid).delete();
  },

  // Set custom claims
  async setCustomClaims(uid: string, claims: object) {
    await auth.setCustomUserClaims(uid, claims);
  },

  // Make user admin
  async makeAdmin(uid: string) {
    await auth.setCustomUserClaims(uid, { admin: true });
    await db.collection('users').doc(uid).update({
      role: 'admin',
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    });
  },

  // List users (paginated)
  async listUsers(maxResults = 1000, pageToken?: string) {
    const result = await auth.listUsers(maxResults, pageToken);

    return {
      users: result.users,
      pageToken: result.pageToken,
    };
  },

  // Disable user
  async disableUser(uid: string) {
    await auth.updateUser(uid, { disabled: true });
  },

  // Generate password reset link
  async generatePasswordResetLink(email: string) {
    return await auth.generatePasswordResetLink(email);
  },

  // Generate email verification link
  async generateEmailVerificationLink(email: string) {
    return await auth.generateEmailVerificationLink(email);
  },
};
```

### Pattern 4: Firestore Operations

```typescript
// src/services/database.ts
import { db } from '../config/firebase';
import * as admin from 'firebase-admin';

export const database = {
  // Create document
  async create<T>(collection: string, data: T, id?: string) {
    const docData = {
      ...data,
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    };

    if (id) {
      await db.collection(collection).doc(id).set(docData);
      return id;
    }

    const docRef = await db.collection(collection).add(docData);
    return docRef.id;
  },

  // Read document
  async get<T>(collection: string, id: string): Promise<T | null> {
    const doc = await db.collection(collection).doc(id).get();

    if (!doc.exists) {
      return null;
    }

    return {
      id: doc.id,
      ...doc.data(),
    } as T;
  },

  // Update document
  async update(collection: string, id: string, data: any) {
    await db.collection(collection).doc(id).update({
      ...data,
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
    });
  },

  // Delete document
  async delete(collection: string, id: string) {
    await db.collection(collection).doc(id).delete();
  },

  // Query documents
  async query<T>(
    collection: string,
    filters: Array<[string, admin.firestore.WhereFilterOp, any]> = [],
    orderBy?: [string, 'asc' | 'desc'],
    limit?: number
  ): Promise<T[]> {
    let query: admin.firestore.Query = db.collection(collection);

    // Apply filters
    filters.forEach(([field, op, value]) => {
      query = query.where(field, op, value);
    });

    // Apply ordering
    if (orderBy) {
      query = query.orderBy(orderBy[0], orderBy[1]);
    }

    // Apply limit
    if (limit) {
      query = query.limit(limit);
    }

    const snapshot = await query.get();

    return snapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data(),
    })) as T[];
  },

  // Batch operations
  async batchWrite(operations: Array<{
    type: 'set' | 'update' | 'delete';
    collection: string;
    id: string;
    data?: any;
  }>) {
    const batch = db.batch();

    operations.forEach(op => {
      const docRef = db.collection(op.collection).doc(op.id);

      switch (op.type) {
        case 'set':
          batch.set(docRef, op.data);
          break;
        case 'update':
          batch.update(docRef, op.data);
          break;
        case 'delete':
          batch.delete(docRef);
          break;
      }
    });

    await batch.commit();
  },

  // Transaction
  async transaction<T>(callback: (transaction: admin.firestore.Transaction) => Promise<T>) {
    return await db.runTransaction(callback);
  },
};
```

### Pattern 5: Express API with Firebase

```typescript
// src/index.ts
import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import { initializeFirebase } from './config/firebase';
import { verifyFirebaseToken } from './middleware/auth';
import { userRoutes } from './routes/users';

// Initialize Firebase
initializeFirebase();

const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Protected routes
app.use('/api/users', verifyFirebaseToken, userRoutes);

// Error handling
app.use((err: any, req: express.Request, res: express.Response, next: express.NextFunction) => {
  console.error(err);
  res.status(500).json({ error: 'Internal server error' });
});

const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

## Environment Variables

```bash
# .env
NODE_ENV=production
PORT=8080

# Option 1: Service account file
GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceAccountKey.json

# Option 2: Individual credentials
FIREBASE_PROJECT_ID=my-project-id
FIREBASE_CLIENT_EMAIL=firebase-adminsdk@my-project.iam.gserviceaccount.com
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"

# Development: Emulator hosts
FIRESTORE_EMULATOR_HOST=localhost:8080
FIREBASE_AUTH_EMULATOR_HOST=localhost:9099
```

## Best Practices

### 1. Secure Service Account Keys

```bash
# Never commit service account files
echo "serviceAccountKey.json" >> .gitignore

# Use secrets management
# Google Cloud: Secret Manager
# AWS: Systems Manager Parameter Store
# Kubernetes: Secrets
# Docker: Secrets
```

### 2. Initialize Firebase Once

```typescript
// ✅ Good - Singleton pattern
let firebaseApp: admin.app.App;
if (!firebaseApp) {
  firebaseApp = admin.initializeApp();
}

// ❌ Bad - Multiple initializations
admin.initializeApp(); // Called multiple times
```

### 3. Use Connection Pooling

Firebase Admin SDK reuses connections automatically, but be mindful of:
- Cloud Functions cold starts
- Container scaling
- Connection limits

### 4. Handle Errors Gracefully

```typescript
try {
  await auth.verifyIdToken(token);
} catch (error: any) {
  if (error.code === 'auth/id-token-expired') {
    // Handle expired token
  } else if (error.code === 'auth/argument-error') {
    // Handle invalid token format
  }
}
```

### 5. Monitor and Log

```typescript
import * as winston from 'winston';

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
  ],
});

// Log Firebase operations
logger.info('User authenticated', { uid: decodedToken.uid });
```

## Resources

- **references/admin-sdk-complete-guide.md**: Comprehensive Admin SDK reference
- **references/deployment-strategies.md**: Detailed deployment guides
- **references/docker-firebase-setup.md**: Docker configuration examples
- **references/kubernetes-firebase.md**: Kubernetes deployment patterns
- **assets/firebase-admin-wrapper.ts**: Production-ready Admin SDK wrapper
- **assets/docker-compose-full.yml**: Complete Docker Compose setup
- **assets/k8s-deployment.yaml**: Kubernetes manifests

## Common Pitfalls

- **Exposing Service Account Keys**: Never commit or expose service account credentials
- **Not Handling Token Expiration**: Always check for expired tokens
- **Over-fetching Data**: Use Firestore queries efficiently with limits
- **Missing Error Handling**: Always handle Firebase errors appropriately
- **Forgetting Emulators**: Use emulators for local development to avoid production data changes
- **Not Setting Timeouts**: Set appropriate timeouts for long-running operations
- **Ignoring Security Rules**: Even with Admin SDK, implement proper authorization logic
- **Container Credentials**: Use secrets management for containerized deployments
