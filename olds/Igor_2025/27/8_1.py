l = [[float(d) for d in x.split()] for x in open('8_1.txt')]
clusters = [[], [], []]
for x in l:
    if -2 <= x[0] <= 0.5:
        clusters[0].append(x)
    elif 0.5 <= x[0] <= 3:
        clusters[1].append(x)
    elif 3.5 <= x[0] <= 7:
        clusters[2].append(x)
# print(len(clusters[0]))
# print(len(clusters[1]))
# print(len(clusters[2]))
del clusters[0]
centroids = [[clusters[0][0], 0], [clusters[1][0], 0]]
print(centroids)
i = 0
for x in clusters:
    mx_sm = 10 ** 10
    for y in x:
        radius = 0
        sm_rast = 0
        for z in x:
            rast = ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
            sm_rast += rast
            radius = max(radius, rast)
        if sm_rast < mx_sm:
            mx_sm = sm_rast
            centroids[i] = [y, radius]
    i += 1
print(int(((centroids[0][1] + centroids[1][1]) / 2) * 10000))