sl = {1: 66, 'two': {2: 5, 10: -10}, 'sixsixsix': 666, '555': 5}
print(sl['two'][10])
#Методы словаря
print(sl.values())
print(sl.keys())
print(sl.items())
print(sl[1])
print(sl.get(2, 1000))
print('ok')
print('ok')
sl['j'] = 1000
sl['j'] = 500
print(sl.setdefault('j', 500))
print(sl)
#print(sl.fromkeys([d for d in range(900, 1900)], 500))
#sl.clear()

print(sl.pop(1)) #удаляет пару по клучу
print('##')
print(sl.popitem()) #удаляет элементы с конца
print(sl.popitem())
print(sl.popitem())
sl.update()
g = sl.copy()
print(sl)
print(g)
