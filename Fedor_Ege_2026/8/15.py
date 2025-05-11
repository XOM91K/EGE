import itertools
k = 0
q = 0
for x in itertools.product (sorted('привычка'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 5 != 0:
        q += 1
        if 'и' not in x and 'а' not in x and 'ы' not in x:
            if len(set(x)) == 5:
                print(q, x)