import math
l = [[d for d in x.split()] for x in open('6_b.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',','.')), float(l[x][1].replace(',','.')), l[x][2]]
clusters = [[], [], []]
for p in l:
    if p[1] > 22:
        clusters[0].append(p)
    elif p[1] < 15:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    #print(len(cluster))
    mn_sm_rast = 10 ** 10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
# Z I
mn = []
for cluster in clusters:
    for p1 in cluster:
        for p2 in cluster:
            if p1 != p2:
                if p1[-1][0] == 'Z' and p1[-1][2:] == 'I' and p2[-1][0] == 'Z' and p2[-1][2:] == 'I':
                    mn.append(math.dist(p1[:-1], p2[:-1]))
B1 = int(min(mn) * 10000)
ct_Jeltiy_Sverhgigant = [0, 0, 0]
ind = 0
for cluster in clusters:
    for p in cluster:
        if p[-1][0] == 'Z' and p[-1][2:] == 'I':
            ct_Jeltiy_Sverhgigant[ind] += 1
    ind += 1
print(ct_Jeltiy_Sverhgigant)
B2 = int(math.dist(centroids[1][:-1], centroids[2][:-1]) * 10000)
print(B1, B2)












# mn = []
# for p in l:
#     if p[-1][0] == 'Y' and p[-1][2:] == 'III':
#         mn.append(math.dist(centroids[0][:-1], p[:-1]))
# A1 = int(min(mn) * 10000)
# A2 = int(max(mn) * 10000)
# print(A1, A2)
# # mx = []
# # for p in l:
# #     if p[-1][0] == 'Y' and p[-1][2:] == 'III':
# #         mx.append(math.dist(centroids[0][:-1], p[:-1]))
# # A1 = int(min(mn) * 10000)
# # A2 = int(max(mx) * 10000)
# # print(A1, A2)