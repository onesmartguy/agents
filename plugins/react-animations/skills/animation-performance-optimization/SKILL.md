---
name: animation-performance-optimization
description: Hardware acceleration, willChange optimization, lazy loading patterns, and performance profiling for Motion animations. Use when optimizing animation performance, achieving 60fps target, or reducing jank in complex animations.
---

# Animation Performance Optimization

Comprehensive guide to achieving 60fps animations with Motion (Framer Motion) through hardware acceleration, optimal property selection, and performance profiling.

## Hardware-Accelerated Properties

### GPU-Accelerated Properties (FAST)

These properties are rendered on the GPU and provide optimal performance:

```jsx
<motion.div
  animate={{
    x: 100,           // transform: translateX()
    y: 50,            // transform: translateY()
    scale: 1.2,       // transform: scale()
    rotate: 45,       // transform: rotate()
    opacity: 0.5      // opacity
  }}
  style={{ willChange: "transform, opacity" }}
/>
```

**Recommended Properties:**
- `x`, `y`, `z` (translate)
- `scale`, `scaleX`, `scaleY`
- `rotate`, `rotateX`, `rotateY`, `rotateZ`
- `opacity`

### CPU-Bound Properties (SLOW)

Avoid animating these properties when possible:

```jsx
// AVOID THESE
<motion.div
  animate={{
    width: 200,       // Triggers layout recalculation
    height: 100,      // Triggers layout recalculation
    top: 50,          // Triggers layout recalculation
    left: 100,        // Triggers layout recalculation
    margin: 20,       // Triggers layout recalculation
    padding: 10       // Triggers layout recalculation
  }}
/>
```

**Alternative Approaches:**
```jsx
// GOOD: Use scale instead of width/height
<motion.div
  animate={{ scale: 1.5 }}
  style={{ willChange: "transform" }}
/>

// GOOD: Use translate instead of top/left
<motion.div
  animate={{ x: 100, y: 50 }}
  style={{ willChange: "transform" }}
/>
```

## willChange Optimization

### Proper Usage

```jsx
// For transform animations
<motion.div
  style={{ willChange: "transform" }}
  animate={{ x: 100, rotate: 45 }}
/>

// For opacity animations
<motion.div
  style={{ willChange: "opacity" }}
  animate={{ opacity: 0.5 }}
/>

// For multiple properties
<motion.div
  style={{ willChange: "transform, opacity" }}
  animate={{ x: 100, opacity: 0.5 }}
/>

// For background/filter animations
<motion.div
  style={{ willChange: "background-color, filter" }}
  animate={{ backgroundColor: "#ff0000", filter: "blur(10px)" }}
/>
```

### Important Notes

- Don't use `willChange: "auto"` (default behavior is better)
- Only specify properties you're actually animating
- Remove willChange after animation completes for long-lived elements
- Overuse can actually hurt performance (creates new layers unnecessarily)

## Lazy Loading with useInView

### Basic Usage

```jsx
import { motion } from "motion/react"
import { useInView } from "motion/react"
import { useRef } from "react"

const LazyComponent = () => {
  const ref = useRef(null)
  const isInView = useInView(ref, {
    once: true,        // Only trigger once
    margin: "0px 0px -100px 0px"  // Trigger 100px before element enters
  })

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 50 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.5 }}
    >
      Content loads only when visible
    </motion.div>
  )
}
```

### Advanced Viewport Detection

```jsx
const options = {
  once: false,             // Trigger multiple times
  amount: 0.5,             // Trigger when 50% visible
  margin: "100px",         // Trigger 100px before/after viewport
  root: containerRef       // Custom scroll container
}

const isInView = useInView(ref, options)
```

## Player Component Performance

### Optimal Pattern (Avoid Re-renders)

