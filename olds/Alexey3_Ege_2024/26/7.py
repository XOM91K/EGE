l = [[int(d) for d in x.split()] for x in open('7.txt')]
for y in range(len(l)):
    l[y] = [l[y][0], l[y][1], y + 1]
print(l)
l = sorted(l, key=lambda d: min(d[:-1]))
shl = []
pkr = []
ind = 0
for x in l:
    if min(x[:-1]) == x[0]:
        if len(shl) < len(l) // 2:
            shl.append(x)
        else:
            pkr.append(x)
    else:
        if len(pkr) < len(l) // 2:
            pkr.append(x)
        else:
            shl.append(x)
    ind = x[-1]
print(shl)
print(pkr)
print(ind)