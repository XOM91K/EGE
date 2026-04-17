import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('7_a.txt')]
clusters = [[], []]
for p in l:
    if p[1] > 6:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
ind = 0
diagonals = [[[], []], [[], []]]
for cluster in clusters:
    mx_rast = 0
    for p1 in cluster:
        for p2 in cluster:
            if math.dist(p1, p2) > mx_rast:
                mx_rast = math.dist(p1, p2)
                diagonals[ind] = [p1, p2]
    ind += 1
print(diagonals)
Px = int((diagonals[0][0][0] + diagonals[0][1][0] + diagonals[1][0][0] + diagonals[1][1][0]) / 4 * 10000)
Py = int((diagonals[0][0][1] + diagonals[0][1][1] + diagonals[1][0][1] + diagonals[1][1][1]) / 4 * 10000)
print(Px, Py)
