---
name: firebase-nextjs-integration
description: Integrate Firebase with Next.js 14+ App Router including authentication, Firestore, server-side rendering with FirebaseServerApp, and secure API routes. Use when building Next.js applications with Firebase authentication, real-time data, or serverless functions.
---

# Firebase Next.js Integration

Master Firebase integration with Next.js 14+ App Router, including client-side and server-side Firebase initialization, authentication, Firestore operations, and SSR patterns with FirebaseServerApp.

## When to Use This Skill

- Building Next.js applications with Firebase authentication
- Implementing server-side rendering with Firebase data
- Using Firestore in Server Components and API Routes
- Securing Next.js routes with Firebase authentication
- Implementing real-time features in Next.js with Firestore
- Using Firebase Admin SDK in Next.js API Routes
- Building authenticated SSR/SSG pages with Firebase
- Migrating from Pages Router to App Router with Firebase

## Core Concepts

### 1. Firebase Initialization Patterns

**Client-Side Initialization (Client Components)**
- Uses Firebase JS SDK
- Browser-only operations
- Real-time listeners
- Client-side authentication

**Server-Side Initialization (Server Components, API Routes)**
- Uses Firebase Admin SDK
- Server-only operations
- No real-time listeners
- Server-side verification

**FirebaseServerApp (New in v10+)**
- Authenticated server-side requests
- SSR with user context
- Hybrid client/server authentication

### 2. Next.js 14+ App Router Specifics

**Server Components (Default)**
- Can use Firebase Admin SDK
- No client-side JavaScript
- Fast initial page loads
- Cannot use real-time listeners

**Client Components (`"use client"`)**
- Can use Firebase JS SDK
- Real-time listeners work
- Interactive features
- Authentication state management

**API Routes (`app/api/`)**
- Server-only code
- Use Firebase Admin SDK
- Secure backend operations
- No CORS issues

### 3. Authentication Flow

1. **Client-side sign-in** → Firebase Auth
2. **Get ID token** → `user.getIdToken()`
3. **Send to server** → Cookie or header
4. **Verify on server** → Firebase Admin SDK
5. **Access protected resources** → Authenticated requests

## Quick Start

### Installation

```bash
# Install Firebase SDKs
npm install firebase firebase-admin

# Install Next.js (if not already)
npm install next@latest react@latest react-dom@latest
```

### Environment Variables

```bash
# .env.local

# Client-side Firebase config (public)
NEXT_PUBLIC_FIREBASE_API_KEY=AIzaSy...
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=myapp.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=myapp
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=myapp.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=123456789
NEXT_PUBLIC_FIREBASE_APP_ID=1:123456789:web:abc123

# Server-side Firebase Admin (private)
FIREBASE_ADMIN_PROJECT_ID=myapp
FIREBASE_ADMIN_CLIENT_EMAIL=firebase-adminsdk@myapp.iam.gserviceaccount.com
FIREBASE_ADMIN_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
```

### Project Structure

```
app/
├── (auth)/
│   ├── login/
│   │   └── page.tsx
│   └── signup/
│       └── page.tsx
├── (protected)/
│   ├── dashboard/
│   │   └── page.tsx
│   └── layout.tsx
├── api/
│   ├── auth/
│   │   └── session/
│   │       └── route.ts
│   └── posts/
│       └── route.ts
├── layout.tsx
└── middleware.ts

lib/
├── firebase/
│   ├── client.ts          # Client-side Firebase
│   ├── admin.ts           # Server-side Firebase Admin
│   └── auth-context.tsx   # Auth provider
└── hooks/
    └── useAuth.ts
```

## Firebase Setup

### Client-Side Firebase (`lib/firebase/client.ts`)

```typescript
// lib/firebase/client.ts
import { initializeApp, getApps, getApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

// Initialize Firebase (singleton pattern)
const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApp();

export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);
export { app };
```

### Server-Side Firebase Admin (`lib/firebase/admin.ts`)

```typescript
// lib/firebase/admin.ts
import { initializeApp, getApps, cert, App } from 'firebase-admin/app';
import { getAuth } from 'firebase-admin/auth';
import { getFirestore } from 'firebase-admin/firestore';

let adminApp: App;

function getAdminApp() {
  if (getApps().length === 0) {
    adminApp = initializeApp({
      credential: cert({
        projectId: process.env.FIREBASE_ADMIN_PROJECT_ID,
        clientEmail: process.env.FIREBASE_ADMIN_CLIENT_EMAIL,
        privateKey: process.env.FIREBASE_ADMIN_PRIVATE_KEY?.replace(/\\n/g, '\n'),
      }),
    });
  } else {
    adminApp = getApps()[0];
  }

  return adminApp;
}

export const adminAuth = getAuth(getAdminApp());
export const adminDb = getFirestore(getAdminApp());
export { getAdminApp };
```

