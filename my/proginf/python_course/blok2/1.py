# string = input("Введите числа через пробел:")
# list_of_strings = string.split() # список строковых представлений чисел
# print(list_of_strings)
# # ['1', '2', '3', '4']
# list_of_numbers = list(map(int, list_of_strings)) # cписок чисел
# print(list_of_numbers)
# # [1, 2, 3, 4]
# print(sum(list_of_numbers[::2])) # sum() вычисляет сумму элементов списка
# # # 5
# l = [
#     "Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов",
#     "Васильев", "Попов", "Новиков", "Федоров", "Морозов",
#     "Волков", "Алексеев", "Лебедев", "Семенов", "Егоров",
#     "Павлов", "Козлов", "Степанов", "Николаев", "Орлов",
#     "Иванов", "Андреев", "Макаров", "Никитин", "Захаров",
#     "Смирнов", "Кузнецов", "Соколов", "Белов", "Петров"
# ]
#
# a = {1, 'b', 'd'}
# print(a) # {'b', 1, 'd'}
# a.add(10) # {'d', 1, 10, 'b'}
# a.remove('b') # {'d', 1, 10}

# abons = {"Иванов", "Петров", "Васильев", "Антонов"}
# print(abons[0])
# # TypeError: 'set' object is not subscriptable
#
# person = {} # с помощью фигурных скобок можно создать словарь
# # словарь заполняется по принципу - ключ:объект (через двоеточие)
# person = {'name' : 'Ivan Petrov'}
# # в него можно также добавлять новые объекты по ключу
# person['age'] = 25
# person['email'] = 'ivan_petrov@example.com'
# person['phone'] = '8(800)222-20-20'
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)222-20-20'}
# print(person['email'])
# # ivan_petrov@example.com
# print(person['address'])
# # KeyError: 'address'
# print(person.keys())
# # dict_keys(['name', 'age', 'email', 'phone'])
# print(person.values())
# # dict_values(['Ivan Petrov', 25, 'ivan_petrov@example.com', '8(800)555-35-35'])
#
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
# person.pop('phone')
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com'}
# print(not True)
# # False
# print(not False)
# # True

# можно проверить, находится ли число 1 в промежутке (0,4)
# cond1 = 0 < 1
# cond2 = 1 < 4
# print(cond1 and cond2)
# # True
# # или, например, содержат ли две строки один и тот же символ
# cond3 = 't' in "python"
# cond4 = 't' in "django"
# print(cond3 and cond4)
# # False
#
# # к слову, логические выражения можно сразу объединять в одно целое
# print(('t' in "python") or ('t' in "django"))
# # True
#
# print('5' in str(123456789))
# # True
# '3' in str(N) and '7' in str(N)
#
#
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a == b)  # True
# print(a is b)  # False
#
#
# is_rainy = True  # дождь будет
#
# if is_rainy:
#     print("Брать зонт")
# else:
#     print("Не брать зонт")
#
# is_rainy = True  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     # в данный блок дописали ещё один условный оператор
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")
#
# if A % 3 == 0:
#     print('Число А кратно 3')
# if A % 2 == 0 or A % 3 == 0:
#     print('Число А кратно 2 или 3')
#
# if a == 10:
#     print('a равно 10')
# elif a < 10:
#     print('a меньше 10')
# else:
#     print('a больше 10')
#
# # хорошо
# month in [3, 4, 5]
# # плохо
# month == 3 or month == 4 or month == 5
#
# month = int(input())
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")
#
# a = 42
# b = 41
# result = a if a > b else b
#
# for value in iterator:
#     # Начало блока кода с телом цикла
#     ...
#     ...
#     ...
#     # Конец блока кода с телом цикла
# # Код, который будет выполняться после цикла
#
# print(list(range(5)))
# # [0, 1, 2, 3, 4]
# print(list(range(1, 5)))
# # [1, 2, 3, 4]
# print(list(range(1, 10, 2)))
# # [1, 3, 5, 7, 9]
#
# S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
# N = 5
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)
#
# while условие:
#     # Начало блока кода с телом цикла
#     # пока условие истинно, цикл выполняется
#     ...
#     ...
#     ...
#     # Конец блока кода с телом цикла
# # Код, который будет выполняться после цикла
#
# S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
#
# # заводим цикл while, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счётчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n)
#
# # плохо
# n = 1
# while n < 10:  # в данной программе это условие всегда True, цикл будет бесконечным
#     print("Hello World")
# # хорошо
# n = 1
# while True:  # в данной программе это условие всегда True, цикл будет бесконечным
#    print("Hello World")
#    n += 1
#    if n > 10:  # условие, при достижении которого цикл while будет принудительно завершён
#        break
#
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# N = 2
# M = 3
# # заполнили матрицу последовательными числами
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
# for i in range(N):  # цикл, отвечающий за строки
#     for j in range(M):  # цикл, отвечающий за столбцы
#         print(matrix[i][j], end=" ")
# # 0 1 2 3 4 5
#
# for i in range(N):
#     for j in range(M):
#         print(matrix[i][j], end=" ")
#     print()  # перенос на новую строку
#
# # 0 1 2
# # 3 4 5
# while True:
#     if n % 3 == 0:
#          n = n // 3
#          if n == 1:
#               break
#     else:
#          break
#
# num = 7
#
# # Классический if-else
# if num % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")
# # Тернарный условный оператор
# result = "Чётное" if num % 2 == 0 else "Нечётное"
# print(result)
# text = "А роза упала на лапу Азора"
# # Удаляем пробелы и приводим к нижнему регистру
# cleaned_text = text.replace(" ", "").lower()
# # арозаупаланалапуазора
# # Классический if-else
# if cleaned_text == cleaned_text[::-1]:
#     print("Это палиндром!")
# else:
#     print("Не палиндром")
# # Тернарный оператор
# result = "Палиндром" if cleaned_text == cleaned_text[::-1] else "Не палиндром"
# print(result)


