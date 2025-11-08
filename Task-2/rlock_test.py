# rlock_test.py
import threading
import time
from do_something import do_something

rlock = threading.RLock()
results = []

def nested_work(id, count, depth):
    """
    Demonstrates recursive locking using RLock.

    The same thread can safely re-acquire the lock multiple times.
    The computation is performed at the innermost recursion level.
    """
    with rlock:
        if depth > 0:
            # Re-enter: safe because this is an RLock (same thread)
            nested_work(id, count, depth - 1)
        else:
            # Perform heavy computation at innermost level
            start_time = time.time()
            out_list = []
            value = do_something(count, out_list)
            duration = time.time() - start_time

            results.append((id, out_list[0], duration))
            print(f"[RLock] Worker {id} completed | "
                  f"Prime count={out_list[0]['prime_count']}, "
                  f"Largest prime={out_list[0]['largest_prime']}, "
                  f"Math result={out_list[0]['math_result']:.2f}, "
                  f"Time={duration:.3f}s")

def worker(id):
    """
    Worker thread function.

    Starts recursive computation using nested RLock acquisition.
    """
    nested_work(id, 2, 2)  # Depth-2 recursion

if __name__ == "__main__":
    threads = []

    for i in range(4):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll workers done (RLock).")
    print("Results Summary:")
    for r in results:
        print(f" - Worker {r[0]} → Prime count={r[1]['prime_count']}, "
              f"Largest prime={r[1]['largest_prime']}, "
              f"Math result={r[1]['math_result']:.2f}, "
              f"Time={r[2]:.3f}s")
