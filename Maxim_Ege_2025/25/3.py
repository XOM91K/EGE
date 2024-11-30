for x in range(0, 10 ** 9, 7777):
    if len(str(x)) == 9 and str(x)[-2:] == '77':
        d = str(x)
        d = d.replace('3', 'Н')
        d = d.replace('5', 'Н')
        d = d.replace('7', 'Н')
        d = d.replace('9', 'Н')
        d = d.replace('1', 'Н')
        d = d.replace('2', 'Ч')
        d = d.replace('4', 'Ч')
        d = d.replace('6', 'Ч')
        d = d.replace('8', 'Ч')
        d = d.replace('0', 'Ч')
        if d[:7] == 'ЧНЧЧНЧН':
            print(x, x // 7777)
