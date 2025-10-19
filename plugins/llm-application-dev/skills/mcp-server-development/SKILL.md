---
name: mcp-server-development
description: MCP (Model Context Protocol) server development guide with TypeScript, tool implementation, client integration, and deployment patterns. Use when building MCP servers, implementing custom tools, or integrating external services.
---

# MCP Server Development

Step-by-step guide to building production-ready MCP servers using the `mcp-comic-strip-studio` server as a reference implementation.

## Quick Start

### 1. Project Setup

```bash
# Create MCP server project
mkdir mcp-my-server
cd mcp-my-server

# Initialize package.json
pnpm init

# Install dependencies
pnpm add @modelcontextprotocol/sdk zod dotenv
pnpm add -D typescript tsup tsx vitest @types/node
```

### 2. Package Configuration

**package.json:**

```json
{
  "name": "mcp-my-server",
  "version": "0.1.0",
  "type": "module",
  "main": "dist/server.js",
  "bin": {
    "mcp-my-server": "./dist/server.js"
  },
  "scripts": {
    "dev": "tsup --watch",
    "build": "tsup",
    "start": "node dist/server.js",
    "test": "vitest"
  }
}
```

**tsconfig.json:**

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": ["ES2022"],
    "moduleResolution": "node",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
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

### 3. Server Implementation

**src/server.ts** (based on mcp-comic-strip-studio/src/server.ts):

```typescript
import 'dotenv/config'
import { Server } from '@modelcontextprotocol/sdk/server/index.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  type Tool
} from '@modelcontextprotocol/sdk/types.js'

// Initialize MCP server
const server = new Server(
  {
    name: 'mcp-my-server',
    version: '0.1.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
)

// Tool definitions
const tools: Tool[] = [
  {
    name: 'example_tool',
    description: 'An example tool that greets the user',
    inputSchema: {
      type: 'object',
      properties: {
        name: {
          type: 'string',
          description: 'Name of the person to greet'
        }
      },
      required: ['name']
    }
  }
]

// List tools handler
server.setRequestHandler(ListToolsRequestSchema, async () => {
  console.error(`[Server] ListTools called - ${tools.length} tools available`)
  return { tools }
})

// Call tool handler
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const toolName = request.params.name
  console.error(`[Server] CallTool: ${toolName}`)

  if (toolName === 'example_tool') {
    const { name } = request.params.arguments as { name: string }

    return {
      content: [{
        type: 'text',
        text: `Hello, ${name}! Welcome to MCP.`
      }],
      isError: false
    }
  }

  return {
    content: [{
      type: 'text',
      text: `Error: Unknown tool "${toolName}"`
    }],
    isError: true
  }
})

// Main server startup
async function main() {
  try {
    console.error('[Server] MCP Server starting...')

    const transport = new StdioServerTransport()
    await server.connect(transport)

    console.error('[Server] Server connected and ready')
    console.error('[Server] Listening on stdio for MCP requests')
  } catch (error) {
    console.error('[Server] Fatal error:', error)
    process.exit(1)
  }
}

main().catch((error) => {
  console.error('[Server] Unhandled error:', error)
  process.exit(1)
})
```

### 4. Build and Test

```bash
# Build server
pnpm build

# Test locally (in terminal)
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | node dist/server.js
```

### 5. Claude Desktop Integration

**~/.config/Claude/claude_desktop_config.json** (macOS):

```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["/absolute/path/to/mcp-my-server/dist/server.js"]
    }
  }
}
```

Restart Claude Desktop to load the server.

## Tool Implementation Patterns

### Basic Tool Structure

From `mcp-comic-strip-studio/src/tools/story/create-beat-sheet.ts`:

