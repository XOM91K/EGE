#Есть два множества a и b
#Создать множество C - объединение множеств a и b
#преобразовать множество C в список
#и преобразовать элементы в списке в корни из чисел
#1) map 2) генератор списков
A = {1, 2, 4, 100, 'a', 66, 'b', 155}
B = {1, 2, 'c', 100, 33}
C = A.union(B)
C = list(C)
G = list(map(lambda x: x ** 0.5 if type(x) == int else x, C)) #через map и lambda
H = [x ** 0.5 if type(x) == int else x for x in C] #через генератор
print(G)
print(H)