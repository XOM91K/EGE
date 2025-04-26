import itertools
ct = 0
for x in itertools.permutations('ДЕВИАЦИЯ'): #АВДЕИЦЯ
    x = ''.join(x)
    if 'АВ' in x or 'ВД' in x or 'ДЕ' in x or 'ЕИ' in x or 'ИЦ' in x or 'ЦЯ' in x:
        x = x.replace('А', '%')
        x = x.replace('Е', '%')
        x = x.replace('И', '%')
        x = x.replace('Я', '%')
        x = x.replace('Д', '№')
        x = x.replace('В', '№')
        x = x.replace('Ц', '№')
        if x[0] == '%' and x[-1] == '№':
            ct += 1
print(ct)