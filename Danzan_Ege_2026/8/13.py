import string, itertools
print(string.ascii_uppercase)
ct = 0
for x in itertools.product('0123456789ABCDEFGHIJKLMNO', repeat=4):
    x = ''.join(x)
    ch = '0123456789ABCDEFGHIJKLMNO'[::2]
    if x[0] != '0' and (x[0] in ch or x[1] in ch or x[2] in ch or x[3] in ch):
        if (x.count('G') + x.count('H') + x.count('I') + x.count('J') + x.count('K') + x.count('L') + x.count('M') + x.count('N') + x.count('O')) > 2:
            ct += 1
print(ct)