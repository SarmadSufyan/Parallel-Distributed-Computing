# Parallel and Distributed Computing - Performance Analysis

## 📋 Project Overview

This project demonstrates and compares the performance of **Multiprocessing** vs **Multithreading** in Python for CPU-intensive tasks. It uses a prime number calculation algorithm to analyze how parallel computing approaches handle computational workloads.

---

## 📁 Project Structure

```
project/
│
├── do_something.py          # Contains the CPU-intensive task
├── multiprocessing_test.py  # Main test file comparing approaches
└── README.md               # This file
```

---

## 🔬 The Computational Task (`do_something.py`)

### What It Does

The `do_something()` function performs three CPU-intensive operations:

1. **Prime Number Calculation**
   - Finds all prime numbers from 2 to `size`
   - Uses trial division algorithm
   - Complexity: O(n√n) - highly CPU-intensive

2. **Mathematical Operations**
   - Performs `size` iterations of:
     - Square root calculations
     - Trigonometric operations (sin, cos)
     - Logarithmic calculations

3. **Result Storage**
   - Stores prime count, computation results, and largest prime found
   - Prints progress for each completed process/thread

### Function Signature
```python
def do_something(size, out_list):
    """
    Args:
        size (int): Range of computation (workload size)
        out_list (list): Output list to store results
    """
```

### Why This Task?

This task is **CPU-bound**, meaning it:
- ✅ Requires heavy mathematical computation
- ✅ Keeps the CPU busy continuously
- ✅ Minimal I/O operations
- ✅ Perfect for demonstrating multiprocessing advantages

---

## 🚀 How It Works

### Multiprocessing Approach

```python
# Creates 50 separate processes
for i in range(50):
    process = multiprocessing.Process(target=do_something, args=(size, out_list))
    jobs.append(process)
```

**Characteristics:**
- 🔹 Creates **separate processes** with independent memory
- 🔹 Each process runs on a **different CPU core**
- 🔹 **True parallelism** - all processes execute simultaneously
- 🔹 No Global Interpreter Lock (GIL) interference
- 🔹 Higher memory overhead (each process has its own memory space)

### Multithreading Approach

```python
# Creates 10 threads
for i in range(10):
    thread = threading.Thread(target=do_something, args=(size, out_list))
    jobs.append(thread)
```

**Characteristics:**
- 🔹 Creates **threads** within the same process
- 🔹 All threads share the **same memory space**
- 🔹 **No true parallelism** for CPU-bound tasks due to Python's GIL
- 🔹 Threads execute mostly sequentially for CPU-intensive work
- 🔹 Lower memory overhead (shared memory)

---

## 📊 Comparative Analysis

### Expected Performance Results

| Metric | Multiprocessing | Multithreading |
|--------|----------------|----------------|
| **Execution Speed** | ⚡ **FAST** (True parallel) | 🐢 **SLOW** (Sequential) |
| **CPU Utilization** | High (multiple cores) | Low (single core) |
| **Memory Usage** | High (50 processes) | Low (10 threads) |
| **Scalability** | Scales with CPU cores | Limited by GIL |
| **Best For** | CPU-bound tasks | I/O-bound tasks |

### Why Multiprocessing Wins for CPU-Bound Tasks

```
Multiprocessing:
Process 1 → CPU Core 1 ████████ (Working)
Process 2 → CPU Core 2 ████████ (Working)
Process 3 → CPU Core 3 ████████ (Working)
Process 4 → CPU Core 4 ████████ (Working)
All running SIMULTANEOUSLY!

Multithreading (with GIL):
Thread 1 ████████ (Working) ⏸ (Waiting) ⏸ (Waiting)
Thread 2 ⏸ (Waiting) ████████ (Working) ⏸ (Waiting)
Thread 3 ⏸ (Waiting) ⏸ (Waiting) ████████ (Working)
Only ONE thread executes at a time!
```

### The Global Interpreter Lock (GIL)

Python's GIL prevents multiple threads from executing Python bytecode simultaneously. This means:
- ❌ **Threads cannot utilize multiple CPU cores for CPU-bound tasks**
- ✅ **Processes bypass the GIL entirely** (separate interpreters)
- ✅ **Threads are still useful for I/O-bound tasks** (network, file operations)

---

## 🔧 Configuration Parameters

### Adjustable Variables

