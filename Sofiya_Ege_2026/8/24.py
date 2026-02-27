import itertools
ct=0
for x in itertools.product('123456789ABCDE', repeat=6):
    x=''.join(x)
    if (x.count('A')+x.count('B')+x.count('C')+x.count('D')+x.count('E'))<=4:
        ct+=1
print(ct * 21)