import itertools
ct = 0
for x in set(itertools.product('ДЕВИАЦИЯ', repeat = 8)):
    x = ''.join(x)
    if ( x[0] in 'ЕИАЯ' ) and ( x[-1] == 'Д' or x[-1] == 'В' or x[-1] == 'Ц'):
        if 'ДЕ' in x:
            ct = ct + 1
print(ct)