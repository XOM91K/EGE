l = [[float(d.replace(',','.')) for d in x.split()] for x in open('4_a.txt')]
clusters = [[],[],[]]
for x in l:
    if x[1] > 0:
        clusters[0].append(x)
    elif x[0] > 2:
        clusters[1].append(x)
    elif x[0] < 2:
        clusters[2].append(x)
corners = [[],[]]
for x in clusters:
    print(len(x))
del clusters[2]
ind = 0
for x in clusters:
    mx_sm_rast = 0
    for y in x:
        sm_rast = 0
        for z in x:
            rast = ((y[0]-z[0])**2+(y[1]-z[1])**2)**0.5
            sm_rast+=rast
        if sm_rast > mx_sm_rast:
            mx_sm_rast = sm_rast
            corners[ind] = y
    ind+=1
#print(corners)
Tx = (corners[0][0]+corners[1][0])/2*10000
Ty = (corners[0][1]+corners[1][1])/2*10000
print(int(Tx),int(Ty))