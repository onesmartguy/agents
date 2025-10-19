# .NET Plugins Implementation Plan

## Executive Summary

This document outlines the comprehensive implementation plan for creating two focused .NET plugins for the Claude Code plugin marketplace:

1. **dotnet-development** - Modern .NET 8+ development with CQRS, DDD, and clean architecture
2. **dotnet-framework** - Legacy .NET Framework 4.8 development with ASP.NET MVC, Web Forms, and EF6

These plugins follow the established patterns from the `python-development` plugin and incorporate domain expertise from the payk12 project's .NET architecture.

---

## Analysis Summary

### Python Development Plugin Structure (Reference)

**Components:**
- **3 Agents** (all Sonnet model):
  - `python-pro`: General Python 3.12+ expert
  - `django-pro`: Django 5.x specialist
  - `fastapi-pro`: FastAPI async specialist
- **1 Command**:
  - `python-scaffold`: Comprehensive project scaffolding for FastAPI, Django, library, CLI
- **5 Skills**:
  - `async-python-patterns`: AsyncIO and concurrent programming
  - `python-testing-patterns`: pytest and testing strategies
  - `python-packaging`: Modern Python packaging
  - `python-performance-optimization`: Performance tuning
  - `uv-package-manager`: Modern dependency management

**Key Patterns Observed:**
- Agents have comprehensive frontmatter (name, description with "Use PROACTIVELY", model)
- Commands provide step-by-step scaffolding with bash commands and complete code examples
- Skills use progressive disclosure with "Use when" activation criteria
- All focused on modern tooling and current best practices

### Existing .NET Agents Analysis (from payk12/.claude)

**dotnet-pro Agent:**
- **Focus**: .NET 8/9/10, custom CQRS, Domain-Driven Design, clean architecture
- **Key Technologies**: FastEndpoints, Entity Framework Core, Mapster, MassTransit
- **Expertise Areas**:
  - Custom CQRS implementation (hand-rolled dispatchers, pipeline behaviors)
  - Domain-Driven Design (aggregates, value objects, domain services)
  - Async programming mastery (Task, ValueTask, Channels, IAsyncEnumerable)
  - Performance optimization (Span<T>, Memory<T>, ArrayPool)
  - Testing (Moq, FluentValidation, Bogus, TestContainers)

**dotnet-legacy-pro Agent:**
- **Focus**: .NET Framework 4.8, ASP.NET MVC 5, Entity Framework 6
- **Key Technologies**: Web API 2, WCF, Web Forms
- **Expertise Areas**:
  - Legacy repository pattern and service layer
  - Entity Framework 6 optimization
  - Backwards compatibility and incremental modernization
  - Integration with modern systems via adapters

**Architecture Patterns (from payk12/docs):**
- CQRS with MediatR pipeline
- Domain Events with Outbox Pattern
- Specification Pattern for reusable queries
- Clean Architecture (Domain, Application, Infrastructure, Presentation)
- Pagination strategies (offset-based, cursor-based, keyset)

---

## Plugin 1: dotnet-development

### Plugin Metadata

```json
{
  "name": "dotnet-development",
  "source": "./plugins/dotnet-development",
  "description": "Modern .NET 8+ development with CQRS, DDD, clean architecture, and async patterns",
  "version": "1.2.2",
  "author": {
    "name": "Seth Hobson",
    "url": "https://github.com/wshobson"
  },
  "homepage": "https://github.com/wshobson/agents",
  "repository": "https://github.com/wshobson/agents",
  "license": "MIT",
  "keywords": [
    "dotnet",
    "csharp",
    "aspnet-core",
    "cqrs",
    "domain-driven-design",
    "essential"
  ],
  "category": "languages",
  "strict": false
}
```

### Agents (3 total, all Sonnet model)

#### 1. dotnet-pro.md

**Frontmatter:**
```yaml
---
name: dotnet-pro
description: Master .NET 8+ with clean architecture, CQRS, Domain-Driven Design, and async patterns. Expert in Entity Framework Core, FastEndpoints, and modern C# development. Use PROACTIVELY for .NET backend architecture, CQRS implementation, or complex domain modeling.
model: sonnet
---
```

