import itertools
ct = 0
for x in itertools.permutations('ТИХОРЕЦК', r = 4):
    x = ''.join(x)
    a = x
    a = a.replace('И' , '*')
    a = a.replace('О' , '*')
    a = a.replace('Е' , '*')

    if a.count('*') == 2 :
        k=0
        if x[0] == 'Т':
            k+=1
        if x[1] == 'И':
            k+=1
        if x[2] == 'Х':
            k+=1
        if x[3] == 'О':
            k+=1
        if k == 2 :
            ct +=1
print(ct)