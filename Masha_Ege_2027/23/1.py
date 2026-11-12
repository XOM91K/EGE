import functools
l = [[float(d) for d in x.split()] for x in open('1.txt')]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1], x[2]])
@functools.lru_cache(50000)
def f(x, y):
    if x == y:
        return 0
    if x not in sl:
        return float('inf')
    dists = []
    for z in sl[x]:
        dists.append(z[1] + f(z[0], y))
    print(dists)
    return min(dists)
print(f(1, 100))