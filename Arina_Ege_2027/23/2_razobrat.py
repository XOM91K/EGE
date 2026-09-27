import functools
s = [x.split() for x in open('2.txt')]
sl = {}
for x in range(len(s)):
    s[x] = [int(s[x][0]), int(s[x][1]), float(s[x][2])]
for x in s:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1], x[2]])
@functools.lru_cache(5000)
def f(x, y):
    if x == y:
        return 1
    if x not in sl:
        return 0
    cnt = 0
    for z in sl[x]:
        cnt += f(z[0], y)
    return cnt
print(f(5,95))