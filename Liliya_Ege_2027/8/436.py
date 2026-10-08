import itertools
ct=0
for x in itertools.product(sorted('0123456789AB'),repeat=7):
    x=''.join(x)
    if x[0]!='0' and x.count('B')==2:
       for y in '02468A':
           x = x.replace(y, '0')
       for y in '13579B':
           x = x.replace(y, '1')
       if '00' not in x and '11' not in x:
            ct+=1
print(ct)