def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
for x in range(999_999_999, 1, -1):
    dls = len(dels(x))
    if (x - dls) % 23 == 0:
        print(x)




#999999690 999999731 999999740 999999789 999999961