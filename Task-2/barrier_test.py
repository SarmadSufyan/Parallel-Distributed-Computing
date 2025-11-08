import threading
import time
from do_something import do_something

# Barrier waits until all threads reach this point
barrier = threading.Barrier(5)

def worker():
    """
    Worker thread function.
    
    Waits at the barrier, performs CPU-intensive computation using
    'do_something', and prints the execution time and result.
    """
    print("> Thread reached barrier")
    barrier.wait()  # Synchronization point
    
    start = time.time()
    out_list = []
    result = do_something(5, out_list)
    duration = time.time() - start

    print(f"✔ Thread done. Prime count={out_list[0]['prime_count']}, "
          f"Largest prime={out_list[0]['largest_prime']}, "
          f"Math result={out_list[0]['math_result']:.2f}, "
          f"Time={duration:.4f}s")

if __name__ == "__main__":
    threads = []
    start_all = time.time()

    for _ in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\nTotal Execution Time: {time.time() - start_all:.4f}s")
