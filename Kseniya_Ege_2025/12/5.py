for n in range(0, 100):
    s = '3' + '9' * n + '5' * n
    while '39' in s or '35' in s or '555' in s:
        if '39' in s:
            s = s.replace('39', '55', 1)
        if '35' in s:
            s = s.replace('35', '9', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    #if (sum(s) % len(s) == 1) == n == t == 0 == 2:
    #3359  - сумма цифр: 20
    if (s.count('5') * 5 + s.count('3') * 3 + s.count('9') * 9) % len(s) == n:
        print(n)
# 5, 5, 5, 2, 2, 4, 4