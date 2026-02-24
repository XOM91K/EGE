def v3(d):
    s = ''
    while d > 0:
        s = str(d % 3) + s
        d //= 3
    return s
for x in range(1, 100000):
    c = 3 ** 200 + 3 ** 10 - x
    c = v3(c)
    if c.count('2') == 200:
        print(x)
