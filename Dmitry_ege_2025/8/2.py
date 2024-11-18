import itertools
ct = 0
for x in itertools.product('567', repeat=12):
    x = ''.join(x)
    if '55' not in x:
        ct = ct + 1
print(ct)
# s = 'ПЕТЯ'
# if 'Т' in s:
#     print('Есть')
# s = 'ГОРБУШКА'
# if 'БУШ' in s:
#     print('Есть')
# s = 'ГОРБУШКА'
# if s[3] in 'ОУА':
#     print('Гласная')
# else:
#     print('Согласная')
# s = 'ГОРУБШКА'
# if 'РУБ' not in s:
#     print('Нету')