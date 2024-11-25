import itertools
ct = 0
for x in itertools.product('ЗИМА', repeat=5):
    x = ''.join(x)
    #if x[0] == 'З' or x[0] == 'М':
    if x[0] in 'ЗМ' and x[-1] in 'ИА':
        ct = ct + 1
print(ct)