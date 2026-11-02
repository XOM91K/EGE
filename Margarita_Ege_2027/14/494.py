def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
for x in range(1, 2031):
    c = 7 ** 170 + 7 ** 100 - x
    c = v7(c)
    if c.count('0') == 71:
        print(x)