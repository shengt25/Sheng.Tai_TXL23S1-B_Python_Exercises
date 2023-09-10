from multiprocessing import Process, Queue, cpu_count
import random
import time


# Probability in circle
def prob_in_circle(number):
    i = 1
    count_inside_circle = 0
    while i <= number:
        i += 1
        coord_x = random.uniform(-1, 1)
        coord_y = random.uniform(-1, 1)
        if coord_x ** 2 + coord_y ** 2 < 1:
            count_inside_circle += 1
    return count_inside_circle


# Single processing
def pi_approx(total_number):
    count_inside_circle = prob_in_circle(total_number)
    pi = 4 * count_inside_circle / total_number
    return pi


# Multi processing
def pi_approx_mp(total_number):
    count_inside_circle = 0
    # get numbers and sub-process's numbers
    processes_count = cpu_count()
    sub_total_number = int(total_number / processes_count)
    # set up multiprocessing
    queue = Queue()
    processes = []
    # run multiprocessing
    for i in range(processes_count):
        p = Process(target=pi_approx_mp_runner, args=(sub_total_number, queue))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    # get result from multiprocessing
    for i in range(processes_count):
        count_inside_circle += queue.get()
    pi = 4 * count_inside_circle / total_number
    return pi


def pi_approx_mp_runner(sub_total_number, queue):
    queue.put(prob_in_circle(sub_total_number))


if __name__ == '__main__':
    total_number = int(input("Enter the total number of random points: "))
    method = int(input("Select: 1.Single processing, 2.Multi processing: "))
    if method == 1:
        time0 = time.time()
        pi = pi_approx(total_number)
        print(f"Approximation of pi: {pi}, finished in {time.time() - time0}s, single processing")
    elif method == 2:
        time0 = time.time()
        pi = pi_approx_mp(total_number)
        print(f"Approximation of pi: {pi}, finished in {time.time() - time0}s, multi processing")
    else:
        print("Invalid method.")
