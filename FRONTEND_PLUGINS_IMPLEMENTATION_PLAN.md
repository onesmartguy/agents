# Frontend & Testing Plugins Implementation Plan

## Executive Summary

This document outlines the comprehensive implementation plan for creating six focused frontend and testing plugins for the Claude Code plugin marketplace:

1. **react-development** - Modern React 18+ development with hooks, performance optimization, and testing
2. **nextjs-development** - Next.js 14+ with App Router, RSC, and full-stack patterns
3. **react-native-development** - React Native with Expo SDK 51+ for cross-platform mobile
4. **tailwind-styling** - Tailwind CSS with CVA, design systems, and modern styling patterns
5. **playwright-testing** - E2E testing with Playwright and modern testing strategies
6. **react-native-expo** - Specialized Expo workflows, EAS Build, and mobile-specific patterns

These plugins follow the established patterns from the `python-development` and `javascript-typescript` plugins and incorporate domain expertise from the payk12 project's React/Next.js/React Native architecture.

---

## Analysis Summary

### Existing Plugins (Reference)

**python-development Plugin:**
- 3 Agents (python-pro, django-pro, fastapi-pro)
- 1 Command (python-scaffold)
- 5 Skills

**javascript-typescript Plugin:**
- 2 Agents (javascript-pro, typescript-pro)
- 1 Command (typescript-scaffold)
- 4 Skills (javascript-testing-patterns, modern-javascript-patterns, nodejs-backend-patterns, typescript-advanced-types)

### payk12 Agents Analysis

**react-pro Agent:**
- **Focus**: Modern React 18+ with Hooks, Context API, Suspense
- **Key Technologies**: Redux Toolkit, Zustand, React Query, Jest, React Testing Library
- **Expertise Areas**:
  - Component architecture (composition, reusable components, SOLID principles)
  - Performance optimization (memoization, code splitting, list virtualization)
  - State management (strategic placement, server-side state with React Query)
  - Testing (user-centric with React Testing Library)
  - Modern patterns (Hooks mastery, error boundaries)

**nextjs-pro Agent:**
- **Focus**: Next.js 14+ with App Router, SSR/SSG/ISR, React Server Components
- **Key Technologies**: TypeScript, API routes, middleware, deployment on Vercel
- **Expertise Areas**:
  - Rendering strategies (SSR, SSG, ISR, client-side)
  - App Router mastery (layouts, loading states, error boundaries, parallel routes)
  - Performance optimization (image optimization, bundle analysis, Core Web Vitals)
  - Full-stack development (API routes, middleware, database integration)
  - SEO excellence (meta tags, structured data, sitemap generation)

**react-native-pro Agent:**
- **Focus**: React Native 0.74+ with Expo SDK 51+
- **Key Technologies**: TypeScript, React Navigation, Zustand, TanStack Query, Reanimated, Gesture Handler
- **Expertise Areas**:
  - Expo ecosystem (managed workflow, EAS Build, expo-dev-client, OTA updates)
  - State management (Zustand v5, TanStack Query v5)
  - Navigation (Expo Router v3, React Navigation v6, deep linking)
  - UI/Animation (Reanimated 3, Gesture Handler, Shopify Restyle)
  - Native features (camera, location, NFC, Bluetooth, biometrics)

**typescript-pro Agent:**
- **Focus**: Advanced TypeScript, type systems, architecture
- **Key Technologies**: Generics, conditional types, mapped types, decorators
- **Expertise Areas**:
  - Advanced type system (complex generics, type inference)
  - Architecture design patterns
  - Type-safe development
  - Testing strategies
  - Tooling mastery (tsconfig, bundlers)

### payk12 Patterns (from docs)

**Component Styling Pattern:**
- **NO CSS FILES** - Tailwind only
- **CVA for variants** - class-variance-authority for type-safe styling
- **Shared variants** - Component styles in `/lib/variants/`
- **Automatic class merging** - tailwind-merge integration
- **Type safety** - VariantProps helper

