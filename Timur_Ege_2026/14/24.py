def v29(d):
    s = []
    while d > 0:
        s.append(str(d % 29))
        d //= 29
    return s
for x in range(1, 8411):
    c = 29 ** 293 + 29 ** 271 - x
    c = v29(c)
    if c.count('0') > 23:
        print(x, c.count('0'))
