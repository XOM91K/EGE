import itertools
n = 0
ct = 0
for x in itertools.product('БЖОУФЦЮ', repeat=4):
    x = ''.join(x)
    n += 1
    if n % 2 == 0 and x[0]== 'Ж' and x[1]== 'О' :
        ct += 1
print(ct)