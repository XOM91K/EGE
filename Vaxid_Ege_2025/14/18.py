def v9(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]
d = 19 ** 81 + 23 ** 709 - 4
d = v9(d)
ct = 0
for x in '1234567':
    ct += d.count('8' + x)
print(ct)