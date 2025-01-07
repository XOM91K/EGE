import itertools
k = 0
for x in itertools.product(sorted('СЕНТЯБРЬ'), repeat = 5):
    x = ''.join(x)
    k += 1
    if x[0] == 'Р' and x.count('Ь') == 0 and k % 2 == 0:
        print(x,k)