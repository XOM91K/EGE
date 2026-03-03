l=[[int(d)for d in x.split()]for x in open('20.txt')]
ct=0
for x in l:
    k = 0
    if x[0]!=min(x) and x[0]!=max(x) and x[-1]!=min(x) and x[-1]!=max(x):
        k += 1
    x=sorted(x)
    povt=[a for a in x if x.count(a)>1]
    if x[-1] not in povt:
        k += 1
    if (x[-1]*x[-2]*x[-3])%x[0]==0:
        k += 1
    if k == 1:
        ct+=1
print(ct)