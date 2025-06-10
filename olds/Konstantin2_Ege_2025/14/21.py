def v4(d):
    s = ''
    while d > 0:
        s += str(d % 4)
        d //= 4
    return s[::-1]
for x in range(1, 3000):
    d = 2 ** 210 + 4 ** 110 - x
    d = v4(d)
    if d.count('0') > 9:
        print(x, d.count('0'))