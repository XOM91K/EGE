l = [[float(d.replace(',','.')) for d in x.split()] for x in open('2_b.txt')]
clusters = [[], [], []]
for x in l:
    if 21 <= x[1] <= 26 and 5 <= x[0] <= 20:
        clusters[0].append(x)
    elif 16 <= x[1] <= 21 and 5 <= x[0] <= 20:
        clusters[1].append(x)
    elif 4 <= x[1] <= 10 and 5 <= x[0] <= 20:
        clusters[2].append(x)
# for x in clusters:
#     print(len(x))
centroids = [[], [], []]
ind = 0
for x in clusters:
    mn_sm_rast = 10 ** 10
    for y in x:
        sm_rast = 0
        for z in x:
            sm_rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = y
    ind += 1
Px = int(abs((centroids[0][0] - centroids[2][0]) * 10000))
Py = int(abs((centroids[0][1] - centroids[2][1]) * 10000))
print(Px, Py)