**State Management:**
- **TanStack Query** - Server state (API data, caching, refetching)
- **Zustand** - Client state (UI state, selections, filters)
- **Clear separation** - Never mix server and client state

---

## Plugin 1: react-development

### Plugin Metadata

```json
{
  "name": "react-development",
  "source": "./plugins/react-development",
  "description": "Modern React 18+ development with hooks, performance optimization, state management, and testing",
  "version": "1.2.2",
  "author": {
    "name": "Seth Hobson",
    "url": "https://github.com/wshobson"
  },
  "homepage": "https://github.com/wshobson/agents",
  "repository": "https://github.com/wshobson/agents",
  "license": "MIT",
  "keywords": [
    "react",
    "hooks",
    "components",
    "state-management",
    "essential"
  ],
  "category": "languages",
  "strict": false
}
```

### Agents (3 total, all Sonnet model)

#### 1. react-pro.md

**Frontmatter:**
```yaml
---
name: react-pro
description: Master React 18+ with Hooks, Context API, Suspense, and modern patterns. Expert in component architecture, performance optimization, and state management. Use PROACTIVELY for React development, component design, or performance optimization.
model: sonnet
---
```

**Content Focus:**
- React 18+ features (Concurrent features, automatic batching, transitions)
- Functional components and Hooks (useState, useEffect, useCallback, useMemo, useRef)
- Component architecture (composition, reusable components, prop patterns)
- Performance optimization (React.memo, useMemo, useCallback, code splitting, lazy loading)
- State management (Context API, Zustand, Redux Toolkit, React Query/TanStack Query)
- Error boundaries and Suspense
- Testing with Jest and React Testing Library
- Modern patterns (compound components, render props, custom hooks)

#### 2. react-query-pro.md

**Frontmatter:**
```yaml
---
name: react-query-pro
description: Master TanStack Query (React Query) for server state management, caching, and data synchronization. Expert in query optimization and async state patterns. Use PROACTIVELY for API integration, caching strategies, or server state management.
model: sonnet
---
```

**Content Focus:**
- TanStack Query v5 fundamentals
- Query and mutation patterns
- Caching strategies and invalidation
- Optimistic updates
- Infinite queries and pagination
- Query keys and organization
- DevTools usage
- Integration with TypeScript
- Error handling and retry logic
- Performance optimization

#### 3. react-testing-pro.md

**Frontmatter:**
```yaml
---
name: react-testing-pro
description: Expert in testing React applications with Jest, React Testing Library, and modern testing patterns. Focuses on user-centric testing and comprehensive coverage. Use PROACTIVELY for writing tests, test architecture, or testing strategy.
model: sonnet
---
```

**Content Focus:**
- React Testing Library philosophy (user-centric testing)
- Testing components, hooks, and context
- Mocking and test doubles
- Async testing (waitFor, findBy queries)
- Testing user interactions
- Snapshot testing
- Coverage strategies
- Integration vs unit tests
- Testing best practices
- Accessibility testing

### Commands (1 total)

#### react-scaffold.md

**Purpose:** Comprehensive React project scaffolding

**Content Structure:**

##### 1. Analyze Project Type
- **Vite + React + TypeScript**: Modern, fast development
- **Create React App (deprecated note)**: Legacy support
- **React Component Library**: Reusable component package
- **React + TanStack Router**: Advanced routing
- **Micro-frontend**: Module federation setup

##### 2. Initialize with Vite

```bash
# Create new Vite project with React + TypeScript
npm create vite@latest my-react-app -- --template react-ts
cd my-react-app

# Install core dependencies
npm install

# Install development tools
npm install -D @testing-library/react @testing-library/jest-dom @testing-library/user-event vitest jsdom
npm install -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
npm install -D prettier eslint-config-prettier
npm install -D @vitejs/plugin-react

# Install state management
npm install zustand @tanstack/react-query

# Install routing
npm install react-router-dom

# Install UI utilities
npm install clsx tailwind-merge
```

