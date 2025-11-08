# communicating_with_pipe.py
import multiprocessing
from do_something import do_something

def worker_task(pipe_conn, count):
    """
    Worker process function.

    Performs computation using 'do_something' and sends the result
    through the given pipe connection.
    """
    out_list = []
    result = do_something(count, out_list)
    pipe_conn.send(out_list[0])
    pipe_conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    
    process = multiprocessing.Process(target=worker_task, args=(child_conn, 3))
    process.start()

    print("⏳ Waiting for result from pipe...")
    result = parent_conn.recv()
    print(f"✅ Result received from pipe | "
          f"Prime count={result['prime_count']}, "
          f"Largest prime={result['largest_prime']}, "
          f"Math result={result['math_result']:.2f}")

    process.join()
