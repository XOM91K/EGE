l = [[float(d.replace(',','.')) for d in x.split()] for x in open('1_a.txt')]
clusters = [[], []]
for point in l:
    if point[1] > 3:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids = [[], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for star in cluster:
            sm_rast += ((centroid[0] - star[0]) ** 2 + (centroid[1] - star[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
for centroid in centroids:
    print(centroid)
print(int((2.67836329019008 + -0.530720837096502) / 2 * 10000), int((4.82882470874288 + 1.31719050307274) / 2 * 10000))
print()