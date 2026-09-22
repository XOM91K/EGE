# a = 5
# print(a)
# print(id(a))
# a = 3
# b = 9
# a, b = b, a
# print(a, b)
#a = input('Введи сколько тебе лет')
# a = 5
# a = 3
# print(a)
# s = '''Ангел
# <Валерик> ("Я к вам пишу случайно; право...")
# "Выхожу один я на дорогу..."
# Дума
# И скучно и грустно
# К* ("Я не унижусь пред тобою...")
# "Как часто, пестрою толпою окружен..."
# Кинжал
# "Когда волнуется желтеющая нива..."
# Листок
# "На севере диком стоит одиноко..."
# "Нет, не тебя так пылко я люблю..."
# Парус
# Поэт
# Пророк
# "Прощай, немытая Россия..."
# Родина
# Узник
# Утес'''
# print(s)
# s = 'abracadabra'
# print(s[::-2])
# print(s[5])
# print(s[:4])
# print(s[1:4])
# print(s[4:7])
# print(s[-3:])
# s = 'hello world!'
# print(s.lower())
# print(s.count('o'))
# print(s.index('o'), s.rindex('o')) #  s.index('g')
# print(s.find('he'), s.rfind('o'), s.find('g'))
# # print(s.islower())
# print(s.isupper())
# print(s.isdigit())
# print(s.isalpha())
# s = 'abc'
# print(s.zfill(10))
# s = 'how are you im fine i am'
# print(s.replace('a', '@'))
# print(s.replace('o', 'O', 1))
# print(5 == 4)
# a = 4
# print(a > 8)
# print('ng' in 'orange')
#s = 'ekskavator'
# print(s.)
# print(s.count('k'))
# print(s.replace('ek', '99'))
# print(len(s))
# print(s.index('k'))
# print(s.index('e'))
# print(s[-3:])
# print(s[:3])
# print(s[::-1])
# print(s[::2])
# print(s[1::3])
# s = 'red blue violet orange'
# s = s.split()
# print(s[-2])
# print('#'.join(s))
#
# l = [1, 2, 3, 54, 4, -2, 2, 5]
# l.sort(reverse=True)
# print(l)
#print(l[::-1])
# # Методы
# l.append(40)
# l.insert(3, 500)
# print(l.index(54))
# print(l)
# l.clear()
# print(l)
# l.append(2)
# l.append(4)
# print(l)
# l.remove(4)
# print(l)
# l.pop(2)
# print(l.count(2))
# print(l)
# Функции
# print(sum(l))
# print(max(l))
# print(min(l))
# print(len(l))
# print(sorted(l))
# print(sorted(l)[::-1])



# l = [100, 4, 10, 12]
# l.append(50)
# print(l)
# print(sum(l))
# print(max(l))
# print(min(l))
# print(sorted(l))

# l = [11, 91, 103]
# if l[1] % 2 == 0:
#     print('Четное')
#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l = []
# for x in range(1, 1001):
#     if x % 7 == 0:
#         l.append(x)
# print(l)
# s = 'abracadabra'
# print(s.upper())
# print(s.replace('a', 'A'))
# print(s.index('r'))
# print(s.count('a'))

# #l = [x for x in range(1, 100_000_000)] # list
# t = (x for x in range(1, 10000000_000_000_000)) # tuple
# #print(l.__sizeof__())
# print(t.__sizeof__())

# s = '9 10 150 250 400'
# s = s.split()
# s = list(map(int, s))
# print(sum(s))
# l = list(map(int, input().split()))
# # print(l)

l = list(map(int, input().split()))
print(l)


