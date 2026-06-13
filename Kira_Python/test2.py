# Списки # list
# input() print() len() str() int() float() bool()
#l = [6, 100, 5, 43, 'hello', 'red', -500, 4.3, True, False]
# print(l[1] + l[3])
# print(l[-1])
# print(l[:3])
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = a.copy()
# print(id(a))
# print(id(b))
# a = [1, 2, 3]
# #a.append([4,5,6])
# a.extend([4,5,6])
# print(a) # Распаковка
# b = a
# b.append(50)
# b.append(-100)
# print(a)
# print(b)
#Методы,которые что-то возвращают
# print(a.count(100))

#a.clear()
# print(a.index(6))
# print(a)
# #Методы-действия:
# a.append(-500)
# #a.sort()
# a.remove(100)
# a.remove(100)
# a.insert(2, 89)
# a.pop(2)
# del a[2]

#b = [5, 100, 6, 7, 20, -25]
# print(sorted(a)[::-1])
# a = sorted(a)
# a.reverse()
# print(a)
# b.sort()
# print(b)

#Методы

# print(l)
# # Функции
# l = sorted(l)
# print(l)
# print(sorted(l))
# print(l)
# print(sum(l))
# print(max(l))
# print(min(l))
# print(len(l))


# #Кортежи tuple
# l = [d for d in range(1, 1_000_000)]
# t = (d for d in range(1, 1_000_000))
# print(l.__sizeof__())
# print(t.__sizeof__())

# Множества set()
# Содержит только уникальные значения
# Являются неперебираемыми
# s = {1, 2, 3, 3, 3, 4, 5, 10, -10, 5, 5, 9}
# s.pop()
# s.pop()
# print(s[1])
# s = 'abracadabra'
# print(set(s))
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b), a | b) # объединение # pipe
# print(a.difference(b), a - b) # разность
# print(a.intersection(b), a & b) # пересечение
# print(a.symmetric_difference(b))
#[] () {}
# Словарь
# sl = {'red': 550, 35: 100, -5: 200, 'brown': 'green'}
# sl.pop('red')
# print(list(sl.items()))
# print(list(sl.values()))
# print(list(sl.keys()))
# print(sl.get('brownфывфв', False))
#print(sl['browns'])
# print(sl['red'])
# print(sl[-5])
# print(sl['green'])

