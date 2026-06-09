l=[[d for d in x.split()]for x in open('19_a.txt')]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(',', '.')), float(l[x][1].replace(',', '.')), l[x][2]]
clusters=[[],[]]
for point in l:
    if point[1]>10:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
z1=0
for p in clusters[0]:
    if p[-1][0]=='Z':
        z1+=1
z2=0
for p in clusters[1]:
    if p[-1][0]=='Z':
        z2+=1

print(min(z1,z2),max(z1,z2))