---
name: dotnet-testing-patterns
description: Master .NET testing with xUnit, NUnit, MSTest, Moq, FluentAssertions, integration testing with WebApplicationFactory, CQRS testing patterns, and code coverage tools. Use when implementing unit tests, integration tests, or test-driven development in .NET applications.
---

# .NET Testing Patterns

Master comprehensive testing strategies for .NET 8+ applications including unit testing with xUnit/NUnit/MSTest, mocking with Moq/NSubstitute, assertions with FluentAssertions, integration testing with WebApplicationFactory, and advanced patterns for CQRS/DDD architectures.

## When to Use This Skill

- Writing unit tests for .NET applications
- Implementing test-driven development (TDD)
- Testing ASP.NET Core APIs and web applications
- Testing CQRS command and query handlers
- Integration testing with real dependencies
- Mocking dependencies and external services
- Testing Entity Framework Core repositories
- Implementing test fixtures and data builders
- Measuring and improving code coverage
- Testing domain-driven design (DDD) patterns

## Core Testing Frameworks

### xUnit.net (Most Popular for Modern .NET)

**Pros:**
- Modern, clean API
- Parallel test execution by default
- No test setup/teardown attributes (uses constructor/IDisposable)
- Widely adopted in .NET Core ecosystem
- Excellent integration with .NET CLI and Visual Studio

**Use when:**
- Starting new .NET projects
- Want parallel execution
- Prefer constructor injection for setup

### NUnit (Mature, Feature-Rich)

**Pros:**
- Rich assertion library
- Parameterized tests with TestCase
- SetUp/TearDown attributes
- Long history and large community

**Use when:**
- Migrating from older .NET Framework projects
- Need extensive parameterization features
- Team familiar with NUnit

### MSTest (Microsoft's Framework)

**Pros:**
- Built-in Visual Studio integration
- Good for enterprise .NET projects
- DataRow for parameterized tests

**Use when:**
- Deep Visual Studio integration required
- Enterprise constraints favor Microsoft-only tools

## Installation

```bash
# xUnit
dotnet add package xUnit
dotnet add package xUnit.runner.visualstudio
dotnet add package Microsoft.NET.Test.Sdk

# NUnit
dotnet add package NUnit
dotnet add package NUnit3TestAdapter
dotnet add package Microsoft.NET.Test.Sdk

# Mocking
dotnet add package Moq
dotnet add package NSubstitute

# Assertions
dotnet add package FluentAssertions

# Integration Testing
dotnet add package Microsoft.AspNetCore.Mvc.Testing

# Test Containers (for integration tests)
dotnet add package Testcontainers
dotnet add package Testcontainers.PostgreSql
dotnet add package Testcontainers.MsSql

# Code Coverage
dotnet add package coverlet.collector
```

## Project Structure

```
YourApp.sln
├── src/
│   ├── YourApp.Domain/
│   ├── YourApp.Application/
│   ├── YourApp.Infrastructure/
│   └── YourApp.Api/
└── tests/
    ├── YourApp.UnitTests/
    │   ├── Domain/
    │   ├── Application/
    │   │   ├── Commands/
    │   │   └── Queries/
    │   └── Infrastructure/
    ├── YourApp.IntegrationTests/
    │   ├── Api/
    │   ├── Fixtures/
    │   └── WebApplicationFactory/
    └── YourApp.ArchitectureTests/
```

## xUnit Testing Patterns

### Basic Unit Test

