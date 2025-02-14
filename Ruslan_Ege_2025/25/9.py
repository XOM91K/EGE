for x in range(7777, 10 ** 9 + 1, 7777):
    s = str(x)
    if s[-2:] == '77':
        s = s.replace('0', 'Ч')
        s = s.replace('2', 'Ч')
        s = s.replace('4', 'Ч')
        s = s.replace('6', 'Ч')
        s = s.replace('8', 'Ч')
        s = s.replace('1', 'Н')
        s = s.replace('3', 'Н')
        s = s.replace('5', 'Н')
        s = s.replace('7', 'Н')
        s = s.replace('9', 'Н')
        if s == 'ЧНЧЧНЧННН':
            print(x, x // 7777)
print('---')
# for c in '02468':
#     for n in '13579':
#         x = c + n + c + c + n + c + n + '77'
#         print(x)
#         x = int(x)
#         if x % 7777 == 0:
#             print(x, x / 7777)
from itertools import *
for c in product('02468', repeat=4):
    c = ''.join(c)
    for n in product('13579', repeat=3):
        n = ''.join(n)
        chislo = c[0] + n[0] + c[1] + c[2] + n[1] + c[3] + n[2] + '77'
        if int(chislo) % 7777 == 0:
            if chislo[0] != '0':
                print(chislo, int(chislo) // 7777)
