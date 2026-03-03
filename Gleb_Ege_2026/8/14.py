import itertools
ct = 0
for x in itertools.product('ГАЛТИК', repeat=8):
    x = ''.join(x)
    if 'КЛ' not in x:
        if x[0] in 'ГЛКТ' and x[-1] in 'АИ':
            ct += 1
print(ct)