---
name: remotion-patterns
description: Remotion component patterns, Player optimization, composition structure, and React best practices for programmatic video creation. Use when building Remotion videos, optimizing Player performance, or structuring video components.
---

# Remotion Patterns

## Player Performance Pattern (CRITICAL)

**BEST PRACTICE - Separate Controls from Player:**
```jsx
//GOOD: Controls as sibling
const VideoPlayer = () => {
  const playerRef = useRef()
  return (
    <div>
      <Player ref={playerRef} component={MyComp} />
      <Controls playerRef={playerRef} />
    </div>
  )
}

// BAD: State in same component causes re-renders
const BadPlayer = () => {
  const [time, setTime] = useState(0)
  return <Player /> {/* Re-renders on every time update! */}
}
```

## Composition Patterns

```jsx
// Basic composition
<Composition
  id="MyVideo"
  component={MyVideo}
  durationInFrames={150}
  fps={30}
  width={1920}
  height={1080}
  defaultProps={{ title: "Hello" }}
/>
```

## Data-Driven Videos

```jsx
import { delayRender, continueRender } from 'remotion'

export const DataVideo = () => {
  const [handle] = useState(() => delayRender())
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(json => {
        setData(json)
        continueRender(handle)
      })
  }, [handle])

  if (!data) return null
  return <VideoWithData data={data} />
}
```

## Environment Variables

```javascript
const apiKey = process.env.REMOTION_API_KEY
// Use in rendering: REMOTION_API_KEY=xxx npm run render
```

## Sequences for Complex Timelines

```jsx
<>
  <Sequence from={0} durationInFrames={60}><Intro /></Sequence>
  <Sequence from={60} durationInFrames={120}><Main /></Sequence>
  <Sequence from={180} durationInFrames={40}><Outro /></Sequence>
</>
```

## Best Practices

1. Use ref pattern for Player controls
2. delayRender/continueRender for async data
3. Environment variables for secrets
4. Zod schemas for prop validation
5. useMemo for expensive calculations

## Resources

- https://www.remotion.dev/docs/player/best-practices
