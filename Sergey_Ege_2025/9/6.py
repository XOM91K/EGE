# – в строке есть повторяющиеся числа;
# – среднее арифметическое всех повторяющихся чисел
# строки меньше среднего арифметического всех её чисел.
l = [[int(d) for d in x.split()] for x in open('6.txt')]
ct = 0
num = 0
for x in l:
    povt = []
    num += 1
    for y in x:
        if x.count(y) > 1:
            povt.append(y)
    if len(set(x)) < len(x) and sum(povt) / len(povt) < sum(x) / len(x):
        ct += num
print(ct)