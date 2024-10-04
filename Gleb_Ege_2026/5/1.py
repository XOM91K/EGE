for x in range(287, 1000):
    x = str(x)
    c1 = int(x[0]) * int(x[1])
    c2 = int(x[1]) * int(x[2])
    if max(c1, c2) == 20 and min(c1, c2) == 5:
        print(x)
# import random
# g = random.randint(1, 10)
# d = int(input('Введите число: '))
# if d == g:
#     print('Вы угадали число')
# else:
#     print('Вы не угадали :(')