l = sorted([int(x) for x in open('13.txt')])
nz = []
mn_ves = l[0]
print(mn_ves)
l = l[1:]
for x in l:
    if mn_ves <= x:
        if abs(x - mn_ves) > 1:
            for y in range(mn_ves + 1, x):
                nz.append(y)
        mn_ves += x
nz2 = nz.copy()

for item in nz:
    if item + l[-1] < mn_ves:
        nz2.append(item + l[-1])
print(len(nz2), max(nz2))
