---
description: Scaffold a new Motion (Framer Motion) animation system with design tokens, variant library, and reusable components
---

You will create a comprehensive Motion (Framer Motion) animation system for a React application.

## What to Create

1. **Animation Design Tokens** (`animation-tokens.js` or `animation-tokens.ts`):
   - Transition presets (fast, base, slow)
   - Spring configurations (gentle, bouncy, stiff)
   - Easing curves (ease, easeIn, easeOut, easeInOut)
   - Duration values (150ms, 300ms, 500ms)

2. **Variant Library** (`animation-variants.js` or `animation-variants.ts`):
   - fadeIn, fadeOut
   - slideInUp, slideInDown, slideInLeft, slideInRight
   - scaleIn, scaleOut
   - staggerContainer
   - Common interaction states (hover, tap, focus)

3. **Animation Utilities** (`animation-utils.js` or `animation-utils.ts`):
   - useReducedMotion hook wrapper
   - Animation helpers (delay calculator, stagger generator)
   - Performance utilities (willChange manager)

4. **Example Components**:
   - AnimatedButton with hover/tap states
   - AnimatedCard with layout animations
   - AnimatedList with stagger
   - PageTransition wrapper

## Implementation Steps

1. **Ask for Requirements**:
   - Project structure (src/lib, src/utils, etc.)
   - TypeScript or JavaScript?
   - Existing design system?
   - Animation style preferences (bouncy vs smooth)?

2. **Create Animation Tokens**:
   ```javascript
   export const transitions = {
     fast: { duration: 0.15, ease: "easeOut" },
     base: { duration: 0.3, ease: [0.4, 0, 0.2, 1] },
     slow: { duration: 0.5, ease: "easeInOut" }
   }

   export const springs = {
     gentle: { type: "spring", stiffness: 120, damping: 14 },
     bouncy: { type: "spring", stiffness: 400, damping: 10 },
     stiff: { type: "spring", stiffness: 500, damping: 30 }
   }
   ```

3. **Create Variant Library**:
   ```javascript
   export const fadeInUp = {
     hidden: { opacity: 0, y: 20 },
     visible: { opacity: 1, y: 0, transition: transitions.base }
   }
   ```

4. **Create Utility Hooks**:
   ```javascript
   export const useReducedMotion = () => {
     return useReducedMotion()
   }
   ```

5. **Create Example Components**:
   - Show proper usage patterns
   - Include accessibility features
   - Demonstrate performance optimization

6. **Documentation**:
   - README with usage examples
   - JSDoc comments on all utilities
   - Performance best practices

## Example Output Structure

```
src/
├── lib/
│   └── animations/
│       ├── tokens.ts
│       ├── variants.ts
│       └── utils.ts
├── components/
│   └── animated/
│       ├── AnimatedButton.tsx
│       ├── AnimatedCard.tsx
│       ├── AnimatedList.tsx
│       └── PageTransition.tsx
└── README-ANIMATIONS.md
```

## Best Practices to Include

1. Use hardware-accelerated properties (transform, opacity)
2. Add willChange for animated properties
3. Implement reduced motion support
4. Use layout prop for layout animations
5. Stagger list animations (100ms intervals)
6. Keep duration between 200-400ms for most interactions
7. Use spring physics for natural feel
8. Profile animations to maintain 60fps

## Testing Recommendations

- Test with reduced motion enabled
- Profile performance on low-end devices
- Verify animations work on Safari/Firefox/Chrome
- Check accessibility with screen readers
- Validate WCAG motion guidelines

After creating the animation system, provide a summary of what was created and usage examples for common scenarios.
