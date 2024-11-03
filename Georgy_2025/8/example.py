import itertools
#permutations - перестановки
d = itertools.permutations('ЙОД')
print(list(d)) # 3! = 6
#product-  составляет комбинации с повторениями символов
g = itertools.product('ЙОД', repeat=3)
print(list(g)) # 3**3 =27
# ГОРАД
