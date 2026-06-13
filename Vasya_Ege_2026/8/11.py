import itertools
k = 0
for x in itertools.product(sorted('ЧЕРМША'), repeat=7):
    x = ''.join(x)
    k += 1
    if (x[0] != 'А' or x[0] != 'Е') and x.count("Р")  >= 2:
        if k % 2 != 0:
            print(k)