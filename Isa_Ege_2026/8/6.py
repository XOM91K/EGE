import itertools
ct=0
for x in itertools.product(set('ГАЛАКТИКА'), repeat=8):
    x=''.join(x)
    if x[0] in 'ГЛКТ' and 'КЛ' not in x and x[-1] in 'АИ':
        ct+=1
print(ct)