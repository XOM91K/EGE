def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
ct = 0
for x in range(800_001, 10 ** 10):
    lst = dels(x)
    if len(lst) >= 2:
        if str(lst[0] + lst[-1])[-1] == '4':
            print(x, lst[0] + lst[-1])
            ct += 1
    if ct == 5:
        break