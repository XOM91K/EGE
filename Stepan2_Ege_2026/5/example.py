# Четыре типа данных: int, str, float
# int - целочисленный (-5, 200, 138, 1000543, -200400)
# str - строковый ('hello', 'привет', 'да', 'д', '5', '59', '@#!')
# float - дробный (-25.3, 1.0, 1000.543..)
# bool - булевский (логический) (True, False)
# a = 40
# print(a + 5) # 45
# print(a * 2) # 80
# print(a / 2) #20.0
# print(a - 100) # -60
# Есть ещё две операции в информатике:
# 1) деление нацело  //  (возвращается целая часть от деления)
# 2) деление по остатку  % (возвращается остаток от деления)
#
# a = 55
# print(a // 10) # 5
# print(a // 20) # 2
# print(a // 5)  # 11
# print(a // 30) # 1
# a = 24
# print(a % 20) # 3
# print(a % 18) # 5
# print(a % 4)  # 0
# print(a % 12) # 0
# print(a % 15) # 9

# Знаки сравнений
# >  <  >=  <=  ==  !=
# a = True
# print(a)
# a = 2 == 3
# print(a)
# a = 133 * 56 > 11 * 5
# print(a)

# print(42 % 21 == 0)
# print(55 % 21 == 0)
# print(65 % 21 == 0)
# print(2 % 21 == 0)
# print(5 % 21 == 0)

# print(7 % 2 == 0) # f
# print(10 % 2 == 0)# t
# print(15 % 2 == 0)# f
# print(40 % 2 == 0)# t
# print(-3 % 2 == 0)# f
# print(50 % 2 == 0)# t
# print(-80 % 2 == 0)# t
# print(94 % 2 == 0)# t
# print(34 % 2 == 0)# t

#money = int(input())

# if money >= 100000:
#     print('Денег много')
# else:
#     print('Денег мало')


# number = int(input())
# if number % 2 == 0:
#     print('Число чётное')
# else:
#     print('Число нечётное')

# a = 'апПаРаТ'
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.count('а'))
# print(a.count('п'))

# s = 'СОЛНЫШКОФЫВФЫВФЫВФЫВФЫВФЫВФЫВФЫВЫЫВЫФВЁ'
# #Взятие элемента по индексу
# print(s[1])
# print(s[4])
# print(s[7])
# print(s[-1])
# print(s[-4])

#Срезы
# s = 'СОЛНЫШКО'
# print(s[0] + s[1] + s[2])
# print(s[-3] + s[-2] + s[-1])
# s1 = 'СОЛНЫШКОГУСЬЛЕБЕДЬНОРКААПЕЛЬСИНГОРКАЯБЛОКО'
# s1[start_index:finish_index:step]
# print(s1[::-1])
# print(s1[0:12])
# print(s1[0:12:2])
# print(s1[:5])
# print(s1[5:])
# Ещё известные функции

# Коллекции
#1. Списки - list
# l = [33, 44, 12, 22, 8]
#print(l[0] + l[1] + l[2] + l[3] + l[4])
# print(sum(l))
# print(max(l))
# print(min(l))
# print(sorted(l)[::-1])
# print(len(l)) #length
# print(l[1] + l[-1])

# c = '1011'
# print(c[1])
# c = 1011
# print(str(c)[1])


# Функции для перевода в 2-ую, 8-ую, 16-ую системы счисления
# d = 18
# print(bin(d)[2:]) # bin - в двоичную
# print(oct(d)[2:]) # oct - в восьмеричную
# print(hex(d)[2:]) # hex - в 16-у
# d = 160276983498123
# print(hex(d)[2:])
# b = '10010'
# print(int(b, 2))
# o = '15623125623'
# print(int(o, 8))
# print(bin(128731273812351381)[2:])