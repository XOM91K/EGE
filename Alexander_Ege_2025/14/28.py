def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
for x in range(1, 4001):
    d = 5 ** 17 + 5 ** 12 - x
    d = v5(d)
    if d.count('0') >= 10:
        print(x, d.count('0'))