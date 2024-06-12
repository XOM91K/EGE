for x in range(0, 100):
    for y in range(0, 100):
        for z in range(0, 100):
            #if (2 * x + 3 * y + z) == 18 and 2 * y + z == 13:
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in s:
                s = s.replace('01', '220', 1)
                s = s.replace('02', '122120', 1)
                s = s.replace('03', '120', 1)
            if s.count('1') == 13 and s.count('2') == 18:
                print(2 + x + y + z)
