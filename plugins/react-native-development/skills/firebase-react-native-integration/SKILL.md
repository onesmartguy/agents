---
name: firebase-react-native-integration
description: Integrate Firebase with React Native and Expo including authentication, Firestore, Cloud Messaging, native features, and platform-specific configuration. Use when building React Native apps with Firebase authentication, push notifications, analytics, or real-time data.
---

# Firebase React Native Integration

Master Firebase integration with React Native and Expo, including authentication, Firestore, Cloud Messaging, native Firebase features, and platform-specific configuration for iOS and Android.

## When to Use This Skill

- Building React Native apps with Firebase authentication
- Implementing push notifications with Firebase Cloud Messaging
- Using Firestore real-time database in mobile apps
- Integrating Firebase Analytics and Crashlytics
- Building cross-platform apps with native Firebase features
- Implementing offline-first mobile apps with Firestore
- Using Firebase Storage for file uploads in React Native
- Migrating from Firebase JS SDK to React Native Firebase

## Firebase Integration Approaches

### React Native Firebase (@react-native-firebase)

**Pros:**
- Full access to native Firebase SDKs
- Better performance (native modules)
- All Firebase features available (Analytics, Crashlytics, Cloud Messaging, etc.)
- Official React Native library
- Works with bare React Native and Expo (with dev client)

**Cons:**
- Requires native builds (no Expo Go)
- More complex setup
- Platform-specific configuration required

**Use when:**
- You need native-only features (Crashlytics, Performance Monitoring)
- You need push notifications
- You want optimal performance
- You're building production apps

### Firebase JS SDK

**Pros:**
- Works with Expo Go
- Simpler setup
- Cross-platform (web compatibility)
- No native builds required

**Cons:**
- Missing native features (no Crashlytics, limited Analytics)
- No Cloud Messaging (push notifications)
- Slower performance for some operations

**Use when:**
- Rapid prototyping with Expo Go
- You only need Auth + Firestore + Storage
- You don't need push notifications
- You want web compatibility

## Installation

### React Native Firebase (Recommended)

```bash
# Install React Native Firebase
npm install @react-native-firebase/app

# Install modules you need
npm install @react-native-firebase/auth
npm install @react-native-firebase/firestore
npm install @react-native-firebase/storage
npm install @react-native-firebase/messaging
npm install @react-native-firebase/analytics
npm install @react-native-firebase/crashlytics

# For Expo projects
npx expo install expo-dev-client
npx expo prebuild
```

### Firebase JS SDK (Expo Go Compatible)

```bash
# Install Firebase JS SDK
npm install firebase

# For AsyncStorage persistence
npm install @react-native-async-storage/async-storage
```

## Project Structure

```
src/
├── config/
│   └── firebase.ts           # Firebase initialization
├── contexts/
│   └── AuthContext.tsx       # Auth provider
├── hooks/
│   ├── useAuth.ts
│   ├── useFirestore.ts
│   └── useNotifications.ts
├── services/
│   ├── auth.ts               # Auth operations
│   ├── firestore.ts          # Firestore operations
│   ├── storage.ts            # Storage operations
│   └── messaging.ts          # Push notifications
├── navigation/
│   └── index.tsx             # Navigation with auth
└── screens/
    ├── Auth/
    │   ├── LoginScreen.tsx
    │   └── SignUpScreen.tsx
    └── App/
        ├── HomeScreen.tsx
        └── ProfileScreen.tsx

# Platform-specific config
android/
└── app/
    └── google-services.json  # Android Firebase config

ios/
└── GoogleService-Info.plist  # iOS Firebase config

# Expo config
app.json                       # Expo configuration
```

## Setup and Configuration

### React Native Firebase Setup

#### 1. iOS Configuration (ios/Podfile)

```ruby
# ios/Podfile
platform :ios, '13.0'

target 'YourApp' do
  use_frameworks! :linkage => :static

  # Firebase pods
  pod 'Firebase/Core'
  pod 'Firebase/Auth'
  pod 'Firebase/Firestore'
  pod 'Firebase/Storage'
  pod 'Firebase/Messaging'
  pod 'Firebase/Analytics'

  # Rest of your config...
end

# After editing, run:
# cd ios && pod install && cd ..
```

