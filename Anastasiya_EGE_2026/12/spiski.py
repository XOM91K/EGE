# Списки
# l = [7, 3, -5, 2, 3, 1, 2, 4, 5, 1]
# #Срезы у списков
# print(sorted(l)[::-1])
# print(l[::-1])
# print(l[:3])
# print(l[-4:])
# print(l[2:4])
# #Методы (через точку вызываются)
#
# l.remove(4)
# print(l)
# l.sort()
# print(l)
# print(l.count(3)) #находит кол-во элементов
# print(l.index(3)) #находит индекс элемента
# l.append(105)
# l.pop(2)
# #оператор del (оранжевый цвет у операторов)
# del l[5]
#
# print(l)
# l.clear()
# print(l)
#Функции у списков  (фиолетовые)
# print(sum(l)) #Сумма элементов списка
# print(max(l)) #Максимальный элемент в списке
# print(min(l)) #Минимальный элемент в списке
# print(len(l)) # Длина списка (сколько в списке элементов)
# print(sorted(l))

# s = 'hello'
# d = 1231233

#print(s.count('2') * 2 + s.count('5') * 5 + s.count('3') * 3)
#s = '1289316249812641904612904162201461401232543567576'
#print(s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9)
# d = []
# for x in range(1, 6):
#     d.append(x)
# print(d)
# print([x for x in range(1, 6)])
#от 2 до 40
#print([x for x in range(2, 41)])
#сгенерировать список, с нечетными числами от 1 до 100, кратные 5
#print([x for x in range(1, 101) if x % 5 == 0 and x % 2 != 0])
s = '589'
print([int(x) for x in s])

# 27
# 3
