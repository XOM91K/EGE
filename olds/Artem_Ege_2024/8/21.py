import itertools
k = 0
for x in itertools.product('ИКЛНОР', repeat=4):
    x = ''.join(x)
    k += 1
    if x == 'КИНО':
        print(k, x)