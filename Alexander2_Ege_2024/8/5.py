import itertools
ct = 0
for x in itertools.product('0123456789abcdef', repeat=3):
    x = ''.join(x)
    if x[0] != '0' and len(set(x)) == 3:
        for y in '0123456789abcdef'[::2]:
            x = x.replace(y, '@')
        for y in '0123456789abcdef'[1::2]:
            x = x.replace(y, '#')
        if '@@' not in x and '##' not in x:
            ct += 1
print(ct)