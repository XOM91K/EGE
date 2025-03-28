for n in range(4, 100):
    s = '2' + '5' * n
    while '25' in s or '35' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '53', 1)
        if '35' in s:
            s = s.replace('35', '2', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)
    if sum([int(x) for x in s]) % 7 == 0:
        print(n)
#s = '5523'
#print(s.count('2') * 2 + s.count('5') * 5 + s.count('3') * 3)
#s = '1289316249812641904612904162201461401232543567576'
#print(sum([int(x) for x in s]))
#print(s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9)
# d = []
# for x in range(1, 6):
#     d.append(x)
# print(d)
# print([x for x in range(1, 6)])
#от 2 до 40
#print([x for x in range(2, 41)])
#сгенерировать список, с нечетными числами от 1 до 100, кратные 5
#print([x for x in range(1, 101) if x % 5 == 0 and x % 2 != 0])
#s = '589'
#print(sum([int(x) for x in s]))