import itertools
k = 0
for x in itertools.product('АВОПР', repeat=4):
    x = ''.join(x)
    k += 1
    if x[0] == 'П':
        print(k)