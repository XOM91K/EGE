# a = 5 # число int
# b = '5' # Строка str
# #print(a + b) # ошибка
# c = 3.2 # число, дробное float
# print(type(a), type(b), type(c))
# a = 4110
# c1 = a % 10
# c2 = a // 1000
# c3 = a // 100 % 10
# c4 = a % 100 // 10
# print(c1 + c2 + c3 + c4)
# print(a / 2)
# print(a // 2)
# print(a % 2)
# print(19 % 5)
# print(22 % 10)
# print(20 // 6)
# print(9 // 5)
# print(5 ** 9)

# Строки
# s = "Hello"
# print(s[::2])
# print(s[::-1])
# print(s[:3])
# print(s[2:])
# print(s[0])
# print(s[1])
# print(s[4])
# print(s[-1])
# print(s[-4])
# s = 'abracadabra'
# print(s[:4])
# print(s[::-2])
# print(s[::3])
# print(s[::-1])
# s = 'abracadFabra'
# print(len(s)) # Функции (фиолетовые)
# print(s.)
# Методы
# print(s.replace('a', '#'))
# print(s)
# print(s.lower())
# print(s.upper())
# s = s.upper()
# print(s)
# print(s.isalpha())
# print(s.istitle())
# print(s.islower())
# print(s.isupper())
# print(s.count('ab'))

# d = 400
# if d < 100:
#     print('Да')
# elif d < 200:
#     print('Да')
# elif d < 500:
#     print('Да')
# else:
#     print('Нет')

# for x in range(5):
#     print('привет')
# for x in 'привет':
#     print(x)
# print(list(range(5)))
# for x in [0, 1, 2, 3, 4]:
#     print(x)
for x in range(100):
    if x % 2 != 0 or x > 50:
        print(x)