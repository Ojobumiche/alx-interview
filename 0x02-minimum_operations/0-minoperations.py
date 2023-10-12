#!/usr/bin/python3
"""0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops


if __name__ == '__main__':
    from random import randint
    from time import time

    start_time = time()

    for i in range(10):
        n = randint(2, 100)
        print("Min # of operations to reach {} char: {}".
              format(n, minOperations(n)))

    print(f'==> Program completed in {time() - start_time:.3f}s')
