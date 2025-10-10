from do_something import do_something   # imports your function
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 10000     # how much work each process/thread does
    procs = 10            # number of processes
    jobs = []

    # -----------------------------
    # MULTIPROCESSING SECTION
    # -----------------------------
    start_time = time.time()
    for i in range(procs):
        out_list = list()
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time)

    # -----------------------------
    # MULTITHREADING SECTION
    # -----------------------------
    jobs = []
    threads = 10
    start_time = time.time()

    for i in range(threads):
        out_list = list()
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for l in jobs:
        l.start()

    for l in jobs:
        l.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time)
