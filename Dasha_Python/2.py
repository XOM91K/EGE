# import random
# t = (random.randint(1, 10_000_000) for x in range(1, 10_000_000)) # tuple
# l = [random.randint(1, 10_000_000) for x in range(1, 10_000_000)] # list
# print(t.__sizeof__()) #dunder методы (магические методы)
# print(l.__sizeof__())
# t[0] = 100
# l[0] = 100
# print(l)
# print(sum(t), sum(l), max(t), max(l))
# print(len(t), len(l), sorted(t), sorted(l))
# d = input()
# d = map(int, d.split())
# print(sum(d))

# list tuple
# множества - set
# l = []
# t = ()
# s = set()
# l = [1, 2, 3]
# t = (1, 2, 3)
# s = {1, 2, 3, 'hello'}
# # s.add(30)
# # s.remove(3)
# # s.clear()
# print(s)
# s1 = {6, 9, -5}
# s2 = {99, 6, 105}
# print(s1.symmetric_difference(s2)) # симметричная разность
# print(s1.intersection(s2)) # пересечение
# print(s1 & s2) #  пересечение
# print(s1.union(s2)) # объединение
# print(s1 | s2) # объединение
# print(s1.difference(s2)) # разность
# print(s1 - s2)# разность

# dict словари
# d = {5: 10, 'red': 109, 3: 'Hello World!', 10: 109}
# # key: 4  value: 100
# d[4] = 100
# d[5] = 15
# print(d)
# d = {'name': 'Иван', 'surname': 'Иванов', 'age': 30}
# print(d['name'])
# print(d[10])
# print(d['red'])
# print(d[5])
# print(d[3])
# s = {1, 2, 3}
# s = set()
# print(type(s))
# s = {}
# print(type(s))