## Authentication Implementation

### Auth Context Provider (`lib/firebase/auth-context.tsx`)

```typescript
'use client';

import { createContext, useContext, useEffect, useState } from 'react';
import { User, onAuthStateChanged } from 'firebase/auth';
import { auth } from './client';

interface AuthContextType {
  user: User | null;
  loading: boolean;
}

const AuthContext = createContext<AuthContextType>({
  user: null,
  loading: true,
});

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      if (user) {
        // Get ID token and store in cookie for server-side verification
        const token = await user.getIdToken();

        // Send token to server to set cookie
        await fetch('/api/auth/session', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ token }),
        });
      } else {
        // Clear session cookie
        await fetch('/api/auth/session', { method: 'DELETE' });
      }

      setUser(user);
      setLoading(false);
    });

    return () => unsubscribe();
  }, []);

  return (
    <AuthContext.Provider value={{ user, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
```

### Root Layout with Auth Provider (`app/layout.tsx`)

```typescript
// app/layout.tsx
import { AuthProvider } from '@/lib/firebase/auth-context';
import './globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}
```

### Session API Route (`app/api/auth/session/route.ts`)

```typescript
// app/api/auth/session/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { adminAuth } from '@/lib/firebase/admin';
import { cookies } from 'next/headers';

const SESSION_COOKIE_NAME = 'session';
const SESSION_COOKIE_MAX_AGE = 60 * 60 * 24 * 5; // 5 days

export async function POST(request: NextRequest) {
  const { token } = await request.json();

  if (!token) {
    return NextResponse.json({ error: 'No token provided' }, { status: 400 });
  }

  try {
    // Verify the ID token
    const decodedToken = await adminAuth.verifyIdToken(token);

    // Create session cookie
    const sessionCookie = await adminAuth.createSessionCookie(token, {
      expiresIn: SESSION_COOKIE_MAX_AGE * 1000,
    });

    // Set cookie
    cookies().set(SESSION_COOKIE_NAME, sessionCookie, {
      maxAge: SESSION_COOKIE_MAX_AGE,
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      path: '/',
    });

    return NextResponse.json({
      success: true,
      uid: decodedToken.uid
    });
  } catch (error) {
    console.error('Session creation error:', error);
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }
}

export async function DELETE() {
  // Clear session cookie
  cookies().delete(SESSION_COOKIE_NAME);
  return NextResponse.json({ success: true });
}

export async function GET() {
  const sessionCookie = cookies().get(SESSION_COOKIE_NAME)?.value;

  if (!sessionCookie) {
    return NextResponse.json({ user: null });
  }

  try {
    const decodedClaims = await adminAuth.verifySessionCookie(sessionCookie);
    return NextResponse.json({ user: decodedClaims });
  } catch (error) {
    return NextResponse.json({ user: null });
  }
}
```

### Login Page (`app/(auth)/login/page.tsx`)

```typescript
'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider } from 'firebase/auth';
import { auth } from '@/lib/firebase/client';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleEmailLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      await signInWithEmailAndPassword(auth, email, password);
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleLogin = async () => {
    setLoading(true);
    setError('');

    try {
      const provider = new GoogleAuthProvider();
      await signInWithPopup(auth, provider);
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
        <h2 className="text-3xl font-bold text-center">Sign In</h2>

        {error && (
          <div className="bg-red-50 text-red-600 p-3 rounded">
            {error}
          </div>
        )}

        <form onSubmit={handleEmailLogin} className="space-y-6">
          <div>
            <label htmlFor="email" className="block text-sm font-medium">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md"
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-sm font-medium">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-2 px-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
          >
            {loading ? 'Signing in...' : 'Sign In'}
          </button>
        </form>

        <div className="relative">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t border-gray-300" />
          </div>
          <div className="relative flex justify-center text-sm">
            <span className="px-2 bg-white text-gray-500">Or continue with</span>
          </div>
        </div>

        <button
          onClick={handleGoogleLogin}
          disabled={loading}
          className="w-full py-2 px-4 border border-gray-300 rounded-md hover:bg-gray-50 disabled:opacity-50 flex items-center justify-center gap-2"
        >
          <svg className="w-5 h-5" viewBox="0 0 24 24">
            {/* Google icon SVG */}
          </svg>
          Sign in with Google
        </button>
      </div>
    </div>
  );
}
```

### Middleware for Protected Routes (`middleware.ts`)

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server';

