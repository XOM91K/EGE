#задача из 2 волны 2023 года, из яндекса.
l = [[int(d) for d in x.split()] for x in open('23.txt')]
print(l)
lnt = []
for x in range(len(l)):
    lnt.append([l[x][0], x])
    lnt.append([l[x][1], x])
lnt = sorted(lnt)
i = 0
f_lnt = [0] * len(l)
ll = 0
rr = -1

while len(lnt) != 0:
    if l[lnt[i][1]][0] == lnt[i][0]:
        f_lnt[ll] = l[lnt[i][1]]
        ll += 1
        ind = lnt[i][1]
        print(ind + 1, l[lnt[i][1]])
        d = 0
        while d != len(lnt):
            if lnt[d][1] == ind:
                del lnt[d]
                d -= 1
            d += 1
    else:
        f_lnt[rr] = l[lnt[i][1]]
        rr -= 1
        ind = lnt[i][1]
        print(ind + 1, l[lnt[i][1]])
        d = 0
        while d != len(lnt):
            if lnt[d][1] == ind:
                del lnt[d]
                d -= 1
            d += 1
ct = 0
for x in f_lnt:
    if x != [5836, 6153]:
        ct += 1
    else:
        break
print(f_lnt)
print(ct)