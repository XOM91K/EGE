import itertools
k = 0
sl = {}
for x in itertools.product(sorted('АИКЛМЬ'), repeat=6):
    x = ''.join(x)
    k += 1
    sl[x] = k
k = 0
for x in itertools.product(sorted('АИКЛМЬ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[0] == 'К' and x[-1] == 'Ь' and len(set(x)) == len(x):
        if abs(sl[x[::-1]] - k) == 26655:
            print(sum(map(int, str(k))))
            break