##### 3. Generate Project Structure

```
my-react-app/
├── src/
│   ├── components/
│   │   ├── ui/
│   │   │   ├── Button.tsx
│   │   │   └── Button.test.tsx
│   │   └── features/
│   ├── hooks/
│   │   └── useLocalStorage.ts
│   ├── lib/
│   │   ├── utils.ts
│   │   └── query-client.ts
│   ├── stores/
│   │   └── useAppStore.ts
│   ├── types/
│   │   └── index.ts
│   ├── App.tsx
│   └── main.tsx
├── tests/
│   ├── setup.ts
│   └── test-utils.tsx
├── vite.config.ts
├── tsconfig.json
├── .eslintrc.cjs
├── .prettierrc
└── package.json
```

##### 4. Configuration Files

Complete vite.config.ts, tsconfig.json, test setup, ESLint, Prettier configs

### Skills (5 total)

#### 1. react-hooks-mastery/SKILL.md

**Frontmatter:**
```yaml
---
name: react-hooks-mastery
description: Master React Hooks including useState, useEffect, useCallback, useMemo, useRef, and custom hooks. Use when building React components, optimizing performance, or creating reusable logic with hooks.
---
```

**Content Focus:**
- All built-in hooks with examples
- Custom hook patterns
- Rules of Hooks
- Performance implications
- Common pitfalls
- Advanced patterns

#### 2. react-performance-optimization/SKILL.md

**Frontmatter:**
```yaml
---
name: react-performance-optimization
description: Optimize React applications with memoization, code splitting, lazy loading, and virtualization techniques. Use when experiencing performance issues or building high-performance UIs.
---
```

**Content Focus:**
- React.memo and when to use it
- useMemo and useCallback
- Code splitting with lazy() and Suspense
- List virtualization
- Bundle optimization
- Performance profiling tools

#### 3. react-state-management/SKILL.md

**Frontmatter:**
```yaml
---
name: react-state-management
description: Implement effective state management with Context API, Zustand, Redux Toolkit, and TanStack Query. Use when architecting state solutions or migrating state management libraries.
---
```

**Content Focus:**
- Strategic state placement
- Context API patterns
- Zustand for client state
- Redux Toolkit for complex state
- TanStack Query for server state
- State architecture decisions

#### 4. react-component-patterns/SKILL.md

**Frontmatter:**
```yaml
---
name: react-component-patterns
description: Build scalable component architectures with composition patterns, compound components, render props, and HOCs. Use when designing reusable component APIs or refactoring component structures.
---
```

**Content Focus:**
- Composition patterns
- Compound components
- Render props
- Higher-order components
- Custom hooks for logic reuse
- Component API design

#### 5. react-testing-patterns/SKILL.md

**Frontmatter:**
```yaml
---
name: react-testing-patterns
description: Test React components effectively with React Testing Library, focusing on user behavior rather than implementation. Use when writing tests or establishing testing standards.
---
```

**Content Focus:**
- User-centric testing approach
- Query priorities (getByRole, getByText, etc.)
- Testing async operations
- Mocking strategies
- Testing context and hooks
- Best practices

---

## Plugin 2: nextjs-development

### Plugin Metadata

```json
{
  "name": "nextjs-development",
  "source": "./plugins/nextjs-development",
  "description": "Next.js 14+ development with App Router, React Server Components, SSR/SSG, and full-stack patterns",
  "version": "1.2.2",
  "keywords": [
    "nextjs",
    "app-router",
    "rsc",
    "ssr",
    "ssg",
    "essential"
  ],
  "category": "languages",
  "strict": false
}
```

### Agents (3 total, all Sonnet model)

#### 1. nextjs-pro.md
- Next.js 14+ with App Router
- RSC (React Server Components)
- Rendering strategies
- Performance optimization
- SEO