#### 2. Android Configuration (android/build.gradle)

```gradle
// android/build.gradle
buildscript {
    dependencies {
        // Add Firebase Gradle plugin
        classpath 'com.google.gms:google-services:4.4.0'
    }
}
```

```gradle
// android/app/build.gradle
apply plugin: "com.android.application"
apply plugin: "com.google.gms.google-services"  // Add this line

android {
    // ... your config
}

dependencies {
    // ... other dependencies
}
```

#### 3. Firebase Config Files

Place downloaded config files:
- `google-services.json` → `android/app/google-services.json`
- `GoogleService-Info.plist` → `ios/YourApp/GoogleService-Info.plist`

#### 4. Expo Configuration (app.json)

```json
{
  "expo": {
    "name": "Your App",
    "plugins": [
      "@react-native-firebase/app",
      "@react-native-firebase/auth",
      "@react-native-firebase/crashlytics",
      [
        "@react-native-firebase/messaging",
        {
          "notificationIconColor": "#000000"
        }
      ]
    ],
    "ios": {
      "bundleIdentifier": "com.yourcompany.yourapp",
      "googleServicesFile": "./GoogleService-Info.plist"
    },
    "android": {
      "package": "com.yourcompany.yourapp",
      "googleServicesFile": "./google-services.json"
    }
  }
}
```

### Firebase Initialization

```typescript
// src/config/firebase.ts
import { initializeApp } from '@react-native-firebase/app';
import auth from '@react-native-firebase/auth';
import firestore from '@react-native-firebase/firestore';
import storage from '@react-native-firebase/storage';
import messaging from '@react-native-firebase/messaging';
import analytics from '@react-native-firebase/analytics';
import crashlytics from '@react-native-firebase/crashlytics';

// Firebase is auto-initialized with google-services.json / GoogleService-Info.plist
// No need to pass config manually

export { auth, firestore, storage, messaging, analytics, crashlytics };

// Enable offline persistence
firestore().settings({
  persistence: true,
  cacheSizeBytes: firestore.CACHE_SIZE_UNLIMITED,
});

// Enable Crashlytics collection
if (__DEV__) {
  crashlytics().setCrashlyticsCollectionEnabled(false);
} else {
  crashlytics().setCrashlyticsCollectionEnabled(true);
}
```

## Authentication

### Auth Context Provider

```typescript
// src/contexts/AuthContext.tsx
import React, { createContext, useContext, useEffect, useState } from 'react';
import auth, { FirebaseAuthTypes } from '@react-native-firebase/auth';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface AuthContextType {
  user: FirebaseAuthTypes.User | null;
  loading: boolean;
  signIn: (email: string, password: string) => Promise<void>;
  signUp: (email: string, password: string) => Promise<void>;
  signOut: () => Promise<void>;
  signInWithGoogle: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<FirebaseAuthTypes.User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = auth().onAuthStateChanged(async (user) => {
      setUser(user);
      setLoading(false);

      // Persist user ID for quick access
      if (user) {
        await AsyncStorage.setItem('userId', user.uid);
      } else {
        await AsyncStorage.removeItem('userId');
      }
    });

    return unsubscribe;
  }, []);

  const signIn = async (email: string, password: string) => {
    try {
      await auth().signInWithEmailAndPassword(email, password);
    } catch (error: any) {
      throw new Error(error.message);
    }
  };

  const signUp = async (email: string, password: string) => {
    try {
      const { user } = await auth().createUserWithEmailAndPassword(email, password);

      // Create user document in Firestore
      await firestore().collection('users').doc(user.uid).set({
        email: user.email,
        createdAt: firestore.FieldValue.serverTimestamp(),
      });
    } catch (error: any) {
      throw new Error(error.message);
    }
  };

  const signOut = async () => {
    try {
      await auth().signOut();
    } catch (error: any) {
      throw new Error(error.message);
    }
  };

  const signInWithGoogle = async () => {
    // Implement Google Sign-In
    // Requires @react-native-google-signin/google-signin
    throw new Error('Not implemented');
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        signIn,
        signUp,
        signOut,
        signInWithGoogle,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
```

### Login Screen

