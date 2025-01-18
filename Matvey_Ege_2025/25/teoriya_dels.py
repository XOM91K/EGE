def dels(d):
    dls = []
    for i in range(1, int(d ** 0.5) + 1):
        if d % i == 0:
            dls.append(i)
            dls.append(d // i)
    return sorted(set(dls))
n = 110000101010100
print(dels(n))
# d = [1, 2123, 3 ,4]
# print(d[1], len(d), sum(d), sorted(d), d[1:4])
# d.append(5)