import itertools, string
print(string.ascii_uppercase)
ct = 0
for x in itertools.product('0123456789ABCDEFGHIJKLMNO', repeat=4):
    x = ''.join(x)
    if x[0] != '0':
        ct_ch = 0
        for y in '0123456789ABCDEFGHIJKLMNO'[::2]:
            ct_ch += x.count(y)
        if ct_ch >= 1:
            ct_15 = 0
            for y in 'GHIJKLMNO':
                ct_15 += x.count(y)
            if ct_15 > 2:
                ct += 1
print(ct)