```csharp
// YourApp.UnitTests/Domain/Entities/OrderTests.cs
using FluentAssertions;
using Xunit;
using YourApp.Domain.Entities;

namespace YourApp.UnitTests.Domain.Entities;

public class OrderTests
{
    [Fact]
    public void Create_WithValidData_ShouldCreateOrder()
    {
        // Arrange
        var customerId = Guid.NewGuid();
        var orderDate = DateTime.UtcNow;

        // Act
        var order = Order.Create(customerId, orderDate);

        // Assert
        order.Should().NotBeNull();
        order.CustomerId.Should().Be(customerId);
        order.OrderDate.Should().Be(orderDate);
        order.Status.Should().Be(OrderStatus.Pending);
    }

    [Fact]
    public void AddItem_WithValidProduct_ShouldAddItemToOrder()
    {
        // Arrange
        var order = Order.Create(Guid.NewGuid(), DateTime.UtcNow);
        var productId = Guid.NewGuid();
        var quantity = 2;
        var price = 10.99m;

        // Act
        order.AddItem(productId, quantity, price);

        // Assert
        order.Items.Should().HaveCount(1);
        order.Items.First().ProductId.Should().Be(productId);
        order.Items.First().Quantity.Should().Be(quantity);
        order.TotalAmount.Should().Be(quantity * price);
    }

    [Theory]
    [InlineData(0)]
    [InlineData(-1)]
    public void AddItem_WithInvalidQuantity_ShouldThrowException(int quantity)
    {
        // Arrange
        var order = Order.Create(Guid.NewGuid(), DateTime.UtcNow);

        // Act
        Action act = () => order.AddItem(Guid.NewGuid(), quantity, 10.99m);

        // Assert
        act.Should().Throw<ArgumentException>()
           .WithMessage("*quantity*");
    }
}
```

### Test Fixtures and Class Fixtures

```csharp
// Shared test data across tests in a class
public class OrderTestFixture : IDisposable
{
    public Guid TestCustomerId { get; }
    public List<Product> TestProducts { get; }

    public OrderTestFixture()
    {
        TestCustomerId = Guid.NewGuid();
        TestProducts = new List<Product>
        {
            Product.Create("Product 1", 10.99m),
            Product.Create("Product 2", 20.99m),
        };
    }

    public void Dispose()
    {
        // Cleanup if needed
    }
}

public class OrderTests : IClassFixture<OrderTestFixture>
{
    private readonly OrderTestFixture _fixture;

    public OrderTests(OrderTestFixture fixture)
    {
        _fixture = fixture;
    }

    [Fact]
    public void Test_UsesFixtureData()
    {
        var order = Order.Create(_fixture.TestCustomerId, DateTime.UtcNow);
        order.CustomerId.Should().Be(_fixture.TestCustomerId);
    }
}
```

### Collection Fixtures (Shared Across Multiple Test Classes)

```csharp
// Define collection
[CollectionDefinition("Database collection")]
public class DatabaseCollection : ICollectionFixture<DatabaseFixture>
{
}

// Use in test classes
[Collection("Database collection")]
public class OrderRepositoryTests
{
    private readonly DatabaseFixture _fixture;

    public OrderRepositoryTests(DatabaseFixture fixture)
    {
        _fixture = fixture;
    }
}

[Collection("Database collection")]
public class CustomerRepositoryTests
{
    private readonly DatabaseFixture _fixture;

    public CustomerRepositoryTests(DatabaseFixture fixture)
    {
        _fixture = fixture;
    }
}
```

## Mocking with Moq

### Basic Mocking

```csharp
using Moq;
using YourApp.Application.Interfaces;
using YourApp.Application.Commands;

public class CreateOrderHandlerTests
{
    private readonly Mock<IOrderRepository> _orderRepositoryMock;
    private readonly Mock<IProductRepository> _productRepositoryMock;
    private readonly Mock<IUnitOfWork> _unitOfWorkMock;
    private readonly CreateOrderHandler _handler;

    public CreateOrderHandlerTests()
    {
        _orderRepositoryMock = new Mock<IOrderRepository>();
        _productRepositoryMock = new Mock<IProductRepository>();
        _unitOfWorkMock = new Mock<IUnitOfWork>();

        _handler = new CreateOrderHandler(
            _orderRepositoryMock.Object,
            _productRepositoryMock.Object,
            _unitOfWorkMock.Object
        );
    }

    [Fact]
    public async Task Handle_ValidCommand_ShouldCreateOrder()
    {
        // Arrange
        var command = new CreateOrderCommand
        {
            CustomerId = Guid.NewGuid(),
            Items = new List<OrderItemDto>
            {
                new() { ProductId = Guid.NewGuid(), Quantity = 2 }
            }
        };

        var product = Product.Create("Test Product", 10.99m);
        product.Id = command.Items.First().ProductId;

        _productRepositoryMock
            .Setup(x => x.GetByIdAsync(command.Items.First().ProductId, It.IsAny<CancellationToken>()))
            .ReturnsAsync(product);

        _unitOfWorkMock
            .Setup(x => x.SaveChangesAsync(It.IsAny<CancellationToken>()))
            .ReturnsAsync(1);

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        result.IsSuccess.Should().BeTrue();
        _orderRepositoryMock.Verify(x => x.AddAsync(
            It.Is<Order>(o => o.CustomerId == command.CustomerId),
            It.IsAny<CancellationToken>()
        ), Times.Once);
        _unitOfWorkMock.Verify(x => x.SaveChangesAsync(It.IsAny<CancellationToken>()), Times.Once);
    }
}
```

