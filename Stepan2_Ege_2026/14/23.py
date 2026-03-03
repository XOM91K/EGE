def v5(d):
    s = ''
    while d > 0:
        s = str(d % 5) + s
        d //= 5
    return s
for y in range(1, 1000):
    d = 5 ** 50 - y
    d = v5(d)
    if d.count('4') == 47:
        print(y)