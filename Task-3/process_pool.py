# pool_process.py
from multiprocessing import Pool
from do_something import do_something

def compute(count):
    """
    Worker function for process pool.

    Performs computation using 'do_something' and returns structured result.
    """
    out_list = []
    do_something(count, out_list)
    res = out_list[0]
    return f"Task Count={count} → Prime count={res['prime_count']}, " \
           f"Largest prime={res['largest_prime']}, " \
           f"Math result={res['math_result']:.2f}"

if __name__ == "__main__":
    counts = [1, 2, 3, 4, 5]  # 5 tasks

    with Pool(processes=3) as pool:  # 3 workers
        results = pool.map(compute, counts)

    print("=== Pool Results ===")
    for r in results:
        print(r)

    print("✅ Process Pool computation completed!")
