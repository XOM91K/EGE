import itertools
ct=0
for x in itertools.product('012345678', repeat=7):
    x=''.join(x)
    if x.count('8')==1 and x[0]!='0':
        x=x.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0').replace('3', '1').replace('5', '1').replace('7', '1')
        if x[0]=='0' and x[-1]=='1':
            ct+=1
print(ct)