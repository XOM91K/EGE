def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
for x in range(1, 2006):
    c = 4 ** 163 * 5 + 12 ** 62 - x
    c = v5(c)
    if c.count('1') < c.count('4'):
        print(x)