# backend-development

> Backend API design, GraphQL architecture, Firebase backend integration, and test-driven backend development

**Version:** 1.2.3
**Category:** development
**Author:** Seth Hobson

## Overview

### What This Plugin Does

The backend-development plugin provides comprehensive backend architecture capabilities including RESTful and GraphQL API design, microservices patterns, Firebase integration, event-driven architectures, and modern backend frameworks. It orchestrates scalable backend systems with built-in resilience, security, and observability patterns.

### Primary Use Cases

- **Scalable API Design**: REST, GraphQL, gRPC APIs with proper versioning and documentation
- **Microservices Architecture**: Service decomposition, inter-service communication, service mesh
- **Firebase Backend Integration**: Cloud Functions, Firestore, Realtime Database, Firebase Storage/CDN
- **Event-Driven Systems**: Message queues, event streaming, event sourcing patterns
- **TDD Backend Development**: Test-driven backend services with comprehensive test coverage

### Who Should Use This

- Backend engineers building scalable APIs and microservices
- Architects designing distributed backend systems
- Teams adopting Firebase for serverless backend infrastructure
- Developers implementing event-driven architectures
- Projects requiring test-driven backend development workflows

## Quick Start

### Installation

1. Install the plugin in Claude Code (already included in marketplace)
2. Verify agents are available:
```bash
# List backend agents
claude agents list | grep backend
```

### Basic Usage

**Design a REST API:**
```bash
@backend-architect design a RESTful API for order management with CRUD operations, pagination, filtering, and proper error handling
```

**Build a GraphQL API:**
```bash
@graphql-architect create a GraphQL schema for an e-commerce platform with products, orders, users, and subscriptions for real-time updates
```

**Firebase Backend Integration:**
```bash
@backend-architect implement Firebase backend with Cloud Functions for API, Firestore for data, and Storage CDN for media assets
```

**Test-Driven Development:**
```bash
@tdd-orchestrator build a user authentication service using TDD with unit tests, integration tests, and E2E tests
```