```typescript
/**
 * Tool arguments interface
 */
export interface CreateBeatSheetArgs {
  episodeId: string
  premise: string
  targetDuration?: number
  genre?: string
  characters?: string[]
}

/**
 * Tool handler function
 */
export async function createBeatSheet(
  args: CreateBeatSheetArgs,
  clients: Clients  // Injected dependencies
): Promise<ToolResult> {
  const {
    episodeId,
    premise,
    targetDuration = 30,
    genre = 'comedy',
    characters = []
  } = args

  try {
    // Input validation
    if (!episodeId || !premise) {
      return {
        content: [{
          type: 'text',
          text: 'Error: episodeId and premise are required'
        }],
        isError: true
      }
    }

    // Tool logic
    const beatSheet = generateBeatStructure(
      premise,
      beatCount,
      genre,
      characters
    )

    // Store in database (optional)
    if (clients.supabase) {
      await clients.supabase.insertBeatSheet(episodeId, beatSheet)
    }

    // Return success
    return {
      content: [{ type: 'text', text: `# Beat Sheet\\n\\n${beatSheet}` }]
    }

  } catch (error) {
    // Error handling
    return {
      content: [{
        type: 'text',
        text: `Error creating beat sheet: ${error instanceof Error ? error.message : 'Unknown error'}`
      }],
      isError: true
    }
  }
}

/**
 * MCP Tool Definition
 */
export const createBeatSheetTool: Tool & { handler: typeof createBeatSheet } = {
  name: 'create_beat_sheet',
  description: 'Generate a structured beat sheet from a story premise',
  inputSchema: {
    type: 'object',
    properties: {
      episodeId: {
        type: 'string',
        description: 'Unique identifier for the episode (e.g., "pilot")'
      },
      premise: {
        type: 'string',
        description: 'The story premise or logline (1-3 sentences)'
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
        description: 'Array of character slugs',
        default: []
      }
    },
    required: ['episodeId', 'premise']
  },
  handler: createBeatSheet
}
```

### Tool with External API Integration

From `mcp-comic-strip-studio/src/tools/image-generation/render-panel.ts`:

```typescript
export async function renderPanel(
  args: RenderPanelArgs,
  clients: Clients
): Promise<ToolResult> {
  const {
    episodeId,
    shotId,
    prompt,
    width = 768,
    height = 1365,
    provider = 'auto'
  } = args

  try {
    // Validate inputs
    if (!episodeId || !shotId || !prompt) {
      return {
        content: [{ type: 'text', text: 'Error: Missing required parameters' }],
        isError: true
      }
    }

    // Set provider preference
    if (provider !== 'auto') {
      process.env.IMAGE_GENERATION_PROVIDER = provider
    }

    // Get provider instance (with automatic fallback)
    const imageProvider = await ProviderFactory.getProvider()

    // Prepare request
    const request: ImageGenerationRequest = {
      prompt,
      width,
      height,
      outputPath: `output/${episodeId}/panels/${shotId}.png`
    }

    // Call external API
    const startTime = Date.now()
    const response = await imageProvider.generate(request)
    const duration = ((Date.now() - startTime) / 1000).toFixed(1)

    // Handle failure
    if (!response.success) {
      return {
        content: [{ type: 'text', text: `Generation failed: ${response.error}` }],
        isError: true
      }
    }

    // Return success with metadata
    return {
      content: [
        {
          type: 'text',
          text: `✅ Panel ${shotId} rendered!\\n` +
                `🎨 Provider: ${response.provider}\\n` +
                `⏱️  Duration: ${duration}s\\n` +
                `💰 Cost: $${response.metadata?.cost?.toFixed(3) || 'N/A'}`
        },
        {
          type: 'resource',
          uri: `file://${path.resolve(response.outputPath!)}`,
          data: { episodeId, shotId, provider: response.provider }
        }
      ]
    }
  } catch (error) {
    return {
      content: [{
        type: 'text',
        text: `Error: ${error instanceof Error ? error.message : 'Unknown error'}`
      }],
      isError: true
    }
  }
}
```

## Client Abstraction Pattern

### Creating a Client

From `mcp-comic-strip-studio/src/clients/comfyui.ts`:

```typescript
export interface ComfyUIClient {
  healthCheck(): Promise<boolean>
  queuePrompt(workflow: any): Promise<{ prompt_id: string }>
  getHistory(promptId: string): Promise<any>
  getImage(filename: string, subfolder: string): Promise<Buffer>
}

