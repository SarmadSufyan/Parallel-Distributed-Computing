# subclass_process.py
from multiprocessing import Process
from do_something import do_something

class MatrixMultiplicationProcess(Process):
    """
    Subclass of Process for performing matrix multiplication tasks.
    """
    def __init__(self, count, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = count

    def run(self):
        """
        Run method executed by the process.

        Performs computation using 'do_something' and prints results.
        """
        print(f"[START] {self.name} with count={self.count}")
        out_list = []
        result = do_something(self.count, out_list)
        res = out_list[0]
        print(f"[DONE] {self.name} → Prime count={res['prime_count']}, "
              f"Largest prime={res['largest_prime']}, "
              f"Math result={res['math_result']:.2f}")

if __name__ == "__main__":
    workers = [
        MatrixMultiplicationProcess(1, name="SubclassWorker-1"),
        MatrixMultiplicationProcess(2, name="SubclassWorker-2"),
        MatrixMultiplicationProcess(3, name="SubclassWorker-3")
    ]

    for w in workers:
        w.start()

    for w in workers:
        w.join()

    print("✅ Subclass-based workers completed!")
