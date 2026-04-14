import itertools
ct = 0
alf = '0123456789abcdefghijklmno'
for x in itertools.product(alf, repeat=4):
    x = ''.join(x)
    if x[0] != '0':
        sm = 0
        for y in x:
            sm += alf.index(y)
        if sm % 5 == 0:
            for y in alf[::2]:
                x = x.replace(y, '#')
            for y in alf[1::2]:
                x = x.replace(y, '@')
            if '##' not in x and '@@' not in x:
                ct += 1
print(ct)