import itertools
ct=0
for x in itertools.product('0123456789ABCDEF', repeat=5):
    x=''.join(x)
    if x[0]!='0':
        if ('1' in x)+('4' in x)+('9' in x)>=1:
            povt3=[a for a in x if x.count(a)>=3]
            if len(povt3)==0:
                ct+=1
print(ct)