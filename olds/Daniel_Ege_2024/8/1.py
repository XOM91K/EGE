import itertools
k = 0
for x in itertools.product('ЕКЛОСТ', repeat=5):
    x = ''.join(x)
    k += 1
    if x[0] == 'С' and 'ОО' in x:
        print(k, x)