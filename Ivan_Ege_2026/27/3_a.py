l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('3_a.txt')]
clusters = [[], []]
for point in l:
    if point[1]>90:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
# в нулевом кластере звезд меньше
centroids = [[], []]
ind = 0
for cluster in clusters:
    minsumr = 99999999
    for centroid in cluster:
        sumr = 0
        for point in cluster:
            sumr += ((centroid[0]-point[0])**2+(centroid[1]-point[1])**2)**0.5
        if sumr < minsumr:
            minsumr = sumr
            centroids[ind] = centroid
    ind += 1
p1 = abs(int((centroids[0][0] + centroids[0][1])*10000))
p2 = abs(int((centroids[1][0] + centroids[1][1])*10000))
print(p1, p2)