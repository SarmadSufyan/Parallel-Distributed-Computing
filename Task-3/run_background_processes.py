# daemon_process.py
from multiprocessing import Process
from time import sleep
from do_something import do_something

def background_task():
    """
    Background task for a daemon process.

    Performs computation using 'do_something'.
    Note: Daemon processes are killed automatically when the main process exits.
    """
    print(f"[START] Daemon {Process().name}")
    out_list = []
    do_something(1, out_list)
    res = out_list[0]
    print(f"[EXIT] Daemon {Process().name} | "
          f"Prime count={res['prime_count']}, "
          f"Largest prime={res['largest_prime']}, "
          f"Math result={res['math_result']:.2f} "
          "(may not show if main ends early)")

if __name__ == "__main__":
    p = Process(target=background_task)
    p.daemon = True  # Important!!
    p.start()

    print("Main process doing some short task...")
    sleep(1)
    print("Main process exiting now!")
    # Daemon will be killed immediately if still running ✅
