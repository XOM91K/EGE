import itertools
ct=0
for x in itertools.permutations('ВЕБИНАР',r=7):
    x=''.join(x)
    x = x.replace('А', "0")
    x = x.replace('Е', "0")
    x = x.replace('И', "0")
    x = x.replace('В', "1")
    x = x.replace('Б', "1")
    x = x.replace('Н', "1")
    x = x.replace('Р', "1")
    if '00' not in x and '11' not in x:
        ct+=1
print(ct)