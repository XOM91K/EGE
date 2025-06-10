import itertools
n = 0
for x in itertools.product('РПОГА', repeat=5):
    x = ''.join(x)
    n +=1
    if x.count('Г') == 2 and x[0] != 'Р' and 'ГГ' not in x and 'О' not in x and 'А' not in x:
        print(n, x)