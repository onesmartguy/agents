---
name: dotnet-debugging-diagnostics
description: Master .NET debugging with dotnet-dump, dotnet-trace, dotnet-counters, dotnet-gcdump, Visual Studio debugger, production diagnostics, memory leak detection, and performance profiling. Use when diagnosing production issues, memory leaks, performance problems, or crashes in .NET applications.
---

# .NET Debugging and Diagnostics

Master comprehensive debugging and diagnostics for .NET 8+ applications including dotnet CLI diagnostic tools, Visual Studio debugging, production diagnostics, memory leak detection, CPU profiling, and crash dump analysis.

## When to Use This Skill

- Diagnosing production crashes and hangs
- Investigating memory leaks and high memory usage
- Analyzing CPU performance issues
- Debugging exceptions and stack traces
- Profiling garbage collection performance
- Analyzing thread contention and deadlocks
- Remote debugging in containers or Kubernetes
- Post-mortem crash dump analysis
- Real-time production monitoring
- Debugging async/await issues

## .NET Diagnostic Tools Overview

### dotnet-dump
- Collect and analyze memory dumps
- Post-mortem analysis without debugger
- Works on Windows, Linux, macOS
- SOS debugging commands

### dotnet-trace
- Collect performance traces
- CPU profiling
- EventPipe traces
- Analyze with PerfView or Visual Studio

### dotnet-counters
- Real-time performance metrics
- Monitor running applications
- CPU usage, memory, GC stats
- Custom EventCounters

### dotnet-gcdump
- GC heap snapshots
- Memory leak investigation
- Object retention analysis
- Smaller than full dumps

### dotnet-monitor
- RESTful diagnostic APIs
- Automated collection triggers
- Container-friendly monitoring

## Installation

```bash
# Install diagnostic tools globally
dotnet tool install --global dotnet-dump
dotnet tool install --global dotnet-trace
dotnet tool install --global dotnet-counters
dotnet tool install --global dotnet-gcdump
dotnet tool install --global dotnet-monitor

# Update tools
dotnet tool update --global dotnet-dump
dotnet tool update --global dotnet-trace
dotnet tool update --global dotnet-counters
dotnet tool update --global dotnet-gcdump
```

## dotnet-dump: Memory Dump Analysis

### Collecting Dumps

```bash
# List running .NET processes
dotnet-dump ps

# Collect dump of running process
dotnet-dump collect --process-id <PID>

# Collect dump with specific name
dotnet-dump collect --process-id <PID> --output /path/to/mydump.dmp

# Collect dump on Linux/Container
dotnet-dump collect --process-id 1 --output /dumps/app.dmp

# Trigger dump generation in code
using System.Diagnostics;
Process.GetCurrentProcess().Kill(sigterm: false);
```

### Analyzing Dumps

```bash
# Open dump for analysis
dotnet-dump analyze mydump.dmp

# Common SOS commands in dump analysis:
> help                    # List all commands
> clrstack               # Show managed call stack
> dumpheap -stat         # Heap statistics by type
> dumpheap -mt <MT>      # Objects of specific type
> gcroot <address>       # Find GC roots for object
> sos DumpObj <address>  # Examine specific object
> eeheap -gc             # GC heap statistics
> threads                # List all threads
> setthread <thread>     # Switch to thread
> dso                    # Dump stack objects
> syncblk                # Show sync blocks (locks)
```

### Common Dump Analysis Scenarios

```bash
# Find memory leaks
> dumpheap -stat
# Look for types with unexpectedly high counts

# Investigate specific type
> dumpheap -type System.String -stat
> dumpheap -mt <MethodTable> -min 1000

# Find what's holding objects
> gcroot <object-address>

# Analyze exceptions
> !dumpheap -type Exception
> !do <exception-address>

# Check for deadlocks
> !syncblk
> threads

# View large object heap
> dumpheap -stat -min 85000

# Memory by generation
> eeheap -gc
```

## dotnet-trace: Performance Profiling

### Collecting Traces

```bash
# List running processes
dotnet-trace ps

# Collect trace (default providers)
dotnet-trace collect --process-id <PID>

# Collect with specific providers
dotnet-trace collect --process-id <PID> \
  --providers Microsoft-Windows-DotNETRuntime

# Collect CPU samples
dotnet-trace collect --process-id <PID> \
  --profile cpu-sampling

# Collect for specific duration
dotnet-trace collect --process-id <PID> \
  --duration 00:00:30

# Collect with custom providers
dotnet-trace collect --process-id <PID> \
  --providers "Microsoft-Extensions-Logging:4:5"

# Common provider profiles
dotnet-trace collect --process-id <PID> --profile gc-verbose
dotnet-trace collect --process-id <PID> --profile gc-collect
```

