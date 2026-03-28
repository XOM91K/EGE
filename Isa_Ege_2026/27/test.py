# for cluster in clusters:
#     mn_sm_rast = 10 ** 10
#     for p1 in cluster:
#         sm_rast = 0
#         for p2 in cluster:
#             sm_rast += ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
#         if sm_rast < mn_sm_rast:
#             mn_sm_rast = sm_rast
#             centroids[ind] = p1
#     ind += 1