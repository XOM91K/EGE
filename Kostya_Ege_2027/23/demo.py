import functools
l = [[int(float(d)) for d in x.split()] for x in open('demo.txt')]
sl = {}
print(l)
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1], x[2]])
@functools.lru_cache(None)
def f(x):
    if x == 100:
        return 0
    if x not in sl:
        return 1000000000
    vars = []
    for y in sl[x]:
        vars.append(y[1] + f(y[0]))
    return min(vars)
print(f(1))