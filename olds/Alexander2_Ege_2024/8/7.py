import itertools
ct = 0
for x in set(itertools.product('ДЕВИАЦИЯ', repeat=8)):
    x = ''.join(x)
    if x[0] in 'ЕИАЯ' and x[-1] in 'ДВЦ':
        can = False
        for y in range(7):
            if ord(x[y]) < ord(x[y + 1]):
                can = True
        if can:
            ct += 1
print(ct)