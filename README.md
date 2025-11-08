# Parallel and Distributed Computing - Lab Projects and Research

## Author Information

**Name:** Sarmad Sufyan Ahmed  
**Degree:** BS-CS (Bachelor of Science in Computer Science)  
**Course:** Parallel and Distributed Computing  
**Institution:** UIT University

---

## 📋 Repository Overview

This repository contains comprehensive implementations and demonstrations of parallel computing concepts in Python, covering threading, multiprocessing, and various synchronization mechanisms. The projects showcase practical applications of concurrent programming techniques for CPU-intensive computational tasks.

### 🎯 Learning Objectives

- Understanding thread synchronization primitives
- Implementing multiprocessing for CPU-bound tasks
- Managing inter-process communication
- Avoiding race conditions and deadlocks
- Optimizing parallel computation performance

---

## 📁 Repository Structure

```
parallel-distributed-computing/
│
├── Task-1/                    # Performance Analysis
│   ├── do_something.py
│   ├── multiprocessing_test.py
│   └── README.md
│
├── Task-2/                    # Thread Synchronization
│   ├── do_something.py
│   ├── barrier_test.py
│   ├── condition_test.py
│   ├── event_test.py
│   ├── lock_test.py
│   ├── rlock_test.py
│   ├── semaphore_test.py
│   ├── queue_test.py
│   └── README.md
│
├── Task-3/                    # Multiprocessing & Process Management
│   ├── do_something.py
│   ├── communicating_with_pipe.py
│   ├── communicating_with_queue.py
│   ├── killing_processes.py
│   ├── process_in_subclass.py
│   ├── process_pool.py
│   ├── run_background_processes_non_daemon.py
│   ├── run_background_processes.py
│   ├── spawning_processes.py
│   └── README.md
│
└── README.md                  # This file
```

---

## 🚀 Project Summaries

### Task-1: Performance Analysis - Multiprocessing vs Multithreading

Comprehensive performance comparison between multiprocessing and multithreading approaches for CPU-intensive computational tasks, demonstrating the impact of Python's Global Interpreter Lock (GIL).

**Key Concepts:**
- **Multiprocessing:** True parallelism with separate processes
- **Multithreading:** Concurrent execution with shared memory
- **GIL Impact:** Understanding Python's Global Interpreter Lock
- **CPU-bound Tasks:** Performance analysis of computational workloads
- **Benchmarking:** Timing and comparing parallel approaches

**Technologies:**
- Python `multiprocessing` module
- Python `threading` module
- CPU-intensive prime number calculations
- Performance measurement and analysis

**Highlights:**
✅ Demonstrates 3-5x performance improvement with multiprocessing  
✅ Clearly shows GIL limitations for CPU-bound tasks  
✅ Compares 50 processes vs 10 threads execution  
✅ Validates multiprocessing for computational workloads  
✅ Provides actionable insights for choosing concurrency models

📖 [View Task-1 Documentation](./Task-1/README.md)

---

### Task-2: Thread Synchronization in Python

Comprehensive demonstration of Python threading synchronization mechanisms using CPU-intensive computational tasks.

**Key Concepts:**
- **Barrier:** Coordinate multiple threads to start simultaneously
- **Condition:** Wait/notify pattern for thread coordination
- **Event:** Simple signaling mechanism between threads
- **Lock:** Mutual exclusion for shared resource protection
- **RLock:** Reentrant locks for recursive operations
- **Semaphore:** Limit concurrent access to resources
- **Queue:** Thread-safe producer-consumer pattern

**Technologies:**
- Python `threading` module
- Python `queue` module
- CPU-intensive prime number calculations
- Mathematical operations (sqrt, sin, cos, log)

**Highlights:**
✅ Prevents race conditions in shared data access  
✅ Demonstrates proper thread coordination  
✅ Implements producer-consumer patterns  
✅ Shows recursive locking mechanisms

📖 [View Task-2 Documentation](./Task-2/README.md)

---

### Task-3: Multiprocessing and Process Management

Advanced multiprocessing techniques demonstrating true parallelism for CPU-bound tasks, bypassing Python's Global Interpreter Lock (GIL).

**Key Concepts:**
- **Queue-based Communication:** Process-safe task distribution
- **Pipe Communication:** Direct two-way process communication
- **Process Termination:** Safe timeout and cleanup mechanisms
- **Process Subclassing:** Object-oriented process design
- **Process Pools:** Efficient task distribution across workers
- **Daemon Processes:** Background process lifecycle management
- **Spawn Method:** Cross-platform process creation

**Technologies:**
- Python `multiprocessing` module
- Inter-process communication (IPC)
- Process pools and workers
- CPU-intensive parallel computations

