s = open('1.tt', encoding='utf-8').read().upper()
ct = 0
for x in 'АЕЁИОУЫЭЮЯ':
    ct += s.count(x)
print(ct)