```typescript
// src/screens/Auth/LoginScreen.tsx
import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Alert,
  ActivityIndicator,
} from 'react-native';
import { useAuth } from '../../contexts/AuthContext';

export default function LoginScreen({ navigation }: any) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const { signIn } = useAuth();

  const handleLogin = async () => {
    if (!email || !password) {
      Alert.alert('Error', 'Please fill in all fields');
      return;
    }

    setLoading(true);
    try {
      await signIn(email, password);
      // Navigation handled by auth state change
    } catch (error: any) {
      Alert.alert('Login Error', error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome Back</Text>

      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        autoCapitalize="none"
        keyboardType="email-address"
      />

      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />

      <TouchableOpacity
        style={styles.button}
        onPress={handleLogin}
        disabled={loading}
      >
        {loading ? (
          <ActivityIndicator color="#fff" />
        ) : (
          <Text style={styles.buttonText}>Sign In</Text>
        )}
      </TouchableOpacity>

      <TouchableOpacity onPress={() => navigation.navigate('SignUp')}>
        <Text style={styles.linkText}>
          Don't have an account? Sign Up
        </Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 30,
    textAlign: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 15,
    marginBottom: 15,
    fontSize: 16,
  },
  button: {
    backgroundColor: '#007AFF',
    borderRadius: 8,
    padding: 15,
    alignItems: 'center',
    marginTop: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  },
  linkText: {
    color: '#007AFF',
    textAlign: 'center',
    marginTop: 20,
  },
});
```

## Firestore Operations

### Custom Firestore Hook

```typescript
// src/hooks/useFirestore.ts
import { useEffect, useState } from 'react';
import firestore, { FirebaseFirestoreTypes } from '@react-native-firebase/firestore';

interface UseFirestoreOptions {
  collection: string;
  where?: [string, FirebaseFirestoreTypes.WhereFilterOp, any][];
  orderBy?: [string, 'asc' | 'desc'];
  limit?: number;
}

export function useFirestore<T>({
  collection: collectionName,
  where = [],
  orderBy,
  limit,
}: UseFirestoreOptions) {
  const [data, setData] = useState<T[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    let query: FirebaseFirestoreTypes.Query = firestore().collection(collectionName);

    // Apply where clauses
    where.forEach(([field, operator, value]) => {
      query = query.where(field, operator, value);
    });

    // Apply ordering
    if (orderBy) {
      query = query.orderBy(orderBy[0], orderBy[1]);
    }

    // Apply limit
    if (limit) {
      query = query.limit(limit);
    }

    // Subscribe to real-time updates
    const unsubscribe = query.onSnapshot(
      (snapshot) => {
        const items = snapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data(),
        })) as T[];

        setData(items);
        setLoading(false);
      },
      (err) => {
        setError(err);
        setLoading(false);
      }
    );

    return () => unsubscribe();
  }, [collectionName, JSON.stringify(where), orderBy, limit]);

  return { data, loading, error };
}
```

### Firestore Service

```typescript
// src/services/firestore.ts
import firestore from '@react-native-firebase/firestore';

export interface Post {
  id?: string;
  title: string;
  content: string;
  userId: string;
  createdAt?: any;
  updatedAt?: any;
}

export const firestoreService = {
  // Create
  async createPost(post: Omit<Post, 'id'>): Promise<string> {
    const docRef = await firestore()
      .collection('posts')
      .add({
        ...post,
        createdAt: firestore.FieldValue.serverTimestamp(),
        updatedAt: firestore.FieldValue.serverTimestamp(),
      });

    return docRef.id;
  },

  // Read
  async getPost(postId: string): Promise<Post | null> {
    const doc = await firestore().collection('posts').doc(postId).get();

    if (!doc.exists) {
      return null;
    }

    return {
      id: doc.id,
      ...doc.data(),
    } as Post;
  },

  // Update
  async updatePost(postId: string, updates: Partial<Post>): Promise<void> {
    await firestore()
      .collection('posts')
      .doc(postId)
      .update({
        ...updates,
        updatedAt: firestore.FieldValue.serverTimestamp(),
      });
  },

  // Delete
  async deletePost(postId: string): Promise<void> {
    await firestore().collection('posts').doc(postId).delete();
  },

  // Batch operations
  async batchCreate(posts: Omit<Post, 'id'>[]): Promise<void> {
    const batch = firestore().batch();

    posts.forEach(post => {
      const docRef = firestore().collection('posts').doc();
      batch.set(docRef, {
        ...post,
        createdAt: firestore.FieldValue.serverTimestamp(),
        updatedAt: firestore.FieldValue.serverTimestamp(),
      });
    });

    await batch.commit();
  },
};
```

