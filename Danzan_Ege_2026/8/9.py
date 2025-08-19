import itertools
k = 0
for x in itertools.product(sorted('АРГУМЕНТ'), repeat=4):
    x = ''.join(x)
    k+=1
    if len(set(x)) == 4 and sorted(x) == list(x):
        print(k, x)