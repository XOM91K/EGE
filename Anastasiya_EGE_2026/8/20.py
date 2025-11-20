import itertools
ct=0
for x in itertools.product('0123456789ABCDEF', repeat=8):
    x=''.join(x)
    x=x.replace('A', '*')
    x = x.replace('B', '*')
    x = x.replace('C', '*')
    x = x.replace('D', '*')
    x = x.replace('E', '*')
    x = x.replace('F', '*')
    if x[0]!='0' and x.count('*')<=4 and x.count('0')==2:
        ct+=1
print(ct)