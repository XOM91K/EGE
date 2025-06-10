import itertools
k =0
for x in itertools.product(sorted('КИРЛ'), repeat=6):
    x = ''.join(x)

    if len(set(x)) == 4 and x.count(x[0]) != 3 and x.count(x[1]) != 3 and x.count(x[2]) != 3 and x.count(x[3]) != 3 and x.count(x[4]) != 3 and x.count(x[5]) != 3:
        k += 1
        if x == 'КИРИЛЛ':
            print(k, x)