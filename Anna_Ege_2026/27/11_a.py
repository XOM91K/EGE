import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('11_a.txt')]
cls = [[], []]
for p in l:
    if p[1] > 5:
        cls[0].append(p)
    else:
        cls[1].append(p)
diags = [[], []]
ind = 0
for cl in cls:
    mx_rast = 0
    for p1 in cl:
        for p2 in cl:
            if math.dist(p1, p2) > mx_rast:
                diags[ind] = [p1, p2]
                mx_rast = math.dist(p1, p2)
    ind += 1
Px = int((diags[0][0][0] + diags[0][1][0] + diags[1][0][0] + diags[1][1][0]) / 4 * 10000)
Py = int((diags[0][0][1] + diags[0][1][1] + diags[1][0][1] + diags[1][1][1]) / 4 * 10000)
print(Px, Py)