from random import *
k = 0
while k != 5:
    a = randint(1, 10)
    b = randint(1, 10)
    znak = choice('+-*')
    print(a, znak, b, '=')
    c = int(input())
    if eval(str(a)+znak+str(b)) == c:
        print('Вы ответили ВЕРНО!')
        k += 1
        if k == 5:
            print('Тест окончен!')
    else:
        print('Вы ответили НЕВЕРНО!')
        k = 0