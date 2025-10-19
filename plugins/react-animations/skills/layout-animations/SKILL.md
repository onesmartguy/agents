---
name: layout-animations
description: Motion layout animations using the layout prop, shared layout transitions, FLIP animations, and automatic position/size transitions. Use when animating layout changes, implementing shared element transitions, or creating responsive animations.
---

# Layout Animations

Comprehensive guide to Motion's (Framer Motion) layout animations using the `layout` prop for automatic FLIP (First, Last, Invert, Play) animations.

## Layout Prop Basics

### Automatic Layout Animations

The `layout` prop automatically animates layout changes:

```jsx
const [isExpanded, setIsExpanded] = useState(false)

<motion.div layout>
  <h2>Title</h2>
  {isExpanded && <p>Additional content appears with smooth animation</p>}
  <button onClick={() => setIsExpanded(!isExpanded)}>
    Toggle
  </button>
</motion.div>
```

**What Gets Animated:**
- Position changes (x, y)
- Size changes (width, height)
- Transform changes
- Border radius (when layout="position")

### Layout Types

```jsx
// Animate all layout properties
<motion.div layout />

// Animate only position (not size)
<motion.div layout="position" />

// Animate only size (not position)
<motion.div layout="size" />
```

## Shared Layout Animations

### Basic Shared Layout

Using `layoutId` creates seamless transitions between different components:

```jsx
// Component A
<motion.div layoutId="shared-element">
  <img src={thumbnail} />
</motion.div>

// Component B (different location/route)
<motion.div layoutId="shared-element">
  <img src={fullImage} />
</motion.div>
```

The element smoothly animates from position A to position B.

### Image Gallery Example

```jsx
const ImageGallery = () => {
  const [selectedId, setSelectedId] = useState(null)

  return (
    <>
      <div className="gallery">
        {images.map(image => (
          <motion.div
            key={image.id}
            layoutId={`image-${image.id}`}
            onClick={() => setSelectedId(image.id)}
          >
            <img src={image.thumbnail} />
          </motion.div>
        ))}
      </div>

      <AnimatePresence>
        {selectedId && (
          <motion.div
            layoutId={`image-${selectedId}`}
            onClick={() => setSelectedId(null)}
          >
            <img src={images.find(i => i.id === selectedId).full} />
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}
```

## Advanced Patterns

### Reordering Lists

```jsx
import { Reorder } from "motion/react"

const [items, setItems] = useState([1, 2, 3, 4])

<Reorder.Group values={items} onReorder={setItems}>
  {items.map(item => (
    <Reorder.Item key={item} value={item}>
      {item}
    </Reorder.Item>
  ))}
</Reorder.Group>
```

### Layout Transition Configuration

```jsx
<motion.div
  layout
  transition={{
    layout: {
      type: "spring",
      stiffness: 300,
      damping: 30
    }
  }}
/>
```

### Nested Layout Animations

```jsx
<motion.div layout>
  <motion.div layout>
    <motion.div layout>
      Nested layout animations work seamlessly
    </motion.div>
  </motion.div>
</motion.div>
```

## Shared Layout Groups

### LayoutGroup for Coordinated Animations

```jsx
import { LayoutGroup } from "motion/react"

<LayoutGroup>
  <motion.div layoutId="box" />
  <motion.div layoutId="circle" />
</LayoutGroup>
```

### Tab Navigation Example

```jsx
const Tabs = ({ tabs, selected, setSelected }) => {
  return (
    <div className="tabs">
      {tabs.map(tab => (
        <button
          key={tab}
          onClick={() => setSelected(tab)}
          className={selected === tab ? "selected" : ""}
        >
          {tab}
          {selected === tab && (
            <motion.div
              layoutId="tab-indicator"
              className="indicator"
              transition={{
                type: "spring",
                stiffness: 500,
                damping: 30
              }}
            />
          )}
        </button>
      ))}
    </div>
  )
}
```

## Layout Animations with Content

### Expand/Collapse Card

```jsx
const Card = ({ title, content }) => {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <motion.div
      layout
      onClick={() => setIsOpen(!isOpen)}
      transition={{
        layout: { duration: 0.3, ease: "easeInOut" }
      }}
    >
      <motion.h2 layout="position">{title}</motion.h2>
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            {content}
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  )
}
```

### Grid to List Transition

