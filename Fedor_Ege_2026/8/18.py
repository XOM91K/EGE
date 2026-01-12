import itertools
k = 0
for x in itertools.product(sorted('ольга'), repeat=5):
    x = ''.join(x)
    k += 1
    print(k,x)