import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_b.txt')]
ctr = [[2, 7], [7, 0], [2, -7]]
clusters = [[], [], [], [], []]

for p in l:
    if p[0] < -1.8 and p[1] > 0:
        clusters[0].append(p)
    elif p[0] < -1.8 and p[1] < 0:
        clusters[1].append(p)
    else:
        mn = 10 ** 10
        inds = 0
        for i in range(len(ctr)):
            dst = math.dist(p, ctr[i])
            if dst < mn:
                mn = dst
                inds = i
        clusters[inds + 2].append(p)

centroids = [[], [], [], [], []]
ind = 0
for cl in clusters:
    print(len(cl))
    srX = 0
    srY = 0
    for p in cl:
        srX += p[0]
        srY += p[1]
    srX = srX / len(cl)
    srY = srY / len(cl)
    centroids[ind] = [srX, srY]
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0]) / 5 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1]) / 5 * 10000))
print(Px, Py)