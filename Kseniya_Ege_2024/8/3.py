import itertools
k = 0
for x in itertools.product('АГИЛМОРТ', repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'Т' and x.count('Г') == 2:
        print(k, x)