---
name: remotion-comic-assembly
description: Remotion workflows for assembling comic segments into vertical video episodes with timing, transitions, and effects. Use when creating video episodes, optimizing Remotion performance, or debugging assembly issues.
---

# Remotion Comic Assembly

Production-ready Remotion workflows for assembling generated comic segments into polished vertical video episodes.

## Project Structure

```javascript
// src/compositions/ComicEpisode.jsx
import { AbsoluteFill, Sequence, useCurrentFrame } from 'remotion'

export const ComicEpisode = ({ shotlist, segments }) => {
  return (
    <AbsoluteFill>
      {shotlist.map((shot, index) => {
        const startFrame = calculateStartFrame(shotlist, index)
        const durationFrames = shot.duration * 30 / 1000  // 30 fps

        return (
          <Sequence
            key={shot.shot_id}
            from={startFrame}
            durationInFrames={durationFrames}
          >
            <Shot shot={shot} segments={segments} />
          </Sequence>
        )
      })}
    </AbsoluteFill>
  )
}
```

## Shot Component

```javascript
// src/compositions/Shot.jsx
import { AbsoluteFill, Img, interpolate, spring, useCurrentFrame } from 'remotion'

export const Shot = ({ shot, segments }) => {
  const frame = useCurrentFrame()

  // Ken Burns effect (subtle zoom)
  const scale = interpolate(
    frame,
    [0, shot.duration * 30 / 1000],
    [1.0, 1.05],
    { extrapolateRight: 'clamp' }
  )

  // Find segments
  const characterPanel = segments.find(
    s => s.id === `${shot.shot_id}_character_panel`
  )

  const speechBubbles = segments.filter(
    s => s.id.startsWith(shot.shot_id) && s.type === 'speech-bubble'
  )

  return (
    <AbsoluteFill style={{ backgroundColor: '#FFFFFF' }}>
      {/* Character panel */}
      <Img
        src={characterPanel.image_path}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transform: `scale(${scale})`
        }}
      />

      {/* Speech bubbles */}
      {speechBubbles.map((bubble, index) => (
        <SpeechBubble
          key={bubble.id}
          bubble={bubble}
          frame={frame}
          delay={index * 10}
        />
      ))}

      {/* Border */}
      <div style={{
        position: 'absolute',
        inset: 0,
        border: '8px solid black'
      }} />
    </AbsoluteFill>
  )
}
```

## Speech Bubble Animation

```javascript
export const SpeechBubble = ({ bubble, frame, delay }) => {
  const scale = spring({
    frame: frame - delay,
    fps: 30,
    config: { damping: 100, stiffness: 200, mass: 0.5 }
  })

  const opacity = interpolate(
    frame - delay,
    [0, 5],
    [0, 1],
    { extrapolateRight: 'clamp' }
  )

  return (
    <div
      style={{
        position: 'absolute',
        top: getBubblePosition(bubble.position).top,
        right: getBubblePosition(bubble.position).right,
        transform: `scale(${scale})`,
        opacity,
        backgroundColor: '#FFFFFF',
        border: '3px solid #000000',
        borderRadius: '20px',
        padding: '20px',
        maxWidth: '400px',
        fontSize: '32px',
        fontFamily: 'Comic Sans MS, cursive',
        fontWeight: 'bold',
        textAlign: 'center'
      }}
    >
      {bubble.dialogue}
    </div>
  )
}
```

## Rendering

```javascript
// scripts/render-episode.js
import { bundle } from '@remotion/bundler'
import { renderMedia, selectComposition } from '@remotion/renderer'

async function renderEpisode(episodeSlug) {
  const shotlist = loadShotlist(episodeSlug)
  const segments = loadSegments(episodeSlug)

  // Bundle
  const bundleLocation = await bundle({
    entryPoint: './src/index.tsx'
  })

  // Select composition
  const composition = await selectComposition({
    serveUrl: bundleLocation,
    id: 'ComicEpisode',
    inputProps: { shotlist, segments }
  })

  // Render
  await renderMedia({
    composition,
    serveUrl: bundleLocation,
    codec: 'h264',
    outputLocation: `episodes/${episodeSlug}/output/episode.mp4`,
    inputProps: { shotlist, segments },
    concurrency: 4,
    quality: 80
  })
}
```

## Performance Optimization

### Player Performance Pattern

```javascript
// CRITICAL: Controls as sibling, not child
const VideoPlayer = () => {
  const playerRef = useRef()

  return (
    <div>
      <Player ref={playerRef} component={MyComp} />
      <Controls playerRef={playerRef} />  {/* Sibling, not child */}
    </div>
  )
}
```

### Memoization

```javascript
const Shot = memo(({ shot, segments }) => {
  // Component logic
}, (prev, next) => {
  return prev.shot.shot_id === next.shot.shot_id
})
```

## Composition Config

```javascript
export const compositionConfig = {
  id: 'ComicEpisode',
  component: ComicEpisode,
  width: 1080,
  height: 1920,
  fps: 30,
  durationInFrames: 9000,  // 5 minutes
  defaultProps: {
    shotlist: [],
    segments: []
  }
}
```

## Resources

- Remotion Docs: https://remotion.dev
- Player Performance: https://remotion.dev/docs/player/player
- Rendering: https://remotion.dev/docs/renderer
