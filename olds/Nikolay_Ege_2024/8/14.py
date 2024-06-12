from itertools import *
k=0
ct=0
for x in product('агилмноф',repeat=5):
    x=''.join(x)
    k+=1
    if k%2!=0 and x[0]!='н' and x.count("о")<=1:
        ct+=1
print(ct)