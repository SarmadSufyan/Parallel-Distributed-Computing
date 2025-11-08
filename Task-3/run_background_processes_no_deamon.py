# non_daemon_process.py
from multiprocessing import Process
from do_something import do_something

def background_task():
    """
    Background task for a non-daemon process.

    Performs computation using 'do_something' and prints results.
    """
    print(f"[START] Non-daemon {Process().name}")
    out_list = []
    do_something(2, out_list)
    res = out_list[0]
    print(f"[DONE] Non-daemon {Process().name} finished matrix work | "
          f"Prime count={res['prime_count']}, "
          f"Largest prime={res['largest_prime']}, "
          f"Math result={res['math_result']:.2f} ✅")

if __name__ == "__main__":
    p = Process(target=background_task)
    # p.daemon = False → Default behavior
    p.start()

    print("Main will wait for background job ✅")
    p.join()
    print("Main process exits after background completes ✅")
