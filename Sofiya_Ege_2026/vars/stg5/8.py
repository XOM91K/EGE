import itertools
ct = 0
for x in itertools.product('0123456789abcdef', repeat=4):
    x = ''.join(x)
    if x[0] != '0' and x.count('d') == 1:
        for y in '0123456789abc^ef'[1::2]:
            x = x.replace(y, '@')
        if '@d' not in x and 'd@' not in x:
            ct += 1
print(ct)