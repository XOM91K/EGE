import itertools
ct = 0
for x in set(itertools.permutations('НОСОЧЕЧКИ', 9)):
    x = ''.join(x)
    x = x.replace('О', '1')
    x = x.replace('Е', '1')
    x = x.replace('И', '1')
    x = x.replace('Н', '0')
    x = x.replace('С', '0')
    x = x.replace('Ч', '0')
    x = x.replace('К', '0')
    if '11' not in x and '00' not in x:
        ct += 1
print(ct)