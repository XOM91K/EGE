#Типы данных

#ctrl + /
# a = 5 #Целочисленный тип (int)
# print(a + 2)
# print(type(a))
# b = '5' #Строковый тип (str)
# print(b + '2') #Присоединение (склеивание)
# print(type(b))
# c = 'Hello'
# d = 'Bye'
# print(c + d)
# print(a * 100)
# print(b * 100) #Дублирование в строках

#Строки str
#d = '3' + 2  # ошибка
#s = 'ПриветПокаУдачиЗвездаЦветокДом'
# print(s[2]) #взятие элемента по индексу
# print(s[0] + s[1] + s[2])
#Срезы
#первые 20 символов
#print(s[0] + s[1] + s[2] + s[3]...)
#print(s[0:20])
#print(s[start_index:finish_index:step])
#s = 'ПриветПокаУдачиЗвездаЦветокДом'
#print(s[5:9])
# print(s[1:4:1])
# print(s[1:4:2])
# print(s[0:20])
# print(s[:20])
#s = 'ПриветПокаУдачиЗвездаЦветокДом'
# print(s[:])
# print(s[4:])
# print(s[::2]) # с шагом 2
# print(s[::3])
#print(s[::-1]) #переворачивание строки
#s = 'ПриветПокаУдачиЗвездаЦветокДом'
# print(s[:6])
# print(s[-3:-1])
# print(s[-3:])

#Методы строк (вызываются через точку)
# s = 'Приветпривет'
# print(s.count('п'))
# print(s.count('вет'))
# print(s.upper())
# print(s.lower())
# print(s.index('п'))
# print(s.isdigit()) # Цифровые ли символы
# print(s.isupper()) # Все ли символы заглавные
# print(s.islower()) # Все ли символы строчные
# print(s.isalpha()) # Все ли символы алфавитные
# print(s.istitle()) # Начинается ли строка со строчной буквы
# s = 'ОЛОВО'
# s = s.replace('О', 'А', 2)
#s = 'ОЛОВОКАРТОШКАВЕДРО'
# s = s.replace('КА', '##')
# print(s)

#Функции строк
# s = 'asodisahdoidhasdoaidhsaodasihdoidsadoisagoigdo12idg2i1odg12oi'
# print(len(s))
# d = int(input())
# print(d + 2)
# s = '100'
# print(int(s) + 2)
#
# d = 100
#print(str(d) + '2')
#s = input() # 1450
#print(int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]))
#s = input()
#print(int(s[0]) * int(s[1]) * int(s[2]) * int(s[3]))

#цикл for перебирает элементы
# d = range(1, 1000)
# #range - задает математическую последовательность
# print(list(d))

# for x in range(2, 1000, 2):
#     print(x, end=" ")
# d = 'СОЛНЫШКО'
# print()
# for x in d:
#     print(x, end=" ")
# d = '11223923812621837632873235812321532132153982173512381235'
# sm = 0
# for x in d:
#     sm += int(x)
# print(sm)
#print(2 + '2')
# c = 100
# #c = c + 5
# c += 5
# print(c)
# s = 'РОМ'
# s += 'А' + s
# print(s)
# d = 7
# d //= 2
# print(d)
# d = 80
# d *= 2
# print(d)
# d -= 20
# print(d)
# // + - * /  **   %
#print(24 % 4)
# d = 8
# d **= 2
# print(d)



d = 112239238126218376
sm = 0
for x in str(d):
    sm  +=int(x)
print(sm)
# for x in range(100):
#     print('Привет')


#while - цикл с условием
# d = 5
# while d > 0:
#     print('Привет')
#     d -= 1
# while True:
#     print('Привет')

#Пользователь вводит числа. Мы должны найти сумму этих чисел
#Пользователь вводит их, до тех пор не введет 0
# a = -1
# sm = 0
# while a != 0:
#     a = int(input())
#     sm += a
# print(sm)
# d = 102
# if d % 2 == 0:
#     print('Число чётное')
# else:
#     print('Число нечётное')
# d = 8175
# #делится на 3 и на 5
# if d % 3 == 0 and d % 5 == 0:
#     print('Да')
#d = 108
# if d > 109 and d > 107:
#     print('Да')
# if d > 109 or d > 107:
#     print('Да')
# sm1 = 344
# sm2 = 467
# if (str(sm1)[-1] == '3' and str(sm2)[-1] != '3') or (str(sm1)[-1] != '3' and str(sm2)[-1] == '3'):
#     print('Да')
# else:
#     print('Нет')

#Списки
#s = '123'
#print(s[1])
# l = [2, 3, 4, 100, -1500, 'Hello', 'Privet Kak dela?', 123]
# print(l[5], l[2], l[7])
#l = [3, 4, 10, -12]
#Функции
# print(len(l)) #выводит длину списка (кол-во элементов в списке)
# print(max(l)) #выводит максимальный элемент
# print(min(l)) #выводит минимальный элемент в сптске
# print(sum(l))
# print(sorted(l))
# print(l)
# l = sorted(l)
# print(l)
#Методы
# l = [3, 4, 10, -12, 20, 20, 3, 3, 1, 50]
# l.remove(-12)
# l.remove(20)
# l.insert(4, 90)
# l.sort(reverse=True)
# #l = l[::-1]
# #l.clear()
# print(l)
# l.pop(3)
# print(l)


# l = [1, 3, 2]
# print(sorted(l, reverse=True))

# print(l.count(20)) #count - считает кол-во элементов в списке
# print(l.index(-12)) #возвращает индекс элемента
# l.append(100)
# print(l)
# l.append(55)
# print(l)

# [1, 2] list
# 123 int
# 'hello' str
# {3, 3, 4} set


# Множества (set)
# s = {1, 2, 2, 4, 5, 10, -10, 10}
# s.add(50)
# print(s)
#print(s[2])
# s = 'abracadabra'
# print(set(s))
# print(len(set(s)))