export interface ComfyUIConfig {
  baseUrl: string
  timeout?: number
}

export function createComfyUIClient(config: ComfyUIConfig): ComfyUIClient {
  const { baseUrl, timeout = 30000 } = config

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

    async getHistory(promptId: string) {
      const response = await fetch(`${baseUrl}/history/${promptId}`, {
        signal: AbortSignal.timeout(timeout)
      })
      return await response.json()
    },

    async getImage(filename: string, subfolder: string): Promise<Buffer> {
      const params = new URLSearchParams({ filename, subfolder, type: 'output' })
      const response = await fetch(`${baseUrl}/view?${params}`)

      if (!response.ok) {
        throw new Error(`Failed to fetch image: ${response.statusText}`)
      }

      return Buffer.from(await response.arrayBuffer())
    }
  }
}
```

### Using Clients in Server

From `mcp-comic-strip-studio/src/server.ts`:

```typescript
export interface Clients {
  comfyui: ComfyUIClient
  supabase: SupabaseClient
}

async function initializeClients(): Promise<Clients> {
  const config = await loadConfig()

  // Create clients
  const comfyuiClient = createComfyUIClient({
    baseUrl: config.comfyui.baseUrl,
    timeout: config.comfyui.timeout
  })

  let supabaseClient
  if (config.supabase.url && config.supabase.serviceRoleKey) {
    supabaseClient = createSupabaseClient({
      url: config.supabase.url,
      serviceRoleKey: config.supabase.serviceRoleKey
    })
  }

  // Health checks
  const comfyuiHealthy = await comfyuiClient.healthCheck()
  console.error(`[Server] ComfyUI: ${comfyuiHealthy ? '✓' : '✗'}`)

  if (supabaseClient) {
    const supabaseHealthy = await supabaseClient.healthCheck()
    console.error(`[Server] Supabase: ${supabaseHealthy ? '✓' : '✗'}`)
  }

  return { comfyui: comfyuiClient, supabase: supabaseClient! }
}

// Pass clients to tool handlers
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const tool = allTools.find(t => t.name === request.params.name)

  if (!tool) {
    return { content: [{ type: 'text', text: 'Unknown tool' }], isError: true }
  }

  try {
    // Inject clients into tool handler
    return await (tool as any).handler(request.params.arguments || {}, clients)
  } catch (error) {
    return {
      content: [{ type: 'text', text: `Error: ${error}` }],
      isError: true
    }
  }
})
```

## Configuration Management

### Config with Zod Validation

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
  apiKeys: z.object({
    googleAI: z.string().optional(),
    replicate: z.string().optional()
  }),
  workingDirectory: z.string().default(process.cwd())
})

export type Config = z.infer<typeof ConfigSchema>

export async function loadConfig(): Promise<Config> {
  const config = {
    comfyui: {
      baseUrl: process.env.COMFYUI_URL || 'http://127.0.0.1:8188',
      timeout: parseInt(process.env.COMFYUI_TIMEOUT || '30000')
    },
    supabase: {
      url: process.env.SUPABASE_URL,
      serviceRoleKey: process.env.SUPABASE_SERVICE_ROLE_KEY
    },
    apiKeys: {
      googleAI: process.env.GOOGLE_AI_API_KEY,
      replicate: process.env.REPLICATE_API_KEY
    },
    workingDirectory: process.env.WORKING_DIRECTORY || process.cwd()
  }

  // Validate and return
  return ConfigSchema.parse(config)
}
```

**.env:**

```bash
# ComfyUI
COMFYUI_URL=http://127.0.0.1:8188
COMFYUI_TIMEOUT=30000

# Supabase (optional)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-key

# API Keys (optional)
GOOGLE_AI_API_KEY=your-gemini-key
REPLICATE_API_KEY=your-replicate-key

# Working Directory
WORKING_DIRECTORY=/path/to/project
```

## Multi-Provider Pattern

### Provider Interface

