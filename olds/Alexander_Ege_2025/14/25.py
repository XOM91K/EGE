def v6(d):
    s = ''
    while d > 0:
        s += str(d % 6)
        d //= 6
    return s[::-1]
for x in range(1, 10000):
    a = 6 ** 900 + 6 ** 10 - x
    a = v6(a)
    if a.count('3') == a.count('5'):
        print(x)