import itertools
ct=0
for x in itertools.permutations('вебинар', 7):
    x=''.join(x)
    x=x.replace('б','в').replace('н','в').replace('р','в')
    x = x.replace('и', 'е').replace('а', 'е')
    if 'вв' not in x and 'ее' not in x:
        ct+=1
print(ct)