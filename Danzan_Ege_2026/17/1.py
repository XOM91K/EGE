l = [int(x) for x in open('1.txt')]
mx = []
# Первое , Что делаем это:
# Находим элемент среди всей последовательности
sr = sum(l) / len(l)
# Второе, что делаем, это перебираем пары/тройки:
for x in range(len(l) - 1):
    if l[x] < sr and l[x + 1] < sr:
        if str(l[x])[-1] == '9' or str(l[x + 1])[-1] == '9':
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))