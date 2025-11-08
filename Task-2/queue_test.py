# queue_test.py
import threading
import time
from queue import Queue
from do_something import do_something

q = Queue()
results = []
NUM_CONSUMERS = 3

def producer():
    """
    Producer thread function.

    Enqueues tasks for consumers to process and sends sentinel values
    to signal completion.
    """
    for i in range(6):
        task_count = 2
        print(f"[Queue] Producer enqueuing task {i}")
        q.put((i, task_count))

    # Send stop signal to each consumer
    for _ in range(NUM_CONSUMERS):
        q.put(None)

def consumer(cid):
    """
    Consumer thread function.

    Retrieves tasks from the queue, processes them using 'do_something',
    and records the results. Stops when a sentinel value (None) is received.
    """
    while True:
        item = q.get()
        if item is None:
            print(f"[Queue] Consumer {cid} received stop signal.")
            q.task_done()
            break

        task_id, count = item
        start_time = time.time()
        out_list = []
        val = do_something(count, out_list)
        duration = time.time() - start_time

        results.append((cid, task_id, out_list[0], duration))
        print(f"[Queue] Consumer {cid} processed task {task_id} | "
              f"Prime count={out_list[0]['prime_count']}, "
              f"Largest prime={out_list[0]['largest_prime']}, "
              f"Math result={out_list[0]['math_result']:.2f}, "
              f"Time={duration:.3f}s")
        q.task_done()

if __name__ == "__main__":
    # Start consumers
    consumers = []
    for i in range(NUM_CONSUMERS):
        t = threading.Thread(target=consumer, args=(i,))
        t.start()
        consumers.append(t)

    # Start producer
    prod = threading.Thread(target=producer)
    prod.start()
    prod.join()

    # Wait until all tasks are processed
    q.join()

    print("\nAll queue tasks processed successfully.")
    print("Results Summary:")
    for r in results:
        print(f" - Consumer {r[0]} → Task {r[1]} | "
              f"Prime count={r[2]['prime_count']}, "
              f"Largest prime={r[2]['largest_prime']}, "
              f"Math result={r[2]['math_result']:.2f}, "
              f"Time={r[3]:.3f}s")

    # Ensure all consumer threads exit
    for c in consumers:
        c.join()