**Content Focus:**
- .NET 8/9/10 features (file-scoped namespaces, record types, nullable reference types)
- Custom CQRS implementation without MediatR dependency
- Domain-Driven Design patterns (aggregates, value objects, domain services)
- Clean Architecture (Domain, Application, Infrastructure, Presentation layers)
- Async programming mastery (Task, ValueTask, Channels, IAsyncEnumerable)
- Performance optimization (Span<T>, Memory<T>, ArrayPool, expression trees)
- Modern testing (xUnit, Moq, FluentValidation, Bogus, TestContainers)
- FastEndpoints for lightweight API development
- Entity Framework Core with async patterns
- Mapster for object mapping
- MassTransit for message brokering
- Azure integration (Container Apps, Service Bus, Application Insights)

**Behavioral Traits:**
- Follows clean architecture principles
- Implements CQRS for complex business logic
- Uses async/await throughout
- Writes testable, maintainable code
- Documents with XML comments
- Applies nullable reference types
- Uses modern C# features (records, pattern matching, switch expressions)

#### 2. aspnet-core-pro.md

**Frontmatter:**
```yaml
---
name: aspnet-core-pro
description: Build high-performance ASP.NET Core APIs with minimal APIs, middleware, authentication, and API versioning. Expert in modern web development with .NET 8+. Use PROACTIVELY for API development, authentication patterns, or web service architecture.
model: sonnet
---
```

**Content Focus:**
- ASP.NET Core 8+ features
- Minimal APIs vs Controller-based APIs
- Middleware pipeline and custom middleware
- Authentication & Authorization (JWT, OAuth2, Identity)
- API versioning strategies (URL, header, query string)
- OpenAPI/Swagger documentation
- Rate limiting and throttling
- CORS configuration
- Health checks and observability
- Response caching and distributed caching
- gRPC services integration
- SignalR for real-time communication
- Background services and hosted services
- Dependency injection patterns
- Configuration management (appsettings, user secrets, environment variables)

**Behavioral Traits:**
- Implements RESTful API best practices
- Uses dependency injection throughout
- Configures comprehensive error handling
- Implements proper authentication/authorization
- Documents APIs with OpenAPI
- Optimizes for performance and scalability

#### 3. ef-core-pro.md

**Frontmatter:**
```yaml
---
name: ef-core-pro
description: Master Entity Framework Core 8+ with migrations, performance optimization, and advanced querying. Expert in database design, LINQ, and data access patterns. Use PROACTIVELY for database architecture, EF Core optimization, or complex data modeling.
model: sonnet
---
```

**Content Focus:**
- Entity Framework Core 8+ features
- Database-first vs Code-first approaches
- Migrations and seeding strategies
- Query optimization (AsNoTracking, compiled queries, split queries)
- Relationship configuration (one-to-one, one-to-many, many-to-many)
- Global query filters
- Value converters and comparers
- Owned entities and table splitting
- Temporal tables for audit history
- Interceptors and events
- Connection resiliency and retry logic
- Database providers (SQL Server, PostgreSQL, SQLite)
- Performance profiling and diagnostics
- Repository and Unit of Work patterns
- Specification pattern implementation

**Behavioral Traits:**
- Optimizes queries for performance
- Uses AsNoTracking for read-only queries
- Implements proper indexing strategies
- Handles concurrency conflicts
- Uses migrations for schema changes
- Tests database logic with TestContainers

### Commands (1 total)

#### dotnet-scaffold.md

**Purpose:** Comprehensive .NET project scaffolding for various architectures

**Content Structure:**

##### 1. Analyze Project Type
- **Clean Architecture API**: CQRS, DDD, multi-layer architecture
- **Minimal API**: Lightweight, modern .NET 8+ API
- **Blazor Application**: Interactive web UI with .NET
- **Library/NuGet Package**: Reusable class library
- **Console Application**: CLI tools
- **Worker Service**: Background processing

##### 2. Initialize with .NET CLI

