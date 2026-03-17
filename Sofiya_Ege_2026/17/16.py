def dels(n):
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
l = [int(x) for x in open('16.txt')]
ans = []
for x in range(len(l) - 1):
    n1 = l[x]
    n2 = l[x + 1]
    if (n1 % 2 == 0 and n2 % 2 != 0) or (n2 % 2 == 0 and n1 % 2 != 0):
        dls1 = dels(n1)
        dls2 = dels(n2)
        if len(set(dls1).intersection(set(dls2))) == 1:
            ans.append(n1 + n2)
            print(dls1, dls2)
print(len(ans), min(ans))