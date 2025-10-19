---
name: voice-character-matching
description: Match AI-generated voices to comic characters using ElevenLabs, voice design principles, and character personality alignment. Use when creating character voices, producing audio comics, or designing voice profiles.
---

# Voice-Character Matching

Guide to creating authentic, character-appropriate AI voices using ElevenLabs for audio comics and video content.

## Character Voice Profiles

### Em (Daughter)

**Voice Characteristics**:
- **Age**: Pre-teen (11-13)
- **Gender**: Female
- **Pitch**: Medium-high
- **Pace**: Fast, energetic
- **Energy**: High, dynamic
- **Tone**: Bright, confident, playful

**Voice Description for Generation**:
```
"Young energetic female voice, pre-teen age 11-13,
confident and bright tone, fast-paced speech,
playful and smart delivery, modern kid energy"
```

**ElevenLabs Settings**:
```javascript
{
  voice_name: "Em_Character",
  stability: 0.4,  // More expressive
  similarity_boost: 0.75,
  style: 0.3,  // Slight style emphasis
  speed: 1.05  // Slightly faster
}
```

**Speech Patterns**:
- Quick, snappy responses
- Modern slang ("W dad", "Father, no")
- Playful sass
- Smart observations
- Confident assertions

### E (Dad)

**Voice Characteristics**:
- **Age**: 30s-40s
- **Gender**: Male
- **Pitch**: Medium-low
- **Pace**: Medium, conversational
- **Energy**: Warm, patient
- **Tone**: Friendly, approachable

**Voice Description**:
```
"Warm friendly male voice, 30s-40s dad energy,
conversational tone, patient and approachable,
slight tech-savvy vibe, genuine warmth"
```

**ElevenLabs Settings**:
```javascript
{
  voice_name: "E_Character",
  stability: 0.5,  // Balanced
  similarity_boost: 0.80,
  style: 0,
  speed: 1.0  // Normal pace
}
```

**Speech Patterns**:
- Dad jokes
- Programming references ("Let me commit to that")
- Patient explanations
- Warm encouragement
- Genuine attempts at connection

### P (Dog)

**Voice Characteristics**:
- **Type**: Thought bubbles / narrator
- **Tone**: Simple, dog-focused, comedic
- **Delivery**: Short, punchy

**Voice Description** (for narrated thoughts):
```
"Gentle warm narrator voice for dog thoughts,
simple playful delivery, comedic timing"
```

**Thought Patterns**:
- Simple words ("Treats?", "Walk?")
- Confusion ("???")
- Love ("Love humans!")
- Guilty ("Didn't mean to...")

## Voice Cloning Workflow

### Recording Requirements

**Sample Quality**:
- Duration: 60 seconds minimum (3 hours optimal)
- Environment: Quiet, no background noise
- Equipment: Professional mic or high-quality recording
- Distance: 2 fists from microphone
- Content: Varied emotions and expressions

**Sample Diversity for Em**:
```
Recording Script (3 minutes total):
1. Excited: "Dad! Check this out! This is so cool!"
2. Sass: "Father... that's a hard no. W attempt though."
3. Thinking: "Hmm, wait... what if we tried it this way?"
4. Explaining: "Okay so basically what happens is..."
5. Happy: "Yes! I knew it would work! This is awesome!"
6. Frustrated: "Ugh, come on! Why isn't this working?"
```

### Voice Generation

```javascript
// Generate voice previews
await mcp__elevenlabs__text_to_voice({
  voice_description: "Young energetic female, pre-teen 11-13, bright confident tone",
  text: "Hey dad! Check out what I built! It's actually pretty cool."
})

// Creates 3 variations, choose best
// Save voice ID for character card
```

### Voice Integration

```javascript
// Add to character card
{
  "slug": "em",
  "voice": {
    "elevenlabs_voice_id": "voice_abc123",
    "voice_name": "Em_Character",
    "settings": {
      "stability": 0.4,
      "similarity_boost": 0.75,
      "speed": 1.05
    }
  }
}
```

## Dialogue Delivery

### Natural Speech Techniques

**Conversational Imperfections** (Em):
```
"So like... [pause] I was thinking, you know,
maybe we could try it... differently?
I mean, if that's cool with you."
```

**Emphasis & Emotion** (E):
```
"Em, this is REALLY important. [serious]
I need you to listen carefully. [pause]
Can you do that for me?"
```

## Audio Comic Production

### Dialogue Recording

```javascript
// Generate dialogue for panels
async function generateDialogue(episode) {
  const shotlist = loadShotlist(episode)

  for (const shot of shotlist) {
    const bubbles = shot.segments.filter(s => s.type === 'speech-bubble')

    for (const bubble of bubbles) {
      const character = getCharacter(bubble.character)
      const voiceSettings = character.voice.settings

      // Generate speech
      const audio = await mcp__elevenlabs__text_to_speech({
        text: bubble.dialogue,
        voice_name: character.voice.voice_name,
        ...voiceSettings
      })

      // Save audio segment
      saveAudio(audio, `${shot.shot_id}_${bubble.id}.mp3`)
    }
  }
}
```

### Sound Effects Integration

```javascript
// Generate sound effects for comic
await mcp__elevenlabs__text_to_sound_effects({
  text: "Keyboard typing on mechanical switches",
  duration_seconds: 2
})

await mcp__elevenlabs__text_to_sound_effects({
  text: "Coffee mug tipping and spilling on laptop",
  duration_seconds: 3
})
```

## Quality Control

**Voice Consistency Checklist**:
- [ ] Voice matches character age
- [ ] Tone aligns with personality
- [ ] Pacing appropriate (Em faster, E measured)
- [ ] Emotional range feels authentic
- [ ] Speech patterns match character
- [ ] No robotic artifacts
- [ ] Natural prosody and inflection

## Resources

- ElevenLabs Voice Lab
- Voice Acting Principles
- Character Voice Design
- Audio Production Guide
