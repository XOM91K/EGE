import itertools
cr=0
for x in itertools.permutations('ГЛУБИНА', 7):
    x=''.join(x)
    if x.index('А')>x.index('Г') and x.index('И')>x.index('Г'):    #как-то по индексу
        cr+=1
print(cr)