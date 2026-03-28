l = [[int(d) for d in x.split()] for x in open('13.txt')]
l = sorted(l, key=lambda d: (d[0], -d[1]))
sr = [d[1] for d in l]
sr = sum(sr) / len(sr)
l = [d for d in l if d[1] > sr]
print(sr)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1], x[2]])
ll = []
for x in sl:
    ctN = 0
    ctP = 0
    for y in sl[x]:
        if y[1] == 0:
            ctP += 1
        else:
            ctN += 1
    ll.append([x, sl[x][0][0], ctP, ctN])
ll = sorted(ll, key=lambda d: (-d[2], -d[1], d[3]))
print(ll)
print(51 * 856)