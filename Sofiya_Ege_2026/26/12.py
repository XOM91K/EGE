l = [[int(d) for d in x.split()] for x in open('12.txt')]
sr = [d[1] for d in l]
sr = sum(sr) / len(sr)
sl = {}
#print(l)
for x in l:
    if x[0] not in sl:
        sl[x[0]] = [x[1], []]
    sl[x[0]][-1].append(x[2])
for x in sl:
    sl[x].append(sl[x][1].count(0))
    sl[x].append(len(sl[x][1]) - sl[x][1].count(0))
fl = []
for x in sl:
    if sl[x][0] > sr:
        fl.append(sl[x])
fl = sorted(fl, key=lambda d: (-d[2], -d[0], d[-1]))
print(fl)
# 0 продан, 1 не продан