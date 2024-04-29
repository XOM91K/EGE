from itertools import *
ct=0
for x in product('567', repeat=12):
    x=''.join(x)
    if '55' not in x and '555'not in x and '5555'not in x and '55555'not in x and '555555'not in x  and '5555555'not in x  and '55555555' not in x and '555555555'not in x:
        ct+=1
print(ct)