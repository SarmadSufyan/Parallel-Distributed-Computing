# condition_test.py
import threading
import time
from do_something import do_something

cond = threading.Condition()
results = []
TARGET = 4

def worker(id, count):
    """
    Worker thread function.

    Performs computation using 'do_something', appends the result to
    the shared list, and notifies the controller when done.
    """
    out_list = []
    val = do_something(count, out_list)
    with cond:
        results.append((id, out_list[0]))
        print(f"[Condition] Worker {id} appended result ({len(results)}/{TARGET})")
        cond.notify_all()  # Notify waiting controller thread(s)

def controller():
    """
    Controller thread function.

    Waits until all worker threads complete their tasks and results
    are available in the shared list.
    """
    with cond:
        while len(results) < TARGET:
            print(f"[Condition] Controller waiting, have {len(results)}/{TARGET}")
            cond.wait(timeout=5)  # Wait until notified or timeout
        print("[Condition] Controller: target reached, processing results:")
        for r in results:
            print(f" - Worker {r[0]} → Prime count: {r[1]['prime_count']}, "
                  f"Largest prime: {r[1]['largest_prime']}, "
                  f"Math result: {r[1]['math_result']:.2f}")

if __name__ == "__main__":
    # Start controller thread
    ctrl = threading.Thread(target=controller)
    ctrl.start()

    # Start worker threads
    threads = []
    for i in range(TARGET):
        t = threading.Thread(target=worker, args=(i, 2))
        threads.append(t)
        t.start()
        time.sleep(0.5)  # Slight delay to stagger workers

    for t in threads:
        t.join()
    ctrl.join()

    print("\nCondition demo finished.")
