from itertools import product
k = 0
for i in set(product('СВЯТОСЛАВ', repeat=7)):
    s = ''.join(i)
    if s.count('С') + s.count('В') + s.count('Т') + s.count('Л') < s.count('Я') + s.count('О') + s.count('А'):
        k += 1
print(k)