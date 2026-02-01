import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_a.txt')]
clusters = [[], []]
for x in l:
    if x[1] > 5:
        clusters[0].append(x)
    else:
        clusters[1].append(x)
diags = [0, 0]
ind = 0
for cluster in clusters:
    mx_rast = 0
    for p1 in cluster:
        for p2 in cluster:
            if math.dist(p1, p2) > mx_rast:
                mx_rast = math.dist(p1, p2)
                diags[ind] = [p1, p2]
    ind += 1
Px = int((diags[0][0][0] + diags[0][1][0] + diags[1][0][0] + diags[1][1][0]) / 4 * 10000)
Py = int((diags[0][0][1] + diags[0][1][1] + diags[1][0][1] + diags[1][1][1]) / 4 * 10000)
print(Px, Py)