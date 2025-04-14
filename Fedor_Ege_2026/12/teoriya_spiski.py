# int, str

#Список list
# l = [22, 10, 40, -2, -5]
# #Функции
# # max, min
# print(max(l))
# # len
# print(len(l))
# # sorted
# print(sorted(l)) #возрастания
# print(sorted(l)[::-1]) #убывания
# print(sorted(l, reverse=True)) #убывания
# # sum
# print(sum(l))

# Методы (вызываются через точку)
l = [88, 10, -5, 5, 5, 5]
# # count()
# print(l.count(5))
# # index()
# print(l.index(10))
# l.pop(2)
# del l[3]
#
# l.remove(88)
# l.append(100)
# l.sort(reverse=True)
# print(l)
# l = [3, 2, 3]
# l = sorted(l)
# #l.sort()
# print(l)
# l = [6, 5, 3]
# r = l.copy()
# r.append(50)
# print(r)
# print(l)
# r = l
# r.append(-10)
# print(r)
# print(l)
# l = [1, 2, 3, 4, 5]
# l.clear()
# print(l)

#Срезы у списков
# l = [5, -5, 10, 12, 14, 2, 1]
# print(l[-3:])
# print(l[:3])

#как найти сумму цифр числа
# s = '901210293712912872198215659128561298012571259812056210912330'
# print(sum(map(int, s)))
# print(list(map(len, s)))
# print(list(map(lambda d: int(d) ** 2 + 5000, s)))

import math
#как найти произведение цифр числа
s = '127126386129361'
print(sum(map(int, s)))
print(math.prod(map(int, s)))