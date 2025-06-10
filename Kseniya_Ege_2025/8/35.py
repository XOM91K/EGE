import itertools
k = 0
for x in itertools.product('WSDA', repeat=5):
    x = ''.join(x)
    k += 1
    if 'DD' in x and x.count('S') >= 1 and x[-1] != 'W':
        print(k)