from itertools import *
k=0
for x in product('воздух',repeat=5):
    x=''.join(x)
    if x.count('о')==x.count('у')==1 and 'во'not in x and 'ов'not in x and 'ув'not in x and 'ву'not in x and 'ох'not in x and 'хо'not in x and 'ух'not in x and 'ху'not in x :
        k+=1
        print(x)
print(k)