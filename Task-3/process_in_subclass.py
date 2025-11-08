from multiprocessing import Process
from do_something import do_something

class PrimeComputationProcess(Process):
    """
    Subclass of Process for performing prime number computation tasks.
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
        out_list = []  # Output list to store results
        do_something(self.count, out_list)
        res = out_list[0]  # Retrieve computation result
        print(f"[DONE] {self.name} → Prime count={res['prime_count']}, "
              f"Largest prime={res['largest_prime']}, "
              f"Math result={res['math_result']:.2f}")

if __name__ == "__main__":
    workers = [
        PrimeComputationProcess(1, name="PrimeWorker-1"),
        PrimeComputationProcess(2, name="PrimeWorker-2"),
        PrimeComputationProcess(3, name="PrimeWorker-3")
    ]

    for w in workers:
        w.start()

    for w in workers:
        w.join()

    print("✅ All prime computation workers completed!")
