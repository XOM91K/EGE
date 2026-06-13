l=[[int(d) for d in x.split()]for x in open('32.txt')]
for x in range(len(l)):
    l[x].append(l[x][0]+l[x][1])
l=sorted(l,key=lambda d: d[2])

print(l)
berem=[l[0]]
print(berem)
for x in range(1,len(l)):
    if l[x][0]>=berem[-1][2]:
        berem.append(l[x])
for x in l:
    print(x)
print(berem[-3:])
print(len(berem))