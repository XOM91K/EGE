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
# print(str(d) + '2')
# s = input() # 1450
# print(int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]))
# s = input()
# print(int(s[0]) * int(s[1]) * int(s[2]) * int(s[3]))