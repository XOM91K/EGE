import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('12_b.txt')]
clusters = [[], [], []]
for p in l:
    if -15 <= p[0] <= -5 and 2 <= p[1] <= 10:
        clusters[0].append(p)
    elif 2 <= p[1] <= 10 and 1 <= p[0] <= 8:
        clusters[1].append(p)
    elif -14 <= p[0] <= -7 and -15 <= p[1] <= -7:
        clusters[2].append(p)
mx_sm_rast1 = 0
tochka1 = []
tochka2 = []
tochka3 = []
for c in clusters:
    print(len(c))
for p1 in clusters[0]:
    for p2 in clusters[1]:
        if math.dist(p1, p2) > mx_sm_rast1:
            mx_sm_rast1 = math.dist(p1, p2)
            tochka1 = [p1, p2]
mx_sm_rast2 = 0
for p1 in clusters[1]:
    for p2 in clusters[2]:
        if math.dist(p1, p2) > mx_sm_rast2:
            mx_sm_rast2 = math.dist(p1, p2)
            tochka2 = [p1, p2]
mx_sm_rast3 = 0
for p1 in clusters[0]:
    for p2 in clusters[2]:
        if math.dist(p1, p2) > mx_sm_rast3:
            mx_sm_rast3 = math.dist(p1, p2)
            tochka3 = [p1, p2]
mx_rast = 0
for p in clusters[2]:
    mx_rast = max(mx_rast, math.dist(p, [2, 2]))
print(int((mx_sm_rast1 + mx_sm_rast2 + mx_sm_rast3) * 100))
print(int(mx_rast * 100))