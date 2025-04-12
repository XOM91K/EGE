def M(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    MM = sorted(set(dls))
    if len(MM) >= 2:
        MM = MM[0] + MM[-1]
        return MM
    else:
        return 0
ct = 0
for x in range(800001, 10 ** 10):
    d = M(x)
    if str(d)[-1] == '4':
        print(x, d)
        ct += 1
        if ct == 5:
            break