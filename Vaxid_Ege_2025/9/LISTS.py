l = [1, 2, 3, 4, 4, -4, 4, 4, 4, 4, 4, 4, 44, 5]
print(l[-1])
print(sum(l)) # сумма чисел в списке
print(max(l)) # максимальный элемент в списке
print(min(l)) # минимальный элемент в списке
print(len(l)) # количество элементо в списке
print(l)
print(l.count(44)) # количество элементов 44
l.append(10)
print(l)
print(l.index(3)) # возвращает индекс элемента
l.sort()
print(l[::-1])