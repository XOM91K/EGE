import itertools
k = 0
w = []
for x in itertools.product(sorted('СТАРЫ'),repeat=5):
    x = ''.join(x)
    k += 1
    w.append(x)
    nepovt = [y for y in x if x.count(y)==1]
    if x[:1] == 'С' and len(nepovt) == 5  :
        print(k, x)