def dels(d):
    l = []
    x = 2
    while x * x <= d:
        while d % x == 0:
            l.append(x)
            d //= x
        x += 1
    if d > 1:
        l.append(d)
    return l
for x in range(220_262_026, 10 ** 9):
    mn = dels(x)
    if len(mn) == 6 and all([str(d).count('2') == 1 for d in mn]):
        print(x, max(mn))