### Using Firestore in Components

```typescript
// src/screens/App/HomeScreen.tsx
import React from 'react';
import { View, Text, FlatList, StyleSheet, ActivityIndicator } from 'react-native';
import { useAuth } from '../../contexts/AuthContext';
import { useFirestore } from '../../hooks/useFirestore';
import { Post } from '../../services/firestore';

export default function HomeScreen() {
  const { user } = useAuth();

  const { data: posts, loading, error } = useFirestore<Post>({
    collection: 'posts',
    where: [['userId', '==', user?.uid]],
    orderBy: ['createdAt', 'desc'],
    limit: 20,
  });

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.center}>
        <Text>Error: {error.message}</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>My Posts</Text>

      <FlatList
        data={posts}
        keyExtractor={(item) => item.id!}
        renderItem={({ item }) => (
          <View style={styles.postCard}>
            <Text style={styles.postTitle}>{item.title}</Text>
            <Text style={styles.postContent}>{item.content}</Text>
          </View>
        )}
        ListEmptyComponent={
          <Text style={styles.emptyText}>No posts yet</Text>
        }
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  postCard: {
    backgroundColor: '#fff',
    padding: 15,
    borderRadius: 8,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  postTitle: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 5,
  },
  postContent: {
    fontSize: 14,
    color: '#666',
  },
  emptyText: {
    textAlign: 'center',
    color: '#999',
    marginTop: 50,
  },
});
```

## Push Notifications (Cloud Messaging)

### Request Permission and Get Token

```typescript
// src/services/messaging.ts
import messaging from '@react-native-firebase/messaging';
import { Platform, Alert } from 'react-native';

export const messagingService = {
  async requestPermission(): Promise<boolean> {
    const authStatus = await messaging().requestPermission();
    const enabled =
      authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
      authStatus === messaging.AuthorizationStatus.PROVISIONAL;

    if (enabled) {
      console.log('Authorization status:', authStatus);
    }

    return enabled;
  },

  async getToken(): Promise<string | null> {
    try {
      const token = await messaging().getToken();
      console.log('FCM Token:', token);
      return token;
    } catch (error) {
      console.error('Error getting FCM token:', error);
      return null;
    }
  },

  async saveTokenToFirestore(userId: string, token: string): Promise<void> {
    await firestore().collection('users').doc(userId).update({
      fcmTokens: firestore.FieldValue.arrayUnion(token),
    });
  },

  onTokenRefresh(callback: (token: string) => void) {
    return messaging().onTokenRefresh(callback);
  },

  onMessage(callback: (message: any) => void) {
    return messaging().onMessage(callback);
  },

  setBackgroundMessageHandler(handler: (message: any) => Promise<void>) {
    messaging().setBackgroundMessageHandler(handler);
  },
};
```

### Setup Notifications in App

```typescript
// App.tsx or index.tsx
import React, { useEffect } from 'react';
import messaging from '@react-native-firebase/messaging';
import { Alert } from 'react-native';
import { messagingService } from './src/services/messaging';

// Background message handler (must be outside component)
messaging().setBackgroundMessageHandler(async remoteMessage => {
  console.log('Background message:', remoteMessage);
});

function App() {
  useEffect(() => {
    // Request permission
    messagingService.requestPermission();

    // Get FCM token
    messagingService.getToken().then(token => {
      if (token) {
        // Save to Firestore or backend
        console.log('FCM Token:', token);
      }
    });

    // Listen for token refresh
    const unsubscribeTokenRefresh = messagingService.onTokenRefresh(token => {
      console.log('Token refreshed:', token);
    });

    // Handle foreground messages
    const unsubscribeMessage = messagingService.onMessage(remoteMessage => {
      Alert.alert(
        remoteMessage.notification?.title || 'New Message',
        remoteMessage.notification?.body
      );
    });

    // Handle notification tap (app opened from notification)
    messaging()
      .getInitialNotification()
      .then(remoteMessage => {
        if (remoteMessage) {
          console.log('Notification caused app to open:', remoteMessage);
        }
      });

    // Handle notification tap (app in background)
    const unsubscribeNotificationOpen = messaging().onNotificationOpenedApp(
      remoteMessage => {
        console.log('Notification opened app from background:', remoteMessage);
      }
    );

    return () => {
      unsubscribeTokenRefresh();
      unsubscribeMessage();
      unsubscribeNotificationOpen();
    };
  }, []);

  return <YourAppComponent />;
}
```

