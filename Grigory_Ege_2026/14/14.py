def v6(d):
    s = ''
    while d > 0:
        s += str(d % 6)
        d //= 6
    return s[::-1]
for x in range(1, 10000):
    d = 6 ** 900 + 6 ** 10 - x
    d = v6(d)
    if d.count('3') == d.count('5'):
        print(x)
        break