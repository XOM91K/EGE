import itertools
k = 0
ct = 0
for x in itertools.product('АЕПСТУХ', repeat=4):
    x = ''.join(x)
    k += 1
    if k > 1000 and x[0] != x[1] and x[1] != x[2] and x[2] != x[3]:
        print(k, x)
        ct += 1
print(ct)