def dels(n):
    dls = []
    for x in range(1, n + 1):
        if n % x == 0:
            dls.append(x)
    return dls
mn = []
st = set(dels(4)).intersection(set(dels(7)))
l = [int(x) for x in open('12.txt')]
for x in range(len(l) - 1):
    if l[x] % 2 != l[x + 1] % 2:
        st = set(dels(l[x])).intersection(set(dels(l[x + 1])))
        if len(st) == 1:
            mn.append(l[x] + l[x + 1])
print(len(mn), min(mn))