**Highlights:**
✅ Bypasses GIL for true parallel execution  
✅ Safe inter-process communication mechanisms  
✅ Proper process lifecycle management  
✅ Cross-platform compatibility with spawn method  
✅ Efficient resource utilization with process pools

📖 [View Task-3 Documentation](./Task-3/README.md)

---

## 🔬 Common Computational Task

All tasks utilize a consistent `do_something()` function that performs CPU-intensive operations:

### Operations Performed:
1. **Prime Number Calculation**
   - Finds all primes up to a given size
   - Uses trial division algorithm
   - Time complexity: O(n√n)

2. **Mathematical Operations**
   - Square root computations
   - Trigonometric functions (sin, cos)
   - Logarithmic calculations

3. **Result Aggregation**
   - Prime count and largest prime
   - Mathematical operation results
   - Performance metrics

### Why This Task?
✅ **CPU-bound:** Heavy mathematical computations  
✅ **Minimal I/O:** Reduces external bottlenecks  
✅ **Measurable:** Easy to benchmark and compare  
✅ **Scalable:** Adjustable workload sizes

---

## 🛠️ Technical Stack

- **Language:** Python 3.x
- **Core Modules:**
  - `threading` - Thread-based parallelism
  - `multiprocessing` - Process-based parallelism
  - `queue` - Thread-safe queues
  - `time` - Performance measurements
  - `math` - Mathematical operations

---

## 📊 Performance Considerations

### Threading (Task-2)
- ⚠️ Limited by Python's GIL for CPU-bound tasks
- ✅ Excellent for I/O-bound operations
- ✅ Lower overhead than processes
- ✅ Shared memory space

### Multiprocessing (Task-3)
- ✅ True parallelism for CPU-bound tasks
- ✅ Bypasses GIL limitations
- ⚠️ Higher memory overhead
- ⚠️ Inter-process communication overhead

---

## 🔧 Getting Started

### Prerequisites

```bash
# Python 3.7 or higher
python --version
```

### Running the Projects

```bash
# Navigate to Task-1 (Performance Analysis)
cd Task-1/

# Run the performance comparison
python multiprocessing_test.py

# Navigate to Task-2 (Thread Synchronization)
cd ../Task-2/

# Run individual demonstrations
python barrier_test.py
python lock_test.py
python queue_test.py

# Navigate to Task-3 (Multiprocessing)
cd ../Task-3/

# Run multiprocessing examples
python process_pool.py
python communicating_with_queue.py
python spawning_processes.py
```

---

## 📚 Key Learnings

### Performance Analysis (Task-1)
- Multiprocessing achieves 3-5x speedup for CPU-bound tasks
- Python's GIL severely limits threading performance for computations
- Process creation overhead is acceptable for heavy workloads
- True parallelism requires separate processes, not threads

### Threading Synchronization (Task-2)
- Understanding when and how to use different synchronization primitives
- Preventing race conditions in concurrent code
- Implementing thread-safe data structures
- Managing thread lifecycle and coordination

### Multiprocessing (Task-3)
- Achieving true parallelism for CPU-intensive tasks
- Safe inter-process communication patterns
- Process lifecycle management and cleanup
- Choosing between threading and multiprocessing

### Best Practices
- Always use proper synchronization for shared resources
- Prefer multiprocessing for CPU-bound tasks
- Use threading for I/O-bound operations
- Implement proper error handling and cleanup
- Monitor and measure performance improvements

---

## 🎓 Course Context

This repository represents practical implementations of concepts covered in the **Parallel and Distributed Computing** course at **UIT University**. The projects demonstrate:

- Fundamental parallel programming concepts
- Python's concurrency and parallelism mechanisms
- Real-world applications of concurrent programming
- Performance optimization techniques
- Safe and efficient parallel algorithm design

---

## 📖 Additional Resources

- [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
- [Python Multiprocessing Documentation](https://docs.python.org/3/library/multiprocessing.html)
- [Python Queue Documentation](https://docs.python.org/3/library/queue.html)
- [Python GIL Explained](https://realpython.com/python-gil/)

---

## 🤝 Contributing

This is an educational project. If you're a fellow student or instructor and notice improvements or have suggestions, feel free to reach out!

---

## 📄 License

This project is created for educational purposes as part of the Parallel and Distributed Computing course at UIT University. Free to use and modify for learning purposes.

---

## 📧 Contact

**Sarmad Sufyan Ahmed**  
BS-CS Student  
UIT University

---

<div align="center">

**⭐ If you find this repository helpful for learning parallel computing concepts, consider starring it! ⭐**

</div>

---

**Last Updated:** November 2025

**Happy Parallel Computing! 🚀**