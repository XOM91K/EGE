import itertools
k = 0
for x in itertools.product(sorted('ЖЧГМЯФИ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[:2] == 'ЖЯ':
        print(k, x)
# permutations - перестановки
# product - комбинации в повторениями
# d = itertools.permutations('ЛЕС', 3)
# g = itertools.product('ЛЕС', repeat=3)