import itertools
ct=0
for x in itertools.product('0123456789ABCDE', repeat=5):
    x=''.join(x)
    x = x.replace('A', '*')
    x = x.replace('B', '*')
    x = x.replace('C', '*')
    x = x.replace('D', '*')
    x = x.replace('E', '*')
    if x.count('8')==1 and x.count('*')>=2 and x[0]!='0':
        ct+=1
print(ct)