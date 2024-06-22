a = 1
mn = 10 ** 10
mx = 0
while a != 99999:
    a = int(input())
    if -10000 <= a <= 10000 or a == 99999:
        if abs(a) % 10 == 8:
            if a < mn:
                mn = a
            if a > mx:
                mx = a
    else:
        print('Вы ввели не то число :)))')
        break
else:
    print(mn, mx)