import math
d = [[int(d) for d in x.split()] for x in open('5.txt')]
s = 6089572
k = 11
mn = 10 ** 10
smm = 10 ** 100
for i in range(13600, len(d)):
    sm = 0
    for j in range(len(d)):
        if abs(d[i][0] - d[j][0]) > s / 2:
            sm += (s % max(d[i][0], d[j][0]) + min(d[i][0], d[j][0])) * math.ceil(d[j][1] / k)
        else:
            sm += abs(d[i][0] - d[j][0]) * math.ceil(d[j][1] / k)
    if sm < smm:
        print(sm, '<<<<<<')
    else:
        print(sm, '>>>>>>')
    smm = sm
print(mn)
#799644142705
#799644133992