```bash
# Create solution
dotnet new sln -n ProjectName

# Create clean architecture structure
dotnet new classlib -n ProjectName.Domain -o src/ProjectName.Domain
dotnet new classlib -n ProjectName.Application -o src/ProjectName.Application
dotnet new classlib -n ProjectName.Infrastructure -o src/ProjectName.Infrastructure
dotnet new webapi -n ProjectName.Api -o src/ProjectName.Api

# Create test projects
dotnet new xunit -n ProjectName.Domain.Tests -o tests/ProjectName.Domain.Tests
dotnet new xunit -n ProjectName.Application.Tests -o tests/ProjectName.Application.Tests
dotnet new xunit -n ProjectName.Api.IntegrationTests -o tests/ProjectName.Api.IntegrationTests

# Add projects to solution
dotnet sln add src/**/*.csproj
dotnet sln add tests/**/*.csproj

# Add project references
dotnet add src/ProjectName.Application/ProjectName.Application.csproj reference src/ProjectName.Domain/ProjectName.Domain.csproj
dotnet add src/ProjectName.Infrastructure/ProjectName.Infrastructure.csproj reference src/ProjectName.Application/ProjectName.Application.csproj
dotnet add src/ProjectName.Api/ProjectName.Api.csproj reference src/ProjectName.Infrastructure/ProjectName.Infrastructure.csproj
```

##### 3. Generate Clean Architecture API Structure

**Complete project structure with:**
- Domain layer (entities, value objects, domain events)
- Application layer (CQRS handlers, DTOs, interfaces)
- Infrastructure layer (EF Core, repositories, external services)
- API layer (FastEndpoints, middleware, authentication)
- Complete CQRS implementation
- Sample entities and handlers
- appsettings.json configuration
- Docker support
- GitHub Actions CI/CD

##### 4. Generate Minimal API Structure

**Lightweight structure with:**
- Minimal API endpoints
- Program.cs with complete configuration
- DTOs and validation
- Dependency injection setup
- Swagger configuration

##### 5. Development Tools Configuration

**Directory.Build.props:**
```xml
<Project>
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
  </PropertyGroup>
</Project>
```

**.editorconfig**, **global.json**, **Dockerfile**, **docker-compose.yml**, **Makefile**, **.github/workflows/ci.yml**

### Skills (6 total)

#### 1. cqrs-patterns/SKILL.md

**Frontmatter:**
```yaml
---
name: cqrs-patterns
description: Master CQRS (Command Query Responsibility Segregation) with custom implementations, pipeline behaviors, and domain events. Use when implementing complex business logic, separating read/write models, or building maintainable command/query layers.
---
```

**Content Focus:**
- CQRS fundamentals (commands vs queries)
- Custom dispatcher implementation
- Handler interfaces and registration
- Pipeline behaviors (validation, logging, authorization, transaction)
- Domain events and event handlers
- Marker interfaces (ICommand, IQuery, ICommandHandler, IQueryHandler)
- Testing CQRS handlers
- Performance considerations
- MediatR integration patterns (optional)

**Progressive Disclosure:**
- **Core**: Basic command/query patterns
- **Intermediate**: Pipeline behaviors and validation
- **Advanced**: Event sourcing and projections
- **References**: Complete CQRS dispatcher implementation

#### 2. domain-driven-design/SKILL.md

**Frontmatter:**
```yaml
---
name: domain-driven-design
description: Apply Domain-Driven Design principles with aggregates, value objects, domain services, and ubiquitous language. Use when modeling complex business domains, designing bounded contexts, or implementing rich domain models.
---
```

**Content Focus:**
- Aggregate root design with invariant protection
- Value objects for domain concepts
- Domain services for cross-aggregate operations
- Repository pattern with specification
- Domain events for state changes
- Bounded context identification
- Anti-corruption layers
- Ubiquitous language
- Strategic vs tactical DDD
- Testing domain logic

#### 3. async-csharp-patterns/SKILL.md

**Frontmatter:**
```yaml
---
name: async-csharp-patterns
description: Master async/await patterns, Task and ValueTask, Channels, and IAsyncEnumerable for high-performance .NET applications. Use when building async APIs, concurrent systems, or I/O-bound applications requiring non-blocking operations.
---
```

