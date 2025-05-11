import multiprocessing
import time

def compute_sum(n):
    print(f"Summing up to {n}")
    return sum(range(n))

if __name__ == '__main__':
    # Workload: large sums
    tasks = [10_000_000, 10_000_000, 10_000_000, 10_000_000]

    print("\n--- Sequential ---")
    start = time.time()
    results_seq = [compute_sum(n) for n in tasks]
    end = time.time()
    print("Results:", results_seq)
    print(f"Sequential time: {end - start:.2f} seconds")

    print("\n--- Multiprocessing ---")
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results_mp = pool.map(compute_sum, tasks)
    end = time.time()
    print("Results:", results_mp)
    print(f"Multiprocessing time: {end - start:.2f} seconds")
