#Кольцевая дорога
import math
mn = 10 ** 10
l = [[int(d) for d in x.split()] for x in open('4.txt')]
K = 8244
for i in range(len(l)):
    sm = 0
    for j in range(len(l)):
        if abs(l[i][0] - l[j][0]) > K / 2:
            sm += abs(K - abs(l[i][0] - l[j][0])) * math.ceil(l[j][1] / 11)
        else:
            sm += abs(l[i][0] - l[j][0]) * math.ceil(l[j][1] / 11)
    print(i, sm)
    mn = min(mn, sm)
print(mn)