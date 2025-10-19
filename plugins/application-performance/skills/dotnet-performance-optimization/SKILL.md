---
name: dotnet-performance-optimization
description: Optimize .NET application performance with BenchmarkDotNet, async/await patterns, memory optimization, Span<T>/Memory<T>, caching strategies, and profiling tools (dotTrace, PerfView). Use when improving application throughput, reducing latency, or optimizing resource usage.
---

# .NET Performance Optimization

Master performance optimization for .NET 8+ applications with BenchmarkDotNet, async patterns, memory optimization, span/memory, caching, and profiling.

## When to Use

- Reducing API response times
- Optimizing database queries with EF Core
- Improving throughput and latency
- Reducing memory allocations
- Optimizing async/await patterns
- Implementing efficient caching
- Profiling and benchmarking code

## BenchmarkDotNet

```bash
dotnet add package BenchmarkDotNet
```

```csharp
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

[MemoryDiagnoser]
[SimpleJob(launchCount: 1, warmupCount: 3, iterationCount: 5)]
public class StringBenchmarks
{
    private const int N = 1000;

    [Benchmark(Baseline = true)]
    public string StringConcat()
    {
        var result = "";
        for (int i = 0; i < N; i++)
            result += "a";
        return result;
    }

    [Benchmark]
    public string StringBuilder()
    {
        var sb = new StringBuilder();
        for (int i = 0; i < N; i++)
            sb.Append("a");
        return sb.ToString();
    }

    [Benchmark]
    public string StringCreate()
    {
        return string.Create(N, (char)'a', (span, state) =>
        {
            span.Fill(state);
        });
    }
}

// Program.cs
BenchmarkRunner.Run<StringBenchmarks>();
```

## Async/Await Optimization

```csharp
// ✅ Good - ValueTask for hot paths
public ValueTask<int> GetCachedValueAsync(string key)
{
    if (_cache.TryGetValue(key, out var value))
        return new ValueTask<int>(value); // Synchronous completion

    return LoadFromDatabaseAsync(key);
}

// ✅ Good - ConfigureAwait(false) in libraries
public async Task<Order> GetOrderAsync(Guid id)
{
    var order = await _repository.GetByIdAsync(id).ConfigureAwait(false);
    return order;
}

// ✅ Good - Parallel async operations
var tasks = ids.Select(id => _repository.GetByIdAsync(id));
var results = await Task.WhenAll(tasks);

// ❌ Bad - Blocking on async
var result = _repository.GetByIdAsync(id).Result; // Deadlock risk
var result2 = _repository.GetByIdAsync(id).GetAwaiter().GetResult();
```

## Memory Optimization with Span<T>

```csharp
// ✅ Good - Span<T> for stack allocation
public int ParseInt(ReadOnlySpan<char> input)
{
    Span<char> digits = stackalloc char[input.Length];
    int digitCount = 0;

    foreach (var c in input)
    {
        if (char.IsDigit(c))
            digits[digitCount++] = c;
    }

    return int.Parse(digits.Slice(0, digitCount));
}

// ✅ Good - ArrayPool for large arrays
using System.Buffers;

var pool = ArrayPool<byte>.Shared;
byte[] buffer = pool.Rent(1024);
try
{
    // Use buffer
}
finally
{
    pool.Return(buffer);
}

// ✅ Good - Memory<T> for async operations
public async Task ProcessDataAsync(Memory<byte> data)
{
    await ProcessChunkAsync(data.Slice(0, 512));
    await ProcessChunkAsync(data.Slice(512));
}
```

## Entity Framework Core Optimization

```csharp
// ✅ Good - AsNoTracking for read-only
var orders = await _context.Orders
    .AsNoTracking()
    .Where(o => o.CustomerId == customerId)
    .ToListAsync();

// ✅ Good - Projection to DTOs
var orderDtos = await _context.Orders
    .Where(o => o.CustomerId == customerId)
    .Select(o => new OrderDto
    {
        Id = o.Id,
        Total = o.TotalAmount
    })
    .ToListAsync();

// ✅ Good - Include for eager loading
var orders = await _context.Orders
    .Include(o => o.Items)
    .ThenInclude(i => i.Product)
    .Where(o => o.CustomerId == customerId)
    .ToListAsync();

// ✅ Good - Split query for collections
var orders = await _context.Orders
    .Include(o => o.Items)
    .AsSplitQuery() // Separate queries for collections
    .ToListAsync();

// ✅ Good - Compiled queries
private static readonly Func<AppDbContext, Guid, Task<Order>> _getOrderQuery =
    EF.CompileAsyncQuery((AppDbContext context, Guid id) =>
        context.Orders
            .Include(o => o.Items)
            .FirstOrDefault(o => o.Id == id));

public async Task<Order> GetOrderAsync(Guid id)
{
    return await _getOrderQuery(_context, id);
}
```

