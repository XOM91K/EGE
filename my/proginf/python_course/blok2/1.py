string = input("Введите числа через пробел:")
list_of_strings = string.split() # список строковых представлений чисел
print(list_of_strings)
# ['1', '2', '3', '4']
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел
print(list_of_numbers)
# [1, 2, 3, 4]
print(sum(list_of_numbers[::2])) # sum() вычисляет сумму элементов списка
# 5