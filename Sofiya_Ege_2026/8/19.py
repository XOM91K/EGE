import itertools
ct=0
k=0
for x in itertools.product(sorted('барш'), repeat=5):
    x=''.join(x)
    k+=1
    if len(set(x))==4:
        x=x.replace('р', 'б').replace('ш', 'б')
        if x.count('б')<=3:
            print(k)