l=[int(x)for x in open('5.txt')]
# print(l)
ct=0
mn=10**10
mx5=[]
for y in l:
    if len(str(abs(y)))==5 and str(y)[-2:]=='17':
        mx5.append(y)
print(max(mx5))
for x in range(len(l)-2):
    if (str(l[x])[-2:]=='17' or str(l[x+1])[-2:]=='17' or str(l[x+2])[-2:]=='17') and (abs(l[x])+abs(l[x+1])+abs(l[x+2]))<=max(mx5):
        ct+=1
        mn=min(mn,l[x]+l[x+1]+l[x+2])
print(ct,mn)
