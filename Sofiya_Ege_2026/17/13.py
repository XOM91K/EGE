l=[int(x) for x in open('13.txt')]
d=max([x for x in l if x%100==17])
ans=[]
for x in range(len(l)-2):
    n1=l[x]
    n2=l[x+1]
    n3=l[x+2]
    if ((999<n1<10000)+(999<n2<10000)+(999<n3<10000))==2:
        if ((n1%5==0)+(n2%5==0)+(n3%5==0))>=1:
            if (n1+n2+n3)>d:
                ans.append(n1+n2+n3)
print(len(ans), max(ans))