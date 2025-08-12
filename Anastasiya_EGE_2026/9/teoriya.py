# l = [1, 2, 3, 4, 5]
# l.append(100)
# l.insert(2, 50)
# l.insert(2, 50)
# #l.sort()
# l.remove(50)
# l.pop(2)
# del l[2]
# print(l.pop(2))
# print(l.index(5))
# print(l.count(100))
# print(l)
#Генераторы списков
# l = [1, 2, 3, 4, 5]
# print(l)
# l = [x for x in range(1, 101) if x % 3 == 0]
# print(l)
#Функции списков
# l = [x for x in range(1, 101) if x % 3 == 0]
# print(sum(l))
# print(min(l))
# print(max(l))
# print(sorted(l))
# l = [8, 8, 5, 4, 10, 10, 12, 12]
# print(set(l))
# s = 'abracadabra'
# print(set(s))
# s = {1, 2, 3}
# s.add(55)
# s.add(-100)
# print(s[3])
# l = [8, 3, 1, 4]
# l.append(55)
# print(l)
# print(l.sort())
# print(l)
# l = [x for x in range(1, 1_000_000)]
# t = (x for x in range(1, 1_000_000))
# s = {x for x in range(1, 1_000_000)}
# print(l.__sizeof__())
# print(t.__sizeof__())
# print(s.__sizeof__())
# l = [1 for x in range(1, 1000)]
# print(l)
# print(set(l))
# l = [1, [1, 9, 10], 3]
# print(l[1][1])
# x = [55, 33, 10, -7, 15, 89, 14]
# ch = [y for y in x if y % 2 == 0]
# print(ch)

x = [1, 3, 9, 15, 20] # возрастания
x = [1, 3, 3, 15, 20] # неубывания

x = [22, 14, 2131, 123123, 12312312]
sm_cif = sum([sum(map(int, str(y))) for y in x])
print(sm_cif)