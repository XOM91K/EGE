l=[int(d) for d in open('8.txt')]
mx7=max([d for d in l if str(d)[-1]=='7'])
sr=[]
mx=[]
for x in range(len(l)-2):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if k == 2:
        k = 0
        if l[x] > mx7:
            k += 1
        if l[x + 1] > mx7:
            k += 1
        if l[x + 2] > mx7:
            k += 1
        if k == 1:
            sr.append(l[x])
            sr.append(l[x + 1])
            sr.append(l[x + 2])
            mx.append(l[x]+l[x+1]+l[x+2])
print(len(mx), sum(set(sr))/len(set(sr)))