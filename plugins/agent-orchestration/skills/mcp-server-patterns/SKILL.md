---
name: mcp-server-patterns
description: MCP (Model Context Protocol) server architecture patterns, multi-provider fallback, tool organization, and client integration strategies. Use when designing MCP servers, implementing provider systems, or orchestrating complex workflows.
---

# MCP Server Patterns

Production-ready patterns for building Model Context Protocol servers with multi-provider support, robust error handling, and scalable tool organization.

## Overview

Based on the `mcp-em-e-comics` server implementation at `/Users/eddie.flores/source/ai-comic-strip/apps/mcp-em-e-comics`, this skill documents proven patterns for MCP server architecture.

## Core Architecture Pattern

### Server Structure

```
mcp-server/
├── src/
│   ├── server.ts              # Main server entry point
│   ├── types/                 # Shared TypeScript types
│   │   └── index.ts
│   ├── clients/               # External service clients
│   │   ├── comfyui.ts
│   │   ├── supabase.ts
│   │   └── gemini.ts
│   ├── tools/                 # Tool implementations (by category)
│   │   ├── story/
│   │   │   ├── index.ts       # Tool exports
│   │   │   ├── create-beat-sheet.ts
│   │   │   └── draft-script.ts
│   │   ├── character-tools/
│   │   ├── image-generation/
│   │   └── assembly/
│   └── utils/                 # Shared utilities
│       ├── config.ts
│       └── validation.ts
├── package.json
└── tsconfig.json
```

### server.ts:73-98 Pattern

```typescript
// Server initialization with health checks
async function initializeClients(): Promise<Clients> {
  const config = await loadConfig()

  // Create client instances
  const comfyuiClient = createComfyUIClient({
    baseUrl: config.comfyui.baseUrl,
    timeout: config.comfyui.timeout,
  })

  let supabaseClient
  if (config.supabase.url && config.supabase.serviceRoleKey) {
    supabaseClient = createSupabaseClient({
      url: config.supabase.url,
      serviceRoleKey: config.supabase.serviceRoleKey,
    })
  }

  // Health checks
  console.error('[Server] Running health checks...')
  const comfyuiHealthy = await comfyuiClient.healthCheck()
  console.error(`[Server] ComfyUI: ${comfyuiHealthy ? '✓ healthy' : '✗ unhealthy'}`)

  if (supabaseClient) {
    const supabaseHealthy = await supabaseClient.healthCheck()
    console.error(`[Server] Supabase: ${supabaseHealthy ? '✓ healthy' : '✗ unhealthy'}`)
  }

  return { comfyui: comfyuiClient, supabase: supabaseClient }
}
```

**Key Benefits:**
- Optional services (Supabase only if configured)
- Health checks on startup
- Clear error logging to stderr
- Client abstraction for testing

## Tool Organization Pattern

### Category-Based Organization

**tools/story/index.ts:12-25**

```typescript
import { createBeatSheetTool } from './create-beat-sheet.js'
import { draftScriptTool } from './draft-script.js'
import { buildShotlistTool } from './build-shotlist.js'
import { validateStoryTool } from './validate-story.js'
import { exportStoryTool } from './export-story.js'

// Export all story tools
export const storyTools = [
  createBeatSheetTool,
  draftScriptTool,
  buildShotlistTool,
  validateStoryTool,
  exportStoryTool,
]
```

**Pattern Benefits:**
- Single responsibility per category
- Easy to add new tools
- Clear import paths
- Scalable to 50+ tools

### Tool Definition Pattern

**tools/story/create-beat-sheet.ts:165-199**

```typescript
export const createBeatSheetTool: any = {
  name: 'create_beat_sheet',  // snake_case convention
  description: 'Generate a structured beat sheet from a story premise for a comic short episode',
  inputSchema: {
    type: 'object',
    properties: {
      episodeId: {
        type: 'string',
        description: 'Unique identifier for the episode (e.g., "pilot", "episode-01")'
      },
      premise: {
        type: 'string',
        description: 'The story premise or logline (1-3 sentences describing the core story)'
      },
      targetDuration: {
        type: 'number',
        description: 'Target duration in seconds (default: 30)',
        default: 30
      },
      genre: {
        type: 'string',
        description: 'Story genre (e.g., "comedy", "drama", "action")',
        default: 'comedy'
      },
      characters: {
        type: 'array',
        items: { type: 'string' },
        description: 'Array of character slugs to feature in the episode',
        default: []
      }
    },
    required: ['episodeId', 'premise']
  },
  handler: createBeatSheet  // Async function
}
```

