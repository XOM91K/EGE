def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sum(sorted(set(dls)))
ct=  0
for x in range(500_001, 10 ** 10):
    R = dels(x)
    if str(R)[-1] == '9':
        print(x, R)
        ct += 1
        if ct == 5:
            break