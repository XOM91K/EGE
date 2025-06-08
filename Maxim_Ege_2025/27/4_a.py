l = [[float(d.replace(',','.')) for d in x.split()] for x in open('4_a.txt')]
clusters = [[],[],[]]
for x in l:
    if x[0] < 1 and x[1] > 0:
        clusters[0].append(x)
    elif x[0] > 1:
        clusters[1].append(x)
    else:
        clusters[2].append(x)
centroids = [[],[],[]]
ind = 0
for x in clusters:
    srX = 0
    srY = 0
    for y in x:
        srX += y[0]
        srY += y[1]
    centroids[ind] = [srX / len(x), srY / len(x)]
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Px, Py)
