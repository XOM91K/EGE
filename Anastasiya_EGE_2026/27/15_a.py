import math
l = [[d.replace(',','.') for d in x.split()] for x in open('15_a.txt')]
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], []]
for p in l:
    if p[1] > 10:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
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
mn_rast = []
for p in clusters[0]:
    #print(p[2][0])
    if p[2] == 'VII':
        mn_rast.append(math.dist(centroids[0][:2], p[:2]))
for p in clusters[1]:
    #print(p[2][0])
    if p[2] == 'VII':
        mn_rast.append(math.dist(centroids[1][:2], p[:2]))
print(int(min(mn_rast) * 10000), int(max(mn_rast) * 10000))