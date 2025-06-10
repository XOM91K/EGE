import itertools
ct = 0
for x in itertools.product('ЗИМА', repeat = 5):
    x = ''.join(x)
    x = x.replace('И','@')
    x = x.replace('А','@')
    x = x.replace('З', '#')
    x = x.replace('М', '#')
    if x[0] == '#' and x[4] == '@':
        ct += 1
print(ct)


import itertools
ct = 0
for x in itertools.product('ЗИМА', repeat = 5):
    x = ''.join(x)
    if x[0] in 'ИА' and x[4] in 'ЗМ':
        ct += 1
print(ct)