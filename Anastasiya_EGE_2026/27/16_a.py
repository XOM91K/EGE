import math

l = [[d.replace(',', '.') for d in x.split()] for x in open('16_a.txt')]
# print(len(l))
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], []]
for p in l:
    if p[1] > 10:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centr = [[], []]
ind = 0
for x in clusters:
    print(len(x))
    mn_rast = 10 ** 10
    for y in x:
        rast = 0
        for z in x:
            rast += math.dist(y[:2], z[:2])
        if rast < mn_rast:
            mn_rast = rast
            centr[ind] = y
    ind += 1
m = []
for p in clusters[1]:
    # print(p)
    if p[2][0] == 'L' and p[2][1] == '3':
        # print(p[2])
        m.append(math.dist(centr[0][:2], p[:2]))
l = []
for p in clusters[0]:
    # print(p)
    if p[2][0] == 'L' and p[2][1] == '3':
        # print(p[2])
        l.append(math.dist(centr[1][:2], p[:2]))
print((int(max(m) * 10000)), int(max(l) * 10000))
