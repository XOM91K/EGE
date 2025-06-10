for n in range(4, 10001):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    #Найти максимальную сумму цифр
    if sum(map(int, s)) > 41:
        print(sum(map(int, s)))