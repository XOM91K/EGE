for x in '0123456789abcde':
    s1 = int('67845' + x + '65', 15)
    s2 = int('1' + x + '23456', 15)
    if (s1 + s2) % 14 == 0:
        print((s1 + s2) // 14)