## Storage Operations

```typescript
// src/services/storage.ts
import storage from '@react-native-firebase/storage';
import { Platform } from 'react-native';

export const storageService = {
  async uploadImage(
    uri: string,
    path: string,
    onProgress?: (progress: number) => void
  ): Promise<string> {
    const filename = uri.substring(uri.lastIndexOf('/') + 1);
    const reference = storage().ref(`${path}/${filename}`);

    // Handle platform-specific URI
    const fileUri = Platform.OS === 'ios' ? uri.replace('file://', '') : uri;

    const task = reference.putFile(fileUri);

    // Monitor progress
    if (onProgress) {
      task.on('state_changed', snapshot => {
        const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        onProgress(progress);
      });
    }

    await task;

    // Get download URL
    const url = await reference.getDownloadURL();
    return url;
  },

  async deleteFile(path: string): Promise<void> {
    const reference = storage().ref(path);
    await reference.delete();
  },

  async listFiles(path: string): Promise<string[]> {
    const reference = storage().ref(path);
    const result = await reference.list();
    return result.items.map(item => item.fullPath);
  },
};
```

## Best Practices

### 1. Enable Offline Persistence

```typescript
// Enable Firestore offline persistence
firestore().settings({
  persistence: true,
  cacheSizeBytes: firestore.CACHE_SIZE_UNLIMITED,
});
```

### 2. Handle Platform Differences

```typescript
// iOS vs Android specific code
import { Platform } from 'react-native';

const config = Platform.select({
  ios: {
    // iOS-specific config
  },
  android: {
    // Android-specific config
  },
});
```

### 3. Optimize Firestore Queries

```typescript
// ✅ Good - Use indexes and limits
const query = firestore()
  .collection('posts')
  .where('userId', '==', userId)
  .orderBy('createdAt', 'desc')
  .limit(20);

// ❌ Bad - Fetching everything
const query = firestore().collection('posts');
```

### 4. Unsubscribe from Listeners

```typescript
// Always clean up listeners
useEffect(() => {
  const unsubscribe = firestore()
    .collection('posts')
    .onSnapshot(snapshot => {
      // Handle updates
    });

  return () => unsubscribe(); // Cleanup
}, []);
```

### 5. Handle Auth State Properly

```typescript
// Wait for auth state to initialize
if (loading) {
  return <LoadingScreen />;
}

return user ? <AuthenticatedApp /> : <AuthFlow />;
```

## Resources

- **references/react-native-firebase-setup.md**: Complete setup guide
- **references/expo-firebase-config.md**: Expo-specific configuration
- **references/push-notifications-guide.md**: Comprehensive push notification setup
- **references/offline-firestore.md**: Offline data sync patterns
- **assets/AuthContext.tsx**: Production-ready auth context
- **assets/FirestoreHooks.ts**: Reusable Firestore hooks
- **assets/NotificationService.ts**: Complete notification service

## Common Pitfalls

- **Forgetting to Install Pods**: Always run `cd ios && pod install` after adding Firebase modules
- **Missing Google Services Files**: Ensure `google-services.json` and `GoogleService-Info.plist` are in correct locations
- **Not Handling Permissions**: Request notification permissions before getting FCM token
- **Ignoring Offline State**: Firebase SDK handles offline, but UI should show offline status
- **Over-querying Firestore**: Use pagination and limits to reduce reads
- **Not Cleaning Up Listeners**: Always unsubscribe to prevent memory leaks
- **Expo Go Limitations**: React Native Firebase requires custom dev client or bare workflow
- **Bundle ID Mismatch**: Ensure bundle IDs in code match Firebase console configuration
