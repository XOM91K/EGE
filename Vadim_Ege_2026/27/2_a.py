import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open(r'2_a.txt')]
cls = [[], [], []]
for p in l:
    if p[0] < 0 and p[1] < 0:
        cls[0].append(p)
    elif p[0] > 0.5 and -6 <= p[1] <= 0:
        cls[1].append(p)
    elif -1 <= p[0] <= 2 and 0 <= p[1] <= 6:
        cls[2].append(p)
ctrs = [[], [], []]
i = 0
for c in cls:
    mx_s = 0
    for p1 in c:
        rast = 0
        for p2 in c:
            rast += math.dist(p1, p2)
        if rast > mx_s:
            mx_s = rast
            ctrs[i] = p1
    i += 1
Tx = abs(int((ctrs[0][0] + ctrs[1][0] + ctrs[2][0]) / 3 * 10000))
Ty = abs(int((ctrs[0][1] + ctrs[1][1] + ctrs[2][1]) / 3 * 10000))

print(Tx, Ty)