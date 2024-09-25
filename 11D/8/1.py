import itertools
ct = 0
can = False
for x in itertools.product(sorted('НОРМАЛЬЕ'), repeat=6):
    x = ''.join(x)
    if x[:6] == 'НЕНОРМ':
        can = True
    if can:
        ct += 1
        print(x)
    if x[:4] == 'НОРМ' and can == True:
        can = False
        break
print(ct - 2)