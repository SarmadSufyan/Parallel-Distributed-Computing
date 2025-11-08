# communicating_with_queue.py
import multiprocessing
from do_something import do_something

def worker_task(task_queue, result_queue):
    """
    Worker process function.

    Retrieves tasks from the task queue, performs computation using
    'do_something', and puts results into the result queue.
    """
    while not task_queue.empty():
        count = task_queue.get()
        out_list = []
        res = do_something(count, out_list)
        result_queue.put((count, out_list[0]))
        task_queue.task_done()

if __name__ == "__main__":
    task_queue = multiprocessing.JoinableQueue()
    result_queue = multiprocessing.Queue()

    # Add different workloads
    for i in [2, 3, 4]:
        task_queue.put(i)

    processes = []
    for _ in range(2):
        p = multiprocessing.Process(target=worker_task, args=(task_queue, result_queue))
        processes.append(p)
        p.start()

    # Wait until all tasks are processed
    task_queue.join()

    print("\n✅ Results from Queue:")
    while not result_queue.empty():
        count, res = result_queue.get()
        print(f"Task count={count} → Prime count={res['prime_count']}, "
              f"Largest prime={res['largest_prime']}, "
              f"Math result={res['math_result']:.2f}")

    for p in processes:
        p.join()