```jsx
const [isGrid, setIsGrid] = useState(true)

<LayoutGroup>
  <div className={isGrid ? "grid" : "list"}>
    {items.map(item => (
      <motion.div
        key={item.id}
        layout
        transition={{
          layout: { type: "spring", stiffness: 300, damping: 30 }
        }}
      >
        {item.content}
      </motion.div>
    ))}
  </div>
</LayoutGroup>
```

## Performance Optimization

### Layout Animations Performance

Layout animations are already optimized using FLIP technique, but you can further optimize:

```jsx
// Use transform when possible
<motion.div
  layout
  style={{ willChange: "transform" }}
/>

// Disable layout on children that don't need it
<motion.div layout>
  <div>Static content (no layout prop)</div>
  <motion.div layout>Animated content</motion.div>
</motion.div>
```

### Avoiding Layout Thrashing

```jsx
// GOOD: Use layout prop
<motion.div layout />

// AVOID: Manual position animations that cause layout
<motion.div animate={{ width: "100%", height: "auto" }} />
```

## Border Radius Animation

```jsx
const [isRound, setIsRound] = useState(false)

<motion.div
  layout
  animate={{
    borderRadius: isRound ? "50%" : "0%"
  }}
  transition={{
    layout: { duration: 0.3 },
    borderRadius: { duration: 0.3 }
  }}
/>
```

## Common Issues & Solutions

### Issue: Children Not Animating

**Problem:**
```jsx
<motion.div layout>
  <div>Child doesn't animate</div>
</motion.div>
```

**Solution:**
```jsx
<motion.div layout>
  <motion.div layout="position">
    Child now animates
  </motion.div>
</motion.div>
```

### Issue: Z-Index During Animation

**Problem:** Elements appear behind others during transition

**Solution:**
```jsx
<motion.div
  layout
  style={{ zIndex: isSelected ? 10 : 1 }}
  layoutId="element"
/>
```

### Issue: Preserve Scroll Position

```jsx
import { LayoutGroup, motion } from "motion/react"

<LayoutGroup>
  <motion.div layout="preserve-aspect">
    Maintains aspect ratio during animation
  </motion.div>
</LayoutGroup>
```

## Best Practices

1. **Use layoutId for Shared Elements**: Ensures smooth transitions between different DOM locations
2. **Combine with AnimatePresence**: For enter/exit animations during layout changes
3. **Layout="position" for Text**: Prevents text reflow during animations
4. **LayoutGroup for Coordination**: Group related layout animations together
5. **Optimize with willChange**: Add `willChange: "transform"` for better performance
6. **Test on Real Devices**: Layout animations can be GPU-intensive

## Real-World Examples

### Accordion

```jsx
const Accordion = ({ items }) => {
  const [expandedIndex, setExpandedIndex] = useState(null)

  return (
    <div>
      {items.map((item, i) => (
        <motion.div
          key={i}
          layout
          onClick={() => setExpandedIndex(i === expandedIndex ? null : i)}
        >
          <motion.h3 layout="position">{item.title}</motion.h3>
          <AnimatePresence>
            {i === expandedIndex && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: "auto" }}
                exit={{ opacity: 0, height: 0 }}
              >
                {item.content}
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
      ))}
    </div>
  )
}
```

### Modal with Shared Element

```jsx
const ProductCard = ({ product, onClick }) => (
  <motion.div
    layoutId={`product-${product.id}`}
    onClick={onClick}
  >
    <motion.img
      layoutId={`product-img-${product.id}`}
      src={product.thumbnail}
    />
    <motion.h3 layoutId={`product-title-${product.id}`}>
      {product.title}
    </motion.h3>
  </motion.div>
)

const ProductModal = ({ product, onClose }) => (
  <motion.div
    layoutId={`product-${product.id}`}
    onClick={onClose}
  >
    <motion.img
      layoutId={`product-img-${product.id}`}
      src={product.full}
    />
    <motion.h3 layoutId={`product-title-${product.id}`}>
      {product.title}
    </motion.h3>
    <p>{product.description}</p>
  </motion.div>
)
```

## Resources

- Motion Layout Animations: https://www.framer.com/motion/layout-animations/
- FLIP Technique: https://aerotwist.com/blog/flip-your-animations/
- Reorder Component: https://www.framer.com/motion/reorder/
- Layout Group: https://www.framer.com/motion/layout-group/
