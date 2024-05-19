for x in range(7777, 10 ** 9 + 1, 7777):
    if str(x)[-2:] == '77':
        d = str(x)
        d = d.replace('0', 'Ч')
        d = d.replace('2', 'Ч')
        d = d.replace('4', 'Ч')
        d = d.replace('6', 'Ч')
        d = d.replace('8', 'Ч')
        d = d.replace('1', 'Н')
        d = d.replace('3', 'Н')
        d = d.replace('5', 'Н')
        d = d.replace('7', 'Н')
        d = d.replace('9', 'Н')
        if d == 'ЧНЧЧНЧННН':
            print(x, x // 7777)
