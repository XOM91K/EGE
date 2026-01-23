def dels(d):
    l = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for x in range(1_533_878, 1, -1):
    d = dels(x)
    if len(d) > 0:
        F = max(d) - min(d)
        if F > 5000 and F%1235 == 0:
            print(x, F)
# 1533874 766935
# 1531404 765700
# 1528934 764465
# 1526469 508820
#
# 1526464 763230
# 1526469 508820
# 1528934 764465
# 1531404 765700
# 1533874 766935