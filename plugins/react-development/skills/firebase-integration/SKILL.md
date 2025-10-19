---
name: firebase-integration
description: Integrate Firebase services (Authentication, Firestore, Realtime Database, Storage, Cloud Functions) with React applications using Firebase JS SDK v10+. Use when implementing authentication, real-time data sync, cloud storage, or serverless functions in React apps.
---

# Firebase Integration with React

Master Firebase services integration in React applications using the modular Firebase JS SDK v10+. This skill covers authentication, databases (Firestore and Realtime Database), storage, and cloud functions with React patterns.

## Core Concepts

### Firebase JS SDK v10+ (Modular)

The Firebase JS SDK v10+ uses a modular approach that enables better tree-shaking and smaller bundle sizes.

**Key Benefits:**
- Tree-shaking support (only import what you use)
- Smaller bundle sizes (up to 80% reduction)
- Better TypeScript support
- Improved performance

**Migration from v8:**
```typescript
// ❌ Old (v8 namespaced API)
import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';

// ✅ New (v10+ modular API)
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth';
import { getFirestore, collection, getDocs } from 'firebase/firestore';
```

## Setup and Configuration

### 1. Installation

```bash
npm install firebase
# or
yarn add firebase
# or
pnpm add firebase
```

### 2. Firebase Configuration File

Create `src/lib/firebase.ts` (or `.js`):

```typescript
import { initializeApp, getApps, getApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';
import { getAnalytics, isSupported } from 'firebase/analytics';

// Firebase configuration from Firebase Console
const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID,
};

// Initialize Firebase (singleton pattern)
const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApp();

// Initialize services
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);

// Initialize Analytics only in browser and if supported
export const analytics = typeof window !== 'undefined' && isSupported()
  ? getAnalytics(app)
  : null;

export default app;
```

### 3. Environment Variables

Create `.env` file:

```env
VITE_FIREBASE_API_KEY=your-api-key
VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
VITE_FIREBASE_APP_ID=your-app-id
VITE_FIREBASE_MEASUREMENT_ID=G-XXXXXXXXXX
```

**Security Note:** Firebase config is safe to expose in client-side code. Security comes from Firestore Security Rules and Authentication.

## Firebase Authentication

### Authentication Provider Setup

```typescript
// src/lib/firebase-auth.ts
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signInWithPopup,
  GoogleAuthProvider,
  GithubAuthProvider,
  signOut as firebaseSignOut,
  onAuthStateChanged,
  User,
  sendPasswordResetEmail,
  updateProfile,
  sendEmailVerification,
} from 'firebase/auth';
import { auth } from './firebase';

// Google Sign-In
const googleProvider = new GoogleAuthProvider();
export const signInWithGoogle = () => signInWithPopup(auth, googleProvider);

// GitHub Sign-In
const githubProvider = new GithubAuthProvider();
export const signInWithGithub = () => signInWithPopup(auth, githubProvider);

// Email/Password Sign Up
export const signUp = (email: string, password: string) =>
  createUserWithEmailAndPassword(auth, email, password);

// Email/Password Sign In
export const signIn = (email: string, password: string) =>
  signInWithEmailAndPassword(auth, email, password);

// Sign Out
export const signOut = () => firebaseSignOut(auth);

// Password Reset
export const resetPassword = (email: string) =>
  sendPasswordResetEmail(auth, email);

// Update User Profile
export const updateUserProfile = (displayName: string, photoURL?: string) =>
  updateProfile(auth.currentUser!, { displayName, photoURL });

// Send Email Verification
export const verifyEmail = () =>
  sendEmailVerification(auth.currentUser!);

// Auth State Observer
export const onAuthChange = (callback: (user: User | null) => void) =>
  onAuthStateChanged(auth, callback);
```

### Authentication Context Provider

