# Task-2: Thread Synchronization in Python

## 📋 Project Overview

This project demonstrates the use of thread synchronization mechanisms in Python using CPU-intensive tasks. Each example uses the `do_something()` function to simulate heavy computation, such as prime number calculations and mathematical operations.

The synchronization primitives explored are:

- **Barrier**
- **Condition**
- **Event**
- **Lock**
- **RLock** (Reentrant Lock)
- **Semaphore**
- **Queue**

The purpose is to show how threads can coordinate, avoid race conditions, and execute safely in parallel.

---

## 📁 Project Structure

```
Task-2/
│
├── do_something.py       # CPU-intensive task implementation
├── barrier_test.py       # Demonstrates Barrier synchronization
├── condition_test.py     # Demonstrates Condition synchronization
├── event_test.py         # Demonstrates Event synchronization
├── lock_test.py          # Demonstrates Lock usage
├── rlock_test.py         # Demonstrates Reentrant Lock (RLock)
├── semaphore_test.py     # Demonstrates Semaphore usage
├── queue_test.py         # Producer-consumer using Queue
└── README.md             # This file
```

---

## 🔬 The Computational Task (`do_something.py`)

### What It Does

`do_something(size, out_list)` performs three main CPU-intensive operations:

1. **Prime Number Calculation**
   - Finds all prime numbers from 2 up to `size`
   - Uses trial division algorithm (O(n√n))

2. **Mathematical Operations**
   - Iterates `size` times performing:
     - Square roots
     - Sine and cosine operations
     - Logarithms

3. **Result Storage**
   - Stores prime count, largest prime, and math result in `out_list`
   - Prints a progress summary

### Function Signature

```python
def do_something(size, out_list):
    """
    Args:
        size (int): Computational workload size
        out_list (list): List to store results
    """
```

### Why This Task?

✅ CPU-bound computation (heavy math operations)  
✅ Minimal I/O interference  
✅ Perfect for demonstrating synchronization effects

---

## 🚀 Thread Synchronization Mechanisms

### 1️⃣ Barrier (`barrier_test.py`)

Threads wait until all threads reach a point before proceeding.

**Example:**
```python
barrier = threading.Barrier(5)
barrier.wait()
```

**Use Case:** Start multiple threads simultaneously or coordinate phases.

---

### 2️⃣ Condition (`condition_test.py`)

Threads wait for a specific condition before continuing.

**Example:**
```python
cond = threading.Condition()
with cond:
    cond.wait(timeout=5)
    cond.notify_all()
```

**Use Case:** Producer-consumer pattern, coordination between threads.

---

### 3️⃣ Event (`event_test.py`)

Threads wait for an event signal to start or continue.

**Example:**
```python
start_event = threading.Event()
start_event.wait()   # threads block
start_event.set()    # release all waiting threads
```

**Use Case:** Start multiple threads simultaneously after initialization.

---

### 4️⃣ Lock (`lock_test.py`)

Ensures mutual exclusion when accessing shared resources.

**Example:**
```python
lock = threading.Lock()
with lock:
    results.append(value)
```

**Use Case:** Protect shared data (results) from race conditions.

---

### 5️⃣ Reentrant Lock (RLock) (`rlock_test.py`)

Allows the same thread to acquire a lock multiple times. Useful in recursive critical sections.

**Example:**
```python
rlock = threading.RLock()
with rlock:
    nested_work(depth - 1)
```

**Use Case:** Recursive or nested operations needing lock safety.

---

### 6️⃣ Semaphore (`semaphore_test.py`)

Limits concurrent access to a resource.

**Example:**
```python
sem = threading.Semaphore(2)
sem.acquire()
# critical section
sem.release()
```

**Use Case:** Restrict number of threads performing CPU work at the same time.

---

### 7️⃣ Queue (`queue_test.py`)

Implements a thread-safe producer-consumer pattern.

**Example:**
```python
from queue import Queue
q = Queue()
q.put(task)
item = q.get()
q.task_done()
```

**Use Case:** Efficient task distribution among multiple consumers.

---

## 📊 Synchronization Comparison

| Primitive | Purpose | Behavior |
|-----------|---------|----------|
| **Barrier** | Wait for all threads to reach a point | Synchronizes thread start or phase |
| **Condition** | Wait/notify for condition | Producer-consumer coordination |
| **Event** | Signal threads to start | Simple signaling |
| **Lock** | Mutual exclusion | Protect shared data |
| **RLock** | Recursive locking | Thread can re-acquire lock |
| **Semaphore** | Limit concurrent access | Control resource usage |
| **Queue** | Thread-safe task distribution | Producer-consumer pattern |

---

## 🔧 How to Run

1. Ensure all files are in the `Task-2` folder.

2. Run a specific synchronization demo:

```bash
python barrier_test.py
python condition_test.py
python event_test.py
python lock_test.py
python rlock_test.py
python semaphore_test.py
python queue_test.py
```

3. Observe console outputs showing thread coordination.

---

## 📈 Sample Output (Barrier Example)

```
> Thread reached barrier
Process completed: Found 5 primes, Largest prime: 5, Math result: 15.12
✔ Thread done. Result=15.12, Time=0.0023s
```

- Barrier ensures all threads start at the same point.
- Condition, Event, Lock, RLock, Semaphore, and Queue examples show synchronized results.

---

## 🎯 Key Learnings

✅ **Barrier:** Coordinate thread phases  
✅ **Condition:** Wait/notify events  
✅ **Event:** Simple signaling  
✅ **Lock/RLock:** Prevent race conditions  
✅ **Semaphore:** Limit concurrent CPU tasks  
✅ **Queue:** Safe producer-consumer task distribution

**Takeaway:** Proper synchronization prevents race conditions and ensures predictable parallel execution.

---

## 🛠️ Technical Notes

- Threads share memory, so locks/synchronization are necessary for shared data.
- CPU-bound tasks may not benefit from threads due to Python's GIL.
- Multiprocessing is recommended for true CPU parallelism.

---

## 👨‍💻 Author

Created for Parallel and Distributed Computing Course

---

## 📄 License

Educational purposes – Free to use and modify

---

**Happy Thread Synchronization! 🚀**