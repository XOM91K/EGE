import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open(r'2_b.txt')]
cls = [[], [], [], [], []]
for p in l:
    if p[1] > 38:
        if -42 <= p[0] < -22:
            cls[0].append(p)
        elif -14 <= p[0] <= 10:
            cls[1].append(p)
    else:
        if -54 <= p[0] <= -36:
            cls[2].append(p)
        elif -26 <= p[0] <= -8:
            cls[3].append(p)
        elif 2 <= p[0] <= 18:
            cls[4].append(p)
ctrs = [[], [], [], [], []]
i = 0
for c in cls:
    print(c)
    mx_s = 0
    for p1 in c:
        rast = 0
        for p2 in c:
            rast += math.dist(p1, p2)
        if rast > mx_s:
            mx_s = rast
            ctrs[i] = p1
    i += 1
Tx = abs(int((ctrs[0][0] + ctrs[1][0] + ctrs[2][0] + ctrs[3][0] + ctrs[4][0]) / 5 * 10000))
Ty = abs(int((ctrs[0][1] + ctrs[1][1] + ctrs[2][1] + ctrs[3][1] + ctrs[4][1]) / 5 * 10000))

print(Tx, Ty)