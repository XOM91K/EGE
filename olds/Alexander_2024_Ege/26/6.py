l = [[d for d in x.split()] for x in open('6.txt')]
for x in range(len(l)):
    l[x] = [l[x][0][-10:].replace('T', '').replace(':', ''), l[x][1], l[x][2]]
    l[x] = [int(g) for g in l[x]]
sl = {}
for x in l:
    if x[1] not in sl:
        sl[x[1]] = [[], 0]
    sl[x[1]][0].append(x[2])
    sl[x[1]][1] = max(sl[x[1]][1], x[0])
mx = 0
pob = []
for x in sl:
    if len(sl[x][0]) > mx:
        mx = len(sl[x][0])
for x in sl:
    if len(sl[x][0]) == mx:
        pob.append([sl[x][-1], x])
print(pob)