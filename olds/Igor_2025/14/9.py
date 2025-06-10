def v3(n):
    s = ''
    while n > 0:
        s += str(n % 6)
        n = n // 6
    return s[::-1]
for x in range(1, 10000):
    d = 6 ** 900 + 6 ** 10 - x
    g = v3(d)
    if g.count('3') == g.count('5'):
        print(x)