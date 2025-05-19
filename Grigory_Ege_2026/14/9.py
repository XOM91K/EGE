def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
d = 53 ** 123 + 65 ** 2222 - 172 ** 12
d = v7(d)
ct = 0
for x in '12345':
    ct += d.count('6' + x)
print(ct)