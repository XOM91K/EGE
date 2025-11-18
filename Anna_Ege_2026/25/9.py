for x in range(7777, 10**9, 7777):
    if str(x)[-2:] == '77':
        s = str(x)
        for y in '02468':
            s = s.replace(y, 'Ч')
        for y in '13579':
            s = s.replace(y, 'Н')
        if s == 'ЧНЧЧНЧННН':
            print(x, x//7777)