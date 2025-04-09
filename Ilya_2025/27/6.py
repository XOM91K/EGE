a = [[float(i.replace(',','.')) for i in x.split()] for x in open('6.txt')]
clusters =[[],[]]
for i in range(len(a)):
    if a[i][1]<6:
        clusters[0].append(a[i])
    else:
        clusters[1].append(a[i])
centroids =[[],[]]
ind =0
for x in clusters:
    minn_rast =10**7
    coords =0
    for y in x:
        rast =0
        for z in x:
            rast+=((z[0]-y[0])**2 + (z[1]-y[1])**2)**0.5
        if minn_rast>rast:
            minn_rast =rast
            coords =y
            centroids[ind]=y
    ind+=1
Px = int((centroids[0][0]+centroids[1][0])/2*10000)
Py = int((centroids[0][1]+centroids[1][1])/2*10000)
print(abs(Px),abs(Py))


# a = [[float(i.replace(',','.')) for i in x.split()] for x in open('8.txt')]
# clusters =[[],[],[]]
# for i in range(len(a)):
#     if a[i][0]<0:
#         clusters[0].append(a[i])
#     elif a[i][1]>8:
#         clusters[1].append(a[i])
#     else:
#         clusters[2].append(a[i])
# centroids =[[],[],[]]
# ind =0
# for x in clusters:
#     minn_rast =10**7
#     coords =0
#     for y in x:
#         rast =0
#         for z in x:
#             rast+=((z[0]-y[0])**2 + (z[1]-y[1])**2)**0.5
#         if minn_rast>rast:
#             minn_rast =rast
#             coords =y
#     centroids[ind]=y
#     ind+=1
# Px = int((centroids[0][0]+centroids[1][0]+centroids[2][0])/3*10000)
# Py = int((centroids[0][1]+centroids[1][1]+centroids[2][1])/3*10000)
# print(Px,Py)