**Content Focus:**
- Task vs ValueTask usage
- Async/await best practices
- ConfigureAwait(false) guidance
- Channels for producer-consumer patterns
- IAsyncEnumerable for streaming
- Parallel processing with Task.WhenAll
- AsyncLocal for ambient context
- Cancellation tokens
- Error handling in async code
- Common async pitfalls

#### 4. entity-framework-core-optimization/SKILL.md

**Frontmatter:**
```yaml
---
name: entity-framework-core-optimization
description: Optimize Entity Framework Core queries with AsNoTracking, compiled queries, split queries, and proper indexing strategies. Use when experiencing EF Core performance issues or building high-traffic data access layers.
---
```

**Content Focus:**
- Query optimization techniques
- AsNoTracking for read-only queries
- Compiled queries for repeated queries
- Split queries for collections
- Projection with Select()
- N+1 query prevention
- Index strategies
- Connection pooling
- Batch operations
- Query performance profiling

#### 5. dotnet-testing-strategies/SKILL.md

**Frontmatter:**
```yaml
---
name: dotnet-testing-strategies
description: Implement comprehensive testing with xUnit, Moq, FluentValidation, Bogus, and TestContainers for .NET applications. Use when setting up test infrastructure, writing unit/integration tests, or implementing TDD workflows.
---
```

**Content Focus:**
- xUnit test organization
- Moq for mocking dependencies
- FluentValidation for input validation
- Bogus for test data generation
- TestContainers for integration tests
- Arrange-Act-Assert pattern
- Theory and InlineData for parameterized tests
- Test fixtures and class fixtures
- Testing async code
- Coverage analysis

#### 6. clean-architecture-dotnet/SKILL.md

**Frontmatter:**
```yaml
---
name: clean-architecture-dotnet
description: Implement Clean Architecture in .NET with proper layer separation, dependency inversion, and domain-centric design. Use when architecting new .NET applications or refactoring to layered architecture.
---
```

**Content Focus:**
- Layer definitions (Domain, Application, Infrastructure, Presentation)
- Dependency flow (all dependencies point inward)
- Domain layer purity (framework-agnostic)
- Application layer use cases
- Infrastructure layer adapters
- Presentation layer (API, UI)
- Cross-cutting concerns
- Project structure and organization
- Testing strategies per layer
- Migration from monolithic architecture

---

## Plugin 2: dotnet-framework

### Plugin Metadata

```json
{
  "name": "dotnet-framework",
  "source": "./plugins/dotnet-framework",
  "description": "Legacy .NET Framework 4.8 development with ASP.NET MVC, Web Forms, Entity Framework 6, and enterprise patterns",
  "version": "1.2.2",
  "author": {
    "name": "Seth Hobson",
    "url": "https://github.com/wshobson"
  },
  "homepage": "https://github.com/wshobson/agents",
  "repository": "https://github.com/wshobson/agents",
  "license": "MIT",
  "keywords": [
    "dotnet-framework",
    "aspnet-mvc",
    "entity-framework-6",
    "legacy",
    "web-forms"
  ],
  "category": "languages",
  "strict": false
}
```

### Agents (3 total, all Sonnet model)

#### 1. dotnet-framework-pro.md

**Frontmatter:**
```yaml
---
name: dotnet-framework-pro
description: Expert .NET Framework 4.8 developer specializing in ASP.NET MVC 5, Entity Framework 6, and legacy enterprise systems. Maintains and modernizes traditional .NET applications with focus on stability and backwards compatibility. Use PROACTIVELY for working with .NET Framework 4.x codebases or legacy enterprise patterns.
model: sonnet
---
```

**Content Focus:**
- .NET Framework 4.8 features and limitations
- ASP.NET MVC 5 (controllers, views, areas, filters, routing)
- Entity Framework 6 (Code First, Database First, migrations)
- Traditional repository pattern and service layer
- Unity, Ninject, Autofac for dependency injection
- Windows Authentication and Forms Authentication
- OWIN/Katana middleware
- IIS configuration and deployment
- Azure App Services for .NET Framework
- Incremental modernization strategies
- Backwards compatibility patterns

