import itertools
ct=0
for x in itertools.product('0123456789ABC', repeat=6):
    x=''.join(x)
    if x[0]!='0':
        if x.count('2')==1:
            if (x.count('A')+ x.count('B')+x.count('C'))<=4:
                ct+=1
print(ct)