### Analyzing Traces

```bash
# Convert to Speedscope format (browser-based viewer)
dotnet-trace convert mytrace.nettrace --format Speedscope

# View in PerfView (Windows)
PerfView.exe mytrace.nettrace

# View in Visual Studio
# File > Open > File > Select .nettrace file
```

### Custom Event Sources

```csharp
// Custom EventSource for application metrics
using System.Diagnostics.Tracing;

[EventSource(Name = "MyCompany-MyApp")]
public sealed class ApplicationEventSource : EventSource
{
    public static readonly ApplicationEventSource Log = new();

    [Event(1, Level = EventLevel.Informational)]
    public void OrderProcessed(string orderId, double processingTime)
    {
        WriteEvent(1, orderId, processingTime);
    }

    [Event(2, Level = EventLevel.Warning)]
    public void HighMemoryUsage(long bytes)
    {
        WriteEvent(2, bytes);
    }
}

// Usage
ApplicationEventSource.Log.OrderProcessed("ORD-123", 145.5);
```

## dotnet-counters: Real-Time Monitoring

### Monitoring Counters

```bash
# List available counters
dotnet-counters list

# Monitor default counters
dotnet-counters monitor --process-id <PID>

# Monitor specific counters
dotnet-counters monitor --process-id <PID> \
  --counters System.Runtime,Microsoft.AspNetCore.Hosting

# Monitor with refresh interval
dotnet-counters monitor --process-id <PID> \
  --refresh-interval 1

# Export to CSV
dotnet-counters collect --process-id <PID> \
  --output metrics.csv --format csv
```

### Important Built-in Counters

```bash
# System.Runtime counters:
- cpu-usage                  # CPU usage percentage
- working-set                # Physical memory usage
- gc-heap-size              # GC heap size
- gen-0-gc-count            # Gen 0 collections
- gen-1-gc-count            # Gen 1 collections
- gen-2-gc-count            # Gen 2 collections
- time-in-gc                # % time in GC
- gen-0-size                # Gen 0 heap size
- gen-1-size                # Gen 1 heap size
- gen-2-size                # Gen 2 heap size
- loh-size                  # Large object heap size
- alloc-rate                # Allocation rate
- exception-count           # Exceptions thrown
- threadpool-thread-count   # ThreadPool threads
- monitor-lock-contention-count  # Lock contention
- threadpool-queue-length   # ThreadPool queue length
- threadpool-completed-items-count

# Microsoft.AspNetCore.Hosting counters:
- requests-per-second
- total-requests
- current-requests
- failed-requests
```

### Custom EventCounters

```csharp
using System.Diagnostics.Tracing;

public class OrderMetrics : EventSource
{
    private readonly EventCounter _ordersProcessedCounter;
    private readonly PollingCounter _activeOrdersCounter;

    public OrderMetrics()
    {
        _ordersProcessedCounter = new EventCounter("orders-processed", this)
        {
            DisplayName = "Orders Processed",
            DisplayUnits = "orders"
        };

        _activeOrdersCounter = new PollingCounter("active-orders", this, () => GetActiveOrderCount())
        {
            DisplayName = "Active Orders"
        };
    }

    public void RecordOrderProcessed()
    {
        _ordersProcessedCounter.WriteMetric(1);
    }

    private double GetActiveOrderCount()
    {
        // Return current active order count
        return 42;
    }
}
```

## dotnet-gcdump: GC Heap Analysis

### Collecting GC Dumps

```bash
# Collect GC heap snapshot
dotnet-gcdump collect --process-id <PID>

# Collect with specific name
dotnet-gcdump collect --process-id <PID> --output myapp.gcdump

# Report without saving
dotnet-gcdump report <gcdump-file>
```

### Analyzing GC Dumps

```bash
# View heap statistics
dotnet-gcdump report myapp.gcdump

# Open in Visual Studio
# Debug > Windows > Memory Usage
# Load gcdump file

# Analyze with PerfView
PerfView.exe /GCDump myapp.gcdump
```

## Visual Studio Debugging

### Breakpoint Types

```csharp
// Conditional breakpoint
if (orderId == "ORD-123")
{
    // Breakpoint here with condition: orderId == "ORD-123"
}

// Tracepoint (log without stopping)
// Right-click breakpoint > Actions > Log message
// Message: "Order {orderId} processed at {DateTime.Now}"

// Data breakpoint (break when value changes)
// Debug > New Breakpoint > Data Breakpoint
```

