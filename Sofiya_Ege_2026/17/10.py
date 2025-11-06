a=[int(x) for x in open('10.txt')]
d=max([x for x in a if abs(x)%10==7])
ans=[]
ct = 0
for x in range(len(a)-2):
    n1=a[x]
    n2=a[x+1]
    n3=a[x+2]
    if (n1%2!=0)+(n2%2!=0)+(n3%2!=0)==2:
        if (n1>d)+(n2>d)+(n3>d)==1:
            ans.append(n1)
            ans.append(n2)
            ans.append(n3)
            ct += 1
ans = set(ans)
ans = sum(ans) / len(ans)
print(ct, ans)