**Behavioral Traits:**
- Maintains backwards compatibility
- Implements incremental improvements
- Tests thoroughly before changes
- Documents legacy business rules
- Uses async/await where beneficial
- Optimizes EF6 queries

#### 2. aspnet-mvc-pro.md

**Frontmatter:**
```yaml
---
name: aspnet-mvc-pro
description: Build and maintain ASP.NET MVC 5 applications with proper routing, controllers, views, and Razor syntax. Expert in traditional MVC patterns and Web API 2. Use PROACTIVELY for ASP.NET MVC 5 development or Web API 2 projects.
model: sonnet
---
```

**Content Focus:**
- ASP.NET MVC 5 architecture
- Controller design patterns
- Razor view engine and syntax
- Partial views and layouts
- Areas for organizing large applications
- Custom action filters
- Model binding and validation
- HTML helpers and tag helpers
- Bundling and minification
- Web API 2 for RESTful services
- OData integration
- Route attribute routing
- Dependency injection with DI containers

**Behavioral Traits:**
- Follows MVC separation of concerns
- Uses attribute routing for APIs
- Implements proper validation
- Optimizes view rendering
- Uses bundling for performance

#### 3. entity-framework-6-pro.md

**Frontmatter:**
```yaml
---
name: entity-framework-6-pro
description: Master Entity Framework 6 with Code First, Database First, migrations, and performance optimization. Expert in legacy data access patterns and SQL Server integration. Use PROACTIVELY for EF6 projects, database migrations, or performance tuning.
model: sonnet
---
```

**Content Focus:**
- Entity Framework 6 patterns
- Code First vs Database First
- Migrations and seeding
- Query optimization (Include, AsNoTracking)
- Complex queries with LINQ
- Stored procedure mapping
- Connection resiliency
- Lazy loading vs eager loading
- Repository and Unit of Work patterns
- Database-specific features (SQL Server)
- Performance profiling
- Compiled queries for EF6

**Behavioral Traits:**
- Optimizes queries to reduce database round trips
- Uses AsNoTracking for read-only scenarios
- Implements proper migration strategies
- Handles concurrency conflicts
- Tests data access with integration tests

### Commands (1 total)

#### dotnet-framework-scaffold.md

**Purpose:** Scaffold .NET Framework 4.8 projects with traditional patterns

**Content Structure:**

##### 1. Analyze Project Type
- **ASP.NET MVC 5 Application**: Full-stack MVC app
- **Web API 2 Project**: RESTful API service
- **Web Forms Application**: Legacy web forms
- **Class Library**: Reusable library for .NET Framework
- **Console Application**: CLI tools for .NET Framework
- **WCF Service**: SOAP-based service

##### 2. Initialize with Visual Studio Templates or CLI

```powershell
# Install templates if not available
# Using dotnet new for .NET Framework (limited support)

# Or use PowerShell/batch scripts to scaffold

# Create solution
md MyLegacyApp
cd MyLegacyApp
dotnet new sln -n MyLegacyApp

# Manual structure for MVC 5 (since templates are limited)
# Provide complete folder structure and file templates
```

##### 3. Generate ASP.NET MVC 5 Structure

**Complete structure with:**
- Controllers/HomeController.cs
- Models/ViewModels
- Views/Shared/_Layout.cshtml
- App_Start/RouteConfig.cs, BundleConfig.cs, FilterConfig.cs
- Web.config configuration
- Global.asax
- Repository and service layer
- EF6 DbContext setup
- Unity DI configuration

##### 4. Generate Web API 2 Structure

**API structure with:**
- Controllers/ApiControllers
- Models/DTOs
- Repository pattern
- WebApiConfig.cs
- Dependency injection setup
- Swagger integration
- CORS configuration

##### 5. Development Tools Configuration

**Web.config**, **packages.config**, **nuget.config**, **.gitignore**, **README.md**, **AppSettings transformations**

### Skills (4 total)

#### 1. aspnet-mvc-5-patterns/SKILL.md

