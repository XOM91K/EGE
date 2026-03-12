l=[int(d) for d in open('31')]
mx=[]
for x in range(len(l)-1):
    for y in range(x+1, len(l)):
        k=0
        if (l[x]+l[y])%18==0:
            k+=1
        if (l[x]*l[y])%18==0:
            k+=1
        if k==1:
            mx.append(l[x]+l[y])
print(len(mx), max(mx))