def dels(d):
    dls = set()
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.add(x)
            dls.add(d // x)
    return sorted(dls)

for x in range(22360, 28284 + 1):
    x = x ** 2
    if 525_784_203 <= x <= 728_943_762:

        g = dels(x)
        #print(x, len(g))
        if len(g) == 3:
            print(x, g[-1])