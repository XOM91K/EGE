for n in range(1, 100):
    s = '9' + '1' * n + '2' * n
    while '91' in s or '92' in s:
        if '91' in s:
            s = s.replace('91', '39', 1)
        if '92' in s:
            s = s.replace('92', '59', 1)
    sm = s.count('3') * 3 + s.count('5') * 5 + s.count('9') * 9
    if len(str(sm)) == 3:
        print(n, sm)