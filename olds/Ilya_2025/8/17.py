import itertools
ct=0
for x in itertools.product('012345', repeat=3):
    x=''.join(x)
    if x.count('5')==1 and '05' not in x and '50' not in x and '25' not in x and '45' not in x and '52' not in x and '54' not in x and x[0]!='0':
        ct+=1
print(ct)