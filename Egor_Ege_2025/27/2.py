# l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('2.txt')]
# clusters = [[], []]
# for x in l:
#     if -4 <= x[1] <= 4:
#         clusters[0].append(x)
#     else:
#         clusters[1].append(x)
# centroids = [clusters[0][0], clusters[1][0]]
# print(centroids)
# ind = 0
# for x in clusters:
#     mn_sm_rast = 10 ** 10
#     for y in x:
#         sm_rast = 0
#         for z in x:
#             sm_rast += ((z[0] - y[0]) ** 2 + (z[1] - y[1]) ** 2) ** 0.5
#         if sm_rast < mn_sm_rast:
#             centroids[ind] = y
#             mn_sm_rast = sm_rast
#     ind += 1
# Px = abs(int((centroids[0][0] + centroids[1][0]) / 2 * 10000))
# Py = abs(int((centroids[0][1] + centroids[1][1]) / 2 * 10000))
# print(Px, Py)


l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('2_b.txt')]
clusters = [[], [], []]
for x in l:
    if -6 <= x[0] <= -1:
        clusters[0].append(x)
    elif x[1] < 8:
        clusters[1].append(x)
    elif x[1] >= 8:
        clusters[2].append(x)
centroids = [[], [], []]
ind = 0
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += ((z[0] - y[0]) ** 2 + (z[1] - y[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            centroids[ind] = y
            mn_sm_rast = sm_rast
    ind += 1
Px = abs(int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000))
Py = abs(int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000))
print(Px, Py)