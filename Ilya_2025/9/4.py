# В файле электронной таблицы в каждой строке записаны семь натуральных чисел.
# Определите сумму чисел в строке таблицы с наименьшим номером, для которой
# выполнены оба условия:
# – в строке есть два числа, которые повторяются
# дважды, остальные три числа различны;
# – максимальное число строки не повторяется.
# В ответе запишите только число.
l = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ct = 0
for x in l:
    povt = []
    nepovt=  []
    for i in x:
        if x.count(i) == 2:
            povt.append(i)
        if x.count(i) == 1:
            nepovt.append(i)
    if len(povt) == 4 and len(nepovt) == 3 and x[-1] != x[-2]:
        ct += 1
        print(x, sum(x))
print(ct)