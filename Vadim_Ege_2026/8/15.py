import itertools
c = 0
for x in itertools.permutations('ТИХОРЕЦК', 4):
    x = ''.join(x)
    g = x
    b = x
    b = b.replace('И','#')
    b = b.replace('О','#')
    b = b.replace('Е','#')
    if b.count('#')==2:
        k=0
        if g[0] == 'Т':
            k+=1
        if g[1] == 'И':
            k+=1
        if g[2] == 'Х':
            k+=1
        if g[3] == 'О':
            k+=1
        if k == 2:
            c+=1
print(c)