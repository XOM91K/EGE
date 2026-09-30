import functools
l = [x.split() for x in open('2045.txt')]
for x in range(len(l)):
    l[x] = [int(l[x][0]), int(l[x][1]), float(l[x][2])]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1], x[2]])
mn = 1000
@functools.lru_cache(None)
def f(x, y):
    global mn
    if x == y:
        return 0
    if x not in sl:
        return float('inf')
    dists = []
    for z in sl[x]:
        dists.append(z[1] + f(z[0], y))
    if len(dists) < mn:
        mn = len(dists)
        return sum(dists)
    else:
        return 0
print(f(102, 2616))