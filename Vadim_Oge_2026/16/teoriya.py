# d = 574 #int
# print(d % 10)
# print(d // 100)
# print(d // 10 % 10)
# s = '574' #str
# print(s[0]) # взять элемент по индексу
# print(s[1])
# print(s[2])
# print(s[0] + s[1])
# print(int(s[0]) + int(s[1]))

# d = 1389
# print(str(d)[2])
# s = '5789'
# print(len(s))
# d = 78444
# print(len(str(d)))
# d = int(input())
# if len(str(d)) == 2:
#     print('Оно двузначное')
# else:
#     print('Оно не двузначное')
# d = int(input())
# # кратно 3 и трёхзначное
# if d % 3 == 0 and len(str(d)) == 3:
#     print('Число кратно трём и трехзначное')
# else:
#     print('Число НЕ кратно трём и НЕ трехзначное')
# sm = 0
# for x in range(5):
#     sm = sm + x
# print(sm)
# sm_chet = 0
# for x in range(100):
#     if x % 2 == 0:
#         sm_chet = sm_chet + x
# print(sm_chet)

# sm_nechet = 0
# # сумму нечетных чисел в диапазоне от 5 до 45
# for x in range(5, 46):
#     if x % 2 != 0:
#         sm_nechet = sm_nechet + x
# print(sm_nechet)

# d = 5
# while d > 0:
#     print('Привет')
#     d = d - 1
#d = int(input())
# найти сумму чисел, введенных с клавиатуры.
# пока не будет введено 0.
# 23
#  2
# 0
# 25
# a = int(input())
# sm = 0
# while a != 0:
#     sm = sm + a
#     a = int(input())
# print(sm)


# найти количество четных чисел, пока не будет введено значение
# a = int(input())
# ct_chet = 0
# while a != 0:
#     if a % 2 == 0:
#         ct_chet = ct_chet + 1
#     a = int(input())
# print(ct_chet)

# найти количество трёхзначных чисел, которые кратны 5, пока не будет введено значение 0
# a = int(input())
# d = 0
# while a != 0:
#     if a % 5 == 0 and len(str(a)) == 3:
#         d = d + 1
#     a = int(input())
# print(d)

# Найти сумму чисел, которые кратны 7 и двузначные.
# вводим числа, до тех пор, пока не будет введено число 0
# a = int(input())
# sm = 0
# while a != 0:
#     if a % 7 == 0 and len(str(a)) == 2:
#         sm = sm + a
#     a = int(input())
# print(sm)

# подаются числа, признаком окончания ввода, явл. число 0
# нужно найти кол-во отрицательных чисел, которые кратны 4
# a = int(input())
# d = 0
# while a != 0:
#     if a < 0 and a % 4 == 0:
#         d = d + 1
#     a = int(input())
# print(d)

# Подается число N. Вводится N чисел, и
# выводится среднее арифметическое этих чисел
# N = int(input())
# sm = 0
# for x in range(N):  # 3 4 5
#     a = int(input())
#     sm += a
# print(sm / N)


# Вводится число N. Потом вводятся N чисел.
# Нужно найти сумму трёхзначных чисел, которые кратны 7
# N = int(input())
# sm = 0
# for x in range(N):
#     a = int(input())
#     if a % 7 == 0 and len(str(a)) == 3:
#         sm += a
# print(sm)

# Вводится число N. Потом вводятся N чисел.
# Найти среднее арифм. двузначных чисел, которые оканчиваются на 8
# Если таких чисел нет, вывести "NO"
# N = int(input()) # 5
# sm = 0
# ct = 0
# for x in range(N):
#     a = int(input())
#     if len(str(a)) == 2 and str(a)[1] == '8':
#         sm += a
#         ct += 1
# if ct == 0:
#     print('NO')
# else:
#     print(sm / ct)




a = int(input())
d = 0
while a != 0:
    if len(str(a)) == 2 and str(a) == '8':
        d += 1
    a = int(input())
print(d)