l=[int(x)for x in open('10.txt')]
ct=0
k=0
srar=0
for x in l:
    if str(x)[-2]=='28':
        k+=1
        srar=sum(x)/k
for x in range (len(l)-2):
    if len(str(abs(l[x])))==4 or len(str(abs(l[x+1])))==4 or len(str(abs(l[x+2])))==4:
        if (str(l[x])[-2:]=='11' and str(l[x + 1])[-2:]=='11' and str(l[x + 2])[-2:])!='11') and str(l[x+1][-2])=='11') or (str(l[x][-2])=='11' and str(l[x+2][-2])=='11'):
            if l[x]>srar and l[x+1]>srar and l[x+2]>srar:
                ct+=1
print(ct)