### Advanced Debugging Features

```csharp
// Immediate Window
// Debug > Windows > Immediate
// Execute code during debugging:
// > order.TotalAmount
// > order.AddItem(Guid.NewGuid(), 1, 10m)

// Watch Window
// Add expressions to watch:
// - order.Items.Count
// - order.TotalAmount
// - DateTime.Now

// Call Stack
// Debug > Windows > Call Stack
// See execution path

// Autos/Locals Windows
// Debug > Windows > Autos/Locals
// View local variables automatically

// Exception Settings
// Debug > Windows > Exception Settings
// Break on specific exceptions
```

### Debugging Async Code

```csharp
// Tasks Window
// Debug > Windows > Tasks
// View all active tasks

// Parallel Stacks
// Debug > Windows > Parallel Stacks
// Visualize thread execution

// Async call stack
// Shows async await chain in call stack
```

## Production Diagnostics in Containers

### Docker Diagnostics

```dockerfile
# Dockerfile with diagnostic tools
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80

# Install diagnostic tools
RUN dotnet tool install --global dotnet-dump && \
    dotnet tool install --global dotnet-trace && \
    dotnet tool install --global dotnet-counters

ENV PATH="${PATH}:/root/.dotnet/tools"

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
# ... build steps ...

FROM base AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "MyApp.dll"]
```

### Collecting Diagnostics from Containers

```bash
# Get container ID
docker ps

# Exec into container
docker exec -it <container-id> /bin/bash

# Collect dump
dotnet-dump collect --process-id 1

# Copy dump out of container
docker cp <container-id>:/app/core_<timestamp> ./

# Or use dotnet-monitor sidecar
# See dotnet-monitor section below
```

### Kubernetes Diagnostics

```yaml
# Pod with diagnostic tools
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  containers:
  - name: app
    image: myapp:latest
    volumeMounts:
    - name: diagnostics
      mountPath: /diagnostics
  - name: dotnet-monitor
    image: mcr.microsoft.com/dotnet/monitor:8
    volumeMounts:
    - name: diagnostics
      mountPath: /diagnostics
  volumes:
  - name: diagnostics
    emptyDir: {}
```

```bash
# Exec into pod
kubectl exec -it myapp -c app -- /bin/bash

# Collect diagnostics
dotnet-dump collect --process-id 1 --output /diagnostics/dump.dmp

# Copy from pod
kubectl cp myapp:/diagnostics/dump.dmp ./dump.dmp -c app
```

## dotnet-monitor: Automated Diagnostics

### Configuration

```json
// appsettings.json for dotnet-monitor
{
  "DiagnosticPort": "/tmp/dotnet-diagnostic.sock",
  "Storage": {
    "DumpTempFolder": "/tmp"
  },
  "Egress": {
    "AzureBlobStorage": {
      "accountUri": "https://mystorageaccount.blob.core.windows.net",
      "containerName": "diagnostics",
      "accountKey": "<key>"
    }
  },
  "CollectionRules": {
    "HighMemoryRule": {
      "Trigger": {
        "Type": "EventCounter",
        "Settings": {
          "ProviderName": "System.Runtime",
          "CounterName": "working-set",
          "GreaterThan": 1000000000
        }
      },
      "Actions": [
        {
          "Type": "CollectDump",
          "Settings": {
            "Egress": "AzureBlobStorage"
          }
        }
      ]
    }
  }
}
```

### REST API Usage

```bash
# Get process info
curl http://localhost:52323/processes

# Collect dump via API
curl -X POST http://localhost:52323/dump?pid=1 \
  -o /tmp/dump.dmp

# Collect trace
curl -X POST http://localhost:52323/trace?pid=1&duration=30 \
  -o /tmp/trace.nettrace

# Get metrics
curl http://localhost:52323/metrics?pid=1
```

## Common Debugging Scenarios

### Memory Leak Investigation

```bash
# Step 1: Monitor memory over time
dotnet-counters monitor --process-id <PID> \
  --counters System.Runtime[working-set,gc-heap-size]

# Step 2: Take baseline GC dump
dotnet-gcdump collect --process-id <PID> --output baseline.gcdump

# Step 3: Exercise application
# Let it run under load...

# Step 4: Force GC and take another dump
# Trigger GC in code or wait for natural GC

dotnet-gcdump collect --process-id <PID> --output after-load.gcdump

# Step 5: Compare dumps in Visual Studio
# Memory Usage tool > Compare snapshots
```

