import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('12_b.txt')]
clusters = [[], [], []]
for p in l:
    if p[0] > 10:
        if p[1] > 42:
            clusters[0].append(p)
        elif p[1] < 32:
            clusters[1].append(p)
        else:
            clusters[2].append(p)
anticentroids = [[], [], []]
ind = 0
for c in clusters:
    print(len(c))
    mx_sm_rast = 0
    for p1 in c:
        sm_rast = 0
        for p2 in c:
            sm_rast += math.dist(p1, p2)
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            anticentroids[ind] = p1
    ind += 1
P1 = anticentroids[0][0]
P2 = anticentroids[1][1]
print(int(P1 * 10000), int(P2 * 10000))