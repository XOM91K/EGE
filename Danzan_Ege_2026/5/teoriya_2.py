# #Списки и кортежи
# l = [1, 2, 3]
# l.append(100)
# l.append(500)
# l.insert(2, 50)
# l.sort(reverse=True)
# l.remove(50)
# l.pop(2)
# del l[2]
# print(l.pop(1))
# print(l)
# t = (1, 2, 3)
# print(t)
# print(t[1])
# Генераторы списков
# l = [1, 2, 3, 4, 5]
# print(l)
# l = list(range(1, 1001))
# print(l)
# l = [x for x in range(1, 1001) if x % 2 == 0 and x > 100]
# print(l)
# l = [x for x in range(1, 10_000_000)]
# t = (x for x in range(1, 10_000_000))
# print(l.__sizeof__())
# print(t.__sizeof__())