### Advanced Moq Patterns

```csharp
public class AdvancedMockingExamples
{
    [Fact]
    public void MockingWithCallbacks()
    {
        var mock = new Mock<IEmailService>();
        var capturedEmail = "";

        mock.Setup(x => x.SendEmail(It.IsAny<string>(), It.IsAny<string>()))
            .Callback<string, string>((to, subject) =>
            {
                capturedEmail = to;
            })
            .ReturnsAsync(true);

        // Use mock...

        capturedEmail.Should().NotBeEmpty();
    }

    [Fact]
    public void MockingWithSequence()
    {
        var mock = new Mock<IRetryService>();

        mock.SetupSequence(x => x.TryConnect())
            .Returns(false)  // First call fails
            .Returns(false)  // Second call fails
            .Returns(true);  // Third call succeeds
    }

    [Fact]
    public void MockingProperties()
    {
        var mock = new Mock<IConfiguration>();

        mock.Setup(x => x["ConnectionString"])
            .Returns("Server=localhost");

        // Or track property changes
        mock.SetupProperty(x => x.Timeout, 30);
    }

    [Fact]
    public void VerifyingCalls()
    {
        var mock = new Mock<ILogger>();

        // Use the mock...

        // Verify exact number of calls
        mock.Verify(x => x.Log(It.IsAny<string>()), Times.Exactly(3));

        // Verify at least once
        mock.Verify(x => x.Log(It.IsAny<string>()), Times.AtLeastOnce());

        // Verify never called
        mock.Verify(x => x.LogError(It.IsAny<string>()), Times.Never());

        // Verify all expected calls were made (strict mode)
        mock.VerifyAll();
    }
}
```

## FluentAssertions

```csharp
using FluentAssertions;
using FluentAssertions.Execution;

public class FluentAssertionsExamples
{
    [Fact]
    public void BasicAssertions()
    {
        var order = Order.Create(Guid.NewGuid(), DateTime.UtcNow);

        // Object assertions
        order.Should().NotBeNull();
        order.Status.Should().Be(OrderStatus.Pending);
        order.OrderDate.Should().BeCloseTo(DateTime.UtcNow, TimeSpan.FromSeconds(1));

        // String assertions
        order.OrderNumber.Should()
            .NotBeNullOrWhiteSpace()
            .And.StartWith("ORD-")
            .And.HaveLength(14);

        // Numeric assertions
        order.TotalAmount.Should()
            .BeGreaterOrEqualTo(0)
            .And.BeLessThan(10000);

        // Collection assertions
        order.Items.Should()
            .NotBeEmpty()
            .And.HaveCount(2)
            .And.OnlyHaveUniqueItems()
            .And.AllSatisfy(item =>
            {
                item.Quantity.Should().BePositive();
                item.Price.Should().BeGreaterThan(0);
            });
    }

    [Fact]
    public void AdvancedCollectionAssertions()
    {
        var products = new List<Product>
        {
            Product.Create("Product A", 10.99m),
            Product.Create("Product B", 20.99m),
            Product.Create("Product C", 30.99m),
        };

        products.Should()
            .Contain(p => p.Name == "Product B")
            .And.NotContain(p => p.Price > 100)
            .And.BeInAscendingOrder(p => p.Price);
    }

    [Fact]
    public void ExceptionAssertions()
    {
        var order = Order.Create(Guid.NewGuid(), DateTime.UtcNow);

        order.Invoking(o => o.AddItem(Guid.Empty, 1, 10))
            .Should().Throw<ArgumentException>()
            .WithMessage("*productId*")
            .And.ParamName.Should().Be("productId");
    }

    [Fact]
    public void AssertionScopes()
    {
        var order = Order.Create(Guid.NewGuid(), DateTime.UtcNow);

        using (new AssertionScope())
        {
            order.CustomerId.Should().NotBeEmpty();
            order.Status.Should().Be(OrderStatus.Pending);
            order.TotalAmount.Should().Be(0);
            // All assertions are evaluated even if some fail
        }
    }
}
```

