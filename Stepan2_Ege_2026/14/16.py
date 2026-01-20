def v3(d):
    s = ''
    while d > 0:
        s = str(d % 3) + s
        d //= 3
    return s
for x in range(1, 100000):
    d = 3 ** 200 + 3 ** 10 - x
    d = v3(d)
    if d.count('2') == 200:
        print(x, d)

