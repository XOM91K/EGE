import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('7_b.txt')]
clusters = [[], [], []]
for p in l:
    if p[1] > 7:
        clusters[0].append(p)
    elif p[1] > 3:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
ind = 0
diagonals = [[[], []], [[], []], [[], []]]
for cluster in clusters:
    mx_rast = 0
    for p1 in cluster:
        for p2 in cluster:
            if math.dist(p1, p2) > mx_rast:
                mx_rast = math.dist(p1, p2)
                diagonals[ind] = [p1, p2]
    ind += 1
Px = int((diagonals[0][0][0] + diagonals[0][1][0] + diagonals[1][0][0] + diagonals[1][1][0] + diagonals[2][0][0] + diagonals[2][1][0]) / 6 * 10000)
Py = int((diagonals[0][0][1] + diagonals[0][1][1] + diagonals[1][0][1] + diagonals[1][1][1] + diagonals[2][0][1] + diagonals[2][1][1]) / 6 * 10000)
print(Px, Py)