## Testing CQRS Handlers

### Command Handler Tests

```csharp
public class CreateOrderCommandHandlerTests
{
    private readonly Mock<IOrderRepository> _orderRepository;
    private readonly Mock<IUnitOfWork> _unitOfWork;
    private readonly Mock<IDomainEventDispatcher> _eventDispatcher;
    private readonly CreateOrderCommandHandler _handler;

    public CreateOrderCommandHandlerTests()
    {
        _orderRepository = new Mock<IOrderRepository>();
        _unitOfWork = new Mock<IUnitOfWork>();
        _eventDispatcher = new Mock<IDomainEventDispatcher>();

        _handler = new CreateOrderCommandHandler(
            _orderRepository.Object,
            _unitOfWork.Object,
            _eventDispatcher.Object
        );
    }

    [Fact]
    public async Task Handle_ValidCommand_ReturnsSuccessResult()
    {
        // Arrange
        var command = new CreateOrderCommand
        {
            CustomerId = Guid.NewGuid(),
            Items = new List<CreateOrderItemDto>
            {
                new() { ProductId = Guid.NewGuid(), Quantity = 2, Price = 10.99m }
            }
        };

        _unitOfWork
            .Setup(x => x.SaveChangesAsync(It.IsAny<CancellationToken>()))
            .ReturnsAsync(1);

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        result.Should().NotBeNull();
        result.IsSuccess.Should().BeTrue();
        result.Value.Should().NotBeEmpty();

        _orderRepository.Verify(
            x => x.AddAsync(It.IsAny<Order>(), It.IsAny<CancellationToken>()),
            Times.Once
        );

        _unitOfWork.Verify(
            x => x.SaveChangesAsync(It.IsAny<CancellationToken>()),
            Times.Once
        );

        _eventDispatcher.Verify(
            x => x.DispatchAsync(It.IsAny<OrderCreatedEvent>(), It.IsAny<CancellationToken>()),
            Times.Once
        );
    }

    [Fact]
    public async Task Handle_EmptyItems_ReturnsFailureResult()
    {
        // Arrange
        var command = new CreateOrderCommand
        {
            CustomerId = Guid.NewGuid(),
            Items = new List<CreateOrderItemDto>()
        };

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        result.IsFailure.Should().BeTrue();
        result.Error.Should().Contain("at least one item");

        _orderRepository.Verify(
            x => x.AddAsync(It.IsAny<Order>(), It.IsAny<CancellationToken>()),
            Times.Never
        );
    }
}
```

### Query Handler Tests

