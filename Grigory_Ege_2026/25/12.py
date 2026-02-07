def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))
for x in range(10000, 31622):
    x = x ** 2
    dl = dels(x)
    if len(dl) == 39 and x % 2 == 0:
        print(x, max([y for y in dl if y % 2 != 0]))
