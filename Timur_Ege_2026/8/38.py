import itertools
import string
ct = 0
print(string.ascii_uppercase)
for x in itertools.product('0123456789ABCDEFGHIJKLMNO', repeat=4):
    x = ''.join(x)
    d = x
    if x[0] != '0':
        for y in '0123456789ABCDEFGHIJKLMNO'[::2]:
            x = x.replace(y, '#')
        for y in '0123456789ABCDEFGHIJKLMNO'[1::2]:
            x = x.replace(y, '@')
        if '##' not in x and '@@' not in x:
            alf = '0123456789ABCDEFGHIJKLMNO'
            sm = 0
            for y in d:
                sm += alf.index(y)
            if sm % 5 == 0:
                ct += 1
print(ct)
