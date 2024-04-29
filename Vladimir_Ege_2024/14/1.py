for x in ('0123456789abcde'):
    c1 = int('67845' + '65', 15)
    c2 = int('1' + '23456', 15)
    summa = c1 + c2
    if summa % 14 == 0:
        print(summa // 14)