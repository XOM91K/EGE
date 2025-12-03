import itertools
ct=0
for x in itertools.product('0123456789abcdef', repeat=8):
    x=''.join(x)
    if x.count('0')==2:
        if (x.count('a')+x.count('b')+x.count('c')+x.count('d')+x.count('e')+x.count('f'))<=4:
            ct+=1
print(ct)