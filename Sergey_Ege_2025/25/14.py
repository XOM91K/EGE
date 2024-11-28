for x in range(7777, 10 ** 9, 7777):
    if len(str(x)) == 9 and str(x)[-2:] == '77':
        d = str(x)
        for y in '02468':
            d = d.replace(y, 'Ч')
        for y in '13579':
            d = d.replace(y, 'Н')
        if d[:-2] == 'ЧНЧЧНЧН':
            print(x, x // 7777)
