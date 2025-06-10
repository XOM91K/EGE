import itertools
ct = 0
for x in set(itertools.product('ДЕВИАЦИЯ', repeat=8)): #АВДЕИЦЯ
    x = ''.join(x)
    if 'ДЕ' in x:
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