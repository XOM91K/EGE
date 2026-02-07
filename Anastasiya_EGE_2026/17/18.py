l=[int(x) for x in open('18.txt')]
mx=[]
ok3=len([x for x in l if len(str(abs(x)))==4 and str(x)[-1]=='3'])
for x in range(len(l)-2):
    if ((sorted([l[x],l[x+1],l[x+2]]))[-1] + (sorted([l[x],l[x+1],l[x+2]]))[-2]) > ok3**2:
        mx.append(l[x]+l[x+1]+l[x+2])
print(len(mx), max(mx))