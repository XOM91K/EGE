for x in range(7777, 10 ** 9, 7777):
    s = str(x)
    if s[-2:] == '77':
        for y in '02468':
            s = s.replace(y, 'Ч')
        for y in '13579':
            s = s.replace(y, 'Н')
        if s == 'ЧНЧЧНЧННН':
            print(x, x // 7777)