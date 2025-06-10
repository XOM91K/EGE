s = open(r'C:\Users\Zarif\Downloads\24_12476 (2).txt').readline()
s = s.replace('ORO', 'O RO').replace('ROR', 'RO R').split(' ')
mx_ln = 0
for x in s:
    x = x.split('RO')
    if len(x) < 22:
        continue

    for y in x:
#№ 12476 PRO100 ЕГЭ 29.12.23 (Уровень: Сложный)
print(s)