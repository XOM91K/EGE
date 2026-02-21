l=[int(x) for x in open('14.txt')]
ans=[]
d=min([x for x in l if x>0 and 999<x<10_000 and sum(map(int, str(x)))==21])
for x in range(len(l)-2):
    n1 = l[x]
    n2 = l[x + 1]
    n3 = l[x + 2]
    if (999<abs(n1)<10_000 and sum(map(int, str(abs(n1))))==15)+(999<abs(n2)<10_000 and sum(map(int, str(abs(n2))))==15)+(999<abs(n3)<10_000 and sum(map(int, str(abs(n3))))==15)==2:
        if 98*(n1+n2+n3)>=d**2:
            ans.append(n1+n2+n3)
print(len(ans), max(ans))