export async function middleware(request: NextRequest) {
  const sessionCookie = request.cookies.get('session')?.value;

  // Check if accessing protected route
  if (request.nextUrl.pathname.startsWith('/dashboard') ||
      request.nextUrl.pathname.startsWith('/profile')) {

    if (!sessionCookie) {
      // Redirect to login if no session
      return NextResponse.redirect(new URL('/login', request.url));
    }

    // Verify session is valid (optional - adds latency)
    // Could verify with Firebase Admin here, but it's already verified in API routes
  }

  // Redirect authenticated users away from auth pages
  if (sessionCookie &&
      (request.nextUrl.pathname.startsWith('/login') ||
       request.nextUrl.pathname.startsWith('/signup'))) {
    return NextResponse.redirect(new URL('/dashboard', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*', '/profile/:path*', '/login', '/signup'],
};
```

## Server Components with Firebase

### Protected Server Component (`app/(protected)/dashboard/page.tsx`)

```typescript
// app/(protected)/dashboard/page.tsx
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import { adminAuth, adminDb } from '@/lib/firebase/admin';

async function getUserData(uid: string) {
  const userDoc = await adminDb.collection('users').doc(uid).get();
  return userDoc.data();
}

async function getUserPosts(uid: string) {
  const postsSnapshot = await adminDb
    .collection('posts')
    .where('userId', '==', uid)
    .orderBy('createdAt', 'desc')
    .limit(10)
    .get();

  return postsSnapshot.docs.map(doc => ({
    id: doc.id,
    ...doc.data(),
  }));
}

export default async function DashboardPage() {
  const sessionCookie = cookies().get('session')?.value;

  if (!sessionCookie) {
    redirect('/login');
  }

  let user;
  try {
    const decodedClaims = await adminAuth.verifySessionCookie(sessionCookie, true);
    user = decodedClaims;
  } catch (error) {
    redirect('/login');
  }

  // Fetch data server-side
  const [userData, posts] = await Promise.all([
    getUserData(user.uid),
    getUserPosts(user.uid),
  ]);

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <h2 className="text-xl font-semibold mb-4">Profile</h2>
        <p><strong>Email:</strong> {user.email}</p>
        <p><strong>Name:</strong> {userData?.name || 'Not set'}</p>
      </div>

      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">Your Posts</h2>
        {posts.length === 0 ? (
          <p className="text-gray-500">No posts yet</p>
        ) : (
          <ul className="space-y-4">
            {posts.map((post: any) => (
              <li key={post.id} className="border-b pb-4">
                <h3 className="font-semibold">{post.title}</h3>
                <p className="text-gray-600 text-sm">{post.content}</p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
```

### Real-Time Client Component in Server Page

```typescript
// app/(protected)/dashboard/RealtimePosts.tsx
'use client';

import { useEffect, useState } from 'react';
import { collection, query, where, orderBy, onSnapshot } from 'firebase/firestore';
import { db } from '@/lib/firebase/client';

interface Post {
  id: string;
  title: string;
  content: string;
  createdAt: any;
}

export function RealtimePosts({ userId }: { userId: string }) {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const q = query(
      collection(db, 'posts'),
      where('userId', '==', userId),
      orderBy('createdAt', 'desc')
    );

    const unsubscribe = onSnapshot(q, (snapshot) => {
      const postsData = snapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data(),
      } as Post));

      setPosts(postsData);
      setLoading(false);
    });

    return () => unsubscribe();
  }, [userId]);

  if (loading) {
    return <div>Loading posts...</div>;
  }

  return (
    <div className="space-y-4">
      {posts.map(post => (
        <div key={post.id} className="p-4 border rounded">
          <h3 className="font-semibold">{post.title}</h3>
          <p className="text-gray-600">{post.content}</p>
        </div>
      ))}
    </div>
  );
}
```

```typescript
// app/(protected)/dashboard/page.tsx (updated)
import { RealtimePosts } from './RealtimePosts';

export default async function DashboardPage() {
  // ... previous code ...

  return (
    <div className="container mx-auto p-8">
      {/* ... static content ... */}

      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">Real-time Posts</h2>
        <RealtimePosts userId={user.uid} />
      </div>
    </div>
  );
}
```

## API Routes with Firebase

### CRUD API Route (`app/api/posts/route.ts`)

```typescript
// app/api/posts/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { cookies } from 'next/headers';
import { adminAuth, adminDb } from '@/lib/firebase/admin';
import { FieldValue } from 'firebase-admin/firestore';

async function verifyAuth(request: NextRequest) {
  const sessionCookie = cookies().get('session')?.value;

  if (!sessionCookie) {
    throw new Error('Unauthorized');
  }

  const decodedClaims = await adminAuth.verifySessionCookie(sessionCookie, true);
  return decodedClaims;
}

// GET /api/posts - List posts
export async function GET(request: NextRequest) {
  try {
    const user = await verifyAuth(request);

    const postsSnapshot = await adminDb
      .collection('posts')
      .where('userId', '==', user.uid)
      .orderBy('createdAt', 'desc')
      .limit(50)
      .get();

    const posts = postsSnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data(),
    }));

    return NextResponse.json({ posts });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 401 });
  }
}

