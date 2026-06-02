k = 199154
uch = [int(x) for x in open('18.txt').readlines()[:k]]
sn = [[int(d) for d in x.split()] for x in open('18.txt').readlines()[k:]]
sn = sorted(sn, key=lambda d: (d[-1], -d[0]))
print(uch)
print(sn)
sm = 0
mx = []
for x in uch:
    for y in sn:
        if y[0] >= x:
            sm += y[1]
            mx.append(y[0])
            break
print(sm, max(mx))