import itertools
ct = 0
for x in itertools.product('чн', repeat=11):
    x = ''.join(x)
    if 'нн' not in x and x.count('н') == 4 :
        if x[0] == 'ч':
            ct += 3 * 4 ** 10
        else:
            ct += 4 ** 11
print(ct)