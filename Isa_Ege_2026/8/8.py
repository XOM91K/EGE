import itertools
k = 0
for x in itertools.product('ГЕКЭ023', repeat=4):
    x = ''.join(x)
    k += 1
    if x[0] in '023' and x[0] != x[1] and x[1] != x[2] and x[2] != x[3]:
        print(k, x)