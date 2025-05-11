d = [[int(d) for d in x.split()] for x in open('10.txt')]
l = sorted(d)
l.append([-1, -1])
ct = 1
ct_l = 0
r = []
for x in range(len(l) - 1):
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 0:
        continue
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 1:
        ct += 1
    elif l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] != 1:
        if ct >= 5:
            ct_l += 1
            ct = 1
    elif l[x][0] != l[x + 1][0]:
        if ct >= 5:
            ct_l += 1
        r.append([l[x][0], ct_l])
        ct = 1
        ct_l = 0
print(r)
print(max(r, key=lambda d: (d[1], d[0])))
