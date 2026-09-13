# print(5 + 5)
# print('5' + '5')
# g = 9
# print('5' + str(g))
# print(2 + int('2'))
# print('5' * 20)
# print('9' + '7')
# d = 5 # int
# s = 'привет' # str
# print(s[1:4])
# a = 'privetkakdela'
# print(a[3:6])
# print(a[2::2])
# print(s[0] + s[1] + s[2] + s[3])
# # Срезы s[старт:финиш:шаг]
#print(s[::-2])
# print(s[::2])
# print(s[::3])
# print(s[:4])
# print(s[-4:-1])
# print(s[-4:])
# print(s[0]) # взять элемент по индексу
# print(s[3])
# print(s[-1])
# print(s[-4])
# print(5 ** 9)
# print(5 / 9)
# print(9 // 5)
# print(12 // 5)
# print(9 % 5)
# print(12 % 5)
# print(7 % 2)
# print(5 % 2)
# print(123823612387213618336181 % 2)
# print(4 % 2)
# print(12 % 2)
# print(12387213612832130 % 2)
# s = 'hello' # str
# Функции
# print(len(s))
#s = 'Hello world'
# Методы
# print(s.replace('l', 'L', 2))
#print(s.count('el'))
#print(s.index('l'))
#print(s.isdigit())
# print(s.upper())
# print(s.lower())
# print(s.islower())
# print(s.isupper())
# int str
# d = 3.14
# b = -9.88 # float
# d = 123926312983
# if d % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')
# word = 'Pythn'   # y o
# if 'y' in word and 'o' in word:
#     print('Да')
# else:
#     print('Нет')
# d = 9999
# if len(str(d)) == 4:
#     print('Да')
# else:
#     print('net')
# a = 353
# b = '353'
#print(a[1])
# print(b[1])
# a = 353
# print(str(a)[1])
#l = [350, 12, -8, 8.5, 900, 12, 12]  # list
#Методы
# print(l.)
# print(l.remove(12))
# print(l.append(800))
# l.extend([500, 350])
# l.pop(2)
# l.sort()
# print(l)
# l.count(12)
# print(l.count(12))
# print(l.index(-8))
# l = [3, 4, 1]
# # Функции
# # print(len(l))
# # print(max(l))
# # print(min(l))
# # print(sum(l))
# print(sorted(l))
# print(l)
# print(l[2])
# print(l[1:3])
# print(l[::-1])
# for x in [0, 1, 2, 3, 4]:
#     print('Hello', x)
#     print('abc', x)
# print(list(range(5)))
# s = 'abracadabra'
# for x in s:
#     print(x)
l = []
for x in range(0, 101):
    if x % 2 == 0:
        l.append(x)
print(l)
print([x for x in range(0, 101) if x % 2 == 0]) # Генератор списков