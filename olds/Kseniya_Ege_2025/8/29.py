import itertools
k = 0
for x in itertools.product('АБДЕОП', repeat=6):
    x = ''.join(x)
    k += 1
    if x[0] == 'О' and k % 2 == 0 and len(set(x)) == 6:
        print(k)