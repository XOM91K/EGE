def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))

for x in range(1_125_002, 10 ** 10):
    d = dels(x)
    mn7 = 0
    for y in d:
        if str(y)[-1] == '7' and y != 7:
            mn7 = y
            break
    if mn7 != 0:
        print(x, mn7)