**Frontmatter:**
```yaml
---
name: aspnet-mvc-5-patterns
description: Master ASP.NET MVC 5 patterns with controllers, views, routing, filters, and model binding. Use when building or maintaining traditional MVC applications or migrating to ASP.NET Core.
---
```

**Content Focus:**
- MVC request pipeline
- Controller design patterns
- Action results (ViewResult, JsonResult, etc.)
- Custom action filters
- Model binding and validation
- Razor syntax and helpers
- Partial views and layouts
- Areas for modular design
- Routing conventions vs attribute routing
- Dependency injection patterns
- Testing MVC controllers

#### 2. entity-framework-6-optimization/SKILL.md

**Frontmatter:**
```yaml
---
name: entity-framework-6-optimization
description: Optimize Entity Framework 6 queries with Include, AsNoTracking, compiled queries, and proper indexing. Use when experiencing EF6 performance issues or working with legacy data access layers.
---
```

**Content Focus:**
- EF6 query optimization
- Include() for eager loading
- AsNoTracking() for read-only
- Compiled queries
- Raw SQL execution
- N+1 query prevention
- Lazy loading pitfalls
- Connection pooling
- Query performance profiling
- Index strategies

#### 3. legacy-dotnet-modernization/SKILL.md

**Frontmatter:**
```yaml
---
name: legacy-dotnet-modernization
description: Strategies for modernizing .NET Framework applications with Strangler Fig pattern, incremental refactoring, and migration to .NET 8+. Use when planning migration from .NET Framework to modern .NET or refactoring legacy codebases.
---
```

**Content Focus:**
- Strangler Fig pattern
- Branch by abstraction
- Incremental database migrations
- API versioning during transition
- Shared contracts for cross-framework compatibility
- Adapter pattern for legacy integration
- Testing strategies during migration
- Risk mitigation
- Migration tools and utilities
- Deployment strategies

#### 4. windows-authentication-patterns/SKILL.md

**Frontmatter:**
```yaml
---
name: windows-authentication-patterns
description: Implement Windows Authentication, Active Directory integration, and enterprise authentication patterns in .NET Framework applications. Use when building intranet applications or integrating with corporate authentication systems.
---
```

**Content Focus:**
- Windows Authentication configuration
- Active Directory integration
- Claims-based authentication
- Role-based authorization
- Impersonation patterns
- Kerberos authentication
- IIS authentication modes
- OWIN authentication middleware
- Hybrid authentication (Windows + Forms)
- Testing authentication

---

## Implementation Timeline

### Phase 1: Foundation (Week 1)
- [ ] Create plugin directory structures
- [ ] Set up marketplace.json entries
- [ ] Create base README.md files for each plugin

### Phase 2: dotnet-development Plugin (Weeks 2-3)
- [ ] Write dotnet-pro agent (comprehensive .NET 8+ expert)
- [ ] Write aspnet-core-pro agent (API development expert)
- [ ] Write ef-core-pro agent (database expert)
- [ ] Create dotnet-scaffold command (complete scaffolding)
- [ ] Develop all 6 skills with progressive disclosure

### Phase 3: dotnet-framework Plugin (Weeks 4-5)
- [ ] Write dotnet-framework-pro agent (legacy .NET expert)
- [ ] Write aspnet-mvc-pro agent (MVC 5 expert)
- [ ] Write entity-framework-6-pro agent (EF6 expert)
- [ ] Create dotnet-framework-scaffold command
- [ ] Develop all 4 skills with progressive disclosure

### Phase 4: Testing & Refinement (Week 6)
- [ ] Test all agents with sample prompts
- [ ] Verify skill activation criteria
- [ ] Test scaffold commands with actual project creation
- [ ] Review consistency with marketplace patterns
- [ ] Update CLAUDE.md with .NET plugin information

### Phase 5: Documentation & Release (Week 7)
- [ ] Create comprehensive plugin documentation
- [ ] Update marketplace catalog
- [ ] Write usage examples
- [ ] Create migration guide from payk12 agents
- [ ] Publish plugins

---

## File Structure

