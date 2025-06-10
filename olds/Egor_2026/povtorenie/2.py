a = 1
ct = 0
mn = 10 ** 10
mx = 0

while a != -1:
    a = int(input())
    if -10000 <= a <= 10000:
        if a ** 2 % 10 == 5 or a % 6 == 0:
            if a < mn:
                mn = a
            if a > mx:
                mx = a
            ct += 1
    else:
        print('Вы ввели неверное число')
        break
else:
    print(ct, mn, mx)