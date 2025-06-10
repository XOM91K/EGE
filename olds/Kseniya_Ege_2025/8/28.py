import itertools
ct = 0
for x in set(itertools.product('ГАЛАКТИКА', repeat=8)):
    x = ''.join(x)
    if x[0] in 'ГЛКТ' and x[-1] in 'АО':
        if 'КЛ' not in x:
            ct += 1
print(ct)
