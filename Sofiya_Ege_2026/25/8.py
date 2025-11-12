import fnmatch
for x in range(7777,10**9,7777):
    if x % 100 == 77:
        s = str(x)
        for d in '02468':
            s = s.replace(d, 'Ч')
        for d in '13579':
            s = s.replace(d, 'Н')
        if s == 'ЧНЧЧНЧННН':
            print(x, x//7777)