```
plugins/
├── dotnet-development/
│   ├── agents/
│   │   ├── dotnet-pro.md
│   │   ├── aspnet-core-pro.md
│   │   └── ef-core-pro.md
│   ├── commands/
│   │   └── dotnet-scaffold.md
│   └── skills/
│       ├── cqrs-patterns/
│       │   ├── SKILL.md
│       │   ├── assets/
│       │   │   └── cqrs-workflow-diagram.md
│       │   └── references/
│       │       ├── custom-dispatcher-implementation.md
│       │       └── pipeline-behaviors.md
│       ├── domain-driven-design/
│       │   ├── SKILL.md
│       │   └── references/
│       │       ├── aggregate-patterns.md
│       │       └── value-objects.md
│       ├── async-csharp-patterns/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── async-best-practices.md
│       ├── entity-framework-core-optimization/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── query-optimization.md
│       ├── dotnet-testing-strategies/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── test-patterns.md
│       └── clean-architecture-dotnet/
│           ├── SKILL.md
│           └── references/
│               └── layer-structure.md
└── dotnet-framework/
    ├── agents/
    │   ├── dotnet-framework-pro.md
    │   ├── aspnet-mvc-pro.md
    │   └── entity-framework-6-pro.md
    ├── commands/
    │   └── dotnet-framework-scaffold.md
    └── skills/
        ├── aspnet-mvc-5-patterns/
        │   ├── SKILL.md
        │   └── references/
        │       └── mvc-patterns.md
        ├── entity-framework-6-optimization/
        │   ├── SKILL.md
        │   └── references/
        │       └── ef6-performance.md
        ├── legacy-dotnet-modernization/
        │   ├── SKILL.md
        │   └── references/
        │       ├── strangler-fig.md
        │       └── migration-strategies.md
        └── windows-authentication-patterns/
            ├── SKILL.md
            └── references/
                └── ad-integration.md
```

---

## Key Design Decisions

### 1. Separation of Modern vs Legacy

**Rationale**: Maintaining two separate plugins rather than one combined plugin allows:
- Focused, minimal token usage (users install only what they need)
- Clear distinction between modern and legacy patterns
- Easier maintenance and updates
- Better discoverability

### 2. Model Selection (All Sonnet)

**Rationale**: Following the python-development pattern, all agents use Sonnet because:
- Complex reasoning required for architecture decisions
- CQRS and DDD patterns require deep understanding
- Code generation needs contextual awareness
- Migration strategies need architectural thinking

### 3. Skill Progressive Disclosure

**Rationale**: Skills use progressive disclosure to:
- Minimize token usage (core concepts always loaded, details on demand)
- Follow Anthropic's Agent Skills Specification
- Provide references/assets for deep-dive examples
- Enable activation based on clear "Use when" criteria

### 4. Comprehensive Scaffolding Commands

**Rationale**: Following python-scaffold pattern:
- Provide complete project structure generation
- Include all necessary configuration files
- Set up modern tooling (Docker, CI/CD, testing)
- Support multiple project types from single command

### 5. Alignment with payk12 Architecture

**Rationale**: Incorporate proven patterns:
- CQRS implementation matches payk12's custom dispatcher approach
- Domain events with outbox pattern
- Specification pattern for reusable queries
- Clean architecture layer separation
- Testing strategies with Moq, FluentValidation, Bogus

---

## Success Criteria

### Plugin Quality
- [ ] All agents have comprehensive frontmatter and content
- [ ] Commands provide working, tested scaffolding
- [ ] Skills follow progressive disclosure architecture
- [ ] All files use proper naming conventions (hyphen-case)
- [ ] Consistent voice and style across all content

### Technical Accuracy
- [ ] Code examples compile and run
- [ ] Architecture patterns match industry best practices
- [ ] Security considerations documented
- [ ] Performance optimization guidance included
- [ ] Testing strategies comprehensive

### Marketplace Integration
- [ ] Proper marketplace.json entries
- [ ] Version numbers consistent
- [ ] Keywords optimized for discovery
- [ ] Category placement appropriate
- [ ] License and attribution correct

