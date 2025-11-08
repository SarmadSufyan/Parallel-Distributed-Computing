# Task-3: Multiprocessing and Process Management in Python

## 📋 Project Overview

This project demonstrates various multiprocessing techniques in Python for CPU-intensive tasks using the `do_something()` function.

The focus is on:

- **Inter-process communication** (Queue, Pipe)
- **Process management** (timeouts, daemon/non-daemon processes)
- **Process creation techniques** (subclassing, process pool, spawning)

It provides practical examples for parallel computation, safe communication, and process lifecycle management.

---

## 📁 Project Structure

```
Task-3/
│
├── do_something.py                          # CPU-intensive task
├── communicating_with_pipe.py               # Pipe-based inter-process communication
├── communicating_with_queue.py              # Queue-based inter-process communication
├── killing_processes.py                     # Terminating long-running processes safely
├── process_in_subclass.py                   # Creating processes using subclassing
├── process_pool.py                          # ProcessPool example for multiple tasks
├── run_background_processes_non_daemon.py   # Non-daemon background processes
├── run_background_processes.py              # Daemon background processes
├── spawning_processes.py                    # Spawn-based process creation
└── README.md                                # This file
```

---

## 🔬 The Computational Task (`do_something.py`)

### What It Does

`do_something(size, out_list)` performs:

1. Prime number calculations
2. Mathematical operations (sqrt, sin, cos, log)
3. Stores results including prime count, largest prime, and computation result

### Function Signature

```python
def do_something(size, out_list):
    """
    Args:
        size (int): Range of computation
        out_list (list): List to store results
    """
```

### Why This Task?

✅ CPU-intensive workload  
✅ Minimal I/O  
✅ Perfect for testing multiprocessing and parallel execution

---

## 🚀 Process Management Techniques

### 1️⃣ Inter-Process Communication

#### a) Queue (`communicating_with_queue.py`)

Thread-safe and process-safe task distribution mechanism using producer-consumer pattern.

**Example:**
```python
from multiprocessing import JoinableQueue, Queue

task_queue = JoinableQueue()
result_queue = Queue()
task_queue.put(task)
res = do_something(task)
result_queue.put(res)
```

**Use Case:** Safe task distribution among multiple processes.

---

#### b) Pipe (`communicating_with_pipe.py`)

Direct communication between two processes.

**Example:**
```python
from multiprocessing import Pipe

parent_conn, child_conn = Pipe()
child_process = Process(target=worker_task, args=(child_conn, 3))
child_process.start()
result = parent_conn.recv()
```

**Use Case:** Send/receive small amounts of data between two processes.

---

### 2️⃣ Process Termination (`killing_processes.py`)

Stop long-running processes safely with a timeout.

**Example:**
```python
p.join(timeout=2)
if p.is_alive():
    p.terminate()
```

**Use Case:** Prevent hanging processes in CPU-intensive tasks.

---

### 3️⃣ Subclassing Process (`process_in_subclass.py`)

Create custom process classes for encapsulated behavior.

**Example:**
```python
class MatrixMultiplicationProcess(Process):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def run(self):
        do_something(self.count)
```

**Use Case:** Encapsulate process behavior in reusable classes.

---

### 4️⃣ Process Pool (`process_pool.py`)

Manage multiple tasks using a pool of worker processes.

**Example:**
```python
from multiprocessing import Pool

with Pool(processes=3) as pool:
    results = pool.map(compute, counts)
```

**Use Case:** Efficiently distribute multiple tasks across limited worker processes.

---

### 5️⃣ Background Processes

#### a) Non-daemon (`run_background_processes_non_daemon.py`)

Process continues until completion, main process waits.

**Example:**
```python
p.daemon = False
p.start()
p.join()
```

---

#### b) Daemon (`run_background_processes.py`)

Process is killed automatically if main process exits.

**Example:**
```python
p.daemon = True
p.start()
```

**Key Difference:** Daemon = background, non-daemon = foreground.

---

### 6️⃣ Spawned Processes (`spawning_processes.py`)

Use spawn method for cross-platform consistency.

**Example:**
```python
from multiprocessing import set_start_method
set_start_method("spawn")
p = Process(target=worker, args=(i,))
p.start()
```

**Use Case:** Windows compatibility or when fork is not desired.

---

## 📊 Synchronization and Performance

- **Multiprocessing** achieves true parallelism for CPU-bound tasks
- **Inter-process communication** (Queue/Pipe) is safe and avoids shared-memory race conditions
- **Proper process lifecycle management** prevents resource leaks or hanging processes
- **Daemon vs non-daemon** processes affects whether background tasks complete if main exits

---

## 🔧 How to Run

1. Ensure all files are in the `Task-3` folder.

2. Run a specific demo:

```bash
python communicating_with_queue.py
python communicating_with_pipe.py
python killing_processes.py
python process_in_subclass.py
python process_pool.py
python run_background_processes_non_daemon.py
python run_background_processes.py
python spawning_processes.py
```

3. Observe console outputs for process execution, communication, and timing.

---

## 🎯 Key Learnings

✅ **Multiprocessing** bypasses the GIL for CPU-bound tasks  
✅ **Queue and Pipe** provide safe inter-process communication  
✅ **Daemon processes** are automatically killed on exit  
✅ **Non-daemon processes** run to completion  
✅ **Process pools** efficiently handle multiple tasks  
✅ **Spawn method** ensures cross-platform safety  
✅ **Subclassing Process** enables modular design

---

## 🛠️ Technical Notes

- **GIL Bypass:** Unlike threading, multiprocessing creates separate Python interpreters, bypassing the Global Interpreter Lock
- **Memory:** Each process has its own memory space, preventing race conditions but requiring explicit communication
- **Overhead:** Process creation has higher overhead than threads; use appropriately for CPU-bound tasks

---

## 👨‍💻 Author

Created for Parallel and Distributed Computing Course

---

## 📄 License

Educational purposes – Free to use and modify

---

**Happy Multiprocessing! 🚀**