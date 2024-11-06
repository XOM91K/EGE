import itertools  # iteration tools
#permutations - перестановки
d = itertools.permutations('НОСАТ')
#product - комбинации с повторениями символов
g = itertools.product('НОС', repeat=5)
print(list(d))
print(list(g))