### User Experience
- [ ] Clear "Use when" activation criteria
- [ ] Agents trigger proactively when appropriate
- [ ] Skills load only when needed
- [ ] Scaffolding generates production-ready code
- [ ] Documentation comprehensive

---

## Migration Notes

### From payk12 Agents

The payk12 project currently has `dotnet-pro` and `dotnet-legacy-pro` agents in `.claude/agents/development/`. These will be adapted for the marketplace plugins:

**Changes:**
- Simplify MCP integration references (context7, sequential-thinking) - marketplace agents don't specify tools
- Enhance content with more code examples and patterns
- Add progressive disclosure structure to knowledge areas
- Create complementary skills for specialized knowledge
- Add scaffolding commands not present in original agents

**Enhancements:**
- Add aspnet-core-pro agent (not in payk12, focused on API development)
- Add ef-core-pro agent (extracted from dotnet-pro, focused on EF Core)
- Add aspnet-mvc-pro agent (extracted from dotnet-legacy-pro, focused on MVC)
- Add entity-framework-6-pro agent (focused on EF6)
- Create comprehensive skill library (10 total skills across both plugins)

---

## Next Steps

1. **Review and Approve Plan**: Stakeholder review of this implementation plan
2. **Begin Phase 1**: Create directory structures and base files
3. **Iterative Development**: Build agents, commands, and skills incrementally
4. **Testing**: Validate with real-world scenarios throughout development
5. **Documentation**: Keep CLAUDE.md and other docs updated
6. **Release**: Publish to marketplace with comprehensive usage guide

---

## Appendix: Example Code Snippets

### CQRS Custom Dispatcher (from dotnet-pro)

```csharp
public interface IDispatcher
{
    Task<TResult> SendAsync<TResult>(ICommand<TResult> command, CancellationToken cancellationToken = default);
    Task<TResult> QueryAsync<TResult>(IQuery<TResult> query, CancellationToken cancellationToken = default);
}

public class Dispatcher : IDispatcher
{
    private readonly IServiceProvider _serviceProvider;

    public Dispatcher(IServiceProvider serviceProvider)
    {
        _serviceProvider = serviceProvider;
    }

    public async Task<TResult> SendAsync<TResult>(ICommand<TResult> command, CancellationToken cancellationToken = default)
    {
        var handlerType = typeof(ICommandHandler<,>).MakeGenericType(command.GetType(), typeof(TResult));
        dynamic handler = _serviceProvider.GetRequiredService(handlerType);
        return await handler.HandleAsync((dynamic)command, cancellationToken);
    }

    public async Task<TResult> QueryAsync<TResult>(IQuery<TResult> query, CancellationToken cancellationToken = default)
    {
        var handlerType = typeof(IQueryHandler<,>).MakeGenericType(query.GetType(), typeof(TResult));
        dynamic handler = _serviceProvider.GetRequiredService(handlerType);
        return await handler.HandleAsync((dynamic)query, cancellationToken);
    }
}
```

### Clean Architecture Project Structure (for scaffold command)

```
Solution/
├── src/
│   ├── ProjectName.Domain/           # Pure domain logic
│   │   ├── Entities/
│   │   ├── ValueObjects/
│   │   ├── DomainEvents/
│   │   └── Interfaces/
│   ├── ProjectName.Application/       # Use cases/CQRS handlers
│   │   ├── Commands/
│   │   ├── Queries/
│   │   ├── DTOs/
│   │   ├── Interfaces/
│   │   └── Behaviors/
│   ├── ProjectName.Infrastructure/    # External concerns
│   │   ├── Persistence/
│   │   ├── Services/
│   │   └── Messaging/
│   └── ProjectName.Api/               # API endpoints
│       ├── Endpoints/
│       ├── Middleware/
│       └── Configuration/
└── tests/
    ├── ProjectName.Domain.Tests/
    ├── ProjectName.Application.Tests/
    └── ProjectName.Api.IntegrationTests/
```

---

**Document Version**: 1.0
**Last Updated**: 2025-01-18
**Author**: AI Implementation Planning
**Status**: Ready for Review
