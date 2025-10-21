l=[int(x) for x in open('1')]
d=[]
for x in range(len(l)):
    if l[x]%3==0 and l[x]%7!=0 and l[x]%17!=0 and l[x]%19!=0 and l[x]%27!=0:
                d.append(l[x])
print(len(d), max(d))