import itertools
k2 = 0
k = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat=5):
    x = ''.join(x)
    k += 1
    x = x.replace('И', '#')
    x = x.replace('Ы', '#')
    x = x.replace('А', '#')
    if k % 5 != 0:
        k2 += 1
        #print(k2, x)
        if '#' not in x and len(list(set(x))) == 5:
            print(k2, x)