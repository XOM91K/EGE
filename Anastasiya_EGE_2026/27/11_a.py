import math
l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('11_a.txt')]
cls = [[], []]
for x in l:
    if x[1] > 5:
        cls[0].append(x)
    else:
        cls[1].append(x)
diags = [[], []]
ind = 0
for cl in cls:
    mx_sm_rast = 0
    for p1 in cl:
        for p2 in cl:
            if math.dist(p1, p2) > mx_sm_rast:
                mx_sm_rast = math.dist(p1, p2)
                diags[ind] = [p1, p2]
    ind += 1
Px = int((diags[0][0][0] + diags[0][1][0] + diags[1][0][0] + diags[1][1][0]) / 4 * 10000)
Py = int((diags[0][0][1] + diags[0][1][1] + diags[1][0][1] + diags[1][1][1]) / 4 * 10000)
print(Px, Py)