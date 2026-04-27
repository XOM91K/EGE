def v45(d):
    s = []
    while d > 0:
        s.append(str(d % 45))
        d //= 45
    return s


for x in range(1, 1000):
    c = 6 ** 2030 + 6 ** 100 - x
    c = v45(c)
    if c.count('33') > 16:
        print(x, oct(c.count('33'))[2:])