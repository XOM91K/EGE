def v6(d):
    s = ''
    while d > 0:
        s = str(d % 6) + s
        d //= 6
    return s
for x in range(1, 2031):
    d = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    d = v6(d)
    if d.count('0') == 202:
        print(x)
