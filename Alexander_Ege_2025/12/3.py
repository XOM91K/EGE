#https://examinf.ru/tasks/901
for n in range(4, 10000):
    s = '5' + '2' * n
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
             s = s.replace('72', '2', 1)
        if '522' in s:
             s = s.replace('522', '27', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
    if sum(map(int, s)) == 22:
        print(n)
# s = '8123891237298217321093732980136239021321093693223' # 13
# print(s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9)
# print(sum(map(int, s)))