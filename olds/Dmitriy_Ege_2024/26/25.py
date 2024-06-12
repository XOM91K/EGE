l = sorted([[int(d) for d in x.split()] for x in open('25.txt')])
pl = []
d = 100000
print(l)
for x in l:
    if x[1] == 1:
        pl.append(x[0])
for x in l:
    if x[1] == 0 and (sum(pl) + (len(pl) * 10)) + (x[0] + 10) <= d:
        pl.append(x[0])
del pl[-1]
for x in range(len(l) - 1, -1, -1):
    if l[x][1] == 0 and (sum(pl) + (len(pl) * 10)) + (l[x][0] + 10) <= d:
        print(l[x][0])
        break
print(len(pl) + 1)