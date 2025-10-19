---
name: motion-orchestration
description: Coordinating multiple Motion animations with timing controls, sequencing, staggering, and complex multi-element choreography. Use when implementing complex animation sequences, coordinated transitions, or multi-step interactions.
---

# Motion Orchestration

Advanced patterns for coordinating multiple animations in Motion (Framer Motion) to create cohesive, professional animation sequences.

## Stagger Patterns

### Basic Staggering

```jsx
const container = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1  // 100ms delay between each child
    }
  }
}

const item = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 }
}

<motion.ul
  variants={container}
  initial="hidden"
  animate="visible"
>
  {items.map((item, i) => (
    <motion.li key={i} variants={item}>
      {item.text}
    </motion.li>
  ))}
</motion.ul>
```

### Advanced Stagger Configuration

```jsx
const advancedStagger = {
  visible: {
    transition: {
      staggerChildren: 0.07,        // Delay between children
      delayChildren: 0.2,            // Delay before first child
      staggerDirection: 1,           // 1=forward, -1=reverse
      when: "beforeChildren"         // Parent animates before children
    }
  }
}
```

### Reverse Stagger on Exit

```jsx
const staggerContainer = {
  enter: {
    transition: {
      staggerChildren: 0.1,
      when: "beforeChildren"
    }
  },
  exit: {
    transition: {
      staggerChildren: 0.05,
      staggerDirection: -1,    // Reverse order on exit
      when: "afterChildren"    // Wait for children to exit
    }
  }
}
```

## Sequential Animations

### Property Sequencing

```jsx
const sequence = {
  animate: {
    opacity: 1,
    scale: 1,
    x: 0,
    transition: {
      opacity: { duration: 0.2, delay: 0 },
      scale: { duration: 0.3, delay: 0.2 },
      x: { duration: 0.4, delay: 0.5 }
    }
  }
}
```

### Keyframe Sequences

```jsx
const keyframeSequence = {
  animate: {
    scale: [1, 1.2, 1.1, 1],
    rotate: [0, 10, -10, 0],
    x: [0, 100, 100, 0],
    transition: {
      duration: 2,
      times: [0, 0.3, 0.6, 1],
      ease: "easeInOut"
    }
  }
}
```

### Multi-Stage Animations

```jsx
const multiStage = {
  initial: { opacity: 0, scale: 0.8, y: 50 },
  animate: {
    opacity: [0, 1, 1, 1],
    scale: [0.8, 1.2, 1.1, 1],
    y: [50, -20, -10, 0],
    transition: {
      duration: 1.2,
      times: [0, 0.3, 0.6, 1],
      ease: [0.43, 0.13, 0.23, 0.96]
    }
  }
}
```

## Timing Control

### Delay Patterns

```jsx
// Fixed delay
<motion.div
  animate={{ x: 100 }}
  transition={{ delay: 0.5 }}
/>

// Dynamic delay based on index
<motion.div
  custom={index}
  animate={{ x: 100 }}
  transition={{ delay: index * 0.1 }}
/>

// Delay before children start
variants={{
  animate: {
    transition: {
      delayChildren: 0.3
    }
  }
}}
```

### Duration Control

```jsx
const timingControl = {
  fast: {
    transition: { duration: 0.15 }
  },
  normal: {
    transition: { duration: 0.3 }
  },
  slow: {
    transition: { duration: 0.6 }
  }
}
```

## Coordinated Transitions

### Page Transitions

```jsx
import { AnimatePresence } from "motion/react"

const PageTransition = ({ children, location }) => {
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={location}
        initial={{ opacity: 0, x: -100 }}
        animate={{ opacity: 1, x: 0 }}
        exit={{ opacity: 0, x: 100 }}
        transition={{
          type: "spring",
          stiffness: 300,
          damping: 30
        }}
      >
        {children}
      </motion.div>
    </AnimatePresence>
  )
}
```

### Shared Layout Transitions

```jsx
// Item in list
<motion.div layoutId={`item-${id}`}>
  <img src={thumbnail} />
</motion.div>

// Same item in detail view
<motion.div layoutId={`item-${id}`}>
  <img src={fullSize} />
</motion.div>
// Seamlessly animates between positions
```