**Best Practices:**
- **Clear naming**: snake_case for tool names (becomes `mcp__server__create_beat_sheet`)
- **Detailed descriptions**: Explain what the tool does and when to use it
- **Property descriptions**: Document each parameter with examples
- **Defaults**: Provide sensible defaults
- **Required fields**: Minimal required params for flexibility

## Multi-Provider Fallback Pattern

### Provider Factory Pattern

**tools/image-providers/factory.ts pattern:**

```typescript
export class ProviderFactory {
  private static providers: ImageProvider[] = [
    new GeminiProvider(),           // Fast, cheap, good consistency
    new ConsistentCharacterProvider(), // Better consistency
    new FluxProvider(),             // Highest quality
    new LocalComfyUIProvider()      // Full control
  ]

  static async getProvider(): Promise<ImageProvider> {
    const preferred = process.env.IMAGE_GENERATION_PROVIDER

    // Try preferred provider first
    if (preferred && preferred !== 'auto') {
      const provider = this.providers.find(p => p.name === preferred)
      if (provider && await provider.isAvailable()) {
        return provider
      }
    }

    // Fallback through providers
    for (const provider of this.providers) {
      if (await provider.isAvailable()) {
        console.error(`[ProviderFactory] Using provider: ${provider.name}`)
        return provider
      }
    }

    throw new Error('No image generation providers available')
  }
}

// Provider interface
export interface ImageProvider {
  name: string
  isAvailable(): Promise<boolean>
  generate(request: ImageGenerationRequest): Promise<ImageGenerationResponse>
}
```

### render-panel.ts:108-125 Integration

```typescript
// Set provider preference if specified
if (provider && provider !== 'auto') {
  process.env.IMAGE_GENERATION_PROVIDER = provider
}

// Get provider instance (with fallback)
const imageProvider = await ProviderFactory.getProvider()

// Prepare generation request
const request: ImageGenerationRequest = {
  prompt: finalPrompt,
  negativePrompt,
  width,
  height,
  referenceImage,
  outputPath: finalOutputPath
}

// Generate image
const response = await imageProvider.generate(request)
```

**Benefits:**
- **Automatic fallback** - No single point of failure
- **Cost optimization** - Use cheapest available provider
- **User control** - Override with specific provider
- **Graceful degradation** - Always have a fallback

## Client Abstraction Pattern

### ComfyUI Client Example

**clients/comfyui.ts pattern:**

```typescript
export interface ComfyUIClient {
  healthCheck(): Promise<boolean>
  queuePrompt(workflow: any): Promise<{ prompt_id: string }>
  getQueueStatus(): Promise<any>
  getHistory(promptId: string): Promise<any>
  getImage(filename: string, subfolder: string): Promise<Buffer>
}

export function createComfyUIClient(config: ComfyUIConfig): ComfyUIClient {
  const baseUrl = config.baseUrl
  const timeout = config.timeout || 30000

  return {
    async healthCheck(): Promise<boolean> {
      try {
        const response = await fetch(`${baseUrl}/system_stats`, {
          signal: AbortSignal.timeout(timeout)
        })
        return response.ok
      } catch {
        return false
      }
    },

    async queuePrompt(workflow: any) {
      const response = await fetch(`${baseUrl}/prompt`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: workflow }),
        signal: AbortSignal.timeout(timeout)
      })

      if (!response.ok) {
        throw new Error(`ComfyUI error: ${response.statusText}`)
      }

      return await response.json()
    },

    // ... other methods
  }
}
```

**Benefits:**
- **Testable** - Mock client for unit tests
- **Type-safe** - TypeScript interfaces
- **Reusable** - Use in multiple tools
- **Configurable** - Inject config at creation

## Error Handling Pattern

### Tool-Level Error Handling

**tools/character-tools/create-character-from-photo.ts:79-88**

```typescript
try {
  // Tool implementation
  const reference = await createCharacterFromPhoto({
    characterName,
    photoPath,
    analysisPrompt,
    updateExisting
  })

  return {
    content: [
      { type: 'text', text: output.join('\n') },
      { type: 'text', text: JSON.stringify(reference, null, 2) }
    ],
    isError: false
  }
} catch (error) {
  return {
    content: [{
      type: 'text',
      text: `Error creating character from photo: ${error instanceof Error ? error.message : 'Unknown error'}`
    }],
    isError: true
  }
}
```

