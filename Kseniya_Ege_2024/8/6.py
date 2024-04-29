import itertools
k = 0
n = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 5 != 0:
        n += 1
        if len(set(x)) == len(x):
            if 'И' not in x and 'А' not in x and 'Ы' not in x:
                print(n, x)