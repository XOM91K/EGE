l=[int(x) for x in open('15.txt')]
ans=[]
d=min([x for x in l if x>0 if x%1000==102])
for x in range(len(l) - 2):
    for y in range(x + 1, len(l) - 1):
        for z in range(y + 1, len(l)):
            n1=l[x]
            n2=l[y]
            n3=l[z]
            if (9999<abs(n1)<100_000 and n1%3==0 and n1 > 0)+(9999<abs(n2)<100_000 and n2%3==0 and n2 > 0)+(9999<abs(n3)<100_000 and n3%3==0 and n3 > 0)==2:
                if (n1**2+n2**2+n3**2)%d==0:
                    ans.append((n1+n2+n3)/3)
print(len(ans), min(ans))