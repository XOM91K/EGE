l=[int(x)for x in open('12.txt')]
ct=0
k=0
mn = 10 ** 10
sr = [x for x in l if str(x)[-2:] == '28']
sr = sum(sr) / len(sr)
for x in range (len(l)-2):
    if len(str(abs(l[x])))==4 or len(str(abs(l[x+1])))==4 or len(str(abs(l[x+2])))==4:
        if (str(l[x])[-2:]=='11' and str(l[x+1])[-2:]=='11' and str(l[x+2])[-2:]!='11') or (str(l[x])[-2:]=='11' and str(l[x+1])[-2:]!='11' and str(l[x+2])[-2:]=='11') or (str(l[x])[-2:]!='11' and str(l[x+1])[-2:]=='11' and str(l[x+2])[-2:]=='11'):
            if l[x]>sr and l[x+1]>sr and l[x+2]>sr:
                ct+=1
                mn =min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct,mn)