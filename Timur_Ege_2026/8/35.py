import itertools
ct=0
for x in itertools.product('0123456789ABC', repeat=6):
    x=''.join(x)
    if x[0]!='0':
        if x.count('0')>1 and (x.count('A') + x.count('B') + x.count('C'))==2:
            x = x.replace('A', '%')
            x = x.replace('B', '%')
            x = x.replace('C', '%')
            if '%%' in x:

                ct+=1
                print(x)
print(ct)