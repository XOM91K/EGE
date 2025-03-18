def v5(d):
    s = ''
    while d > 0:
        s = str(d % 5) + s
        d //= 5
    return s

for x in range(1, 2005):
    c =4 ** 163 * 5 + 12 ** 62 - x
    d = v5(c)
    if d.count('1') < d.count('4'):
        print(x)