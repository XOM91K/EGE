for x in range(7777, 10 ** 9, 7777):
    s = str(x)
    if s[-2:] == '77':
        s = s.replace('1', 'Н')
        s = s.replace('3', 'Н')
        s = s.replace('5', 'Н')
        s = s.replace('7', 'Н')
        s = s.replace('9', 'Н')
        s = s.replace('0', 'Ч')
        s = s.replace('2', 'Ч')
        s = s.replace('4', 'Ч')
        s = s.replace('6', 'Ч')
        s = s.replace('8', 'Ч')
        if s == 'ЧНЧЧНЧННН':
            print(x, x // 7777)