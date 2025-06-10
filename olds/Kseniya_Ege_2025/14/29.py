def v3(d):
    s = ''
    while d > 0:
        s = str(d % 3) + s
        d //= 3
    return s
for x in range(1, 2030):
    s = 3 ** 100 - x
    d = v3(s)
    if d.count('0') >= 6:
        print(x, d.count('0'))