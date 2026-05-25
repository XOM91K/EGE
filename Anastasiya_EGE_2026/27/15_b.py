import math
l = [[d.replace(',','.') for d in x.split()] for x in open('15_b.txt')]
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], [], []]
for p in l:
    if p[1] > 22:
        clusters[0].append(p)
    elif p[0] > 20:
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
mn_rast = []
for p1 in clusters[0]:
    for p2 in clusters[1]:
        for p3 in clusters[2]:
            if p1[2] != 'VII' and p2[2] != 'VII' and int(p1[2][1]) >= 8 and int(p2[2][1]) >= 8:
                mn_rast.append(math.dist(p1[:2], p2[:2]))
            if p2[2] != 'VII' and p3[2] != 'VII' and int(p2[2][1]) >= 8 and int(p3[2][1]) >= 8:
                mn_rast.append(math.dist(p2[:2], p3[:2]))
            if p1[2] != 'VII' and p3[2] != 'VII' and int(p1[2][1]) >= 8 and int(p3[2][1]) >= 8:
                mn_rast.append(math.dist(p1[:2], p3[:2]))

mn_rast2 = []
for i in range(len(clusters[0]) - 1):
    for j in range(i + 1, len(clusters[0])):
        p1 = clusters[0][i]
        p2 = clusters[0][j]
        if p1[2] != 'VII' and p2[2] != 'VII' and int(p1[2][1]) >= 8 and int(p2[2][1]) >= 8:
            mn_rast2.append(math.dist(p1[:2], p2[:2]))
for i in range(len(clusters[1]) - 1):
    for j in range(i + 1, len(clusters[1])):
        p1 = clusters[1][i]
        p2 = clusters[1][j]
        if p1[2] != 'VII' and p2[2] != 'VII' and int(p1[2][1]) >= 8 and int(p2[2][1]) >= 8:
            mn_rast2.append(math.dist(p1[:2], p2[:2]))
for i in range(len(clusters[2]) - 1):
    for j in range(i + 1, len(clusters[2])):
        p1 = clusters[2][i]
        p2 = clusters[2][j]
        if p1[2] != 'VII' and p2[2] != 'VII' and int(p1[2][1]) >= 8 and int(p2[2][1]) >= 8:
            mn_rast2.append(math.dist(p1[:2], p2[:2]))
for p1 in clusters[0]:
    for p2 in clusters[1]:
        for p3 in clusters[2]:
            if p1[2] != 'VII' and p2[2] != 'VII' and int(p1[2][1]) >= 8 and int(p2[2][1]) >= 8:
                mn_rast.append(math.dist(p1[:2], p2[:2]))
            if p2[2] != 'VII' and p3[2] != 'VII' and int(p2[2][1]) >= 8 and int(p3[2][1]) >= 8:
                mn_rast.append(math.dist(p2[:2], p3[:2]))
            if p1[2] != 'VII' and p3[2] != 'VII' and int(p1[2][1]) >= 8 and int(p3[2][1]) >= 8:
                mn_rast.append(math.dist(p1[:2], p3[:2]))

print(int(min(mn_rast) * 10000),int((sum(mn_rast2) / len(mn_rast2)) * 10000))
# mn_rast = []
# for p in clusters[0]:
#     #print(p[2][0])
#     if p[2] == 'VII':
#         mn_rast.append(math.dist(centroids[0][:2], p[:2]))
# for p in clusters[1]:
#     #print(p[2][0])
#     if p[2] == 'VII':
#         mn_rast.append(math.dist(centroids[1][:2], p[:2]))
# print(int(min(mn_rast) * 10000), int(max(mn_rast) * 10000))