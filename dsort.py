#!/usr/bin/python3

# dsort.py
#
# Distribution sort with partitioning implementation

import functools
import math
import random
import time
import timeit

M = (1 << 12)  # Memory size
B = (1 << 6)   # Block size
sMB = math.ceil(math.sqrt(M / B))

def dsort(array):
    if len(array) <= M:
        return sorted(array)

    # Select pivots
    pivots = random.sample(array, k=sMB)

    # Sort pivots
    pivots.sort()

    # Scan
    partitions = [[] for _ in range(len(pivots) + 1)]
    for ele in array:
        pnum = functools.reduce(lambda count, x: count + (x < ele), pivots, 0)
        partitions[pnum].append(ele)

    # Recurse
    return functools.reduce(
        lambda aggregate, x: aggregate + dsort(x), partitions, [])

if '__main__' == __name__:
    random.seed(6851)
    array = list(random.randint(0, 1 << 64 - 1) for _ in range(1 << 16))

    start = time.time()
    dresult = dsort(array)
    dsort_time = time.time() - start

    start = time.time()
    qresult = sorted(array)
    qsort_time = time.time() - start

    assert(dresult == qresult)
    print("Sorting correct")
    print("dsort time:", dsort_time)
    print("qsort time:", qsort_time)
