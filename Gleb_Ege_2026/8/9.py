import itertools
k = 0
r = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat=5):
    x = ''.join(x)
    r += 1
    if r % 5 != 0:
        k += 1
        if 'А' not in x and 'Ы' not in x and 'И' not in x and len(set(x)) == 5:
            print(k, x)