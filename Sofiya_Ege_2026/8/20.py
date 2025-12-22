import itertools
ct=0
for x in itertools.product('012345678', repeat=4):
    x=''.join(x)
    if x[0]!='0' and x.count('8')==1:
        left = x[:x.index('8')]
        right = x[x.index('8') + 1:]
        if sum(map(int, left)) == sum(map(int, right)):
            ct += 1
print(ct)