#### 2. nextjs-api-pro.md
- API Routes and Route Handlers
- Server Actions
- Middleware
- Authentication patterns
- Database integration

#### 3. nextjs-deployment-pro.md
- Vercel deployment
- Self-hosting strategies
- Edge runtime
- Performance monitoring
- Build optimization

### Commands (1 total)

#### nextjs-scaffold.md
- Create Next.js projects with App Router
- Configure for different deployment targets
- Set up authentication
- Database integration
- Testing setup

### Skills (5 total)

1. **app-router-patterns** - App Router, layouts, loading states
2. **server-components** - RSC patterns, server/client boundaries
3. **nextjs-data-fetching** - SSR, SSG, ISR, streaming
4. **nextjs-api-routes** - Route handlers, Server Actions
5. **nextjs-optimization** - Image optimization, bundle analysis, Core Web Vitals

---

## Plugin 3: react-native-development

### Plugin Metadata

```json
{
  "name": "react-native-development",
  "source": "./plugins/react-native-development",
  "description": "React Native 0.74+ with modern architecture, state management, and native integrations",
  "version": "1.2.2",
  "keywords": [
    "react-native",
    "mobile",
    "ios",
    "android",
    "cross-platform"
  ],
  "category": "languages",
  "strict": false
}
```

### Agents (3 total, all Sonnet model)

#### 1. react-native-pro.md
- React Native 0.74+ fundamentals
- Component architecture
- State management (Zustand, TanStack Query)
- Navigation (React Navigation v6)
- Performance optimization

#### 2. react-native-ui-pro.md
- UI/UX patterns for mobile
- React Native Reanimated 3
- Gesture Handler
- Responsive design
- Platform-specific styling

#### 3. react-native-native-modules-pro.md
- Native module integration
- Bridging to native code
- Platform-specific implementations
- Third-party library integration
- Debugging native code

### Commands (1 total)

#### react-native-scaffold.md
- Initialize React Native projects
- Configure navigation
- Set up state management
- Testing infrastructure
- Platform-specific setup

### Skills (5 total)

1. **react-native-navigation** - React Navigation v6, deep linking
2. **react-native-animations** - Reanimated 3, Gesture Handler
3. **react-native-state-management** - Zustand + TanStack Query patterns
4. **react-native-performance** - FlatList optimization, memory management
5. **react-native-platform-specific** - iOS/Android differences, platform code

---

## Plugin 4: tailwind-styling

### Plugin Metadata

```json
{
  "name": "tailwind-styling",
  "source": "./plugins/tailwind-styling",
  "description": "Tailwind CSS with CVA, design systems, and modern styling patterns for scalable applications",
  "version": "1.2.2",
  "keywords": [
    "tailwind",
    "css",
    "styling",
    "design-system",
    "cva"
  ],
  "category": "development",
  "strict": false
}
```

### Agents (2 total, all Sonnet model)

#### 1. tailwind-pro.md
- Tailwind CSS configuration
- Utility-first CSS patterns
- Custom configuration
- Plugin development
- Performance optimization

#### 2. design-system-pro.md
- Building design systems with Tailwind
- Component variant systems (CVA)
- Theming and dark mode
- Accessibility
- Documentation

### Commands (1 total)

#### tailwind-setup.md
- Initialize Tailwind in projects
- Configure for different frameworks
- Set up CVA
- Create design tokens
- Component library setup

### Skills (4 total)

1. **tailwind-configuration** - Config optimization, plugins, themes
2. **cva-variant-patterns** - class-variance-authority for type-safe variants
3. **design-tokens** - Color systems, spacing, typography
4. **responsive-design-patterns** - Mobile-first, breakpoints, containers

---

## Plugin 5: playwright-testing

### Plugin Metadata

