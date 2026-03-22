import itertools
k = 0
for x in itertools.product(sorted('ЦИТРУС'), repeat=5):
    x = ''.join(x)
    k += 1
    if x.count('И') == 2 and 'ЦЦ' not in x:
        print(k, x)
