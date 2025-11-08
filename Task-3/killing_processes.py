# killing_processes.py
import multiprocessing
import time
from do_something import do_something

def long_task():
    """
    Long-running process task.

    Performs a heavy computation using 'do_something'.
    """
    print("🚀 Process started... performing heavy computation")
    out_list = []
    do_something(10, out_list)  # Large workload
    print("✅ Task finished successfully | "
          f"Prime count={out_list[0]['prime_count']}, "
          f"Largest prime={out_list[0]['largest_prime']}, "
          f"Math result={out_list[0]['math_result']:.2f}")

if __name__ == "__main__":
    p = multiprocessing.Process(target=long_task)
    p.start()

    # Wait for 2 seconds only
    p.join(timeout=2)

    if p.is_alive():
        print("⛔ Timeout reached! Terminating the process...")
        p.terminate()
        p.join()

    print("✅ Process terminated safely.")
