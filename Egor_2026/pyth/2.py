#Есть число, например 20.
#Вывести список с делителями этого числа
# 1, 2, 4, 5, 10, 20
def dels(number):
    dl = []
    for x in range(1, number + 1):
        if number % x == 0:
            dl.append(x)
    return dl
print(dels(180))
