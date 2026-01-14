import itertools
k=0
for x in itertools.product(sorted('СТАРЫ'),repeat=5):
    x=''.join(x)
    k+=1
    if k%2!=0 and x[0]=='С':
        if x.count('А')==1 and x.count('С')==1 and x.count('Т')==1 and x.count('Р')==1 and x.count('Ы')==1:
            print(k,x)