def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
n = 53 ** 123 + 65 ** 2222 - 172 ** 12
n = v7(n)
print(n.count('61') + n.count('62') + n.count('63') + n.count('64') + n.count('65'))
ct = 0
for x in '12345':
    ct += n.count('6' + x)
print(ct)