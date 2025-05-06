l = [[int(d) for d in x.split()] for x in open('22.txt')]
r = []
inds = []
a = []
b = []
for x in range(len(l)):
    r.append([l[x][0], x + 1, True if l[x][0] <= l[x][1] else False])
    r.append([l[x][1], x + 1, True if l[x][0] <= l[x][1] else False])
r = sorted(r)
print(r)
last = 0
for x in r:
    if x[1] not in inds:
        if x[-1]:
            a.append(x[1])
            inds.append(x[1])
            last = x[1]
        else:
            b.append(x[1])
            inds.append(x[1])
            last = x[1]
if last == a[-1]:
    print(len(a) - 1)
else:
    print(len(a))
print(last)
#448
#515
print(a)
print(b)