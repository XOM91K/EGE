import itertools
k = 0
ct = 0
for x in itertools.product(sorted('ОЗСЕНЮГТП'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'С' and x.count('Т') <= 1:
        print(k, x)
        ct += 1
print(ct)