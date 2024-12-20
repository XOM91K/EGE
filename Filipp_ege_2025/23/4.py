def f(x, y, flag): #флаг, количество вычитаний подряд
    if str(x)[-1] == "3" or '11' in flag or x > 89:
        return 0
    elif x == y:
        return 1
    else:
        return f(x - 1, y, flag + '1') + f(x - 5, y, flag + '1') + f(x + 7, y, flag + '3') + f(2 * x, y, flag + '4')

print(f(9, 60, '') * f(60, 84, ''))