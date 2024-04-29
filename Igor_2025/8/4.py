import itertools
ct = 0
k = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat=5):
    x = ''.join(x)
    ct += 1
    if ct % 5 != 0:
        k += 1
        if 'А' not in x and 'И' not in x and 'Ы' not in x:
            if len(set(x)) == 5:
                print(k, x)