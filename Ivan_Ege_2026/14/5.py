def v7(d):
    s = ''
    while d > 0:
        s = str(d % 7) + s
        d //= 7
    return s
for x in range(1, 2031):
    d = 7 ** 170 + 7 ** 100 - x
    d = v7(d)
    if d.count('0') == 71:
        print(x)