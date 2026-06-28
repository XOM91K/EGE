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
ct = 0
for x in range(5_000_001, 10 ** 7):
    l = dels(x)
    if len(l) == 3 and all(str(k).count('2') == 1 for k in l):
        print(x, max(l))
        ct += 1

        if ct == 5:
            break
