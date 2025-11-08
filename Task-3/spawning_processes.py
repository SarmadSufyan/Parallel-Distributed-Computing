# spawned_processes.py
from multiprocessing import Process, set_start_method
from do_something import do_something

def worker(i):
    """
    Worker process for spawned multiprocessing.

    Performs computation using 'do_something'.
    """
    print(f"[SPAWN] Worker-{i} started")
    out_list = []
    do_something(1, out_list)
    res = out_list[0]
    print(f"[DONE] Worker-{i} → Prime count={res['prime_count']}, "
          f"Largest prime={res['largest_prime']}, "
          f"Math result={res['math_result']:.2f}")

if __name__ == "__main__":
    try:
        # Windows default = spawn. Unix default = fork, but we force spawn for consistency
        set_start_method("spawn")
    except RuntimeError:
        pass  # Method already set earlier

    workers = []
    for i in range(3):
        p = Process(target=worker, args=(i,))
        workers.append(p)
        p.start()

    for p in workers:
        p.join()

    print("✅ All spawned processes completed!")