## Caching Strategies

```csharp
using Microsoft.Extensions.Caching.Memory;
using Microsoft.Extensions.Caching.Distributed;

// Memory Cache
public class OrderService
{
    private readonly IMemoryCache _cache;

    public async Task<Order> GetOrderAsync(Guid id)
    {
        return await _cache.GetOrCreateAsync($"order:{id}", async entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5);
            entry.SetPriority(CacheItemPriority.High);

            return await _repository.GetByIdAsync(id);
        });
    }
}

// Distributed Cache (Redis)
public class ProductService
{
    private readonly IDistributedCache _cache;

    public async Task<Product> GetProductAsync(Guid id)
    {
        var key = $"product:{id}";
        var cached = await _cache.GetStringAsync(key);

        if (cached != null)
            return JsonSerializer.Deserialize<Product>(cached);

        var product = await _repository.GetByIdAsync(id);

        await _cache.SetStringAsync(key,
            JsonSerializer.Serialize(product),
            new DistributedCacheEntryOptions
            {
                AbsoluteExpirationRelativeToNow = TimeSpan.FromHours(1)
            });

        return product;
    }
}

// Response Caching
[ResponseCache(Duration = 60, VaryByQueryKeys = new[] { "page", "pageSize" })]
public async Task<IActionResult> GetOrders([FromQuery] int page, [FromQuery] int pageSize)
{
    var orders = await _orderService.GetPagedAsync(page, pageSize);
    return Ok(orders);
}
```

## HTTP Client Optimization

```csharp
// ✅ Good - Use IHttpClientFactory
services.AddHttpClient<IProductService, ProductService>(client =>
{
    client.BaseAddress = new Uri("https://api.example.com");
    client.Timeout = TimeSpan.FromSeconds(30);
});

// ✅ Good - Connection pooling
services.AddHttpClient("ProductApi")
    .ConfigurePrimaryHttpMessageHandler(() => new SocketsHttpHandler
    {
        PooledConnectionLifetime = TimeSpan.FromMinutes(2),
        MaxConnectionsPerServer = 20
    });

// ✅ Good - Retry policies with Polly
services.AddHttpClient("ProductApi")
    .AddTransientHttpErrorPolicy(builder =>
        builder.WaitAndRetryAsync(3, retryAttempt =>
            TimeSpan.FromSeconds(Math.Pow(2, retryAttempt))));
```

## JSON Serialization

```csharp
using System.Text.Json;

// ✅ Good - System.Text.Json with source generators
[JsonSerializable(typeof(Order))]
[JsonSerializable(typeof(List<Order>))]
internal partial class AppJsonContext : JsonSerializerContext { }

// Usage
var options = new JsonSerializerOptions
{
    TypeInfoResolver = AppJsonContext.Default
};
var json = JsonSerializer.Serialize(order, options);

// ✅ Good - Utf8JsonReader for large files
public async Task<List<Order>> ParseOrdersAsync(Stream stream)
{
    var orders = new List<Order>();
    var reader = new Utf8JsonReader(await BinaryData.FromStreamAsync(stream));

    // Parse JSON without allocating strings
    while (reader.Read())
    {
        if (reader.TokenType == JsonTokenType.StartObject)
        {
            orders.Add(ParseOrder(ref reader));
        }
    }

    return orders;
}
```

## Best Practices

**1. Profile Before Optimizing**
```bash
dotnet-trace collect --process-id <PID> --profile cpu-sampling
# Analyze with PerfView or VS
```

**2. Use Analyzers**
```xml
<PackageReference Include="Microsoft.CodeAnalysis.NetAnalyzers" Version="8.0.0" />
<PackageReference Include="Roslynator.Analyzers" Version="4.7.0" />
```

**3. Minimize Allocations**
```csharp
// ✅ Use object pooling
private static readonly ObjectPool<StringBuilder> _pool =
    new DefaultObjectPool<StringBuilder>(new StringBuilderPooledObjectPolicy());

var sb = _pool.Get();
try
{
    sb.Append("data");
    return sb.ToString();
}
finally
{
    _pool.Return(sb);
}
```

**4. Optimize Logging**
```csharp
// ✅ Good - Source generators
public static partial class Log
{
    [LoggerMessage(EventId = 1, Level = LogLevel.Information,
        Message = "Processing order {OrderId}")]
    public static partial void ProcessingOrder(ILogger logger, Guid orderId);
}

// ❌ Bad - String interpolation
_logger.LogInformation($"Processing order {orderId}");
```

## Resources
- **BenchmarkDotNet Documentation**: https://benchmarkdotnet.org
- **PerfView Guide**: https://github.com/Microsoft/perfview
- **Span<T> Guide**: https://learn.microsoft.com/en-us/dotnet/standard/memory-and-spans
