import itertools
k = 0
for x in itertools.product(sorted('гондубш'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'б' and x.count('н') >= 2 and 'у' not in x:
        print(k, x)