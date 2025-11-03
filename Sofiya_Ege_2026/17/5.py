a=[int(x) for x in open('5.txt')]
d=min([x for x in a if x%2==0])
ans=[]
for x in range(len(a)-2):
    n1=a[x]
    n2=a[x+2]
    if ((n1%2==0) and (n2%2!=0)) or ((n2%2==0) and (n1%2!=0)):
        if a[x + 1] % d == 0:
            ans.append(n1+n2)
print(len(ans), min(ans))