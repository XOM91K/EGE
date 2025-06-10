import math
def dels(n):
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            if x ** (1 / 3) % 1 == 0:
                dls.append(x)
            if (n // x) ** (1 / 3) % 1 == 0:
                dls.append(n // x)
    return sorted(set(dls))
for x in range(228224, 531136):
    dls = dels(x)
    if len(dls) >= 4:
        print(len(dls), max(dls))