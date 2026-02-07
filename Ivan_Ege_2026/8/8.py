import itertools, string
print(string.ascii_uppercase)
ct = 0
for x in itertools.product('0123456789ABCDEFGHIJKLMNO', repeat=4):
    x = ''.join(x)
    c = 0
    cc = 0
    if x[0] != '0':
        for e in x:
            if e in '0123456789ABCDEFGHIJKLMNO'[::2]:
                c += 1
            if e in 'GHIJKLMNO':
                cc += 1
        if c > 0 and cc > 2:
            ct += 1
print(ct)