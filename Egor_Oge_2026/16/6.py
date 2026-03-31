#Задание ОГЭ 16. (Задача №979)
a = int(input())
otvet = 10 ** 7
for x in range(a):
    hour = int(input())
    mins = int(input())
    otvet = min(otvet, hour * 60 + mins)
print(otvet // 60, otvet % 60)