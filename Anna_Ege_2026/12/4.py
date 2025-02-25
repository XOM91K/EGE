for n in range(1, 100):
    s = '3' + '9' * n + '5' * n
    while '39' in s or '35' in s or '555' in s:
        if '39' in s:
            s = s.replace('39', '55', 1)
        if '35' in s:
            s = s.replace('35', '9', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    if sum(map(int, s)) % len(s) == n:
        print(n)
# s = '1289361239186294'
# print(s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9)
# print(sum(map(int, s)))