// POST /api/posts - Create post
export async function POST(request: NextRequest) {
  try {
    const user = await verifyAuth(request);
    const { title, content } = await request.json();

    if (!title || !content) {
      return NextResponse.json(
        { error: 'Title and content required' },
        { status: 400 }
      );
    }

    const postRef = await adminDb.collection('posts').add({
      title,
      content,
      userId: user.uid,
      userEmail: user.email,
      createdAt: FieldValue.serverTimestamp(),
      updatedAt: FieldValue.serverTimestamp(),
    });

    return NextResponse.json({
      success: true,
      postId: postRef.id,
    });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 401 });
  }
}

// DELETE /api/posts/[id] - Delete post
export async function DELETE(request: NextRequest) {
  try {
    const user = await verifyAuth(request);
    const postId = request.nextUrl.searchParams.get('id');

    if (!postId) {
      return NextResponse.json({ error: 'Post ID required' }, { status: 400 });
    }

    // Verify ownership
    const postDoc = await adminDb.collection('posts').doc(postId).get();

    if (!postDoc.exists) {
      return NextResponse.json({ error: 'Post not found' }, { status: 404 });
    }

    if (postDoc.data()?.userId !== user.uid) {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
    }

    await postDoc.ref.delete();

    return NextResponse.json({ success: true });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 401 });
  }
}
```

## Best Practices

### 1. Separate Client and Server Firebase Configs

```typescript
// ✅ Good - Separate configs
// lib/firebase/client.ts - Client-side only
// lib/firebase/admin.ts - Server-side only

// ❌ Bad - Mixing client and admin
import { initializeApp } from 'firebase/app';
import { initializeApp as initializeAdminApp } from 'firebase-admin/app';
```

### 2. Use Session Cookies for SSR

```typescript
// ✅ Good - Session cookies for server verification
const sessionCookie = await adminAuth.createSessionCookie(idToken, {
  expiresIn: 60 * 60 * 24 * 5 * 1000
});

// ❌ Bad - Using ID tokens directly (expires in 1 hour)
```

### 3. Implement Proper Error Handling

```typescript
// ✅ Good - Graceful error handling
try {
  const user = await adminAuth.verifySessionCookie(sessionCookie);
} catch (error) {
  if (error.code === 'auth/session-cookie-expired') {
    redirect('/login');
  }
  // Handle other errors
}
```

### 4. Use Server Components for Initial Data

```typescript
// ✅ Good - Fetch initial data server-side
export default async function Page() {
  const posts = await fetchPosts(); // Server-side
  return <ClientPosts initialPosts={posts} />;
}

// ❌ Bad - Fetching all data client-side
'use client';
export default function Page() {
  const [posts, setPosts] = useState([]);
  useEffect(() => {
    fetchPosts().then(setPosts); // Client-side only
  }, []);
}
```

### 5. Optimize Firestore Reads

```typescript
// ✅ Good - Use pagination
const query = adminDb
  .collection('posts')
  .orderBy('createdAt', 'desc')
  .limit(20); // Paginate

// ❌ Bad - Fetching all documents
const query = adminDb.collection('posts'); // Could be thousands
```

## Resources

- **references/nextjs-app-router-auth.md**: Complete App Router authentication patterns
- **references/server-components-firebase.md**: Server Components with Firebase data fetching
- **references/firebase-admin-api-routes.md**: API Routes with Firebase Admin SDK
- **references/firebaseserverapp-ssr.md**: SSR with FirebaseServerApp
- **assets/auth-middleware.ts**: Production-ready authentication middleware
- **assets/firebase-hooks.ts**: Custom React hooks for Firebase
- **assets/api-helpers.ts**: Reusable API route helpers

## Common Pitfalls

- **Using Client SDK in Server Components**: Always use Firebase Admin SDK server-side
- **Not Setting HttpOnly Cookies**: Session cookies must be httpOnly for security
- **Mixing Auth States**: Keep client and server auth state in sync
- **Over-fetching Data**: Use pagination and limits in Firestore queries
- **Missing Error Boundaries**: Wrap client components with error boundaries
- **Not Handling Token Expiration**: Implement token refresh logic
- **Ignoring Security Rules**: Always implement Firestore security rules
- **Exposing Admin Keys**: Never expose Firebase Admin credentials client-side
