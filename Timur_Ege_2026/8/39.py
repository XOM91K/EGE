import itertools
ct=0
for x in itertools.product('0123456789ABC',repeat=5):
    x=''.join(x)
    if x[0] != '0':
        if x.count('0')==1:
            if '11' not in x and '22' not in x and '33' not in x and '44' not in x and '55' not in x and '66' not in x and '77' not in x and '88' not in x and '99' not in x and 'AA' not in x and  'BB' not in x and 'CC' not in x:
                ct+=1
print(ct)