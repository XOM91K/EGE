def v25(d):
    s = []
    while d > 0:
        s.append(str(d % 25))
        d //= 25
    return s


for x in range(1, 2500):
    c = 25 ** 150 + 25 ** 100 - x
    c = v25(c)
    if c.count('0') > 51:
        print(x, c.count('0'))
