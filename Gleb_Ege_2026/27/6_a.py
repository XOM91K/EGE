import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('6_a.txt')]
cl = [[], []]
for p in l:
    if p[0] > 2:
        cl[0].append(p)
    else:
        cl[1].append(p)
diags = [[], []]
ind = 0
for c in cl:
    mx_rast = 0
    for p1 in c:
        for p2 in c:
            if math.dist(p1, p2) > mx_rast:
                mx_rast = math.dist(p1, p2)
                diags[ind] = [p1, p2]
    ind += 1
Px = int((diags[0][0][0] + diags[0][1][0] + diags[1][0][0] + diags[1][1][0]) / 4 * 10000)
Py = int((diags[0][0][1] + diags[0][1][1] + diags[1][0][1] + diags[1][1][1]) / 4 * 10000)
print(Px, Py)