def dels(n):
    dls = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dls.append(i)
            dls.append(n // i)
    return sorted(set(dls))
for x in range(1_533_878, -1, -1):
    F = dels(x)
    if len(F) > 0:
        F = max(F) - min(F)
        if F > 5000 and F % 1235 == 0:
            print(x, F)