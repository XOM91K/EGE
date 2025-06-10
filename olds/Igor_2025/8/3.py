import itertools
ct = 0
for x in itertools.product('чн', repeat=12):
    x = ''.join(x)
    if 'нн' not in x and x.count('н') == 5:
        if x[0] == 'н':
            ct += 4 ** 12
        else:
            ct += 3 * 4 ** 11
print(ct)
