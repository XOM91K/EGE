import itertools
k=0
for x in itertools.product(sorted('АРГУМЕНТ'), repeat=4):
    x=''.join(x)
    k+=1
    if x.count(x[0]) == 1 and x.count(x[1]) == 1 and x.count(x[2]) == 1 and x.count(x[3]) == 1:
        if list(x) == sorted(x):
            print(k, x)
# print(sorted('АГЕМНРТУ'))
# print('АГЕМНРТУ')