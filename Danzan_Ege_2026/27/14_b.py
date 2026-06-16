import math

l = [x.replace(',', '.').split() for x in open('14_b.txt')]
l = [[float(d[0]), float(d[1]), d[2]] for d in l]
clusters = [[], [], []]
for p in l:
    if p[1] < 30:
        clusters[0].append(p)
    elif p[0] > 16:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:2], p2[:2])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
ct = [0, 0, 0]
for x in range(3):
    for p in clusters[x]:
        if p[2][:1] == 'K' and p[2][-3:] == 'III':
            ct[x] += 1
print(ct)
B1 = int(math.dist(centroids[1][:2], centroids[2][:2]) * 10000)


rast = []
for p1 in l:
    for p2 in l:
        if (p1[2][:1] == 'G' and p1[2][2:] == 'V') and (p2[2][:1] == 'G' and p2[2][2:] == 'V'):
            rast.append(math.dist(p1[:2], p2[:2]))
B2 = int(max(rast) * 10000)
print(B1, B2)