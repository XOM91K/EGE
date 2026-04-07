def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
for x in range(999_999_999, 10 ** 7, -1):
    ln = len(dels(x))
    if (x - ln) % 23 == 0:
        print(x)
# 999999961
# 999999789
# 999999740
# 999999731
# 999999690

999999690
999999731
999999740
999999789
999999961