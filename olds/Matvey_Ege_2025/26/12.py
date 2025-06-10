l = [[int(d) for d in x.split()] for x in open('12.txt')]
l = sorted(l, key=lambda d: (d[1:].count(2), -sum(d[1:]), d[0]))
dv25 = len(l) // 4
print(dv25)
ct = 0
for x in l:
    ct += 1
    print(ct, x, x[1:].count(2))
