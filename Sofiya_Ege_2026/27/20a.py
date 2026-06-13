import math
l = [[float(d) for d in x.split()]for x in open('20a.txt')]
bls = [[1, 1, 2], [20, 20, 3]]
clusters = [[0, 0], [0, 0]]
for p in l:
    for x in range(len(bls)):
        R = bls[x][-1]
        d = math.dist(bls[x][:2], p)
        if R <= d <= 3 * R:
            clusters[x][0] += d - R
            clusters[x][1] += 1
print(clusters)
print(int((clusters[0][0] / clusters[0][1]) * 1000), int((clusters[1][0] / clusters[1][1]) * 1000))