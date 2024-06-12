import itertools
ct = 0
for x in itertools.product('01234567', repeat=6):
    s = ''.join(x)
    ch = sum([int(x) for x in s if int(x) % 2 == 0])
    nch = sum([int(x) for x in s if int(x) % 2 != 0])
    if s == s[::-1] and ch <= nch and s[0] != '0':
        ct += 1
print(ct)