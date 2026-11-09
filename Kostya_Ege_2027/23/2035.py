import functools
l = [[d for d in x.split()] for x in open('2035.txt')]
c = []
for x in l:
    c.append([int(x[0]),int(x[1]),float(x[2])])
sl = {}
for x in c:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1],x[2]])
print(sl)
@functools.lru_cache(None)
def f(x, y):
    ct = 0
    if x == y:
        return 1
    if x not in sl:
        return 0
    for z in sl[x]:
        ct += f(z[0], y)
    return ct
print(f(10, 92))