import itertools
#iteration tools
n = 0
for x in itertools.product('ЗИМА', repeat=5):
    x = ''.join(x)
    if x[0] in 'ЗМ' and x[-1] in 'ИА':
        n += 1
print(n)
