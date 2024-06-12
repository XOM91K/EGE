from itertools import *
k=0
ct=0
for x in product('соткаегэ',repeat=6):
    k+=1
    x=''.join(x)
    if x[0]!='а' and x[-1]!='э'and x.count('т')==1:
        ct+=1
print(ct)
