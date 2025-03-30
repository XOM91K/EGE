import itertools
k = 0
t = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 5 != 0:
        t += 1
        if 'И' not in x and 'А' not in x and 'Ы' not in x:
            if len(set(x)) == 5:
                print(t, x, set(x))