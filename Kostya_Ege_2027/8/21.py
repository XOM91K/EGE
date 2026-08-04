import itertools
k = 0
for x in itertools.product(sorted('ПАВСИКЙ'), repeat=6):
    x = ''.join(x)
    if 'АИ' in x or 'ИА' in x or 'АА' in x or 'ИИ' in x:
        k += 1
    if x == 'КАКААА':
        print(k)