### Modal with Backdrop

```jsx
const Modal = ({ isOpen, onClose }) => {
  return (
    <AnimatePresence>
      {isOpen && (
        <>
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)" }}
          />
          <motion.div
            initial={{ opacity: 0, scale: 0.8, y: 50 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.8, y: 50 }}
            transition={{
              type: "spring",
              damping: 25,
              stiffness: 300
            }}
          >
            Modal content
          </motion.div>
        </>
      )}
    </AnimatePresence>
  )
}
```

## Animation Hooks

### useAnimation for Programmatic Control

```jsx
import { useAnimation } from "motion/react"

const Component = () => {
  const controls = useAnimation()

  const handleClick = async () => {
    await controls.start({ x: 100 })
    await controls.start({ x: 0 })
    await controls.start({ scale: 1.2 })
    await controls.start({ scale: 1 })
  }

  return (
    <motion.div animate={controls}>
      <button onClick={handleClick}>Animate</button>
    </motion.div>
  )
}
```

### Conditional Orchestration

```jsx
const [step, setStep] = useState(0)

<motion.div
  animate={step === 0 ? "initial" : step === 1 ? "middle" : "final"}
  variants={{
    initial: { x: 0, opacity: 1 },
    middle: { x: 100, opacity: 0.5 },
    final: { x: 200, opacity: 0 }
  }}
/>
```

## Complex Choreography

### Multi-Element Dance

```jsx
const choreography = {
  container: {
    animate: {
      transition: {
        staggerChildren: 0.05,
        delayChildren: 0.1
      }
    }
  },
  item: (i) => ({
    animate: {
      y: [0, -30, 0],
      transition: {
        duration: 0.5,
        delay: i * 0.1,
        repeat: Infinity,
        repeatDelay: 1
      }
    }
  })
}

<motion.div variants={choreography.container}>
  {[0,1,2,3,4].map(i => (
    <motion.div
      key={i}
      custom={i}
      variants={choreography.item}
    />
  ))}
</motion.div>
```

### Wave Animation

```jsx
const wave = (i, total) => ({
  animate: {
    y: [0, -20, 0],
    transition: {
      duration: 1,
      delay: (i / total) * 0.5,
      repeat: Infinity,
      ease: "easeInOut"
    }
  }
})

{items.map((item, i) => (
  <motion.div
    key={i}
    custom={{ i, total: items.length }}
    variants={wave}
  />
))}
```

## Best Practices

1. **Timing Consistency**: Use design tokens for durations
2. **Easing Functions**: Match easing to interaction type
3. **Stagger Values**: 50-150ms for most list animations
4. **Exit Animations**: Keep them shorter than enter (0.2s vs 0.3s)
5. **Performance**: Limit concurrent animations to 10-15 elements
6. **Accessibility**: Respect `prefers-reduced-motion`

## Common Patterns

### Loading Skeleton Shimmer

```jsx
const shimmer = {
  animate: {
    backgroundPosition: ["200% 0", "-200% 0"],
    transition: {
      duration: 2,
      repeat: Infinity,
      ease: "linear"
    }
  }
}

<motion.div
  variants={shimmer}
  animate="animate"
  style={{
    background: "linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%)",
    backgroundSize: "200% 100%"
  }}
/>
```

### Pulse Effect

```jsx
const pulse = {
  animate: {
    scale: [1, 1.05, 1],
    opacity: [1, 0.8, 1],
    transition: {
      duration: 2,
      repeat: Infinity,
      ease: "easeInOut"
    }
  }
}
```

### Cascading Cards

```jsx
const cascadeContainer = {
  animate: {
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.2
    }
  }
}

const cascadeItem = {
  initial: { opacity: 0, y: 50, rotateX: -15 },
  animate: {
    opacity: 1,
    y: 0,
    rotateX: 0,
    transition: {
      type: "spring",
      stiffness: 100,
      damping: 15
    }
  }
}
```

## Resources

- Motion Orchestration: https://www.framer.com/motion/transition/
- Timing Functions: https://easings.net/
- Animation Examples: https://www.framer.com/motion/examples/
