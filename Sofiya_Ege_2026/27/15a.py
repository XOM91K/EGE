l=[[float(d.replace(',', '.'))for d in x.split()]for x in open('15a.txt')]
clusters=[[],[],[]]
for point in l:
    if point[1]>5:
        clusters[0].append(point)
    elif point[0]<2:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
print(len(clusters[0]),len(clusters[1]),len(clusters[2]))
cray=[[],[],[]]
ind=0
from math import *
from random import *
from turtle import *
tochka = 0
def min_kray(cl1, cl2):
    mn_rast = 10 ** 10
    tochka = 0
    for p1 in cl1:
        for p2 in cl2:
            r1 = dist(p1, p2)
            if r1 < mn_rast:
                mn_rast = r1
                tochka = p1
    return (mn_rast, tochka)
print(min_kray(clusters[0], clusters[1]), min_kray(clusters[0], clusters[2]))
print(min_kray(clusters[1], clusters[2]), min_kray(clusters[1], clusters[0]))
print(min_kray(clusters[2], clusters[0]), min_kray(clusters[2], clusters[1]))
# [4.401297, 6.064333]
# [1.121883, 1.560516]
# [4.541109, 4.52741]
print( int((4.401297 + 1.121883 + 4.541109 + 2.295715 + 0.985094 + 3.628501) /6  * 10000))
print( int((6.021642 + 6.064333 + 1.560516 + 2.967868 + 4.52741 + 1.667381) /6  * 10000))
# Px=int(((cray[0][0]+cray[1][0]+cray[2][0] + cray[0][0]+cray[1][0]+cray[2][0])/3)*10_000)
# Py=int(((cray[0][1]+cray[1][1]+cray[2][1] + cray[0][0]+cray[1][0]+cray[2][0])/3)*10_000)
# print(Px, Py)
# # tracer(0)
# up()
# for cluster in clusters:
#     color=random(), random(), random()
#     for x, y in cluster:
#         goto(x*30, y*30)
#         dot(5, color)
# update()
# done()


