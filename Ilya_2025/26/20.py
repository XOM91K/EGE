a  =[int(i) for i in open(r'20.txt')]
st = set(a)
ct=0
maxx=0
nech= sorted([x for x in a if x%2!=0])
for i in range(len(nech) - 1):
    for j in range(i + 1, len(nech)):
        zn = (nech[i]+nech[j])//2
        if zn in st:
            ct+=1
            maxx=max(maxx, zn)
print(ct, maxx)