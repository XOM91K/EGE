def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))

l = [int(x) for x in open('11.txt')]
su = []
for x in range(len(l)-1):
    if l[x] % 2 != l[x + 1] % 2:
        d1 = set(dels(l[x]))
        d2 = set(dels(l[x + 1]))
        if d1.intersection(d2) == {1}:
            su.append(l[x] + l[x + 1])
print(len(su), min(su))
