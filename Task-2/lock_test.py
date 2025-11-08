# lock_test.py
import threading
import time
from do_something import do_something

lock = threading.Lock()
results = []

def worker(id, count):
    """
    Worker thread function.

    Performs CPU-intensive computation using 'do_something' and appends
    the result to a shared list protected by a lock.
    """
    start_time = time.time()
    out_list = []
    value = do_something(count, out_list)
    duration = time.time() - start_time

    # Protect shared results with a lock
    with lock:
        results.append((id, out_list[0], duration))
        print(f"[Lock] Worker {id} appended result | "
              f"Prime count={out_list[0]['prime_count']}, "
              f"Largest prime={out_list[0]['largest_prime']}, "
              f"Math result={out_list[0]['math_result']:.2f}, "
              f"Time={duration:.3f}s")

if __name__ == "__main__":
    threads = []
    num_workers = 5
    count = 3  # Computation size for each worker

    total_start = time.time()
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(i, count))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll workers done (Lock).")
    print(f"Total Execution Time: {time.time() - total_start:.3f}s")

    print("Results Summary:")
    for r in results:
        print(f" - Worker {r[0]} → Prime count={r[1]['prime_count']}, "
              f"Largest prime={r[1]['largest_prime']}, "
              f"Math result={r[1]['math_result']:.2f}, "
              f"Time={r[2]:.3f}s")
