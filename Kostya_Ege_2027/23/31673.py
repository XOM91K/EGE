import functools
l = [[d for d in x.split()] for x in open('31673.txt')]
c = []
for x in l:
    c.append([int(x[0]),int(x[1]),float(x[2])])
sl = {}
for x in c:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1],x[2]])
@functools.lru_cache(None)
def f(x, y):
    if x == y:
        return 0
    if x not in sl:
        return float('inf')
    vars = []
    for z in sl[x]:
        vars.append(z[1] + f(z[0], y))
    return min(vars)
print(f(2691, 2840) + f(2840, 9180) + f(9180, 9514))