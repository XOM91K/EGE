l = [[int(d) for d in x.split()] for x in open('22.txt')]
l = sorted(l, key=lambda d: d[0])
sr = [x[1] for x in l]
sr = sum(sr) / len(sr)
print(sr)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = [x[1], []]
    sl[x[0]][-1].append(x[2])
l = []
for x in sl:
    if sl[x][0] > sr:
        l.append([x, sl[x][0], sl[x][1]])
l = sorted(l, key=lambda d: (-d[-1].count(0), -d[1], d[-1].count(1)))
print(l)
print(l[0][1] * l[0][-1].count(0))
print(l[0][-1].count(1))