```json
{
  "name": "playwright-testing",
  "source": "./plugins/playwright-testing",
  "description": "End-to-end testing with Playwright, modern test automation, and CI/CD integration",
  "version": "1.2.2",
  "keywords": [
    "playwright",
    "e2e",
    "testing",
    "automation",
    "ci-cd"
  ],
  "category": "testing",
  "strict": false
}
```

### Agents (2 total, all Sonnet model)

#### 1. playwright-pro.md
- Playwright fundamentals
- Page Object Model
- Test organization
- Debugging strategies
- Parallel execution

#### 2. playwright-ci-pro.md
- CI/CD integration
- Docker containers
- Test reporting
- Performance testing
- Visual regression

### Commands (1 total)

#### playwright-scaffold.md
- Initialize Playwright
- Set up page objects
- Configure for different browsers
- CI/CD integration
- Reporting setup

### Skills (4 total)

1. **playwright-patterns** - Locators, actions, assertions
2. **page-object-model** - Scalable test architecture
3. **playwright-ci-integration** - GitHub Actions, GitLab CI
4. **visual-regression-testing** - Screenshot comparison

---

## Plugin 6: react-native-expo

### Plugin Metadata

```json
{
  "name": "react-native-expo",
  "source": "./plugins/react-native-expo",
  "description": "Expo SDK 51+ workflows, EAS Build, OTA updates, and managed/bare workflow patterns",
  "version": "1.2.2",
  "keywords": [
    "expo",
    "react-native",
    "eas-build",
    "mobile",
    "expo-router"
  ],
  "category": "languages",
  "strict": false
}
```

### Agents (3 total, all Sonnet model)

#### 1. expo-pro.md
- Expo SDK 51+ features
- Managed vs bare workflow
- EAS Build configuration
- OTA updates
- Expo modules

#### 2. expo-router-pro.md
- Expo Router v3 (file-based routing)
- Navigation patterns
- Deep linking
- Layouts and nesting
- TypeScript integration

#### 3. eas-build-pro.md
- EAS Build configuration
- Build profiles
- CI/CD integration
- App signing
- Distribution

### Commands (1 total)

#### expo-scaffold.md
- Initialize Expo projects
- Configure EAS Build
- Set up Expo Router
- Environment configuration
- Development builds

### Skills (5 total)

1. **expo-managed-workflow** - Managed workflow best practices
2. **expo-router-v3** - File-based routing patterns
3. **eas-build-configuration** - Build profiles, environments
4. **expo-modules** - Custom native modules with Expo
5. **expo-ota-updates** - Over-the-air update strategies

---

## Implementation Timeline

### Phase 1: Foundation (Week 1)
- [ ] Create all 6 plugin directory structures
- [ ] Set up marketplace.json entries
- [ ] Create base README.md files

### Phase 2: React & Next.js Plugins (Weeks 2-4)
- [ ] react-development plugin (3 agents, 1 command, 5 skills)
- [ ] nextjs-development plugin (3 agents, 1 command, 5 skills)

### Phase 3: React Native Plugins (Weeks 5-7)
- [ ] react-native-development plugin (3 agents, 1 command, 5 skills)
- [ ] react-native-expo plugin (3 agents, 1 command, 5 skills)

### Phase 4: Supporting Plugins (Weeks 8-9)
- [ ] tailwind-styling plugin (2 agents, 1 command, 4 skills)
- [ ] playwright-testing plugin (2 agents, 1 command, 4 skills)

### Phase 5: Testing & Refinement (Week 10)
- [ ] Test all agents with sample prompts
- [ ] Verify skill activation
- [ ] Test scaffold commands
- [ ] Review consistency

### Phase 6: Documentation & Release (Week 11)
- [ ] Comprehensive documentation
- [ ] Update marketplace catalog
- [ ] Usage examples
- [ ] Publish plugins

---

## File Structure Example (react-development)

