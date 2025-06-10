import itertools
k = 0
for x in itertools.product('АГЕМНРТУ', repeat=4):
    x = ''.join(x)
    k += 1
    if ''.join(sorted(x)) == x and len(set(x)) == 4:
        print(k, x)