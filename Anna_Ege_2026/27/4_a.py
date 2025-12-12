# l = [[float(d.replace(',','.')) for d in x.split()] for x in open('1174a')]
# clusters = [[], [], [],[]]
# for x in l:
#     if x[1] > 14:
#         clusters[0].append(x)
#     elif x[1] < 4:
#         clusters[1].append(x)
#     elif x[0] > 15:
#         clusters[2].append(x)
#     else:
#         clusters[3].append(x)
# centroids = [[], [], [], []]
# ind = 0
# for x in clusters:
#     mn_sm_rast = 10 ** 10
#     for y in x:
#         rast = 0
#         for z in x:
#             rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
#         if rast < mn_sm_rast:
#             mn_sm_rast = rast
#             centroids[ind] = y
#     ind += 1
# Px = (int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] ) / 4 * 10000))
# Py = (int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1]) / 4 * 10000))
# print(Px, Py)

l = [[float(d.replace(',','.')) for d in x.split()] for x in open('4_a.txt')]
clusters = [[], [], [],[],[]]
for x in l:
    if x[1] > 10:
        clusters[0].append(x)
    elif x[0] < 7 and x[1] < 4:
        clusters[1].append(x)
    elif 5< x[1] < 8:
        clusters[2].append(x)
    elif 23< x[0] < 28 and x[1] <5:
        clusters[3].append(x)
    elif x[0] > 29 and x[1]<4:
        clusters[4].append(x)
centroids = [[], [], [], [],[]]
ind = 0
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        rast = 0
        for z in x:
            rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
        if rast < mn_sm_rast:
            mn_sm_rast = rast
            centroids[ind] = y
    ind += 1
Px = (int((centroids[0][0] + centroids[1][0] + centroids[2][0] + centroids[3][0] + centroids[4][0]) / 5 * 10000))
Py = (int((centroids[0][1] + centroids[1][1] + centroids[2][1] + centroids[3][1] + centroids[4][1])/ 5 * 10000))
print(Px, Py)