# N = 6
# a = [x ** 2 for x in range(1, N)]
# print(a)
# [1, 4, 9, 16, 25, 36]

#

# N = 10
# a = [0.5*x+1 for x in range(N)]
# # [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]

# d_input = input("Введите целые числа через пробел: ")
# a = [d for d in d_input.split()]
# # ['1', '2', '3', '4']
# print(a)
# d_input = list(map(int, input("Целые числа через пробел: ").split()))
#
# d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
# a = ["четное" if x % 2 == 0 else "нечетное" for x in d]
# # ['четное', 'нечетное', 'нечетное', 'четное', 'четное', 'нечетное', 'четное', 'четное', 'нечетное']
# print(a)
# def name_func():
#     # начало тела функции
#     ...
#     # конец тела функции
#
# # Проверяем числа 7, 10, 13, 17, 21 на простоту
#
# # Проверка для 7
# num = 7
# is_prime = True
# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
# print(f"Число {num}: {'простое' if is_prime else 'не простое'}")
#
# # Проверка для 10
# num = 10
# is_prime = True
# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
# print(f"Число {num}: {'простое' if is_prime else 'не простое'}")
#
# # Проверка для 13
# num = 13
# is_prime = True
# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
# print(f"Число {num}: {'простое' if is_prime else 'не простое'}")
#
# def is_prime(num):
#     """Проверяет, является ли число простым."""
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# # Проверяем числа 7, 10, 13, 17, 21
# numbers = [7, 10, 13, 17, 21]
#
# for num in numbers:
#     print(f"Число {num}: {'простое' if is_prime(num) else 'не простое'}")
#
# # функция, которая возводит любое число в квадрат
# # def pow_func(base):
# #    print(base ** 2)
# # pow_func(3)  # 9
# # pow_func(5)  # 25
# # pow_func()
# # # TypeError: pow_func() missing 1 required positional argument: 'base'

# # функция, которая возводит любое число в степень n
# def pow_func(base, n=2):
#    print(base ** n)
# pow_func(3)  # 9
# pow_func(5, 3)  # 125
# def pow_func(base, n=2):
#    print(base ** n)
#
# print(pow_func(3))
# # 9
# # None
#
# def pow_func(base, n=2):
#     inside_result = base ** n
#     return inside_result
#
# print(pow_func(3))
# # 9
#
# outside_result = pow_func(3)
# print(outside_result)
# # 9
#
# def pow_func(base, n=2):
#    inside_result = base ** n
#    return inside_result
#
# print(inside_result)
# # ----> 5 print(inside_result)
# #       6 # 9
# #
# # # NameError: name 'inside_result' is not defined
#
# def local():
#    x = 5  # локальная переменная
#    print(x)
# x = 10
# local()
# print(x)
# # 5
# # 10
#
# def local():
#   print(x)  # так как x нет в локальной области видимости, мы берём её из глобальной области
#
# x = 10
# local()
# print(x)
#
# # 10
# # 10

# x = 3
# def func():
#    global x
#    print(x)
#    x = 5
#    x += 5
#    return x
# print(func())
# # 3
# # 10
# # UnboundLocalError: local variable 'x' referenced before assignment
# d = input() # 1 2 3 4 5
# d = d.split() # ['1', '2', '3', '4']
# d = map(int, d) # <map object at 0x000001B3BAFE53A0>
# print(sum(d)) # 15
# d = list(d)
# print(d)
#
# d = list(map(int, input().split())) # 1 2 3 4 5
# # [1, 2, 3, 4, 5]
# print(sum(d)) # 15
#
# def func(a, b, c):
#    print('a =', a)
#    print('b =', b)
#    print('c =', c)
#
# func(1, 2, 3)
# # a = 1
# # b = 2
# # c = 3
#
# func(3, 2, 1)
# # a = 3
# # b = 2
# # c = 1
# # Правильно
# func(1, 2, c=3)
#
# # Неправильно
# func(a=1, 2, 3)
# func(a=1, b=2, c=3)
# # a = 1
# # b = 2
# # c = 3
#
# func(c=3, b=2, a=1)
# # a = 1
# # b = 2
# # c = 3
# # Правильно
# func(a, b, c=3)
# # Неправильно
# func(a=1, b, c)
# # SyntaxError: positional argument follows keyword argument
# print(1)
# print(1, 2)
# print(1, 2, 3)
# ...
#
# # 1
# # 1 2
# # 1 2 3
# # ...
#
# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)
# # [[1, 2, 3], 4, 5, 6]
#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
# # [1, 2, 3, 4, 5, 6]
# print(a) # [1, 2, 3]
# print(*a)  # 1 2 3

def my_func(*args, **kwargs):
   print(type(args), args, '---', tuple(args))
   print(type(kwargs), kwargs, '---', tuple(kwargs))
my_func(1, 2, 3, color='red', param=6)
#<class 'tuple'> (1, 2, 3) --- (1, 2, 3)
#<class 'dict'> {'color': 'red', 'param': 6} --- ('color', 'param')
def is_positive(number):
   return number > 0