```typescript
// src/contexts/AuthContext.tsx
import React, { createContext, useContext, useEffect, useState } from 'react';
import type { User } from 'firebase/auth';
import { onAuthChange } from '@/lib/firebase-auth';

interface AuthContextType {
  user: User | null;
  loading: boolean;
}

const AuthContext = createContext<AuthContextType>({
  user: null,
  loading: true,
});

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthChange((user) => {
      setUser(user);
      setLoading(false);
    });

    return unsubscribe;
  }, []);

  return (
    <AuthContext.Provider value={{ user, loading }}>
      {children}
    </AuthContext.Provider>
  );
};
```

### Protected Route Component

```typescript
// src/components/ProtectedRoute.tsx
import { Navigate } from 'react-router-dom';
import { useAuth } from '@/contexts/AuthContext';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

export const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
};
```

### Login Component Example

```typescript
// src/components/Login.tsx
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signIn, signInWithGoogle } from '@/lib/firebase-auth';

export const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleEmailSignIn = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await signIn(email, password);
      navigate('/dashboard');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSignIn = async () => {
    setLoading(true);
    setError(null);

    try {
      await signInWithGoogle();
      navigate('/dashboard');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container">
      <h1>Sign In</h1>
      {error && <div className="error">{error}</div>}

      <form onSubmit={handleEmailSignIn}>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Signing in...' : 'Sign In'}
        </button>
      </form>

      <button onClick={handleGoogleSignIn} disabled={loading}>
        Sign in with Google
      </button>
    </div>
  );
};
```

## Firestore Database

### Firestore Operations

```typescript
// src/lib/firestore-operations.ts
import {
  collection,
  doc,
  getDoc,
  getDocs,
  addDoc,
  setDoc,
  updateDoc,
  deleteDoc,
  query,
  where,
  orderBy,
  limit,
  startAfter,
  DocumentSnapshot,
  QueryConstraint,
  Timestamp,
  serverTimestamp,
  onSnapshot,
  writeBatch,
} from 'firebase/firestore';
import { db } from './firebase';

// Generic CRUD operations

// Create document with auto-generated ID
export const createDocument = async <T extends Record<string, any>>(
  collectionName: string,
  data: T
) => {
  const docRef = await addDoc(collection(db, collectionName), {
    ...data,
    createdAt: serverTimestamp(),
    updatedAt: serverTimestamp(),
  });
  return docRef.id;
};

// Create document with custom ID
export const setDocument = async <T extends Record<string, any>>(
  collectionName: string,
  docId: string,
  data: T,
  merge = false
) => {
  await setDoc(
    doc(db, collectionName, docId),
    {
      ...data,
      updatedAt: serverTimestamp(),
    },
    { merge }
  );
};

// Read single document
export const getDocument = async <T>(
  collectionName: string,
  docId: string
): Promise<T | null> => {
  const docSnap = await getDoc(doc(db, collectionName, docId));
  if (docSnap.exists()) {
    return { id: docSnap.id, ...docSnap.data() } as T;
  }
  return null;
};

// Read multiple documents with query
export const getDocuments = async <T>(
  collectionName: string,
  ...queryConstraints: QueryConstraint[]
): Promise<T[]> => {
  const q = query(collection(db, collectionName), ...queryConstraints);
  const querySnapshot = await getDocs(q);
  return querySnapshot.docs.map(
    (doc) => ({ id: doc.id, ...doc.data() } as T)
  );
};

// Update document
export const updateDocument = async (
  collectionName: string,
  docId: string,
  data: Partial<any>
) => {
  await updateDoc(doc(db, collectionName, docId), {
    ...data,
    updatedAt: serverTimestamp(),
  });
};

// Delete document
export const deleteDocument = async (
  collectionName: string,
  docId: string
) => {
  await deleteDoc(doc(db, collectionName, docId));
};

// Real-time listener
export const subscribeToDocument = <T>(
  collectionName: string,
  docId: string,
  callback: (data: T | null) => void
) => {
  return onSnapshot(doc(db, collectionName, docId), (doc) => {
    if (doc.exists()) {
      callback({ id: doc.id, ...doc.data() } as T);
    } else {
      callback(null);
    }
  });
};

// Real-time collection listener
export const subscribeToCollection = <T>(
  collectionName: string,
  callback: (data: T[]) => void,
  ...queryConstraints: QueryConstraint[]
) => {
  const q = query(collection(db, collectionName), ...queryConstraints);
  return onSnapshot(q, (snapshot) => {
    const data = snapshot.docs.map(
      (doc) => ({ id: doc.id, ...doc.data() } as T)
    );
    callback(data);
  });
};

// Batch operations
export const batchWrite = async (
  operations: Array<{
    type: 'set' | 'update' | 'delete';
    collection: string;
    docId: string;
    data?: any;
  }>
) => {
  const batch = writeBatch(db);

  operations.forEach(({ type, collection: coll, docId, data }) => {
    const docRef = doc(db, coll, docId);

    switch (type) {
      case 'set':
        batch.set(docRef, data);
        break;
      case 'update':
        batch.update(docRef, data);
        break;
      case 'delete':
        batch.delete(docRef);
        break;
    }
  });

  await batch.commit();
};

// Pagination helper
export const paginateQuery = async <T>(
  collectionName: string,
  pageSize: number,
  lastDoc?: DocumentSnapshot,
  ...queryConstraints: QueryConstraint[]
) => {
  const constraints = [...queryConstraints, limit(pageSize)];
  if (lastDoc) {
    constraints.push(startAfter(lastDoc));
  }

  const q = query(collection(db, collectionName), ...constraints);
  const snapshot = await getDocs(q);

  const data = snapshot.docs.map(
    (doc) => ({ id: doc.id, ...doc.data() } as T)
  );
  const lastVisible = snapshot.docs[snapshot.docs.length - 1];

  return { data, lastDoc: lastVisible, hasMore: snapshot.docs.length === pageSize };
};
```