```jsx
// GOOD: Controls as sibling, not parent
const VideoPlayer = () => {
  const playerRef = useRef()

  return (
    <div>
      <Player ref={playerRef} />
      <Controls playerRef={playerRef} />
    </div>
  )
}

const Controls = ({ playerRef }) => {
  const [time, setTime] = useState(0)

  // Player doesn't re-render when time updates
  return <div>Current time: {time}</div>
}
```

### Anti-Pattern (Causes Re-renders)

```jsx
// BAD: Time state in same component as Player
const VideoPlayer = () => {
  const [time, setTime] = useState(0)  // Causes Player re-render

  return (
    <div>
      <Player />
      <div>Current time: {time}</div>
    </div>
  )
}
```

## Performance Profiling

### Chrome DevTools

1. Open DevTools → Performance tab
2. Start recording
3. Trigger animation
4. Stop recording
5. Look for:
   - Frame rate (target: 60fps)
   - Long tasks (> 50ms)
   - Layout thrashing (purple bars)
   - Paint operations (green bars)

### React DevTools Profiler

```jsx
import { Profiler } from "react"

<Profiler id="animation" onRender={(id, phase, actualDuration) => {
  console.log(`${id} ${phase} took ${actualDuration}ms`)
}}>
  <AnimatedComponent />
</Profiler>
```

### Motion Debug Mode

```jsx
import { MotionConfig } from "motion/react"

<MotionConfig isStatic={false}>
  {/* Animations enabled */}
</MotionConfig>

<MotionConfig isStatic={true}>
  {/* Animations disabled for testing */}
</MotionConfig>
```

## Memory Optimization

### Cleanup on Unmount

```jsx
import { useAnimation } from "motion/react"
import { useEffect } from "react"

const Component = () => {
  const controls = useAnimation()

  useEffect(() => {
    controls.start({ x: 100 })

    return () => {
      controls.stop()  // Cancel in-flight animations
    }
  }, [controls])

  return <motion.div animate={controls} />
}
```

### Limit Concurrent Animations

```jsx
// AVOID: Too many simultaneous animations
{items.map(item => (
  <motion.div key={item.id} animate={{ x: 100 }} />
))}

// GOOD: Stagger animations
<motion.div
  variants={{
    visible: {
      transition: { staggerChildren: 0.1 }
    }
  }}
>
  {items.map(item => (
    <motion.div key={item.id} variants={itemVariant} />
  ))}
</motion.div>
```

## Best Practices Checklist

- [ ] Use hardware-accelerated properties (transform, opacity)
- [ ] Add willChange for animated properties
- [ ] Implement lazy loading with useInView
- [ ] Avoid animating layout properties (width, height, top, left)
- [ ] Keep Player components pure (avoid parent state updates)
- [ ] Profile with Chrome DevTools (target 60fps)
- [ ] Cleanup animations on unmount
- [ ] Limit concurrent animations (use stagger)
- [ ] Test on low-end devices
- [ ] Respect prefers-reduced-motion

## Performance Metrics

**Target Metrics:**
- Frame rate: 60fps (16.67ms per frame)
- Animation duration: 200-400ms for most interactions
- Time to Interactive (TTI): < 3s
- First Contentful Paint (FCP): < 1s

## Common Performance Issues

### Issue: Janky Animations

**Cause:** Animating layout properties
**Solution:** Use transform instead

```jsx
// BAD
animate={{ width: 200 }}

// GOOD
animate={{ scaleX: 2 }}
```

### Issue: Slow Initial Load

**Cause:** Too many animations on mount
**Solution:** Lazy load with useInView

### Issue: Memory Leaks

**Cause:** Not cleaning up animations
**Solution:** Use cleanup functions

## Resources

- Chrome DevTools Performance: https://developer.chrome.com/docs/devtools/performance/
- Web Animation Performance: https://web.dev/animations/
- Motion Performance: https://www.framer.com/motion/guide-upgrade/#performance
- GPU vs CPU Rendering: https://www.html5rocks.com/en/tutorials/speed/high-performance-animations/
