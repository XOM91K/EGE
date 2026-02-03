import math
l = [[float(d) for d in x.split()] for x in open('10_a.txt')]
cls = [[], [], []]
for p in l:
    if p[1] > 5.5:
        cls[0].append(p)
    elif p[1] < 2:
        cls[1].append(p)
    else:
        cls[2].append(p)
ctrs = [[], [], []]
radiuses = [[], [], []]
ind = 0
for cl in cls:
    mn_sm_rast = 10 ** 10
    for p1 in cl:
        sm_rast = 0
        mx_rast = 0
        for p2 in cl:
            sm_rast += math.dist(p1, p2)
            mx_rast = max(mx_rast, math.dist(p1, p2))
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            ctrs[ind] = p1
            radiuses[ind] = mx_rast
    ind += 1
print(radiuses)
print(int(min(radiuses) * 10000), int(max(radiuses) * 10000))