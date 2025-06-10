for x in '0123456789abcde':
    a = int('67845' + x + '65', 15)
    b = int('1' + x + '23456', 15)
    if (a + b) % 14 == 0:
        print((a + b) // 14)