See [Complete Workflow Examples](#complete-workflow-examples) for end-to-end scenarios.

## Agents Reference

This plugin provides **3 specialized Sonnet agents** for complex backend architecture and design:

### backend-architect

**Model:** Sonnet (complex reasoning for architecture decisions)

**Purpose:** Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC APIs, event-driven architectures, service mesh patterns, and modern backend frameworks.

**When to Use Proactively:**
- Creating new backend services or APIs
- Designing microservices architecture with proper service boundaries
- Implementing inter-service communication patterns (sync/async)
- Building resilience into backend systems (circuit breakers, retries, timeouts)
- Planning event-driven architectures with message queues or streams

**Example Invocations:**
```bash
# REST API design
@backend-architect design a RESTful API for inventory management with real-time stock updates, batch operations, and webhook notifications

# Microservices
@backend-architect create microservices architecture for multi-tenant SaaS platform with user management, billing, and analytics services

# Event-driven
@backend-architect design event-driven order processing system using Kafka with order placement, payment, and fulfillment services
```

**Key Capabilities:**
- REST/GraphQL/gRPC API design with versioning
- Microservices patterns and service boundaries
- Event-driven architectures (Kafka, RabbitMQ, SQS)
- Authentication/authorization (OAuth, JWT, RBAC)
- Resilience patterns (circuit breakers, retries, timeouts)
- Observability (tracing, logging, metrics)
- Caching strategies and performance optimization

### graphql-architect

**Model:** Sonnet (complex schema design and optimization)

**Purpose:** GraphQL API specialist focusing on schema design, resolvers, subscriptions, federation, and performance optimization with DataLoader patterns.

**When to Use Proactively:**
- Designing GraphQL schemas with proper type systems
- Building GraphQL APIs with queries, mutations, and subscriptions
- Implementing DataLoader patterns to prevent N+1 queries
- Creating federated GraphQL architectures
- Optimizing GraphQL performance and complexity

**Example Invocations:**
```bash
# Schema design
@graphql-architect design GraphQL schema for social media platform with users, posts, comments, likes, and real-time notifications

# Federation
@graphql-architect create federated GraphQL gateway combining user service, product service, and order service

# Performance
@graphql-architect optimize GraphQL API with DataLoaders, query complexity analysis, and response caching
```

### tdd-orchestrator

**Model:** Sonnet (orchestrates test-driven development workflows)

**Purpose:** TDD expert guiding red-green-refactor cycles for backend services with comprehensive unit, integration, and E2E test coverage.

**When to Use Proactively:**
- Building backend services using TDD methodology
- Writing tests before implementation
- Creating comprehensive test suites for APIs
- Implementing integration tests for databases
- Setting up E2E testing for workflows

**Example Invocations:**
```bash
# TDD workflow
@tdd-orchestrator build authentication service using TDD with JWT tokens, refresh tokens, and password reset

# Test suite
@tdd-orchestrator create comprehensive test suite for payment API with unit, integration, and E2E tests
```

## Skills Reference

This plugin includes **5 progressive disclosure skills**:

### api-design-principles

**Description:** Master REST and GraphQL API design principles. Use when designing new APIs, reviewing specifications, or establishing API standards.

**Activation Triggers:**
- Designing new REST or GraphQL APIs
- Refactoring existing APIs
- Establishing API design standards
- Reviewing API specifications before implementation

**Key Techniques:**
- RESTful design: Resource-oriented architecture, HTTP methods, URL patterns
- GraphQL schema design: Types, queries, mutations, subscriptions
- API versioning strategies: URL, header, query parameter
- Pagination: Cursor-based, offset-based, keyset pagination
- Error handling: Consistent formats, status codes
- HATEOAS: Hypermedia controls, discoverable APIs
- DataLoader: N+1 query prevention, batch loading

See `/plugins/backend-development/skills/api-design-principles/SKILL.md` for complete examples.

### architecture-patterns

**Description:** Modern backend architecture patterns including Clean Architecture, DDD, CQRS, Event Sourcing, and Hexagonal Architecture.

**Key Patterns:**
- Clean Architecture with dependency inversion
- Domain-Driven Design: Aggregates, entities, value objects
- CQRS: Command-query separation
- Event Sourcing: Event store, projections
- Hexagonal Architecture: Ports and adapters

### firebase-backend-integration

**Description:** Comprehensive Firebase backend integration with Cloud Functions, Firestore, Realtime Database, and Cloud Storage.

**Key Features:**
- Cloud Functions: HTTP triggers, Firestore triggers, scheduled functions
- Firestore: Collections, documents, queries, transactions, security rules
- Firebase Authentication: Email/password, social providers
- Cloud Storage: File uploads, signed URLs, CDN integration

### firebase-storage-cdn

**Description:** Firebase Cloud Storage integration with CDN delivery, signed URLs, and media optimization.

### microservices-patterns

**Description:** Microservices architecture patterns including service decomposition, inter-service communication, and distributed transactions.

**Key Patterns:**
- Service decomposition with DDD
- Communication: Sync (REST, gRPC), async (events, messages)
- Service discovery: Consul, etcd, Kubernetes
- Resilience: Circuit breakers, retries, bulkheads
- Saga pattern for distributed transactions
- Service mesh: Istio, Linkerd

## Commands Reference

### /backend-development:feature-development

**Description:** Orchestrate end-to-end feature development from requirements to production deployment.

**Usage:**
```bash
/backend-development:feature-development \
  --feature <description> \
  --methodology <traditional|tdd|bdd|ddd> \
  --complexity <simple|medium|complex|epic> \
  [--deployment-strategy <direct|canary|feature-flag|blue-green>]
```

**12-Phase Workflow:**
1. Business analysis & requirements
2. Technical architecture design
3. Security assessment
4. Backend implementation
5. Frontend implementation
6. Data pipeline integration
7. Automated testing
8. Security validation
9. Performance optimization
10. Deployment pipeline
11. Observability setup
12. Documentation

**Example:**
```bash
/backend-development:feature-development \
  --feature "User authentication with OAuth 2.0" \
  --methodology tdd \
  --complexity medium \
  --deployment-strategy feature-flag
```

## Complete Workflow Examples

### Workflow 1: REST API for E-Commerce

Build a complete RESTful API for an e-commerce platform with proper architecture, testing, and deployment.

**Steps:**

1. **Design API Architecture**
```bash
@backend-architect design RESTful API for e-commerce with:
- Product catalog with search and filtering
- Shopping cart with session management
- Order processing with payment integration
- User management with OAuth 2.0
- Admin panel for inventory management
```

Agent provides:
- OpenAPI/Swagger specification
- Service architecture diagram
- Database schema recommendations
- Authentication strategy
- Caching architecture

2. **Implement with TDD**
```bash
@tdd-orchestrator implement the product catalog API using TDD:
- Write tests for product CRUD operations
- Implement search with Elasticsearch
- Add pagination and filtering
- Include caching with Redis
```

3. **Add GraphQL for Mobile**
```bash
@graphql-architect add GraphQL API for mobile app:
- Unified schema for products, cart, orders
- Real-time subscriptions for order status
- DataLoader for optimized queries
```

4. **Deploy with Observability**
```bash
@backend-architect add observability:
- Distributed tracing with Jaeger
- Metrics with Prometheus
- Centralized logging with ELK
- Alerts for SLO violations
```

**Expected Output:**
- REST API with full CRUD
- GraphQL API for mobile
- 90%+ test coverage
- Production monitoring

### Workflow 2: Firebase Serverless Backend

Build serverless backend with Firebase for a mobile application.

**Steps:**

1. **Design Firebase Architecture**
```bash
@backend-architect design Firebase backend for mobile app:
- Cloud Functions for REST API endpoints
- Firestore for user data and content
- Realtime Database for chat messaging
- Firebase Storage for user-uploaded media
- Firebase Authentication with social providers
```

2. **Implement Cloud Functions**
```bash
@backend-architect implement Cloud Functions:
- HTTP triggers for REST API
- Firestore triggers for data validation
- Scheduled functions for cleanup tasks
- Pub/Sub triggers for async processing
```

3. **Set Up Security Rules**
```bash
@backend-architect create Firestore security rules:
- Role-based access control
- Field-level validation
- Rate limiting for writes
- Data privacy compliance
```

4. **Optimize for Scale**
```bash
@backend-architect optimize Firebase backend:
- Firestore query indexing
- Cloud Storage CDN configuration
- Cloud Function cold start optimization
- Cost monitoring and budgets
```

### Workflow 3: Event-Driven Microservices

Build event-driven order processing system with Kafka.

**Steps:**

1. **Design Event Architecture**
```bash
@backend-architect design event-driven order processing:
- Kafka for event streaming
- Event types: OrderPlaced, PaymentProcessed, OrderShipped
- Event sourcing for order state
- CQRS for read/write separation
```

2. **Implement Event Producers**
```bash
@backend-architect implement order service:
- Publish OrderPlaced events
- Handle PaymentProcessed events
- Implement saga pattern for distributed transactions
```

3. **Build Event Consumers**
```bash
@backend-architect create consumer services:
- Payment service listens to OrderPlaced
- Fulfillment service listens to PaymentProcessed
- Notification service listens to all order events
```

4. **Add Monitoring**
```bash
@backend-architect setup event monitoring:
- Kafka lag monitoring
- Event processing metrics
- Dead letter queue for failed events
- Event replay capabilities
```

## Plugin Relationships

### Similar Plugins

- **full-stack-orchestration**: Coordinates backend + frontend + testing + security + deployment
- **api-scaffolding**: Provides REST/GraphQL/Firebase templates and quick-start scaffolding
- **database-design**: Specializes in database schema design and query optimization

### Differences

**backend-development vs full-stack-orchestration:**
- backend-development: Pure backend architecture, APIs, microservices
- full-stack-orchestration: End-to-end feature delivery across all layers
- **Use case:** backend-development for backend-only work, full-stack for complete features

**backend-development vs api-scaffolding:**
- backend-development: Custom architecture and complex patterns
- api-scaffolding: Templates and rapid prototyping
- **Use case:** backend-development for design, api-scaffolding for quick starts

**backend-development vs database-design:**
- backend-development: Defers database schema to database-architect
- database-design: Specializes in schema, queries, optimization
- **Workflow:** database-design → backend-development (data layer first)

### Works Well With

- **database-design**: Design data layer before backend (sequential)
- **security-scanning**: Security validation for backend services
- **observability-monitoring**: Monitoring and alerting infrastructure
- **cicd-automation**: CI/CD pipelines for backend deployment
- **unit-testing**: Comprehensive test suites
- **api-testing-observability**: API testing and OpenAPI docs

### Integration Patterns

**Sequential Workflow:**
```bash
@database-architect design schema
@backend-architect design services
@security-auditor review architecture
@test-automator create test suite
```

**Parallel Workflow:**
```bash
# Run simultaneously:
# - Backend API development
# - Frontend development (with mock APIs)
# - Database schema creation
# - CI/CD pipeline setup
```

## Best Practices

### Do's

✅ Design APIs contract-first before implementation
✅ Use proper HTTP methods and status codes for REST
✅ Implement DataLoader patterns for GraphQL N+1 prevention
✅ Build resilience patterns from the start
✅ Add comprehensive observability
✅ Write tests first in TDD workflow
✅ Version APIs for backward compatibility
✅ Document APIs with OpenAPI/GraphQL schema

### Don'ts

❌ Don't design database schemas (use database-architect)
❌ Don't skip API documentation
❌ Don't ignore resilience patterns
❌ Don't implement without tests in TDD
❌ Don't expose internal implementation details
❌ Don't skip pagination for large collections
❌ Don't forget rate limiting and authentication

### Common Pitfalls

**1. N+1 Query Problem**
- **Issue:** Each item triggers a database query
- **Solution:** Use DataLoader for GraphQL batch loading
- **Solution:** Use eager loading in REST

**2. Breaking API Changes**
- **Issue:** Changes break existing clients
- **Solution:** Version APIs properly (URL or header versioning)
- **Solution:** Use deprecation warnings

**3. Missing Resilience Patterns**
- **Issue:** Service failures cascade
- **Solution:** Implement circuit breakers, retries, timeouts

**4. Poor Error Handling**
- **Issue:** Inconsistent error responses
- **Solution:** Standardize error formats, use proper status codes

**5. Lack of Observability**
- **Issue:** Unable to debug production
- **Solution:** Add tracing, structured logging, metrics from day one

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Agent suggests database design | Backend-architect defers to database-architect | Use @database-architect first |
| N+1 queries in GraphQL | Missing DataLoader | Implement DataLoader pattern from skill |
| Circuit breaker open | Too many failures | Check service health, implement fallback |
| Rate limit exceeded | Too many requests | Add rate limiting, implement caching |
| Firebase quota exceeded | High usage | Monitor usage, optimize queries, upgrade |

### Debugging Techniques

**Distributed Tracing:**
```bash
@backend-architect implement OpenTelemetry tracing with Jaeger
```

**Performance Profiling:**
- Profile slow endpoints with APM tools
- Identify N+1 queries
- Analyze database execution plans

## Advanced Topics

### Power User Features

- **api-design-principles**: REST/GraphQL patterns with code examples
- **architecture-patterns**: Clean Architecture, DDD, CQRS, Event Sourcing
- **firebase-backend-integration**: Cloud Functions, Firestore, security rules
- **microservices-patterns**: Service decomposition, communication, resilience

### Performance Tuning

**Response Time:**
- Profile with APM tools
- Implement query-level caching
- Use CDN for static assets
- Optimize queries (with database-architect)

**Throughput:**
- Horizontal scaling with load balancers
- Async processing for long tasks
- Connection pooling
- Request batching

**Cost (Firebase):**
- Monitor Firestore operations
- Use Cloud Functions minimum instances wisely
- Implement caching to reduce reads
- Optimize Storage bandwidth

## Contributing

Contributions welcome! See [main repository](https://github.com/wshobson/agents) for guidelines.

## License

MIT

## Support

- **Issues:** [GitHub Issues](https://github.com/wshobson/agents/issues)
- **Discussions:** [GitHub Discussions](https://github.com/wshobson/agents/discussions)

---

**Plugin:** backend-development v1.2.3  
**Agents:** 3 (backend-architect, graphql-architect, tdd-orchestrator)  
**Skills:** 5 (api-design-principles, architecture-patterns, firebase-backend-integration, firebase-storage-cdn, microservices-patterns)  
**Commands:** 1 (feature-development)
