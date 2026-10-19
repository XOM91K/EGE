import functools
l = [x.split() for x in open('5.txt')]
for i in range(len(l)):
    l[i] = [int(l[i][0]), int(l[i][1]), float(l[i][2])]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1], x[2]])
@functools.lru_cache(5000)
def f(x, y):
    if x == y:
        return 0
    if x not in sl:
        return float('inf')
    dists = []
    for z in sl[x]:
        dists.append(1 + f(z[0], y))
    return min(dists)
print(f(402, 8318))