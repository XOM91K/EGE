import itertools
k = -1
for x in sorted(set(itertools.product('КАЛЕЙДОСКОП', repeat=6)))[::-1]:
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] == 'К' and x.count('Й') >= 2 and 'С' not in x and 'Е' not in x:
        print(k)
        break