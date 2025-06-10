import itertools
ct = 0
for x in itertools.product('ОБЩЕСТВ', repeat=5):
    x = ''.join(x)
    if x[0] != 'Щ' and x[0] != 'Б':
        if x[4] == 'В' and x[3] == 'В':
            if 'ЕВ' not in x and 'ЕВ' not in x and 'ТБ' in x:
                ct += 1
print(ct)