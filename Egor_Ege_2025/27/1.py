l = [[float(d.replace(',', '.')) for d in x.split()] for x in open('1.txt')]
# clusters = [[], [], []]
# for x in l:
#     if 1 <= x[0] <= 5:
#         clusters[0].append(x)
#     else:
#         clusters[1].append(x)
# centroids = [clusters[0][0], clusters[1][0]]
# ind = -1
# for x in clusters:
#     ind += 1
#     mx_sum_rast = 10 ** 10
#     for y in x:
#         sum_rast = 0
#         for z in x:
#             d = ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
#             sum_rast += d
#         if sum_rast < mx_sum_rast:
#             mx_sum_rast = sum_rast
#             centroids[ind] = y
# Px = int(((centroids[0][0] + centroids[1][0]) / 2) * 10000)
# Py = int(((centroids[0][1] + centroids[1][1]) / 2) * 10000)
# print(Px, Py)
clusters = [[], [], []]
for x in l:
    if -1 <= x[0] <= 3 and -1 <= x[1] <= 4:
        clusters[0].append(x)
    elif 5 <= x[0] <= 8:
        clusters[1].append(x)
    elif 2 <= x[0] <= 5 and 6 <= x[1] <= 12:
        clusters[2].append(x)
# centroids = [clusters[0][0], clusters[1][0]]
# ind = -1
# for x in clusters:
#     ind += 1
#     mx_sum_rast = 10 ** 10
#     for y in x:
#         sum_rast = 0
#         for z in x:
#             d = ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
#             sum_rast += d
#         if sum_rast < mx_sum_rast:
#             mx_sum_rast = sum_rast
#             centroids[ind] = y
# Px = int(((centroids[0][0] + centroids[1][0]) / 2) * 10000)
# Py = int(((centroids[0][1] + centroids[1][1]) / 2) * 10000)
# print(Px, Py)