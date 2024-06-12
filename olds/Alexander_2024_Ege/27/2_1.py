l = [22, 17, 15, 50, 98, 1]
M = 10
k = 2
print()
from itertools import islice, tee
from functools import reduce
from operator import mul

def find_triplets(K, N, M, numbers):
    numbers = list(numbers)
    total_count = 0
    for i in range(len(numbers)-2):
        if i - K >= 0:
            start_index = max(i - K + 1, 0)
        else:
            continue
        end_index = min(i + 2, len(numbers))
        for j in islice(tee(numbers), start_index, end_index):
            if (i - K, i, j) in product_subgroups(K, N, numbers):
                total_count += int(mul(j) % M == 0)
    return total_count

def product_subgroups(K, N, numbers):
    for n in numbers:
        if n - K < 0 or n - 2 * K >= N:
            return
        start_index = n - K