```csharp
public class GetOrderByIdQueryHandlerTests
{
    private readonly Mock<IOrderRepository> _orderRepository;
    private readonly Mock<IMapper> _mapper;
    private readonly GetOrderByIdQueryHandler _handler;

    public GetOrderByIdQueryHandlerTests()
    {
        _orderRepository = new Mock<IOrderRepository>();
        _mapper = new Mock<IMapper>();

        _handler = new GetOrderByIdQueryHandler(
            _orderRepository.Object,
            _mapper.Object
        );
    }

    [Fact]
    public async Task Handle_ExistingOrder_ReturnsOrderDto()
    {
        // Arrange
        var orderId = Guid.NewGuid();
        var order = Order.Create(Guid.NewGuid(), DateTime.UtcNow);
        var orderDto = new OrderDto { Id = orderId };

        _orderRepository
            .Setup(x => x.GetByIdAsync(orderId, It.IsAny<CancellationToken>()))
            .ReturnsAsync(order);

        _mapper
            .Setup(x => x.Map<OrderDto>(order))
            .Returns(orderDto);

        var query = new GetOrderByIdQuery(orderId);

        // Act
        var result = await _handler.Handle(query, CancellationToken.None);

        // Assert
        result.Should().NotBeNull();
        result.IsSuccess.Should().BeTrue();
        result.Value.Should().BeEquivalentTo(orderDto);
    }

    [Fact]
    public async Task Handle_NonExistingOrder_ReturnsNotFoundResult()
    {
        // Arrange
        var orderId = Guid.NewGuid();

        _orderRepository
            .Setup(x => x.GetByIdAsync(orderId, It.IsAny<CancellationToken>()))
            .ReturnsAsync((Order)null);

        var query = new GetOrderByIdQuery(orderId);

        // Act
        var result = await _handler.Handle(query, CancellationToken.None);

        // Assert
        result.IsFailure.Should().BeTrue();
        result.Error.Should().Contain("not found");
    }
}
```

## Integration Testing with WebApplicationFactory

### Custom WebApplicationFactory

```csharp
// YourApp.IntegrationTests/Fixtures/CustomWebApplicationFactory.cs
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.AspNetCore.TestHost;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;
using Testcontainers.PostgreSql;

public class CustomWebApplicationFactory : WebApplicationFactory<Program>, IAsyncLifetime
{
    private readonly PostgreSqlContainer _dbContainer = new PostgreSqlBuilder()
        .WithImage("postgres:16")
        .WithDatabase("testdb")
        .WithUsername("testuser")
        .WithPassword("testpass")
        .Build();

    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        builder.ConfigureTestServices(services =>
        {
            // Remove existing DbContext
            services.RemoveAll<DbContextOptions<ApplicationDbContext>>();

            // Add test database
            services.AddDbContext<ApplicationDbContext>(options =>
            {
                options.UseNpgsql(_dbContainer.GetConnectionString());
            });

            // Replace services for testing
            services.RemoveAll<IEmailService>();
            services.AddScoped<IEmailService, FakeEmailService>();

            // Ensure database is created
            var sp = services.BuildServiceProvider();
            using var scope = sp.CreateScope();
            var db = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();
            db.Database.EnsureCreated();
        });
    }

    public async Task InitializeAsync()
    {
        await _dbContainer.StartAsync();
    }

    public new async Task DisposeAsync()
    {
        await _dbContainer.DisposeAsync();
    }
}
```

### API Integration Tests

```csharp
// YourApp.IntegrationTests/Api/OrdersControllerTests.cs
public class OrdersControllerTests : IClassFixture<CustomWebApplicationFactory>
{
    private readonly HttpClient _client;
    private readonly CustomWebApplicationFactory _factory;

    public OrdersControllerTests(CustomWebApplicationFactory factory)
    {
        _factory = factory;
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task CreateOrder_WithValidData_ReturnsCreated()
    {
        // Arrange
        var request = new CreateOrderRequest
        {
            CustomerId = Guid.NewGuid(),
            Items = new List<OrderItemRequest>
            {
                new() { ProductId = Guid.NewGuid(), Quantity = 2 }
            }
        };

        // Act
        var response = await _client.PostAsJsonAsync("/api/orders", request);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.Created);
        response.Headers.Location.Should().NotBeNull();

        var order = await response.Content.ReadFromJsonAsync<OrderResponse>();
        order.Should().NotBeNull();
        order!.Id.Should().NotBeEmpty();
        order.CustomerId.Should().Be(request.CustomerId);
    }

    [Fact]
    public async Task GetOrder_ExistingOrder_ReturnsOrder()
    {
        // Arrange - Create order first
        var createRequest = new CreateOrderRequest
        {
            CustomerId = Guid.NewGuid(),
            Items = new List<OrderItemRequest>
            {
                new() { ProductId = Guid.NewGuid(), Quantity = 1 }
            }
        };

        var createResponse = await _client.PostAsJsonAsync("/api/orders", createRequest);
        var createdOrder = await createResponse.Content.ReadFromJsonAsync<OrderResponse>();

        // Act
        var response = await _client.GetAsync($"/api/orders/{createdOrder!.Id}");

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);

        var order = await response.Content.ReadFromJsonAsync<OrderResponse>();
        order.Should().NotBeNull();
        order!.Id.Should().Be(createdOrder.Id);
    }

    [Fact]
    public async Task DeleteOrder_ExistingOrder_ReturnsNoContent()
    {
        // Arrange
        var createRequest = new CreateOrderRequest
        {
            CustomerId = Guid.NewGuid(),
            Items = new List<OrderItemRequest>
            {
                new() { ProductId = Guid.NewGuid(), Quantity = 1 }
            }
        };

        var createResponse = await _client.PostAsJsonAsync("/api/orders", createRequest);
        var createdOrder = await createResponse.Content.ReadFromJsonAsync<OrderResponse>();

        // Act
        var response = await _client.DeleteAsync($"/api/orders/{createdOrder!.Id}");

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.NoContent);

        // Verify it's deleted
        var getResponse = await _client.GetAsync($"/api/orders/{createdOrder.Id}");
        getResponse.StatusCode.Should().Be(HttpStatusCode.NotFound);
    }
}
```

