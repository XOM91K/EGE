l=[[int(d) for d in x.split()]for x in open('26.txt')]
l=sorted(l)
sl={}

d=[]
for x in l:
    if x[0] not in sl:
        sl[x[0]]=[]
    sl[x[0]].append(x[1])
print(sl)
for x in sl:
    ct = 1
    #print(x, sl[x][0])
    for y in range(len(sl[x])-1):
        if sl[x][y+1]-sl[x][y] == 1:
            ct += 1
            d.append((x, ct))
        else:
            ct = 1
print(sorted(d, key=lambda r: (-r[1], -r[0]))[0])