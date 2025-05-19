import itertools
ct=0
for x in set(itertools.permutations('АМФИБРАХИЙ' , r = 10 )):
    x=''.join(x)
    if x.index('Б')== 4  and x.index('Р')== 5 :
        ct+=1
print(ct)