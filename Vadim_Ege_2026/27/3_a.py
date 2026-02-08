l = [[float(d.replace(',','.')) for d in x.split()] for x in open('3_a.txt')]
clusters = [[], [], []]
for p in l:
    if p[0] > 1:
        clusters[0].append(p)
    elif p[1] > 0:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cl in clusters:
    srX = 0
    srY = 0
    for p in cl:
        srX += p[0]
        srY += p[1]
    srX = srX / len(cl)
    srY = srY / len(cl)
    centroids[ind] = [srX, srY]
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Px, Py)