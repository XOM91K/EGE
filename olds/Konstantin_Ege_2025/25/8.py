for x in range(7777, 10 ** 9, 7777):
    if x % 100 == 77 and len(str(x)) == 9:
        s = str(x)
        s = s.replace('0', 'Ч')
        s = s.replace('2', 'Ч')
        s = s.replace('4', 'Ч')
        s = s.replace('6', 'Ч')
        s = s.replace('8', 'Ч')
        s = s.replace('1', 'Н')
        s = s.replace('3', 'Н')
        s = s.replace('5', 'Н')
        s = s.replace('7', 'Н')
        s = s.replace('9', 'Н')
        if s[:7] == 'ЧНЧЧНЧН':
            print(x, x // 7777)