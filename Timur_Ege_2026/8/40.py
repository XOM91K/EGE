import itertools
k=0
sm = 0
for x in itertools.product(sorted('СДАЙЕГЭ'), repeat=6):
    x=''.join(x)
    k+=1
    if 'ЕГЭ' in x:
        sm += k
print(sm)