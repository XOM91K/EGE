# 199154 95384
l = [x for x in open('29.txt')]
s = sorted([int(x) for x in l[:199154]])
sn = [[int(d) for d in x.split()] for x in l[199154:]]
sl = {}
for x in sn:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
for x in sl:
    sl[x] = min(sl[x])
sl = sl.items()
sl = sorted(sl, key=lambda d: (d[1], -d[0]))
print(sl)
sm = 0
mx_mosh = []
for x in s:
    for y in sl:
        if x <= y[0]:
            sm += y[1]
            mx_mosh.append(y[0])
            break
print(sm, max(mx_mosh))