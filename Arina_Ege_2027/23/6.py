# import functools
# l = [x.split() for x in open("6.txt")]
# sl = {}
# for x in range(len(l)):
#     l[x] = [int(l[x][0]), int(l[x][1]), float(l[x][2])]
# for x in l:
#     if x[0] not in sl:
#         sl[x[0]] = []
#     sl[x[0]].append([x[1], x[2]])
# @functools.lru_cache(5000)
# def f(x, y):
#     if x == y:
#         return 0
#     if x not in sl:
#         return float("inf")
#     dists = []
#     for z in sl[x]:
#         dists.append(z[1]+f(z[0], y))
#     return min(dists)
# print(f(514, 3260)+f(3260,7826))

import functools
l = [x.split() for x in open("6.txt")]
sl = {}
for x in range(len(l)):
    l[x] = [int(l[x][0]), int(l[x][1]), float(l[x][2])]
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1], x[2]])
@functools.lru_cache(5000)
def f(x, y):
    if x == 3260:
        return float('inf')
    if x == y:
        return 0
    if x not in sl or x == 3260:
        return float("inf")
    dists = []
    for z in sl[x]:
        dists.append(z[1]+f(z[0], y))
    return min(dists)
print(f(514, 7836))