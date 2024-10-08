import itertools
# permutations - перестановки
# составляет перестановки из символов
d = itertools.permutations('СОН', 3)
print(list(d))
# product - все возможные комбинации из символов
g = itertools.product('СОН', repeat=3)
for x in g:
    x = ''.join(x)
    print(x)