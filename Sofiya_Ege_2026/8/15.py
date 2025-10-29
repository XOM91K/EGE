import itertools
ct=0
k=0
for x in itertools.product('калейдоскоп', repeat=6):
    x=''.join(x)
    if x[0]=='к':
        if x.count('й')
            ct+=1
print(ct)