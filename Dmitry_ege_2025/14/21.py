def v4(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]
for x in range(1, 2001):
    d = 4 ** 210 + 4 ** 110 - x
    d = v4(d)
    if d.count('0') < 101:
        print(x, d.count('0'))