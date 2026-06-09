l = [[int(d) for d in x.split()] for x in open('19.txt')]
l = sorted(l, key=lambda d: (d[1], d[0]))
leks = [l[0]]
ct = 1
ub = 0
for x in l:
    if ct == 3:
        ub = 10
        ct = 0
    elif x[0] >= leks[-1][1] + ub:
        ub = 0
        leks.append(x)
        ct += 1
k = 0
for x in leks:
    k += 1
    print(x, k)
print(len(leks))
for x in l:
    if x[0] > 1246:
        print(x)
print(57-21)