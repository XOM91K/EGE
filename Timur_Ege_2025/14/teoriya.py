d = 8
#print(d)
# list (списки)
t = [18, 8, 10, 18, 18]
print(t.count(18)) #находит кол-во элементов
t.remove(18) #удаляет элемент
print(t.index(8)) #возвращает индекс элемента
t.append(99) #добавляет элемент в конец списка

print(t)

print(t[0] + t[2]) # 8 + 18 = 26
print(len(t)) # 5
print(sum(t)) # 72
print(set(t))
print(max(t))
print(min(t))
print(sorted(t))