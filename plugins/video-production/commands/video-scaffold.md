---
description: Scaffold a new Remotion video project with compositions, components, and rendering configuration
---

Create a production-ready Remotion video project.

## Setup Steps

1. Initialize Remotion project
2. Create composition structure
3. Set up rendering configuration
4. Add example components
5. Configure environment variables

## Implementation

```bash
npx create-video --typescript

# Project structure
src/
├── Root.tsx              # Root component with compositions
├── compositions/
│   ├── MainVideo.tsx
│   └── SocialPost.tsx
├── components/
│   ├── Title.tsx
│   └── Background.tsx
└── config.ts             # Rendering config
```

Include best practices:
- Player ref pattern for controls
- Environment variable usage
- delayRender/continueRender for async data
- Zod schemas for props
- TypeScript types
