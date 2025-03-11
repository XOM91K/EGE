for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            #s = '1' * x + '2' * y + '3' * z
            # while '00' not in s:
            #     s = s.replace('01', '210', 1)
            #     s = s.replace('02', '31210', 1)
            #     s = s.replace('03', '22131210', 1)
            ct1 = x + 2 * y + 3 * z
            ct2 = x + y + 3 * z
            ct3 = y + z
            if ct1 == 56 and ct2 == 44 and ct3 == 19:
            #if s.count('1') == 56 and s.count('2') == 44 and s.count('3') == 19:
                print(x + y + z)