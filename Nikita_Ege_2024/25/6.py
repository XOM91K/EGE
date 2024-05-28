def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x % 2 == 0:
                dls.append(x)
            if (n // x) % 2 == 0:
                dls.append(n // x)
    return sorted(set(dls))
for x in range(397_438, 443_521):
    d = dels(x)
    if len(d) >= 142:
        print(len(d), d[-1])
