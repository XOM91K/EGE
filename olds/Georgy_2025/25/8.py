def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0 :
            dls.append(x)
            if x != n // x:
                dls.append(n // x)
    return sorted(set(dls))
ct = 0
for x in range(1125000, 10 ** 10):
    R = [y for y in dels(x) if y%10 == 7 and y!=7]
    if len(R) > 0:
        ct += 1
        print(x,min(R))
        if ct == 5:
            break