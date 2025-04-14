def dels(d):
    dls = []
    for i in range(2, int(d ** 0.5) + 1):
        if d % i == 0:
            dls.append(i)
            dls.append(d // i)
    dls = sorted(set(dls))
    if len(dls) > 0:
        return dls[0] + dls[-1]
    else:
        return 0
for i in range(700000, 8000000):
    if str(dels(i))[-1] == '4':
        print(i, dels(i))