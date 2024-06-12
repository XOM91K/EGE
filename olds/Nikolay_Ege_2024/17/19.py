l=[int(x)for x in open('19.txt')]
print(l)
ln4=[]
mn25=[]
mx=0
ct=0
for y in l:
    if str(y)[-2:]=='25':
        mn25.append(y)

for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k >= 2 and (l[x]*l[x+1]*l[x+2]) <= min(mn25)**2:
        ct+=1
        mx=max(mx,l[x]*l[x+1]*l[x+2])
print(ct,mx)