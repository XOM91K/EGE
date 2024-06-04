for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in s:
                s = s.replace('01', '103', 1)
                s = s.replace('02', '2011', 1)
                s = s.replace('03', '130', 1)
                if s.count('1') == 92 and s.count('2') == 16 and s.count('3') == 52:
                    print(z)