```typescript
export interface ImageProvider {
  name: string
  cost: number  // Cost per image in USD
  isAvailable(): Promise<boolean>
  generate(request: ImageGenerationRequest): Promise<ImageGenerationResponse>
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

### Provider Factory

```typescript
export class ProviderFactory {
  private static providers: ImageProvider[] = [
    new GeminiProvider(),           // $0.002, 4-6s, good consistency
    new ConsistentCharacterProvider(), // $0.01, 10-15s, better consistency
    new FluxProvider(),             // $0.03, 15-20s, best quality
    new LocalComfyUIProvider()      // Free, variable time, full control
  ]

  static async getProvider(preference?: string): Promise<ImageProvider> {
    // Try preferred provider first
    if (preference && preference !== 'auto') {
      const provider = this.providers.find(p => p.name === preference)
      if (provider && await provider.isAvailable()) {
        console.error(`[ProviderFactory] Using preferred: ${provider.name}`)
        return provider
      }
      console.error(`[ProviderFactory] Preferred provider ${preference} unavailable, falling back...`)
    }

    // Fallback through providers in order
    for (const provider of this.providers) {
      if (await provider.isAvailable()) {
        console.error(`[ProviderFactory] Using provider: ${provider.name}`)
        return provider
      }
    }

    throw new Error('No image generation providers available')
  }

  static async listProviders() {
    const statuses = await Promise.all(
      this.providers.map(async (p) => ({
        name: p.name,
        cost: `$${p.cost.toFixed(3)}/image`,
        available: await p.isAvailable()
      }))
    )
    return statuses
  }
}
```

### Provider Implementation Example

```typescript
import { GoogleGenerativeAI } from '@google/generative-ai'

export class GeminiProvider implements ImageProvider {
  name = 'gemini-2.5-flash'
  cost = 0.002

  private client: GoogleGenerativeAI | null = null

  async isAvailable(): Promise<boolean> {
    if (!process.env.GOOGLE_AI_API_KEY) {
      return false
    }

    try {
      this.client = new GoogleGenerativeAI(process.env.GOOGLE_AI_API_KEY)
      return true
    } catch {
      return false
    }
  }

  async generate(request: ImageGenerationRequest): Promise<ImageGenerationResponse> {
    if (!this.client) {
      return { success: false, provider: this.name, error: 'Client not initialized' }
    }

    try {
      const model = this.client.getGenerativeModel({ model: 'imagen-3.0-generate-001' })

      const result = await model.generateImages({
        prompt: request.prompt,
        numberOfImages: 1,
        aspectRatio: `${request.width}:${request.height}`
      })

      // Download and save image
      const imageData = result.images[0].data
      await fs.promises.writeFile(request.outputPath, Buffer.from(imageData, 'base64'))

      return {
        success: true,
        provider: this.name,
        outputPath: request.outputPath,
        metadata: {
          cost: this.cost,
          model: 'imagen-3.0-generate-001'
        }
      }
    } catch (error) {
      return {
        success: false,
        provider: this.name,
        error: error instanceof Error ? error.message : 'Unknown error'
      }
    }
  }
}
```

## Testing

### Unit Testing Tools

```typescript
import { describe, it, expect, beforeEach } from 'vitest'
import { createBeatSheet } from '../tools/story/create-beat-sheet'

// Mock clients
const mockClients = {
  comfyui: {
    healthCheck: async () => true,
    queuePrompt: async () => ({ prompt_id: 'test-123' }),
    getHistory: async () => ({}),
    getImage: async () => Buffer.from('')
  },
  supabase: {
    healthCheck: async () => true,
    insertBeatSheet: async (id, content) => ({ id, content })
  }
}

describe('createBeatSheet', () => {
  it('should create beat sheet with valid inputs', async () => {
    const result = await createBeatSheet({
      episodeId: 'test-episode',
      premise: 'A developer learns debugging',
      targetDuration: 60,
      genre: 'comedy'
    }, mockClients)

    expect(result.isError).toBe(false)
    expect(result.content[0].text).toContain('Beat Sheet')
    expect(result.content[0].text).toContain('test-episode')
  })

  it('should return error for missing required fields', async () => {
    const result = await createBeatSheet({
      episodeId: '',
      premise: '',
    }, mockClients)

    expect(result.isError).toBe(true)
    expect(result.content[0].text).toContain('Error')
  })

  it('should use default values', async () => {
    const result = await createBeatSheet({
      episodeId: 'test',
      premise: 'Test premise'
    }, mockClients)

    expect(result.isError).toBe(false)
    // Should use default duration (30s) and genre (comedy)
  })
})
```

### Integration Testing

```bash
# Test MCP server manually
pnpm build

