for one in range(1, 100):
    for two in range(1, 100):
        for dre in range(1, 100):
            s = '0' + '1'*one + '2'* two + '3'* dre + '0'
            while '00' not in s:
                s= s.replace('01', '103', 1)
                s= s.replace('02', '2011', 1)
                s = s.replace('03', '130', 1)
            o = s.count('1')
            d = s.count('2')
            t = s.count('3')
            if o == 92 and d == 16 and t == 52:
                print(dre)