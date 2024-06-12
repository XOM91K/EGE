from itertools import *
k=0
for x in product('апрсу',repeat=5):
    x=''.join(x)
    k+=1
    if x.count('у')<=1 and 'аа' not in x:
        print(k,x)
        break