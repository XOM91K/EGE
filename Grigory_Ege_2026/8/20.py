import itertools
k=0
for x in itertools.product(sorted('01234567'),repeat=5):
    s = ''.join(x)
    if s[-1]!='2' and s[-1]!='6':
        if s.count('7')<=2 and x[0] != '0':
            for nc in '1357':
                s = s.replace(nc,'*')
            if s[0]!='*':
                k+=1
print(k)