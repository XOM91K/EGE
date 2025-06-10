import itertools
n = 0
k = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat=5):
    x = ''.join(x)
    n += 1
    if n % 5 != 0:
        k += 1
        if len(set(x)) == 5:
            if 'И' not in x and 'Ы' not in x and 'А' not in x:
                print(k, x)
                break