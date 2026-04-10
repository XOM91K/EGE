import itertools
k=0
for x in itertools.product('РПОГА', repeat=5):
    x=''.join(x)
    k+=1
    if x.count('Г')==2 and 'ГГ' not in x:
        if x[0]!='Р':
            if x.count('О')==0 and x.count('А')==0:
                print(k,x)