### Custom Hook for Firestore Collection

```typescript
// src/hooks/useFirestoreCollection.ts
import { useEffect, useState } from 'react';
import { QueryConstraint } from 'firebase/firestore';
import { getDocuments, subscribeToCollection } from '@/lib/firestore-operations';

interface UseFirestoreCollectionOptions<T> {
  collectionName: string;
  queryConstraints?: QueryConstraint[];
  realtime?: boolean;
}

export function useFirestoreCollection<T>({
  collectionName,
  queryConstraints = [],
  realtime = false,
}: UseFirestoreCollectionOptions<T>) {
  const [data, setData] = useState<T[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    if (realtime) {
      // Real-time subscription
      const unsubscribe = subscribeToCollection<T>(
        collectionName,
        (newData) => {
          setData(newData);
          setLoading(false);
        },
        ...queryConstraints
      );

      return unsubscribe;
    } else {
      // One-time fetch
      const fetchData = async () => {
        try {
          const result = await getDocuments<T>(
            collectionName,
            ...queryConstraints
          );
          setData(result);
        } catch (err) {
          setError(err as Error);
        } finally {
          setLoading(false);
        }
      };

      fetchData();
    }
  }, [collectionName, realtime, JSON.stringify(queryConstraints)]);

  return { data, loading, error };
}
```

### Usage Example

```typescript
// src/components/TodoList.tsx
import { where, orderBy } from 'firebase/firestore';
import { useAuth } from '@/contexts/AuthContext';
import { useFirestoreCollection } from '@/hooks/useFirestoreCollection';
import { createDocument, updateDocument, deleteDocument } from '@/lib/firestore-operations';

interface Todo {
  id: string;
  title: string;
  completed: boolean;
  userId: string;
  createdAt: any;
}

export const TodoList = () => {
  const { user } = useAuth();
  const { data: todos, loading, error } = useFirestoreCollection<Todo>({
    collectionName: 'todos',
    queryConstraints: [
      where('userId', '==', user?.uid),
      orderBy('createdAt', 'desc'),
    ],
    realtime: true, // Enable real-time updates
  });

  const addTodo = async (title: string) => {
    await createDocument('todos', {
      title,
      completed: false,
      userId: user?.uid,
    });
  };

  const toggleTodo = async (todoId: string, completed: boolean) => {
    await updateDocument('todos', todoId, { completed });
  };

  const removeTodo = async (todoId: string) => {
    await deleteDocument('todos', todoId);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h2>My Todos</h2>
      {todos.map((todo) => (
        <div key={todo.id}>
          <input
            type="checkbox"
            checked={todo.completed}
            onChange={() => toggleTodo(todo.id, !todo.completed)}
          />
          <span>{todo.title}</span>
          <button onClick={() => removeTodo(todo.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
};
```

