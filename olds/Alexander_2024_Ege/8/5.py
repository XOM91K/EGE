import itertools
s=0
for x in itertools.product('012345678',repeat=7):
    x = ''.join(x)
    if(x[0]not in '0246')and not(x[-3] == x[-2] == x[-1]):
        s+=1
print(s)