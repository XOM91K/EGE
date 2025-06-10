a = [[float(j.replace(',','.')) for j in i.split()]for i in open("5_b.txt")]
clusters = [[], [], [], [], []]
for i in a:
    if i[0] < -1.5 and i[1] > 0:
        clusters[0].append(i)
    elif i[0] < -1.5 and i[1] < 0:
        clusters[1].append(i)
    elif i[1] > 4 / 5 * i[0]:
        clusters[2].append(i)
    elif i[1] < -5 / 7 * i[0]:
        clusters[3].append(i)
    else:
        clusters[4].append(i)
ind = 0
centroids = [[], [], [], [], []]
for i in clusters:
    x1 = 0
    y1 = 0
    k = 0
    for j in i:
        x1 += j[0]
        y1 += j[1]
        k += 1
    centroids[ind] = [x1 / k, y1 / k]
    ind += 1
print(centroids)
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0]) / 5 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1]) / 5 * 10000)
print(abs(Px), abs(Py))