## Test Data Builders

```csharp
// YourApp.UnitTests/Builders/OrderBuilder.cs
public class OrderBuilder
{
    private Guid _customerId = Guid.NewGuid();
    private DateTime _orderDate = DateTime.UtcNow;
    private List<(Guid ProductId, int Quantity, decimal Price)> _items = new();

    public OrderBuilder WithCustomerId(Guid customerId)
    {
        _customerId = customerId;
        return this;
    }

    public OrderBuilder WithOrderDate(DateTime orderDate)
    {
        _orderDate = orderDate;
        return this;
    }

    public OrderBuilder WithItem(Guid productId, int quantity, decimal price)
    {
        _items.Add((productId, quantity, price));
        return this;
    }

    public OrderBuilder WithRandomItems(int count = 3)
    {
        for (int i = 0; i < count; i++)
        {
            _items.Add((Guid.NewGuid(), Random.Shared.Next(1, 10), Random.Shared.Next(10, 100)));
        }
        return this;
    }

    public Order Build()
    {
        var order = Order.Create(_customerId, _orderDate);

        foreach (var (productId, quantity, price) in _items)
        {
            order.AddItem(productId, quantity, price);
        }

        return order;
    }
}

// Usage in tests
public class OrderBuilderTests
{
    [Fact]
    public void BuildOrder_WithBuilder()
    {
        var order = new OrderBuilder()
            .WithCustomerId(Guid.NewGuid())
            .WithOrderDate(new DateTime(2025, 1, 15))
            .WithItem(Guid.NewGuid(), 2, 10.99m)
            .WithItem(Guid.NewGuid(), 1, 20.99m)
            .Build();

        order.Items.Should().HaveCount(2);
        order.TotalAmount.Should().Be(42.97m);
    }
}
```

## Code Coverage

### Running Coverage

```bash
# Run tests with coverage
dotnet test /p:CollectCoverage=true /p:CoverletOutputFormat=opencover

# Generate HTML report with ReportGenerator
dotnet tool install -g dotnet-reportgenerator-globaltool
reportgenerator -reports:"**/coverage.opencover.xml" -targetdir:"coveragereport" -reporttypes:Html

# Or use coverlet with detailed output
dotnet test /p:CollectCoverage=true /p:CoverletOutput=./coverage/ /p:CoverletOutputFormat=\"json,opencover,lcov,cobertura\"

# View coverage in VS Code with Coverage Gutters extension
```

### Coverage Configuration

```xml
<!-- Directory.Build.props -->
<Project>
  <PropertyGroup>
    <CollectCoverage>true</CollectCoverage>
    <CoverletOutputFormat>opencover</CoverletOutputFormat>
    <Exclude>[*.Tests]*,[*.TestUtilities]*</Exclude>
    <ExcludeByAttribute>Obsolete,GeneratedCode,CompilerGenerated</ExcludeByAttribute>
    <Threshold>80</Threshold>
    <ThresholdType>line,branch</ThresholdType>
  </PropertyGroup>
</Project>
```

