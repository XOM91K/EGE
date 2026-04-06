l=[int(x) for x in open('19.txt')]
ans=[]
d=[x for x in l if 999<abs(x)<10000 and x%17==0]
for x in range(len(l)-2):
    n1=l[x]
    n2=l[x+1]
    n3=l[x+2]
    if (str(n1)[0]==str(n1)[-1])+(str(n2)[0]==str(n2)[-1])+(str(n3)[0]==str(n3)[-1])==1:
        if (9999 < abs(n1) < 100000 and (str(n1)[1]=='7')) + (9999 < abs(n2) < 100000 and (str(n2)[1]=='7')) + (9999 < abs(n3) < 100000 and (str(n3)[1]=='7')) ==2:
            ans.append(max(n1,n2,n3))
print(len(ans), sum(ans))# 54384