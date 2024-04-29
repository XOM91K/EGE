for n in range(101):
    s = '3' * n
    while '333' in s:
        s = s.replace('333', '4', 1)
        s = s.replace('4444', '3', 1)
    if s == '43':
        print(n)