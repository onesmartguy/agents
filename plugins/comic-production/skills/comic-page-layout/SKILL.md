---
name: comic-page-layout
description: Print page layout design, panel composition, HTML5 Canvas rendering, and PDF export for comic pages. Use when designing print layouts, assembling pages, or exporting to PDF.
---

# Comic Page Layout

Professional page layout techniques for print comic production using HTML5 Canvas and PDF export.

## Standard Page Specifications

**Comic Book Size**: 6.875" x 10.5" @ 300 DPI
- **Width**: 2550 pixels
- **Height**: 3300 pixels
- **Bleed**: 37.5 pixels (0.125")
- **Safe Zone**: -75 pixels from edge (0.25")

## Panel Grid Layouts

### 6-Panel Standard

```
┌─────────────────────────────┐
│       PANEL 1 (Wide)        │  2550x800px
├──────────────┬──────────────┤
│   PANEL 2    │   PANEL 3    │  1200x600px each
├──────────────┴──────────────┤
│       PANEL 4 (Wide)        │  2550x600px
├───────┬─────────┬───────────┤
│ PAN 5 │ PANEL 6 │  PANEL 7  │  800x500px each
└───────┴─────────┴───────────┘
```

### Dynamic Layout

```javascript
const layoutPresets = {
  action: [
    { x: 75, y: 75, width: 800, height: 1200 },     // Tall left
    { x: 900, y: 75, width: 1575, height: 600 },    // Wide top-right
    { x: 900, y: 700, width: 1575, height: 600 },   // Wide mid-right
    { x: 75, y: 1325, width: 2400, height: 1000 }   // Splash bottom
  ],

  conversation: [
    { x: 75, y: 75, width: 2400, height: 600 },     // Wide establish
    { x: 75, y: 700, width: 1175, height: 700 },    // Left speaker
    { x: 1275, y: 700, width: 1200, height: 700 },  // Right speaker
    { x: 75, y: 1425, width: 2400, height: 800 }    // Wide reaction
  ]
}
```

## Canvas Rendering

```javascript
class PageLayout {
  constructor() {
    this.canvas = document.createElement('canvas')
    this.canvas.width = 2550
    this.canvas.height = 3300
    this.ctx = this.canvas.getContext('2d')
    this.panels = []
  }

  addPanel(shot, segments, bounds) {
    this.panels.push({ shot, segments, bounds })
  }

  async render() {
    // White background
    this.ctx.fillStyle = '#FFFFFF'
    this.ctx.fillRect(0, 0, 2550, 3300)

    // Render each panel
    for (const panel of this.panels) {
      await this.renderPanel(panel)
    }

    return this.canvas
  }

  async renderPanel({ shot, segments, bounds }) {
    this.ctx.save()

    // Clip to panel
    this.ctx.beginPath()
    this.ctx.rect(bounds.x, bounds.y, bounds.width, bounds.height)
    this.ctx.clip()

    // Character panel (base)
    const charPanel = segments.find(s => s.type === 'character-panel')
    const img = await loadImage(charPanel.image_path)
    this.ctx.drawImage(img, bounds.x, bounds.y, bounds.width, bounds.height)

    // Speech bubbles
    const bubbles = segments.filter(s => s.type === 'speech-bubble')
    for (const bubble of bubbles) {
      this.renderSpeechBubble(bubble, bounds)
    }

    this.ctx.restore()

    // Border
    this.ctx.strokeStyle = '#000000'
    this.ctx.lineWidth = 8
    this.ctx.strokeRect(bounds.x, bounds.y, bounds.width, bounds.height)
  }

  renderSpeechBubble(bubble, panelBounds) {
    const pos = this.calculateBubblePosition(bubble.position, panelBounds)

    // Draw bubble
    this.ctx.fillStyle = '#FFFFFF'
    this.ctx.strokeStyle = '#000000'
    this.ctx.lineWidth = 3

    this.drawRoundedRect(this.ctx, pos.x, pos.y, 300, 100, 20)

    // Text
    this.ctx.fillStyle = '#000000'
    this.ctx.font = 'bold 24px Comic Sans MS'
    this.ctx.textAlign = 'center'
    this.wrapText(this.ctx, bubble.dialogue, pos.x + 150, pos.y + 50, 260)
  }

  drawRoundedRect(ctx, x, y, width, height, radius) {
    ctx.beginPath()
    ctx.moveTo(x + radius, y)
    ctx.lineTo(x + width - radius, y)
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius)
    ctx.lineTo(x + width, y + height - radius)
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height)
    ctx.lineTo(x + radius, y + height)
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius)
    ctx.lineTo(x, y + radius)
    ctx.quadraticCurveTo(x, y, x + radius, y)
    ctx.closePath()
    ctx.fill()
    ctx.stroke()
  }

  wrapText(ctx, text, x, y, maxWidth) {
    const words = text.split(' ')
    const lines = []
    let currentLine = ''

    for (const word of words) {
      const testLine = currentLine + word + ' '
      if (ctx.measureText(testLine).width > maxWidth && currentLine !== '') {
        lines.push(currentLine)
        currentLine = word + ' '
      } else {
        currentLine = testLine
      }
    }
    lines.push(currentLine)

    const lineHeight = 30
    const startY = y - (lines.length * lineHeight) / 2

    lines.forEach((line, i) => {
      ctx.fillText(line, x, startY + i * lineHeight)
    })
  }
}
```

## PDF Export

```javascript
import { jsPDF } from 'jspdf'

async function exportToPDF(canvases, outputPath) {
  const pdf = new jsPDF({
    orientation: 'portrait',
    unit: 'in',
    format: [6.875, 10.5],
    compress: true
  })

  for (let i = 0; i < canvases.length; i++) {
    if (i > 0) pdf.addPage()

    const imgData = canvases[i].toDataURL('image/jpeg', 0.95)
    pdf.addImage(imgData, 'JPEG', 0, 0, 6.875, 10.5)
  }

  pdf.save(outputPath)
}
```

## Page Assembly Workflow

```javascript
async function assemblePages(episodeSlug) {
  const shotlist = loadShotlist(episodeSlug)
  const segments = loadSegments(episodeSlug)

  // Group shots into pages
  const pages = groupIntoPages(shotlist)  // By page attribute

  const renderedPages = []

  for (let i = 0; i < pages.length; i++) {
    const pageLayout = new PageLayout()

    // Calculate panel layout
    const layout = calculatePanelLayout(pages[i])

    for (let j = 0; j < pages[i].length; j++) {
      const shot = pages[i][j]
      const shotSegments = segments.filter(s => s.id.startsWith(shot.shot_id))
      pageLayout.addPanel(shot, shotSegments, layout[j])
    }

    const canvas = await pageLayout.render()
    renderedPages.push(canvas)
  }

  // Export to PDF
  await exportToPDF(renderedPages, `episodes/${episodeSlug}/output/pages.pdf`)
}
```

## Reading Flow

**Western Comics**: Left-to-right, top-to-bottom
**Manga**: Right-to-left, top-to-bottom

Ensure panel arrangement guides reader naturally.

## Print Guidelines

- **Bleed**: Extend important elements 0.125" beyond trim
- **Safe Zone**: Keep text 0.25" from edges
- **Resolution**: 300 DPI minimum
- **Color Mode**: CMYK for print, RGB for digital
- **File Format**: PDF/X-1a for professional printing

## Resources

- jsPDF: https://github.com/parallax/jsPDF
- Canvas API: MDN Canvas Documentation
- Print Specifications: Comic printing standards
