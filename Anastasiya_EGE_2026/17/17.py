l=[int(x) for x in open('17.txt')]
k=0
mx=[]
sr=[x for x in l if x>0]
sr = sum(sr)/len(sr)
for x in range(len(l)-2):
    if max([l[x], l[x + 1], l[x + 2]]) - min([l[x], l[x + 1], l[x + 2]])<sr:
        k+=1
        mx.append(l[x]+l[x+1]+l[x+2])
print(k,max(mx))