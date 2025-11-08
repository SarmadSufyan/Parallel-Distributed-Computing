import threading
import time
from do_something import do_something

start_event = threading.Event()
results = []

def worker(id, count):
    """
    Worker thread function.

    Waits for the start event, performs computation using 'do_something',
    and stores the result along with execution time.
    """
    print(f"[Event] Worker {id} waiting for start event...")
    start_event.wait()  # Blocks until the event is set

    start_time = time.time()
    out_list = []
    result = do_something(count, out_list)
    duration = time.time() - start_time

    results.append((id, out_list[0], duration))
    print(f"[Event] Worker {id} finished | "
          f"Prime count={out_list[0]['prime_count']}, "
          f"Largest prime={out_list[0]['largest_prime']}, "
          f"Math result={out_list[0]['math_result']:.2f}, "
          f"Time={duration:.3f}s")

if __name__ == "__main__":
    threads = []

    for i in range(5):
        t = threading.Thread(target=worker, args=(i, 3))
        threads.append(t)
        t.start()

    print("Main thread sleeping 2s then setting event (simulate setup)...")
    time.sleep(2)
    start_event.set()  # All waiting threads start simultaneously

    for t in threads:
        t.join()

    print("\nAll workers done (Event).")
    print("Results Summary:")
    for r in results:
        print(f" - Worker {r[0]} → Prime count={r[1]['prime_count']}, "
              f"Largest prime={r[1]['largest_prime']}, "
              f"Math result={r[1]['math_result']:.2f}, "
              f"Time={r[2]:.3f}s")
