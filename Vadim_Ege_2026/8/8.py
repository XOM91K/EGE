import itertools
k = 0
ct = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat = 5):
    x = ''.join(x)
    k+=1
    if k%5 != 0:
        ct+=1
        if len(set(x)) == 5 and 'А' not in x and 'И' not in x and 'Ы' not in x:
            print(ct, x)
            break