### High CPU Investigation

```bash
# Collect CPU trace
dotnet-trace collect --process-id <PID> \
  --profile cpu-sampling \
  --duration 00:00:30

# Analyze in PerfView or Visual Studio
# Look for hot paths in CPU samples
```

### Deadlock Detection

```bash
# Collect dump during hang
dotnet-dump collect --process-id <PID>

# Analyze dump
dotnet-dump analyze mydump.dmp

# Check sync blocks
> syncblk

# View threads
> threads

# Switch to blocked thread
> setthread <thread-id>

# View stack
> clrstack
```

### Exception Investigation

```csharp
// Enable first-chance exception logging
AppDomain.CurrentDomain.FirstChanceException += (sender, args) =>
{
    Console.WriteLine($"First-chance exception: {args.Exception}");
};

// Or use diagnostic listener
var listener = new DiagnosticListener("MyApp");
listener.Subscribe(new ExceptionObserver());

class ExceptionObserver : IObserver<KeyValuePair<string, object>>
{
    public void OnNext(KeyValuePair<string, object> value)
    {
        if (value.Key == "System.Diagnostics.Exception")
        {
            var exception = value.Value as Exception;
            // Log exception
        }
    }
}
```

## Best Practices

### 1. Always Collect Diagnostics in Production

```csharp
// Add diagnostic endpoints in production
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddHealthChecks();

var app = builder.Build();

app.MapHealthChecks("/health");

// Diagnostic endpoint (secure this!)
app.MapGet("/diagnostics/gc", () =>
{
    var info = GC.GetGCMemoryInfo();
    return new
    {
        HeapSize = info.HeapSizeBytes,
        MemoryLoad = info.MemoryLoadBytes,
        Generation = GC.MaxGeneration
    };
});
```

### 2. Use Structured Logging

```csharp
using Microsoft.Extensions.Logging;

public class OrderService
{
    private readonly ILogger<OrderService> _logger;

    public async Task ProcessOrder(Order order)
    {
        using (_logger.BeginScope(new Dictionary<string, object>
        {
            ["OrderId"] = order.Id,
            ["CustomerId"] = order.CustomerId
        }))
        {
            _logger.LogInformation("Processing order {OrderId}", order.Id);

            try
            {
                await _repository.SaveAsync(order);
                _logger.LogInformation("Order {OrderId} saved successfully", order.Id);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process order {OrderId}", order.Id);
                throw;
            }
        }
    }
}
```

### 3. Implement Circuit Breakers

```csharp
using Polly;
using Polly.CircuitBreaker;

var circuitBreaker = Policy
    .Handle<HttpRequestException>()
    .CircuitBreakerAsync(
        exceptionsAllowedBeforeBreaking: 3,
        durationOfBreak: TimeSpan.FromSeconds(30),
        onBreak: (exception, duration) =>
        {
            _logger.LogWarning("Circuit breaker opened for {Duration}", duration);
        },
        onReset: () =>
        {
            _logger.LogInformation("Circuit breaker reset");
        });
```

### 4. Monitor ThreadPool

```csharp
// Log ThreadPool metrics
ThreadPool.GetAvailableThreads(out var workerThreads, out var ioThreads);
ThreadPool.GetMaxThreads(out var maxWorkerThreads, out var maxIoThreads);

_logger.LogInformation(
    "ThreadPool: {WorkerThreads}/{MaxWorkerThreads} worker, {IoThreads}/{MaxIoThreads} IO",
    workerThreads, maxWorkerThreads, ioThreads, maxIoThreads);
```

## Resources

- **references/sos-command-reference.md**: Complete SOS debugging commands
- **references/perfview-guide.md**: PerfView analysis guide
- **references/visual-studio-debugging.md**: VS debugging techniques
- **references/production-diagnostics.md**: Production monitoring patterns
- **assets/diagnostic-scripts.sh**: Common diagnostic scripts
- **assets/dump-analysis.md**: Dump analysis workflows

## Common Pitfalls

- **Not Collecting Baselines**: Always have baseline metrics before issues
- **Forgetting Symbol Files**: Include PDB files for proper stack traces
- **Over-Collecting**: Balance diagnostics overhead with performance
- **Not Securing Endpoints**: Protect diagnostic endpoints in production
- **Ignoring GC Stats**: GC can be source of performance issues
- **Missing Context**: Capture sufficient context (logs, metrics, traces)
- **Not Testing Tools**: Familiarize with tools before production incidents
- **Dump Size**: Full dumps can be huge; use gcdumps when possible
