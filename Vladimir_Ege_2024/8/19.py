import itertools
k = 0
ct = 0
for x in itertools.product(sorted('ХЩНГБЛЗЦ'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] == 'Б' and x.count('Ц') >= 2:
        ct += 1
print(ct)