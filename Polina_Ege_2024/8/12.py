import itertools
ct = 0
for x in itertools.product('БАНДЕРОЛЬ',repeat = 7):
     x = ''.join(x)
     if x.count('Ь') <= 1:
         if 'ЕБ ' not in x and 'БЕ' not in x and 'НЕ' not in x and 'ЕН' not in x and 'ДЕ' not in x and  'ЕД' not in x and 'РЕ' not in x and 'ЕР' not in x and 'ЛЕ' not in x and 'ЕЛ' not in x :
            ct+=1
print(ct)