import itertools # iteration tools
# #permutations - перестановки
# #3! = 1 * 2 * 3 = 6
# #4! = 1 * 2 * 3 * 4 = 24
# for x in itertools.permutations('МГЛА', 4):
#     x = ''.join(x)
#     print(x)

#product - комбинации с повторениями букв
#ССС
#ССО
#ССН
#СОС
#СОО
#СОН
#3**3 = 27
#10**9 = 1.000.000.000
#1.000.000 = 1 секунда
# for x in itertools.product('СНОВЕДЕНИЕ', repeat=9):
#     x = ''.join(x)
#     print(x)


# a = 'abracadabra'
# # set - функция, которая возвращает множество
# # множество - это уникальная последовательность элементов
# a = set(a)
# print(len(a))
# days = {11, 12 ,11, 8, -9, -9, 5, 5}
# days2 = {99, 88}
# days.add(500)
# print(type(days), days)
# days.remove(11)
# days.update('abra')
# print(days.union(days2))
# print(days2.union(days))
# print(days.intersection(days2))
# d = list()
# d = []
# d.append(-2)
# print(d)
# g = set()
#
# r = {}
# r = dict()
# print(type(g))
# print(days)
# days = [11, 12 ,11, 8, -9, -9, 5, 5]
# days.append(2)
# days.append(2)
# days.append(2)
# days.append(2)
# days.append(2)
# days.append(2)
# days.append(2)
# days.append(2)
# print(type(days), days)



# numbers = [1, 2, 3]
# dumbers = (1, 2, 3)
# rumbers = {1, 2, 3, 3}
# print(numbers, numbers.__sizeof__())
# print(dumbers, dumbers.__sizeof__())
# print(rumbers, rumbers.__sizeof__())