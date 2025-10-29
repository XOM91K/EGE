import itertools
ct=0
for x in itertools.product('кремний', repeat=5):
    x=''.join(x)
    if x.count('й')<=2:
        x=x.replace('е', 'и')
        if x.count('и')%2==0 and x.count('и') > 0:
            ct+=1
print(ct)