#Множества set
d = set() #пустое множество
d = {5, 'e', 6, 'd', 'd', 'd', 'd', 3, 1, 10}
a = {33, 22, 3, 1}
print(type(d)) #узнать тип
d.add(10)
d.add(10) #добавление элемента add
print(d)
print(d.symmetric_difference(a)) #вычитание из множества a
print(d.intersection(a)) #пересечение (выводятся одинаковые элементы)
print(d)
d.remove(1) #удаляет конкретный элемент
print(d)
print(a)
print(d.isdisjoint(a)) #выводит true, если ни один элемент из множества
#a не лежит в множестве d
print(d.union(a)) #объединение множеств
print(d.pop())
print(d)
print(d.pop()) #удаляет последний элемент
d.clear() #очищает множество
print(d)