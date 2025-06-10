from itertools import product
k = 0
for i in product(sorted('АРГУМЕНТ'), repeat=4):
    s = ''.join(i)
    k += 1
    if len(set(s)) == 4:
        if sorted(s) == list(s):
            print(k, s)
