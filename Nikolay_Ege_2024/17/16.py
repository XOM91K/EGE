l=[int(x)for x in open('16.txt')]
mx=0
a=[]
ct=0
for y in l:
    if str(y)[-2:]=='25':
        a.append(y)
print(min(a))

for x in range(len(l)-2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k >= 2:
        if (l[x]*l[x+1]*l[x+2])<=min(a)**2:
            ct+=1
            mx=max(mx,l[x]*l[x+1]*l[x+2])
print(ct,mx)