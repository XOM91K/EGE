import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('6_b.txt')]
cl = [[], [], []]
for p in l:
    if p[1] > 7:
        cl[0].append(p)
    elif p[1] < 2:
        cl[1].append(p)
    else:
        cl[2].append(p)
diags = [[], [], []]
ind = 0
for c in cl:
    mx_rast = 0
    for p1 in c:
        for p2 in c:
            if math.dist(p1, p2) > mx_rast:
                mx_rast = math.dist(p1, p2)
                diags[ind] = [p1, p2]
    ind += 1
print(diags)
Px = int((diags[0][0][0] + diags[0][1][0] + diags[1][0][0] + diags[1][1][0] + diags[2][0][0] + diags[2][1][0]) / 6 * 10000)
Py = int((diags[0][0][1] + diags[0][1][1] + diags[1][0][1] + diags[1][1][1] + diags[2][0][1] + diags[2][1][1]) / 6 * 10000)
print(Px, Py)