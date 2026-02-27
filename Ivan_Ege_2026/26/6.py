l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l)
mesta = [d for d in range(1, 5701)]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
print(sl)
for x in sl:
    for y in range(len(sl[x])):
        if sl[x][y] in mesta:
            mesta.remove(sl[x][y])
    ct = 1
    for y in range(len(mesta) - 1):
        if mesta[y + 1] - mesta[y] == 1:
            ct += 1
            if ct >= 3:
                print(x, mesta[y - ct + 2])
        else:
            ct = 1