# semaphore_test.py
import threading
import time
from do_something import do_something

# Allow at most 2 threads to run computation simultaneously
sem = threading.Semaphore(2)
results = []

def worker(id, count):
    """
    Worker thread function.

    Waits for the semaphore, performs computation using 'do_something',
    and stores the result along with execution time.
    """
    print(f"[Semaphore] Worker {id} waiting for semaphore...")
    sem.acquire()
    try:
        print(f"[Semaphore] Worker {id} START")
        start_time = time.time()
        out_list = []
        val = do_something(count, out_list)
        duration = time.time() - start_time

        results.append((id, out_list[0], duration))
        print(f"[Semaphore] Worker {id} DONE | "
              f"Prime count={out_list[0]['prime_count']}, "
              f"Largest prime={out_list[0]['largest_prime']}, "
              f"Math result={out_list[0]['math_result']:.2f}, "
              f"Time={duration:.3f}s")
    finally:
        sem.release()

if __name__ == "__main__":
    threads = []

    for i in range(6):
        t = threading.Thread(target=worker, args=(i, 2))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll workers done (Semaphore).")
    print(f"Results Summary (total={len(results)}):")
    for r in results:
        print(f" - Worker {r[0]} → Prime count={r[1]['prime_count']}, "
              f"Largest prime={r[1]['largest_prime']}, "
              f"Math result={r[1]['math_result']:.2f}, "
              f"Time={r[2]:.3f}s")