## Firebase Storage

### File Upload Operations

```typescript
// src/lib/storage-operations.ts
import {
  ref,
  uploadBytes,
  uploadBytesResumable,
  getDownloadURL,
  deleteObject,
  listAll,
  UploadTaskSnapshot,
} from 'firebase/storage';
import { storage } from './firebase';

// Simple file upload
export const uploadFile = async (
  path: string,
  file: File
): Promise<string> => {
  const storageRef = ref(storage, path);
  const snapshot = await uploadBytes(storageRef, file);
  return getDownloadURL(snapshot.ref);
};

// Upload with progress tracking
export const uploadFileWithProgress = (
  path: string,
  file: File,
  onProgress: (progress: number) => void,
  onError: (error: Error) => void,
  onComplete: (downloadURL: string) => void
) => {
  const storageRef = ref(storage, path);
  const uploadTask = uploadBytesResumable(storageRef, file);

  uploadTask.on(
    'state_changed',
    (snapshot: UploadTaskSnapshot) => {
      const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
      onProgress(progress);
    },
    (error) => {
      onError(error);
    },
    async () => {
      const downloadURL = await getDownloadURL(uploadTask.snapshot.ref);
      onComplete(downloadURL);
    }
  );

  return uploadTask; // Return to allow cancellation
};

// Delete file
export const deleteFile = async (path: string): Promise<void> => {
  const storageRef = ref(storage, path);
  await deleteObject(storageRef);
};

// List files in directory
export const listFiles = async (path: string): Promise<string[]> => {
  const storageRef = ref(storage, path);
  const result = await listAll(storageRef);
  const urls = await Promise.all(
    result.items.map((item) => getDownloadURL(item))
  );
  return urls;
};
```

### Image Upload Component

```typescript
// src/components/ImageUpload.tsx
import { useState } from 'react';
import { uploadFileWithProgress } from '@/lib/storage-operations';
import { useAuth } from '@/contexts/AuthContext';

export const ImageUpload = () => {
  const { user } = useAuth();
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [uploading, setUploading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [downloadURL, setDownloadURL] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
    }
  };

  const handleUpload = () => {
    if (!file || !user) return;

    setUploading(true);
    setError(null);

    const path = `users/${user.uid}/images/${Date.now()}-${file.name}`;

    uploadFileWithProgress(
      path,
      file,
      (progress) => setProgress(progress),
      (error) => {
        setError(error.message);
        setUploading(false);
      },
      (url) => {
        setDownloadURL(url);
        setUploading(false);
        setProgress(0);
      }
    );
  };

  return (
    <div>
      <input type="file" accept="image/*" onChange={handleFileChange} />

      {preview && <img src={preview} alt="Preview" style={{ maxWidth: '200px' }} />}

      {file && (
        <button onClick={handleUpload} disabled={uploading}>
          {uploading ? `Uploading... ${progress.toFixed(0)}%` : 'Upload'}
        </button>
      )}

      {error && <div className="error">{error}</div>}

      {downloadURL && (
        <div>
          <p>Upload successful!</p>
          <img src={downloadURL} alt="Uploaded" style={{ maxWidth: '200px' }} />
          <p>URL: {downloadURL}</p>
        </div>
      )}
    </div>
  );
};
```

## Best Practices

### 1. Security Rules

