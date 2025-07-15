import itertools
ct=0
#ВОЛК
for x in itertools.product('ПОЛЯКВ', repeat=4):
    x=''.join(x)
    k = 0
    if x[0] == 'В':
        k += 1
    if x[1] == 'О':
        k += 1
    if x[2] == 'Л':
        k += 1
    if x[3] == 'К':
        k += 1
    if k == 2:
        ct+=1
print(ct)