l = [[int(d) for d in x.split()] for x in open('212.txt')]
#l = sorted(l, key=lambda d: (d[0]))
#print(l)
r = []
for x in range(len(l)):
    r.append([l[x][0], 0, x + 1])
    r.append([l[x][1], 1, x + 1])
r = sorted(r)
mesta  = [0] * 997
ll = 0
rr = -1
last = 0
for x in r:
    if x[-1] not in mesta:
        if x[1] == 0:
            mesta[ll] = x[-1]
            ll += 1
        else:
            mesta[rr] = x[-1]
            rr -= 1
        last = x[-1]
print(mesta)
print(last, mesta.index(last))
