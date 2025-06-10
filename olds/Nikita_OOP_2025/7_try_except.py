import random
for x in range(10):
    y = int(input())
    if y == 0:
        raise ArithmeticError("ноль не вводи !")
    d = random.randint(-3, 3)
    try:
        if y % d == 0:
            print(f'Ваше число {y} кратно зарандомленному {d}')
        else:
            print(f'Ваше число {y} не кратно зарандомленному {d}')
    except:
        raise "ЗероДивижинЕрор: вы пытаетесь делить на ноль)))000"