### Server-Level Error Handling

**server.ts:160-182**

```typescript
try {
  // Call tool handler with arguments and clients
  const result = await (tool as any).handler(
    request.params.arguments || {},
    clients
  )

  console.error(`[Server] Tool ${toolName} completed successfully`)
  return result

} catch (error) {
  console.error(`[Server] Tool ${toolName} error:`, error)

  return {
    content: [{
      type: 'text',
      text: `Error executing ${toolName}: ${error instanceof Error ? error.message : 'Unknown error'}`
    }],
    isError: true
  }
}
```

**Pattern Benefits:**
- **Two-level catching** - Tool errors caught at tool level, unexpected errors at server level
- **User-friendly messages** - Always return useful error text
- **Error logging** - Log to stderr for debugging
- **isError flag** - Claude can detect failures

## Config Management Pattern

**utils/config.ts pattern:**

```typescript
import 'dotenv/config'
import { z } from 'zod'

const ConfigSchema = z.object({
  comfyui: z.object({
    baseUrl: z.string().url().default('http://127.0.0.1:8188'),
    timeout: z.number().default(30000)
  }),
  supabase: z.object({
    url: z.string().url().optional(),
    serviceRoleKey: z.string().optional()
  }),
  workingDirectory: z.string().default(process.cwd())
})

export async function loadConfig() {
  const config = {
    comfyui: {
      baseUrl: process.env.COMFYUI_URL || 'http://127.0.0.1:8188',
      timeout: parseInt(process.env.COMFYUI_TIMEOUT || '30000')
    },
    supabase: {
      url: process.env.SUPABASE_URL,
      serviceRoleKey: process.env.SUPABASE_SERVICE_ROLE_KEY
    },
    workingDirectory: process.env.WORKING_DIRECTORY || process.cwd()
  }

  // Validate config
  return ConfigSchema.parse(config)
}
```

**Benefits:**
- **Type-safe** - Zod validation
- **Defaults** - Sensible defaults for local dev
- **Environment-based** - 12-factor app principle
- **Validation** - Catch config errors early

## Logging Pattern

### Structured Logging to stderr

```typescript
// Always log to stderr (MCP spec: stdout reserved for JSON-RPC)
console.error('[Server] Em & E Comics MCP Server starting...')
console.error(`[Server] ComfyUI: ${comfyuiHealthy ? '✓' : '✗'}`)
console.error(`[Server] ListTools called - ${allTools.length} tools available`)
console.error(`[Server] CallTool: ${toolName}`)
console.error(`[Server] Tool ${toolName} completed successfully`)
console.error(`[Server] Tool ${toolName} error:`, error)
```

**Log Levels by Convention:**
- `[Server]` - Server lifecycle events
- `[ProviderFactory]` - Provider selection
- `[Tool]` - Tool execution (optional)
- `[Client]` - Client operations (optional)

## Type Safety Pattern

**types/index.ts:**

```typescript
export interface Clients {
  comfyui: ComfyUIClient
  supabase: SupabaseClient
}

export interface ToolResult {
  content: Array<{
    type: 'text' | 'resource'
    text?: string
    uri?: string
    data?: any
  }>
  isError?: boolean
}

export interface ImageGenerationRequest {
  prompt: string
  negativePrompt?: string
  width: number
  height: number
  referenceImage?: string
  outputPath: string
}

export interface ImageGenerationResponse {
  success: boolean
  provider: string
  outputPath?: string
  error?: string
  metadata?: {
    cost?: number
    duration?: number
    model?: string
  }
}
```

## Tool Registration Pattern

**server.ts:124-138**

```typescript
async function registerHandlers(clients: Clients) {
  const allTools = getAllTools()  // Combines all tool categories

  // List tools handler
  server.setRequestHandler(ListToolsRequestSchema, async () => {
    console.error(`[Server] ListTools called - ${allTools.length} tools available`)

    return {
      tools: allTools.map(tool => ({
        name: tool.name,
        description: tool.description,
        inputSchema: tool.inputSchema,
      })),
    }
  })

  // Call tool handler
  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    // ... tool execution logic
  })
}
```

