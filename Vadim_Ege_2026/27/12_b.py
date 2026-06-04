import math
l = [x.replace(',','.').split() for x in open('12_b.txt')]
l = [[float(d[0]), float(d[1]), d[2]] for d in l]
clusters = [[], [], []]
for p in l:
    if p[1] > 22:
        clusters[0].append(p)
    elif p[0] > 22:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
ind = 0
centroids = [[], [], []]
for cluster in clusters:
    #print(len(cluster))
    mn_sm_rast = 10 ** 10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid[:-1], point[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
mn_rast = []
for p1 in clusters[0]:
    for p2 in clusters[1]:
        if p1[2][1].isdigit() and int(p1[2][1]) >= 8 and p2[2][1].isdigit() and int(p2[2][1]) >= 8:
            mn_rast.append(math.dist(p1[:-1], p2[:-1]))
for p1 in clusters[0]:
    for p2 in clusters[2]:
        if p1[2][1].isdigit() and int(p1[2][1]) >= 8 and p2[2][1].isdigit() and int(p2[2][1]) >= 8:
            mn_rast.append(math.dist(p1[:-1], p2[:-1]))
for p1 in clusters[1]:
    for p2 in clusters[2]:
        if p1[2][1].isdigit() and int(p1[2][1]) >= 8 and p2[2][1].isdigit() and int(p2[2][1]) >= 8:
            mn_rast.append(math.dist(p1[:-1], p2[:-1]))
sr_rast = []
for x in range(3):
    for p1 in clusters[x]:
        for p2 in clusters[x]:
            if p1 != p2 and p1[2][1].isdigit() and int(p1[2][1]) >= 8 and p2[2][1].isdigit() and int(p2[2][1]) >= 8:
                sr_rast.append(math.dist(p1[:-1], p2[:-1]))
sr_rast = sum(sr_rast) / len(sr_rast)
print(int(min(mn_rast) * 10000), int(sr_rast * 10000))

# mn_rast = []
# for x in range(2):
#     for p in clusters[x]:
#         if centroids[x] != p:
#             if p[2] == 'VII':
#                mn_rast.append(math.dist(p[:-1], centroids[x][:-1]))
# print(int(min(mn_rast) * 10000), int(max(mn_rast) * 10000))