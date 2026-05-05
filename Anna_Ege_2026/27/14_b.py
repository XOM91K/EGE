# import math
# l = [[float(d.replace(',','.')) for d in x.split()] for x in open('14_b.txt')]
# clusters = [[], [], []]
# for p in l:
#     if p[1] > 22:
#         clusters[0].append(p)
#     elif p[0] > 24:
#         clusters[1].append(p)
#     else:
#         clusters[2].append(p)
# ind = 0
# centroids = [[], [], []]
# for cluster in clusters:
#     print(len(cluster))
#     mn_sm_rast = 10 ** 10
#     for p1 in cluster:
#         sm_rast = 0
#         for p2 in cluster:
#             sm_rast += math.dist(p1, p2)
#         if sm_rast < mn_sm_rast:
#             mn_sm_rast = sm_rast
#             centroids[ind] = p1
#     ind += 1
# print(centroids)
# ct = 0
# for p in clusters[0]:
#     if centroids[0][0] - 0.6 < p[0] < centroids[0][0] + 0.6 and centroids[0][1] - 0.6 < p[1] < centroids[0][1] + 0.6:
#         ct += 1
# print(ct, int(abs(centroids[1][1] - centroids[2][1]) * 10000))
# # ct = 0
# # for p in clusters[0]:
# #     if p[1] > centroids[0][1]:
# #         ct += 1
# # print(ct, int((centroids[0][0] - centroids[1][0]) * 10000))
# # 162
s = 0
for i in range(20):
    if i % 3 == 0 and i > 5:
        s = s + 2
print(s + 1)