# d = 123
# print(d + 5, d - 5, d * 5, d // 3, d / 4, d % 7, d ** 5)
# print(9 % 5)
# print(9 // 5)
# print(12 % 10)
#s = 'Hello'
#print(s[1], s[4])
# print(s + '5')
# print(s * 5)
# s = 'abracadabra'
# s[start_index:finish_index:step]
# print(s[::-1])
# print(s[1::2])
# print(s[-4:])
# print(s[:4])
# print(s[0] + s[1] + s[2] + s[3])
# Функции
# s = 'abra55cadabr'
# print(s.)
# print(s.isdigit())
# print(s.isalpha())
# print(s.upper())
# print(s.lower())
# print(s.istitle())
# print(s.index('r'))
# print(s.rindex('r'))
# s = 'b' + s[1:]
# # s[0] = 'b'
# print(s)
# print(len(s))
# # Методы
# print(s.count('a'), s.count('ab'))
# print(s.replace('a', '@'))
# print(s)
# s = 'abaaraa'
# print(s.replace('a', 'A'))
# s = s.replace('a', 'A')
# print(s)

# list Списки
# l = [1, 2, 3, [1, 2, 3], 4, 5, 'for']
# print(l[::2])
# print(l[::-1])
# print(l[2:])
# print(l[3][2])
# print(l[-1])
# s = 'asidhqwoa'
# print(sorted(s))
# l = [55, 100, -30, 22, 19, 100]
# print(sorted(l))
# print(l)
# l.sort()
# print(l)
# Методы строк
# Методы действия (они не возвращают значение)
#l.append(500)
#l.clear()
# l.sort(reverse=True)
# print(l)
# l.insert(3, 778)
# del l[2]
# print(l.pop(2))
# l.remove(100)
# l.remove(100)
# print(l)
# Методы, которые возвращают значение
# print(l.count(100))
# print(l.index(100))
# Функции
# print(sorted(l, reverse=True))
# print(sorted(l)[::-1])
# print(sum(l))
# print(max(l))
# print(min(l))
# print(len(l))

# # кортежи tuple
# l = [x for x in range(1, 100_000_000)]
# # l[1] = '5'
# # print(l)
# t = (x for x in range(1, 100_000_000))
# # t[1] = '5'
# print(l.__sizeof__())
# print(t.__sizeof__())
# # print(type(l))
# # print(type(t))


# Множества set
# s = {1, 2, 2, 3, 3, 3, 3, 5, 5}
# # l = [1, 2, 3]
# # t = (1, 2, 3)
# print(s)
# print(s.__sizeof__())
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a - b)
# print(b - a)
# print(a | b)
# print(a & b)
# s = 'abracadabra'
# # print(list(s))
# # print(tuple(s))
# s = set(s)
# print(s[2])
# s = {8, 5, 10, 2}
# print(max(s))
# print(sorted(s))
# d = int(input())
# if d % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')
# # Тернарный условный оператор
# print('Число четное' if d % 2 == 0 else 'Число нечетное')
# for i in range(0, 101):
#     print(i)
# str, list, tuple,
# for i in (0, 1, 9):
#     print(i)
# for i in 'hello':
#     print(i)
# for i in range(1, 100, 2):
#     print(i)
# for i in range(100, 1, -1):
#     print(i)
# l = []
# for i in range(0, 1_000_001):
#     l.append(i)
# print(l)
# Генаратор списков
# print([i ** 2 for i in range(0, 1000) if i > 500 and i % 127 == 0])
# d = 10
# while d > 0:
#     d -= 1
#     if d == 5:
#         continue
#     print('hello', d)

# Переводы в системы счисления
d = 12381
print(bin(d)[2:]) # в 2-ую систему
print(oct(d)[2:]) # 8ую
print(hex(d)[2:]) # 16ую
print(int('305d', 16))
print(int('30135', 8))