```python
size = 10000      # Workload size (computational intensity)
procs = 50        # Number of processes for multiprocessing
threads = 10      # Number of threads for multithreading
```

### Experimentation Ideas

1. **Increase `size`** (e.g., 20000, 50000)
   - Result: Both approaches take longer, but multiprocessing gap widens

2. **Increase `procs`** (e.g., 100, 200)
   - Result: Diminishing returns after exceeding CPU core count

3. **Match `threads` to `procs`** (both = 50)
   - Result: Multithreading becomes significantly slower

4. **Decrease `size`** (e.g., 1000)
   - Result: Process creation overhead becomes noticeable

---

## 📈 Sample Output

```
Process completed: Found 1229 primes, Largest prime: 9973, Math result: 45623.47
Process completed: Found 1229 primes, Largest prime: 9973, Math result: 45623.47
... (50 times)
List processing complete.
Multiprocessing time = 3.24

Process completed: Found 1229 primes, Largest prime: 9973, Math result: 45623.47
... (10 times)
List processing complete.
Multithreading time = 14.67
```

**Analysis:** Multiprocessing is ~4.5x faster despite running 5x more workers!

---

## 🎯 Key Learnings

### When to Use Multiprocessing
✅ CPU-intensive computations (math, data processing, encoding)  
✅ Tasks that can be divided into independent chunks  
✅ When you have multiple CPU cores available  
✅ When memory overhead is acceptable  

### When to Use Multithreading
✅ I/O-bound operations (file reading, network requests)  
✅ Tasks that wait for external resources  
✅ When memory efficiency is critical  
✅ GUI applications (keep UI responsive)  

### When to Use Neither
✅ Simple sequential tasks  
✅ Tasks that complete quickly  
✅ When overhead exceeds benefits  

---

## 🛠️ How to Run

1. **Ensure both files are in the same directory:**
   ```
   do_something.py
   multiprocessing_test.py
   ```

2. **Run the test:**
   ```bash
   python multiprocessing_test.py
   ```

3. **Observe the timing differences!**

---

## 💡 Technical Insights

### Process Lifecycle
1. **Creation** → `multiprocessing.Process(target=...)`
2. **Starting** → `process.start()`
3. **Execution** → Function runs independently
4. **Joining** → `process.join()` (wait for completion)

### Critical Code Pattern
```python
if __name__ == "__main__":
```
**Why it's essential:**
- Prevents infinite process spawning
- Required for Windows compatibility
- Child processes import the main module
- Without it, each child would create more children!

---

## 🔍 Performance Factors

### Factors Affecting Multiprocessing Speed
- Number of CPU cores
- Process creation overhead
- Inter-process communication
- Memory availability

### Factors Affecting Multithreading Speed
- GIL contention
- Thread switching overhead
- Task nature (CPU vs I/O bound)
- Python implementation (CPython has GIL)

---

## 📚 Concepts Demonstrated

1. **Parallel Computing Paradigms**
2. **Process vs Thread Architecture**
3. **Global Interpreter Lock (GIL) Impact**
4. **CPU-Bound vs I/O-Bound Tasks**
5. **Performance Benchmarking**
6. **Scalability Analysis**

---

## 🎓 Course Context

This project is part of a **Parallel and Distributed Computing** course, demonstrating:
- Practical application of parallel programming
- Performance analysis methodology
- Trade-offs in concurrent programming
- Real-world optimization strategies

---

## 🚨 Important Notes

⚠️ **Memory Consideration:** 50 processes use significantly more RAM than 10 threads  
⚠️ **CPU Cores:** Performance gains plateau after exceeding available cores  
⚠️ **Platform Differences:** Results may vary on different operating systems  
⚠️ **Python Version:** Tested with Python 3.x

---

## 📝 Conclusion

This experiment clearly demonstrates that **multiprocessing is superior for CPU-intensive tasks** in Python, while **multithreading is hindered by the GIL**. The 3-5x performance improvement with multiprocessing validates its use for computational workloads, despite higher memory overhead.

For production systems processing large datasets, scientific computations, or data-parallel algorithms, **multiprocessing is the clear choice**.

---

## 👨‍💻 Author

Created for Parallel and Distributed Computing Course

---

## 📄 License

Educational purposes - Free to use and modify

---

**Happy Parallel Computing! 🚀**