#из яндекса
def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x % 2 == 0:
                dls.append(x)
            if (n // x) % 2 == 0:
                dls.append(n // x)
    return sorted(set(dls))
for x in range(397438, 443521):
    if len(dels(x)) >= 142:
        print(len(dels(x)), max(dels(x)))