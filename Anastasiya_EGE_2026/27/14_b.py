import math
l = [[float(d.replace(',','.')) for d in x.split()] for x in open('14_b.txt')]
clusters = [[], [], []]
for p in l:
    if 10 <= p[1] <= 30:
        if p[0] > 19:
            clusters[0].append(p)
        elif p[1] < 19:
            clusters[1].append(p)
        else:
            clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    sm_rust=10**10
    for centroid in cluster:
        rast=0
        for point in cluster:
            rast+=((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2)**0.5
        if rast<sm_rust:
            sm_rust=rast
            centroids[ind]=centroid
    ind+=1
ctB1 = 0
ctB2 = 0
for p in l:
    if math.dist(p, centroids[1]) <= 10:
        ctB1 += 1
for p in l:
    if math.dist(p, centroids[0]) > 5:
        ctB2 += 1
print(ctB1, ctB2 - 3)
# Q1 - количество точек всех кластеров, находящихся на
# расстоянии не более 10 от центра кластера с наибольшим
# количеством точек (включая сам центр), и Q2 -  количество
# точек всех кластеров, находящихся на
# расстоянии более 5 от центра кластера с наименьшим количеством точек.