## Testing Pattern

```typescript
// Mock clients for testing
const mockClients: Clients = {
  comfyui: {
    healthCheck: async () => true,
    queuePrompt: async () => ({ prompt_id: 'test-123' }),
    // ... other methods
  },
  supabase: {
    healthCheck: async () => true,
    insertBeatSheet: async () => ({ id: 'test-beat-sheet' }),
    // ... other methods
  }
}

// Test tool directly
import { createBeatSheet } from '../tools/story/create-beat-sheet'

describe('createBeatSheet', () => {
  it('should create beat sheet with valid inputs', async () => {
    const result = await createBeatSheet({
      episodeId: 'test',
      premise: 'Test premise',
      targetDuration: 30,
      genre: 'comedy'
    }, mockClients)

    expect(result.isError).toBe(false)
    expect(result.content[0].text).toContain('Beat Sheet')
  })
})
```

## Production Deployment Patterns

### Claude Desktop Integration

**claude_desktop_config.json:**

```json
{
  "mcpServers": {
    "em-e-comics": {
      "command": "node",
      "args": [
        "/Users/eddie.flores/source/ai-comic-strip/apps/mcp-em-e-comics/dist/server.js"
      ]
    }
  }
}
```

### Environment Configuration

**.env:**

```bash
# ComfyUI Configuration
COMFYUI_URL=http://127.0.0.1:8188
COMFYUI_TIMEOUT=30000

# Supabase Configuration (optional)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# Image Generation
IMAGE_GENERATION_PROVIDER=auto  # or gemini, consistent, flux, local

# API Keys
GOOGLE_AI_API_KEY=your-gemini-key
REPLICATE_API_KEY=your-replicate-key

# Working Directory
WORKING_DIRECTORY=/Users/eddie.flores/source/ai-comic-strip
```

### Build Configuration

**package.json:**

```json
{
  "name": "mcp-em-e-comics",
  "version": "0.1.0",
  "type": "module",
  "main": "dist/server.js",
  "bin": {
    "mcp-em-e-comics": "./dist/server.js"
  },
  "scripts": {
    "dev": "tsup --watch",
    "build": "tsup",
    "start": "node dist/server.js",
    "test": "vitest"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0",
    "@supabase/supabase-js": "^2.45.0",
    "dotenv": "^17.2.3",
    "zod": "^3.23.0"
  }
}
```

**tsup.config.ts:**

```typescript
import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['src/server.ts'],
  format: ['esm'],
  dts: true,
  clean: true,
  shims: true,
  minify: false,
  sourcemap: true
})
```

## Scalability Patterns

### Tool Count Management

- **0-10 tools**: Single file OK
- **10-30 tools**: Category-based organization (story/, character/, etc.)
- **30-50 tools**: Add subcategories (story/beat-sheet/, story/script/)
- **50+ tools**: Consider multiple MCP servers by domain

### Performance Optimization

```typescript
// Lazy-load heavy dependencies
async function createBeatSheet(args, clients) {
  // Only import AI client when actually needed
  const { generateWithClaude } = await import('../utils/ai-client')

  // Tool implementation...
}

// Cache expensive operations
const styleCache = new Map()

export async function getStylePresets() {
  if (styleCache.has('presets')) {
    return styleCache.get('presets')
  }

  const presets = await loadStylePresets()
  styleCache.set('presets', presets)
  return presets
}
```

## Best Practices Summary

1. **Organize by category** - Group related tools
2. **Abstract clients** - Testable, reusable
3. **Multi-provider fallback** - No single point of failure
4. **Health checks on startup** - Fail fast
5. **Detailed input schemas** - Self-documenting
6. **Two-level error handling** - Tool + server level
7. **Log to stderr** - stdout reserved for JSON-RPC
8. **Type everything** - TypeScript for safety
9. **Environment config** - 12-factor app
10. **Test tools directly** - Mock clients

## Reference Implementation

**Full example**: `/Users/eddie.flores/source/ai-comic-strip/apps/mcp-em-e-comics`

**Key files to study:**
- `src/server.ts` - Server initialization and registration
- `src/tools/image-generation/render-panel.ts` - Multi-provider pattern
- `src/clients/comfyui.ts` - Client abstraction
- `src/types/index.ts` - Type definitions
- `package.json` - Build and dependency management
