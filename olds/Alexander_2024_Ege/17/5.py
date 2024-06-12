def dvuh(x,y):
    if (((len(str(x))==2) and (len(str(y))!=2))) or (((len(str(x))!=2) and (len(str(y))==2))):
        return x+y
    else:
        return 0
mn=10**10
mx=-10**9
c=0
f=[int(x) for x in open('5.txt')]
for i in range(len(f)-1):
    mx=max(mx,dvuh(f[i],f[i+1]))

for y in range(len(f)):
    if f[y]>mx:
        c+=1
        mn=min(mn,f[y])
print(c)
print(mn)