# List tools
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | node dist/server.js

# Call tool
echo '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"create_beat_sheet","arguments":{"episodeId":"test","premise":"Test story"}}}' | node dist/server.js
```

## Deployment

### Claude Desktop

**~/.config/Claude/claude_desktop_config.json:**

```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["/absolute/path/to/dist/server.js"]
    }
  }
}
```

### NPM Package

```bash
# Publish to npm
pnpm build
npm publish

# Users install globally
npm install -g mcp-my-server

# Claude Desktop config
{
  "mcpServers": {
    "my-server": {
      "command": "mcp-my-server"
    }
  }
}
```

### Docker (for complex dependencies)

**Dockerfile:**

```dockerfile
FROM node:20-slim

WORKDIR /app

COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install --frozen-lockfile

COPY . .
RUN pnpm build

CMD ["node", "dist/server.js"]
```

**Claude Desktop config:**

```json
{
  "mcpServers": {
    "my-server": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "my-server-image"]
    }
  }
}
```

## Best Practices

1. **Always log to stderr** - stdout is reserved for JSON-RPC
2. **Validate inputs** - Use Zod or TypeScript for type safety
3. **Abstract external services** - Create client interfaces
4. **Implement health checks** - Fail fast on startup
5. **Provide detailed error messages** - Help users debug
6. **Use environment variables** - 12-factor app principle
7. **Handle timeouts** - Set reasonable timeouts for external APIs
8. **Support optional services** - Graceful degradation
9. **Document tool schemas** - Clear descriptions and examples
10. **Test tools independently** - Mock clients for unit tests

## Common Patterns

### Progress Reporting

```typescript
// For long-running operations
export async function generateEpisode(args, clients): Promise<ToolResult> {
  const steps = ['beatsheet', 'script', 'shotlist', 'panels', 'assembly']

  for (let i = 0; i < steps.length; i++) {
    const step = steps[i]
    console.error(`[generateEpisode] Step ${i + 1}/${steps.length}: ${step}`)

    // Execute step...
    await executeStep(step, args, clients)
  }

  return {
    content: [{
      type: 'text',
      text: '✅ Episode generation complete!'
    }]
  }
}
```

### Batching

```typescript
// Process items in batches
export async function batchGenerate(args, clients): Promise<ToolResult> {
  const { items, batchSize = 5 } = args

  const results = []
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize)

    const batchResults = await Promise.all(
      batch.map(item => processItem(item, clients))
    )

    results.push(...batchResults)

    // Log progress
    console.error(`[batchGenerate] Processed ${i + batch.length}/${items.length}`)
  }

  return {
    content: [{
      type: 'text',
      text: `Processed ${results.length} items`
    }]
  }
}
```

### Caching

```typescript
const cache = new Map<string, any>()

export async function getCachedData(key: string, fetcher: () => Promise<any>) {
  if (cache.has(key)) {
    console.error(`[Cache] Hit: ${key}`)
    return cache.get(key)
  }

  console.error(`[Cache] Miss: ${key}`)
  const data = await fetcher()
  cache.set(key, data)
  return data
}

// Usage in tool
const styles = await getCachedData('style-presets', async () => {
  return await loadStylePresetsFromDisk()
})
```

## Resources

- **Reference Implementation**: `/Users/eddie.flores/source/ai-comic-strip/apps/mcp-comic-strip-studio`
- **MCP SDK Docs**: https://github.com/anthropics/model-context-protocol
- **TypeScript Handbook**: https://www.typescriptlang.org/docs/
- **Zod Documentation**: https://zod.dev/
