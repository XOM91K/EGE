l = [sorted([int(d) for d in x.split()]) for x in open('2.txt')]
k = 0
for x in l:
    k_nech = 0
    for y in x:
        if y % 2 != 0:
            k_nech += 1
    if (len(set(x)) < len(x) and k_nech != 3) or (len(set(x)) >= len(x) and k_nech == 3):
        print(x, k_nech)
        k += 1
print(k)
# № 6106) (А. Богданов) В файле электронной таблицы 9-190.xls
# в каждой строке записаны 6 натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для
# которых выполнено ровно одно из двух условий:
# – в строке есть повторяющиеся числа;
# – в строке есть ровно три нечетных числа.