import math

l = [[d.replace(',', '.') for d in x.split()] for x in open('16_b.txt')]
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], [], []]
for p in l:
    if p[1] > 22:
        clusters[0].append(p)
    elif p[0] > 22:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centr = [[], [], []]
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
ct_S = [0, 0, 0]
for x in range(3):
    for p in clusters[x]:
        if p[2][0] == 'L':
            ct_S[x] += 1
            print(p)
    print('---------------')
mx_rast = []
print(ct_S)
for p1 in clusters[0]:
    for p2 in clusters[1]:
        if p1[2][0] == 'L' and p2[2][0] == 'L':
            mx_rast.append(math.dist(p1[:-1], p2[:-1]))
for p1 in clusters[0]:
    for p2 in clusters[2]:
        if p1[2][0] == 'L'and p2[2][0] == 'L':
            mx_rast.append(math.dist(p1[:-1], p2[:-1]))
for p1 in clusters[2]:
    for p2 in clusters[1]:
        if p1[2][0] == 'L' and p2[2][0] == 'L':
            mx_rast.append(math.dist(p1[:-1], p2[:-1]))
print(int(math.dist(centr[0][:-1], centr[1][:-1]) * 10000), int(max(mx_rast) * 10000))
# m = []
# for p in clusters[1]:
#     # print(p)
#     if p[2][0] == 'L' and p[2][1] == '3':
#         # print(p[2])
#         m.append(math.dist(centr[0][:2], p[:2]))
# l = []
# for p in clusters[0]:
#     # print(p)
#     if p[2][0] == 'L' and p[2][1] == '3':
#         # print(p[2])
#         l.append(math.dist(centr[1][:2], p[:2]))
# print((int(max(m) * 10000)), int(max(l) * 10000))
