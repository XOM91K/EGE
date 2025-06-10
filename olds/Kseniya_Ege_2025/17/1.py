l = [int(x) for x in open('1.txt')]
ct = 0
sr = sum(l) / len(l)
sm = []
#сначала ищем среднее арифметическое всех чисел в файле, а потом уже решаем задачу в цикле
# print(l)
for x in range(len(l) - 1): #поиндексовый перебор списка
    if l[x] < sr and l[x + 1] < sr:
        if str(l[x])[-1] == '9' or str(l[x + 1])[-1] == '9':
            ct += 1
            sm.append(l[x] + l[x + 1])
print(ct)
print(max(sm))
# for x in l: #поэлементный перебор
#     print(x)