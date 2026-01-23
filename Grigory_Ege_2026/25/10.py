for x in range(7777, 10 ** 9, 7777):
    if str(x)[-2:] == '77':
        s = str(x)
        s = s.replace('2', '0')
        s = s.replace('4', '0')
        s = s.replace('6', '0')
        s = s.replace('8', '0')
        s = s.replace('3', '1')
        s = s.replace('5', '1')
        s = s.replace('7', '1')
        s = s.replace('9', '1')
        if s == '010010111':
            print(x, x // 7777)