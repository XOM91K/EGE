l = [[int(d) for d in x.split()] for x in open('10_416.txt')]
l = sorted(l, key=lambda d: sum(d))
k = [[0] for x in range(20)]
yy = 0
for x in l[:20]:
    k[yy].append(max(k[yy][-1], x[0]) + x[1])
    yy += 1
for x in l[20:]:
    for y in range(len(k)):
        if x[0] >= k[y][-1] and k[-1][-1] != 0:
            k[y].append(max(k[y][-1], x[0]) + x[1])
            break
    else:
        mn = 10 ** 10
        for z in k:
            mn = min(mn, z[-1])
        ind = 0
        for z in range(len(k)):
            if k[z][-1] == mn:
                ind = z
        k[ind].append(max(k[ind][-1], x[0]) + x[1])
print(max(k, key=len))