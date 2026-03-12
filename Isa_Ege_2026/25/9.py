def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))
for x in range(699_999, 1, -1):
    l = dels(x)
    if len(l) > 0:
        M = sum(l) // len(l)
        if str(M)[-3:] == '313':
            print(x, M)






# 695526 28313
# 695533 18313
# 695606 31313
# 695940 33313
# 696525 22313
# 697664 31313
# 698196 43313