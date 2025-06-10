a = int(input())
sm = 0
pr = 1
c1 = a // 100
c2 = a // 10 % 10
c3 = a % 10
if len(str(abs(c1 + c2 + c3))) == 2:
    print('а) Является')
else:
    print('а) Не является')
if len(str(abs(c1 * c2 * c3))) == 3:
    print('б) Является')
else:
    print('б) Не является')