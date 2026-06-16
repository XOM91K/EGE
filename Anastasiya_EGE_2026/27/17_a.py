import math
l=[[d.replace(',','.') for d in x.split()] for x in open('17_a.txt')]
for p in range(len(l)):
    l[p]=[float(l[p][0]),float(l[p][1]),l[p][2]]
clusters=[[],[]]
for p in l:
    if p[1]>15:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
anti=[[],[]]
ind=0
for x in clusters:
    print(len(x))
    mx_rast=0
    for y in x:
        rast=0
        for z in x:
            rast+=math.dist(y[:-1],z[:-1])
        if rast > mx_rast:
            mx_sm_rast = rast
            anti[ind] = y
    ind+=1
print(anti)
mn=[]

for p in clusters[1]:
    if p != anti[1]:
        mn.append(math.dist(p[:-1],anti[1][:-1]))
print(int((sum(mn) / len(mn)) * 10000))