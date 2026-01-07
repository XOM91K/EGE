import itertools
ct=0
for x in itertools.product('012345', repeat=3):
    x = ''.join(x)
    print(x)
    x = x.replace('4', '2')
    if x.count('5')==1 and x[0] != '0' and '50' not in x and '52' not in x and '25' not in x and '05' not in x:
        ct+=1
print(ct)