**Firestore Security Rules:**
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can only read/write their own data
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Users can only read/write their own todos
    match /todos/{todoId} {
      allow read, write: if request.auth != null
        && resource.data.userId == request.auth.uid;
    }
  }
}
```

**Storage Security Rules:**
```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    // Users can only upload to their own folder
    match /users/{userId}/{allPaths=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

### 2. Data Structure Best Practices

**Flat Structure (Recommended):**
```typescript
// ✅ Good: Flat collections with references
collections/users/{userId}
collections/posts/{postId} with userId field
collections/comments/{commentId} with postId field
```

**Avoid Deep Nesting:**
```typescript
// ❌ Avoid: Deep nested sub-collections
collections/users/{userId}/posts/{postId}/comments/{commentId}
```

### 3. Performance Optimization

- **Index Frequently Queried Fields** in Firebase Console
- **Use Pagination** for large datasets
- **Limit Query Results** with `limit()`
- **Use Real-time Listeners Sparingly** (they count against quota)
- **Batch Operations** when updating multiple documents

### 4. Error Handling

```typescript
import { FirebaseError } from 'firebase/app';

try {
  await signIn(email, password);
} catch (error) {
  if (error instanceof FirebaseError) {
    switch (error.code) {
      case 'auth/user-not-found':
        setError('No account found with this email');
        break;
      case 'auth/wrong-password':
        setError('Incorrect password');
        break;
      case 'auth/too-many-requests':
        setError('Too many failed attempts. Please try again later');
        break;
      default:
        setError(error.message);
    }
  }
}
```

### 5. Environment-Specific Configuration

```typescript
// src/lib/firebase.ts
const firebaseConfig = import.meta.env.PROD
  ? {
      // Production config
      apiKey: import.meta.env.VITE_FIREBASE_API_KEY_PROD,
      // ...
    }
  : {
      // Development config
      apiKey: import.meta.env.VITE_FIREBASE_API_KEY_DEV,
      // ...
    };
```

### 6. Offline Persistence (Firestore)

```typescript
import { enableIndexedDbPersistence } from 'firebase/firestore';

enableIndexedDbPersistence(db).catch((err) => {
  if (err.code === 'failed-precondition') {
    // Multiple tabs open, persistence can only be enabled in one tab
    console.warn('Persistence failed');
  } else if (err.code === 'unimplemented') {
    // Browser doesn't support persistence
    console.warn('Persistence not supported');
  }
});
```

## Common Patterns

### Compound Queries

```typescript
import { where, and, or } from 'firebase/firestore';

// AND query
const activeAdminTodos = await getDocuments<Todo>(
  'todos',
  where('userId', '==', userId),
  where('completed', '==', false),
  where('priority', '==', 'high')
);

// OR query (Firebase v9.14+)
const urgentOrHighPriority = await getDocuments<Todo>(
  'todos',
  or(
    where('priority', '==', 'urgent'),
    where('priority', '==', 'high')
  )
);

// Complex query with AND/OR
const complexQuery = await getDocuments<Todo>(
  'todos',
  and(
    where('userId', '==', userId),
    or(
      where('status', '==', 'active'),
      where('status', '==', 'pending')
    )
  )
);
```

### Transaction for Atomic Operations

```typescript
import { runTransaction } from 'firebase/firestore';

const transferPoints = async (fromUserId: string, toUserId: string, points: number) => {
  await runTransaction(db, async (transaction) => {
    const fromDoc = doc(db, 'users', fromUserId);
    const toDoc = doc(db, 'users', toUserId);

    const fromSnapshot = await transaction.get(fromDoc);
    const toSnapshot = await transaction.get(toDoc);

    if (!fromSnapshot.exists() || !toSnapshot.exists()) {
      throw new Error('User not found');
    }

    const fromPoints = fromSnapshot.data().points;
    if (fromPoints < points) {
      throw new Error('Insufficient points');
    }

    transaction.update(fromDoc, { points: fromPoints - points });
    transaction.update(toDoc, { points: toSnapshot.data().points + points });
  });
};
```

---

**Key Takeaways:**
- Use Firebase JS SDK v10+ modular API for tree-shaking
- Implement proper security rules (never rely on client-side validation alone)
- Use TypeScript for better type safety
- Handle errors gracefully with user-friendly messages
- Structure data flat with references, not deeply nested
- Use real-time listeners sparingly (quota implications)
- Always cleanup subscriptions in useEffect return
- Test security rules thoroughly before production
