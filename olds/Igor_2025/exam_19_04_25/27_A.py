f = [[float(a) for a in x.split()] for x in open('27_A.txt').readlines()]

clusters = [[], []]
centroids = [[[], 10**10], [[], 10**10]]

for x in f:
    if x[1] < -1:
        clusters[0].append(x)
    else:
        clusters[1].append(x)

for i in range(len(clusters)):
    for centr in clusters[i]:
        sm_rast = 0
        for star in clusters[i]:
            rast = ((centr[0]-star[0])**2 + (centr[1]-star[1])**2)**0.5
            sm_rast += rast
        if centroids[i][1] > sm_rast:
            centroids[i][0] = centr
            centroids[i][1] = sm_rast

Px = abs(int(sum(x[0][0] for x in centroids) / 2 * 10_000))
Py = abs(int(sum(x[0][1] for x in centroids) / 2 * 10_000))

print(Px, Py)