```
plugins/react-development/
├── agents/
│   ├── react-pro.md
│   ├── react-query-pro.md
│   └── react-testing-pro.md
├── commands/
│   └── react-scaffold.md
└── skills/
    ├── react-hooks-mastery/
    │   ├── SKILL.md
    │   └── references/
    │       └── hooks-api-reference.md
    ├── react-performance-optimization/
    │   ├── SKILL.md
    │   └── references/
    │       └── optimization-techniques.md
    ├── react-state-management/
    │   ├── SKILL.md
    │   └── references/
    │       ├── zustand-patterns.md
    │       └── tanstack-query-patterns.md
    ├── react-component-patterns/
    │   ├── SKILL.md
    │   └── references/
    │       └── advanced-patterns.md
    └── react-testing-patterns/
        ├── SKILL.md
        └── references/
            └── testing-library-queries.md
```

---

## Key Design Decisions

### 1. Separate Plugins for Each Technology

**Rationale**:
- Focused, minimal token usage
- Users install only what they need
- Clear separation of concerns
- Easier maintenance

### 2. Expo as Separate Plugin

**Rationale**:
- Expo has distinct workflow patterns
- EAS Build and OTA updates are specialized
- Managed vs bare workflow deserves focused attention
- Expo Router v3 is file-based (different from React Navigation)

### 3. Tailwind as Dedicated Plugin

**Rationale**:
- CVA (class-variance-authority) patterns are complex
- Design system architecture deserves focused expertise
- Tailwind configuration is framework-agnostic
- payk12 pattern: NO CSS FILES, CVA for variants

### 4. State Management Agents

**Rationale**:
- TanStack Query (React Query) deserves dedicated agent
- Server state vs client state separation is critical
- Follows payk12 pattern: TanStack Query + Zustand

### 5. Playwright Separate from React

**Rationale**:
- E2E testing is cross-framework
- CI/CD integration is specialized knowledge
- Page Object Model patterns are framework-agnostic
- Can be used with React, Next.js, Vue, etc.

---

## Success Criteria

### Plugin Quality
- [ ] Comprehensive agents with examples
- [ ] Working scaffold commands
- [ ] Progressive disclosure in skills
- [ ] Consistent naming and style

### Technical Accuracy
- [ ] Code examples work
- [ ] Architecture patterns match best practices
- [ ] Security considerations documented
- [ ] Performance guidance included

### Marketplace Integration
- [ ] Proper marketplace.json entries
- [ ] Consistent versioning
- [ ] Optimized keywords
- [ ] Correct categories

### User Experience
- [ ] Clear activation criteria
- [ ] Proactive agent triggering
- [ ] Skills load when needed
- [ ] Production-ready scaffolding

---

## Alignment with payk12 Patterns

### Component Styling (Tailwind + CVA)
- NO CSS FILES policy
- CVA for type-safe variants
- tailwind-merge integration
- Shared variants in `/lib/variants/`

### State Management
- TanStack Query for server state
- Zustand for client state
- Clear separation of concerns
- Type-safe with TypeScript

### React Native
- Expo SDK 51+ managed workflow
- Zustand v5 + TanStack Query v5
- Expo Router v3 (file-based)
- Shopify Restyle for theming
- React Native Reanimated 3

### Testing
- React Testing Library (user-centric)
- Playwright for E2E
- Jest/Vitest for unit tests
- Integration tests with real databases

---

## Total Plugin Statistics

**6 Plugins:**
- react-development: 3 agents + 1 command + 5 skills = 9 components
- nextjs-development: 3 agents + 1 command + 5 skills = 9 components
- react-native-development: 3 agents + 1 command + 5 skills = 9 components
- tailwind-styling: 2 agents + 1 command + 4 skills = 7 components
- playwright-testing: 2 agents + 1 command + 4 skills = 7 components
- react-native-expo: 3 agents + 1 command + 5 skills = 9 components

**Total: 16 agents, 6 commands, 28 skills = 50 components**

---

**Document Version**: 1.0
**Last Updated**: 2025-01-18
**Author**: AI Implementation Planning
**Status**: Ready for Review
