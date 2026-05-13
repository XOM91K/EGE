from math import *

l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('10_a.txt')]
cls = [[], []]
for p in l:
    if p[1] > 10:
        cls[0].append(p)
    else:
        cls[1].append(p)
ind = 0
points = [[[], []], [[], []]]
for cl in cls:
    for p in cl:
        mx_rast = 0
        for c in cl:
            if dist(c, p) > mx_rast:
                mx_rast = dist(c, p)
                points[ind] = [p, c]
                points[ind] = [p, c]
    ind += 1
#print(int(min(p) * 10000), int(max(Py) * 10000))
print((points[0][0][0] + points[0][1][0]) * 10000)
print((points[1][0][0] + points[1][1][0]) * 10000)