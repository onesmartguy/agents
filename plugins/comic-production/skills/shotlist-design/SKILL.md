---
name: shotlist-design
description: Transform scripts into production-ready shotlists with camera angles, segment specifications, and timing. Use when converting beat sheets to shotlists, planning visual sequences, or optimizing panel compositions.
---

# Shotlist Design

Comprehensive guide to transforming narrative scripts into detailed, production-ready shotlists for comic generation.

## Shotlist JSON Structure

```json
{
  "shot_id": "S01",
  "sequence": 1,
  "duration": 150,
  "page": 1,
  "panel_position": "top",
  "caption": "Garage: E codes, bat nearby.",
  "panel": {
    "characters": ["e", "p"],
    "environment": "suburban garage at dusk, workbench with laptop",
    "camera": {
      "shot_type": "medium-wide",
      "angle": "eye-level 3/4",
      "framing": "rule-of-thirds, E left, P right"
    },
    "lighting": "warm overhead, screen glow",
    "mood": "relaxed, focused",
    "consistency": {
      "identity": ["instantid:characters/e/refs/head01.png"],
      "pose_ref": "assets/poses/e_sitting_typing.png",
      "lineart": true
    }
  },
  "segments": [
    {
      "id": "S01_character_panel",
      "type": "character-panel",
      "priority": 1,
      "characters": ["e", "p"],
      "description": "E at laptop, P lying beside workbench"
    },
    {
      "id": "S01_speech",
      "type": "speech-bubble",
      "priority": 2,
      "character": "e",
      "dialogue": "Just one more commit...",
      "bubble_style": "casual",
      "position": "upper-right"
    }
  ]
}
```

## Camera Shot Types

**Extreme Wide Shot (EWS)**: Full environment, characters small
- *Use*: Establishing shots, location reveals, scale

**Wide Shot (WS)**: Full body, environment visible
- *Use*: Action sequences, multiple characters, context

**Medium-Wide (MWS)**: Waist/knees up, balanced character-environment
- *Use*: Conversations, two-person scenes

**Medium Shot (MS)**: Waist up
- *Use*: Standard dialogue, interactions

**Medium Close-Up (MCU)**: Chest up
- *Use*: Emotional moments, important dialogue

**Close-Up (CU)**: Head and shoulders
- *Use*: Reactions, emphasis, emotion

**Extreme Close-Up (ECU)**: Part of face or object detail
- *Use*: Drama, comedy emphasis, object focus

## Camera Angles

**Eye-Level**: Neutral, comfortable, most common
**High Angle**: Looking down, vulnerable, weak, small
**Low Angle**: Looking up, powerful, heroic, large
**Dutch Angle**: Tilted, unease, chaos, confusion
**Over-the-Shoulder (OTS)**: Conversation perspective
**Bird's Eye**: Overhead, layout, patterns
**Worm's Eye**: Extreme low, dramatic power

## Composition Rules

**Rule of Thirds**:
```
┌─────┬─────┬─────┐
│  •  │     │  •  │  Power points
├─────┼─────┼─────┤
│  •  │     │  •  │
├─────┼─────┼─────┤
│  •  │     │  •  │
└─────┴─────┴─────┘
```
Place subjects at intersections, horizon on top/bottom third.

**Leading Lines**: Environmental elements guide eye to subject
**Framing**: Use doors, windows, objects to frame subject
**Symmetry**: Balanced for formal moments, confrontations
**Depth**: Foreground, midground, background layers

## Segment Types

1. **character-panel** (priority 1): Main panel with characters
2. **speech-bubble** (priority 2): Dialogue overlay
3. **thought-bubble** (priority 2): Internal thoughts
4. **sound-effect-text** (priority 2): "BOOM!", "CRASH!"
5. **comic-effect** (priority 3): Motion lines, impact stars
6. **border** (priority 4): Panel frame
7. **caption** (priority 2): Narration boxes
8. **background-layer** (priority 0): Rendered first

Lower priority = background, higher priority = foreground.

## Beat Sheet → Shotlist Conversion

**Ratio**: 1 beat = 2-4 shots

**Example**:
```
BEAT: "P knocks over coffee onto E's laptop. Screen goes black. E panics."

Converts to 4 shots:
S06: Close-up of P's tail near coffee mug (tension)
S07: Coffee spilling in slow-motion (disaster)
S08: E's horrified face reaction (emotion)
S09: Dead laptop screen, E slumped (aftermath)
```

## Timing Guidelines

**Video Format (30 fps)**:
- Establish shot: 3-5 seconds (90-150 frames)
- Medium shot: 2-3 seconds (60-90 frames)
- Close-up: 1.5-2.5 seconds (45-75 frames)
- Dialogue: ~2 seconds per bubble (60 frames)
- Quick cut: 0.5-1 second (15-30 frames)

**Print Format**:
- No duration (panels are static)
- Panel size indicates importance/time
- Page turn = major transition

## Page Layout Planning

**Standard 6-8 Panel Page**:
```
┌─────────────────────┐
│     PANEL 1 (W)     │  Wide establish
├──────────┬──────────┤
│ PANEL 2  │ PANEL 3  │  Action/reaction
├──────────┴──────────┤
│     PANEL 4 (W)     │  Medium shot
├─────┬──────┬────────┤
│ P5  │  P6  │   P7   │  Quick sequence
├─────┴──────┴────────┤
│     PANEL 8 (W)     │  Punchline/reveal
└─────────────────────┘
```

## Visual Storytelling Techniques

### Show, Don't Tell
Bad: Caption: "E was angry"
Good: Panel: E red-faced, clenched fists, steam from ears

### Transitions
- **Moment-to-Moment**: Hand reaching → grasping → turning
- **Action-to-Action**: Wind up → throw → ball flying → catch
- **Subject-to-Subject**: E speaking → Em listening → P sleeping
- **Scene-to-Scene**: Garage day → Garage night
- **Aspect-to-Aspect**: Window → coffee → laptop → E (mood building)

## Quality Checklist

- [ ] Shot types varied (not all medium shots)
- [ ] Camera angles support emotional tone
- [ ] Composition follows visual principles
- [ ] Clear reading order
- [ ] Each shot has clear purpose
- [ ] Pacing matches narrative beats
- [ ] Segments prioritized correctly
- [ ] Character consistency refs included
- [ ] Environmental details specified
- [ ] Lighting/mood described

## Resources

- Understanding Comics (Scott McCloud)
- Film Language Composition Guide
- Storyboarding Essentials
