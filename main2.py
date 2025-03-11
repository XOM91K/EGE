import math


def count_numbers():
    # Первая цифра (наибольший разряд) может принимать значения 1, 2, 3, 4.
    first_digit_options = 4

    # Количество способов выбрать и упорядочить оставшиеся 7 цифр из оставшихся 14 цифр:
    rest_permutations = math.perm(14, 7)  # начиная с Python 3.8

    # Итоговое количество:
    return first_digit_options * rest_permutations


print(count_numbers())
