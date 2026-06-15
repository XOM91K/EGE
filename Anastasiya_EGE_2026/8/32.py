import itertools
sm = 0
k=0
for x in itertools.product(sorted('АВЕКЛМОРС'),repeat=7):
    x=''.join(x)
    k+=1
    if x[0] not in 'АВЕ' and x[1] not in 'АВЕ' and x[2] not in 'АВЕ' and x.count('Р')==3 and 'РР' not in x and x.count('С')==1:
        if x.index('С')<x.index('Р'):
            print(k,x)
            sm += k
print(sm)