## Best Practices

### 1. AAA Pattern (Arrange-Act-Assert)

```csharp
[Fact]
public void Method_Scenario_ExpectedBehavior()
{
    // Arrange - Set up test data and dependencies
    var sut = new SystemUnderTest();
    var input = "test input";

    // Act - Execute the method being tested
    var result = sut.Method(input);

    // Assert - Verify the outcome
    result.Should().Be("expected");
}
```

### 2. One Assert Per Test (When Possible)

```csharp
// ✅ Good - One logical assertion
[Fact]
public void Order_ShouldHaveCorrectTotalAmount()
{
    var order = new OrderBuilder()
        .WithItem(Guid.NewGuid(), 2, 10.00m)
        .WithItem(Guid.NewGuid(), 1, 5.00m)
        .Build();

    order.TotalAmount.Should().Be(25.00m);
}

// ❌ Bad - Multiple unrelated assertions
[Fact]
public void Order_Tests()
{
    var order = new OrderBuilder().Build();
    order.TotalAmount.Should().Be(0);
    order.Status.Should().Be(OrderStatus.Pending);
    order.CustomerId.Should().NotBeEmpty();
}
```

### 3. Test Naming Convention

```csharp
// Pattern: MethodName_Scenario_ExpectedBehavior

[Fact]
public void AddItem_WithNegativeQuantity_ThrowsArgumentException() { }

[Fact]
public void AddItem_WithValidData_AddsItemToOrder() { }

[Fact]
public void CalculateTotal_WithDiscountCode_AppliesDiscount() { }
```

### 4. Avoid Test Interdependence

```csharp
// ✅ Good - Independent tests
public class IndependentTests
{
    [Fact]
    public void Test1()
    {
        var order = new OrderBuilder().Build();
        // Test specific scenario
    }

    [Fact]
    public void Test2()
    {
        var order = new OrderBuilder().Build();
        // Test different scenario
    }
}

// ❌ Bad - Tests depend on execution order
public class DependentTests
{
    private static Order _sharedOrder;

    [Fact]
    public void Test1_CreatesOrder()
    {
        _sharedOrder = new OrderBuilder().Build();
    }

    [Fact]
    public void Test2_ModifiesOrder() // Depends on Test1
    {
        _sharedOrder.AddItem(Guid.NewGuid(), 1, 10m);
    }
}
```

### 5. Mock Only External Dependencies

```csharp
// ✅ Good - Mock external services
[Fact]
public void Test_MocksExternalDependencies()
{
    var emailService = new Mock<IEmailService>();
    var paymentGateway = new Mock<IPaymentGateway>();

    var handler = new OrderHandler(emailService.Object, paymentGateway.Object);
    // Test...
}

// ❌ Bad - Mocking domain logic
[Fact]
public void Test_MocksDomainLogic()
{
    var order = new Mock<IOrder>(); // Don't mock domain entities
    // Test...
}
```

## Resources

- **references/xunit-complete-guide.md**: Comprehensive xUnit documentation
- **references/moq-advanced-patterns.md**: Advanced mocking patterns
- **references/integration-testing-guide.md**: Complete integration testing guide
- **references/test-containers-setup.md**: Testcontainers configuration
- **assets/test-builders.cs**: Reusable test data builders
- **assets/custom-assertions.cs**: Custom FluentAssertions extensions
- **assets/test-utilities.cs**: Common testing utilities

## Common Pitfalls

- **Testing Implementation Details**: Test behavior, not implementation
- **Brittle Tests**: Tests that break with minor refactoring
- **Slow Tests**: Integration tests that don't use test containers
- **Missing Assertions**: Tests that don't verify outcomes
- **Over-Mocking**: Mocking everything instead of just external dependencies
- **Shared State**: Tests that depend on shared mutable state
- **Magic Numbers**: Using hardcoded values without explanation
- **Ignoring Async**: Not properly awaiting async methods in tests
