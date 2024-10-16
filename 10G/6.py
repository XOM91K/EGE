n = int(input('Введите n: '))
l = [0, 1]
for x in range(n - 2):
    l.append(l[-1] + l[-2])
print(f'{n}-е число Фибоначчи: {l[-1]} {l}')