import itertools
k = 0
l=[]
for x in itertools.product(sorted('ГРАНИТ'),repeat=6):
    x=''.join(x)
    k += 1
    if k % 2 !=0 and x[0]!='А' and x[0]!='И' and x[0]!='Г' and  x.count('А')==1 :
        l.append(k)
print(min(l))