from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


def count_unique_strings_with_periods(a, b, c):
    # Находим наименьшее общее кратное для a и b
    period_ab = lcm(a, b)

    # Находим наибольший общий делитель для НОК(a,b) и c
    common_period = gcd(period_ab, c)

    # Если общий период равен 1, нет общего периода с c
    if common_period == 1:
        return 2 ** period_ab
    else:
        # Вычитаем количество строк с общим периодом
        return 2 ** period_ab - 2 ** common_period


# Пример использования функции
a = 6
b = 3
c = 2
print(count_unique_strings_with_periods(a, b, c))