---
name: motion-variants-patterns
description: Motion (Framer Motion) variant definitions, propagation, orchestration, and state-based animation patterns. Use when implementing reusable animation states, coordinating multi-element animations, or building animation libraries.
---

# Motion Variants Patterns

Comprehensive guide to Motion (formerly Framer Motion) variants for creating reusable, orchestrated animation systems.

## Core Concepts

### Basic Variant Definition

Variants define named animation states that can be reused across components:

```jsx
const variants = {
  hidden: {
    opacity: 0,
    y: 20
  },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.3,
      ease: "easeOut"
    }
  }
}

<motion.div
  variants={variants}
  initial="hidden"
  animate="visible"
/>
```

### Variant Propagation

Variants automatically flow down to child motion components:

```jsx
const container = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
}

const item = {
  hidden: { y: 20, opacity: 0 },
  visible: { y: 0, opacity: 1 }
}

<motion.ul variants={container} initial="hidden" animate="visible">
  {items.map(item => (
    <motion.li key={item.id} variants={item} />
  ))}
</motion.ul>
```

**Key Rules:**
- Child components automatically inherit parent variant names
- Propagation stops if child has explicit `animate` prop
- Use for coordinated multi-element animations

## Orchestration Patterns

### Stagger Children

```jsx
const staggerContainer = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,      // Delay between each child
      delayChildren: 0.3,         // Delay before first child
      when: "beforeChildren",     // Parent animates before children
      staggerDirection: 1         // 1 = forward, -1 = reverse
    }
  }
}
```

### Sequential Animations

```jsx
const sequence = {
  initial: { opacity: 0, scale: 0.8 },
  animate: {
    opacity: 1,
    scale: 1,
    transition: {
      opacity: { duration: 0.3, delay: 0 },
      scale: { duration: 0.5, delay: 0.2 }
    }
  }
}
```

### Keyframe Animations

```jsx
const keyframeVariant = {
  animate: {
    scale: [1, 1.2, 1.1, 1],
    rotate: [0, 90, 180, 270, 360],
    transition: {
      duration: 2,
      times: [0, 0.25, 0.5, 0.75, 1],
      ease: "easeInOut"
    }
  }
}
```

## Dynamic Variants

### Function-Based Variants

```jsx
const dynamicVariant = {
  hidden: (custom) => ({
    opacity: 0,
    x: custom.direction === "left" ? -100 : 100
  }),
  visible: {
    opacity: 1,
    x: 0
  }
}

<motion.div
  custom={{ direction: "left" }}
  variants={dynamicVariant}
  initial="hidden"
  animate="visible"
/>
```

### State-Based Variants

```jsx
const buttonVariants = {
  idle: { scale: 1 },
  hover: { scale: 1.05 },
  tap: { scale: 0.95 },
  loading: {
    opacity: 0.6,
    transition: { duration: 0 }
  }
}

<motion.button
  variants={buttonVariants}
  initial="idle"
  whileHover="hover"
  whileTap="tap"
  animate={isLoading ? "loading" : "idle"}
/>
```

## Advanced Patterns

### Exit Animations with Variants

```jsx
const modalVariants = {
  hidden: {
    opacity: 0,
    scale: 0.8
  },
  visible: {
    opacity: 1,
    scale: 1
  },
  exit: {
    opacity: 0,
    scale: 0.8,
    transition: { duration: 0.2 }
  }
}

<AnimatePresence>
  {isOpen && (
    <motion.div
      variants={modalVariants}
      initial="hidden"
      animate="visible"
      exit="exit"
    />
  )}
</AnimatePresence>
```

### Gesture Variants

```jsx
const dragVariants = {
  drag: {
    scale: 1.1,
    cursor: "grabbing"
  },
  idle: {
    scale: 1,
    cursor: "grab"
  }
}

<motion.div
  drag
  variants={dragVariants}
  whileDrag="drag"
  animate="idle"
/>
```

## Variant Libraries

### Common Variant Patterns

```jsx
// variants-library.js
export const fadeInUp = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.3 }
  }
}

export const fadeInDown = {
  hidden: { opacity: 0, y: -20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.3 }
  }
}

export const scaleIn = {
  hidden: { opacity: 0, scale: 0.8 },
  visible: {
    opacity: 1,
    scale: 1,
    transition: { duration: 0.3 }
  }
}

export const slideIn = (direction = "left") => ({
  hidden: {
    x: direction === "left" ? -100 : 100,
    opacity: 0
  },
  visible: {
    x: 0,
    opacity: 1,
    transition: { type: "spring", stiffness: 100 }
  }
})
```

## Best Practices

1. **Naming Convention**: Use descriptive state names (hidden/visible, idle/active/disabled)
2. **Transition Configuration**: Define transitions in the target state, not initial
3. **Reusability**: Create a centralized variant library for consistency
4. **Performance**: Use hardware-accelerated properties (transform, opacity)
5. **Type Safety**: Use TypeScript for variant definitions

## Performance Considerations

- Variants are more performant than inline animations
- Variant propagation is optimized internally by Motion
- Reuse variants across components to reduce memory footprint
- Avoid creating new variant objects on every render

## TypeScript Support

```typescript
import { Variants } from "motion/react"

const variants: Variants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1 }
}
```

## Resources

- Motion Variants Documentation: https://www.framer.com/motion/component/#variants
- Motion Examples: https://www.framer.com/motion/examples/
- Animation Orchestration Guide: https://www.framer.com/motion/transition/
