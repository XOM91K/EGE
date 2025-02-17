import itertools
ct = 0
for x in itertools.product('ГАЛКТИ', repeat=8):
    x = ''.join(x)
    if x[0] in 'ГЛКТ' and x[-1] in 'АИ':
        if 'КЛ' not in x:
            ct += 1
print(ct)